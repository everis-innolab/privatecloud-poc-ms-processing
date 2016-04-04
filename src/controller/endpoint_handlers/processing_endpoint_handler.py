# -*- encoding: utf8 -*-
import json
import urllib2
import bottle
from src.constants import POSITIVE_REMAINDERS
from src.constants import RANDOM_SLEEP_BOUNDS_MS
from src.controller.endpoint_handlers.base_endpoint_handler import BaseEndpointHandler
from src.controller.endpoint_handlers.transaction_classifier import TransactionClassifier
from src.controller.exceptions import MalformedTransactionException
from src.model.transaction_dao import TransactionDAO


class ProcessingEndpointHandler(BaseEndpointHandler):

    def __init__(self, eureka_agent, logger):
        super(ProcessingEndpointHandler, self).__init__(eureka_agent, logger)
        self.__clf = \
            TransactionClassifier(RANDOM_SLEEP_BOUNDS_MS, POSITIVE_REMAINDERS)

    def transactions_post(self):
        try:
            postdata = bottle.request.body.read()
            transaction_dto = self.__parse_transaction_data_to_dto(postdata)
            #if self.__clf.is_transaction_fraudulent(transaction_dto):
            self.handle_fraudulent_transaction(transaction_dto)
            self._logger.info("Handled Transaction Request")
            return self.return_response("OK", 201)

        except MalformedTransactionException, e:
            self._logger.exception("Error handling transaction\n")
            return self.return_response(e.message, 400)

    def __parse_transaction_data_to_dto(self, body_raw_string):
        body_as_dict = json.loads(body_raw_string)
        return TransactionDAO().build_from_document(body_as_dict)

    def handle_fraudulent_transaction(self, transaction_dto):
        """
        If the transaction is fraudulent we should send it to the output
        """
        try:
            proxy_handler = urllib2.ProxyHandler({})
            opener = urllib2.build_opener(proxy_handler)
            url = self._eureka_agent.get_output_handler_url()
            self._logger.info("Sending Fraudulent Transaction to :%s"%url)
            req = urllib2.Request(
                url=url,
                data = json.dumps(TransactionDAO().to_dict(transaction_dto)),
                headers={'Content-Type': 'application/json'}
            )
            self._logger.info("output_handler_url :%s"%self._eureka_agent.get_output_handler_url())
            response = opener.open(req)

        except Exception, e:
            msg = "Could not send the fraudulent transaction to the Output " \
                  "Handler"
            self._logger.exception(msg)