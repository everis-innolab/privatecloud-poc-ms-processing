from src.controller.exceptions import MalformedTransactionException
from src.controller.logs.logger_factory import LoggerFactory
from src.controller.singleton import Singleton
from src.model.transaction_dto import TransactionDTO


class TransactionDAO(Singleton):

    def __init__(self):
        super(TransactionDAO, self).__init__()

    def to_dict(self, TransactionDTO):
        dict= {}
        dict["_id"] = TransactionDTO._id
        dict["client_country"] = TransactionDTO.client_country
        dict["client_id"] = TransactionDTO.client_id
        dict["commerce_tpv"] = TransactionDTO.commerce_tpv
        dict["client_credit_card"] = TransactionDTO.client_credit_card
        dict["transaction_amount"] = TransactionDTO.transaction_amount
        dict["commerce_id"] = TransactionDTO.commerce_id
        dict["client_country_name"] = TransactionDTO.client_country_name
        dict["commerce_country"] = TransactionDTO.commerce_country
        dict["commerce_country_name"] = TransactionDTO.commerce_country_name
        dict["commerce_account_iban"] = TransactionDTO.commerce_account_iban
        dict["transaction_datetime"] = TransactionDTO.transaction_datetime
        dict["client_name"]=TransactionDTO.client_name
        dict["client_last_name"]=TransactionDTO.client_last_name
        return dict

    def build_from_document(self, source_doc):
        try:
            _id = source_doc.get("_id", None)
            client_country = source_doc["client_country"]
            client_id = source_doc["client_id"]
            commerce_tpv = source_doc.get("commerce_tpv", None)
            client_credit_card = source_doc["client_credit_card"]
            transaction_amount = source_doc["transaction_amount"]
            commerce_id = source_doc["commerce_id"]
            client_country_name = source_doc["client_country_name"]
            commerce_country = source_doc["commerce_country"]
            commerce_country_name = source_doc["commerce_country_name"]
            commerce_account_iban = source_doc["commerce_account_iban"]
            transaction_datetime = source_doc["transaction_datetime"]
            client_name=source_doc["client_name"]
            client_last_name=source_doc["client_last_name"]

            return TransactionDTO(
                _id = _id,
                client_country = client_country,
                client_id = client_id,
                commerce_tpv = commerce_tpv,
                client_credit_card = client_credit_card,
                transaction_amount = transaction_amount,
                commerce_id = commerce_id,
                client_country_name = client_country_name,
                commerce_country = commerce_country,
                commerce_country_name = commerce_country_name,
                commerce_account_iban = commerce_account_iban,
                transaction_datetime = transaction_datetime,
                client_name=client_name,
                client_last_name=client_last_name
            )

        except Exception, e:
            logger = LoggerFactory.get_logger()

            logger.exception(
                "Error parsing document into Transaction Object: %s"%str(source_doc)
            )
            raise MalformedTransactionException()
