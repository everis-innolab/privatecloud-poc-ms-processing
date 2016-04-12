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
        self._logger.info("Post Handler just started")
        try:
            postdata = bottle.request.body.read()
            self._logger.info("Parsing DTO")
            transaction_dto = self.__parse_transaction_data_to_dto(postdata)
            self.__predict_transaction(transaction_dto)
            self._logger.info("Handled Transaction Request")
            return self.return_response("OK", 201)
        except MalformedTransactionException, e:
            self._logger.exception("Malformed Transaction. Returning 400")
            return self.return_response(e.message, 400)
        except Exception, e:
            self._logger.exception("Error handling transaction. Returning 500")
            return self.return_response(e.message, 500)

    def __parse_transaction_data_to_dto(self, body_raw_string):
        body_as_dict = json.loads(body_raw_string)
        return TransactionDAO().build_from_document(body_as_dict)

    def __predict_transaction(self, transaction_dto):
        try:
            self._logger.info("Predicting Transaction")
            code = self.__clf.get_fraud_code(transaction_dto)
            trans_dict = TransactionDAO().to_dict(transaction_dto)
            body_data = self.insert_code_and_get_as_dumps(trans_dict, code)
            self._logger.info("Sending Transaction to Output. Code: %s"%str(code))
            self.__post_to_output(body_data)
        except:
            self._logger.error("Error Predicting Transaction")

    def insert_code_and_get_as_dumps(self, transaction_dict, fraud_code):
        try:
            transaction_dict["fraud_code"]=fraud_code
            data_as_json = json.dumps(transaction_dict)
            return data_as_json
        except:
            self._logger.error("Error inserting code intro transaction dict")


    def __post_to_output(self, transaction_body_data):
        try:
            opener = self.__get_url_opener_with_empty_proxy()
            req=self.__build_post_request(transaction_body_data)
            self._logger.info("Sending to URL: %s"%req.get_full_url())
            response = opener.open(req)
        except Exception, e:
            msg = "Error sending Transaction"
            self._logger.exception(msg)

    def __build_post_request(self, body_data):
        try:
            self._logger.info("Building Request")
            url = self._eureka_agent.get_output_handler_url()
            req = urllib2.Request(
                url=url, data = body_data,
                headers={'Content-Type': 'application/json'}
            )
            return req
        except:
            self._logger.error("Error building Post Request")

    def __get_url_opener_with_empty_proxy(self):
        proxy_handler = urllib2.ProxyHandler({})
        return urllib2.build_opener(proxy_handler)