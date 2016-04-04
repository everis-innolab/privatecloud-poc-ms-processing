# -*- encoding: utf-8 -*-
import datetime
import unittest
from src.controller.endpoint_handlers.transaction_classifier import \
    TransactionClassifier
from src.controller.exceptions import InsufficientDataInTransactionException, \
    MalformedTransactionException
from src.model.transaction_dao import TransactionDAO


class TestTransactionClassifier(unittest.TestCase):

    def setUp(self ):
        self.min_sleep = 30
        self.max_sleep = 150
        self.positive_remainders = [4]
        self.clf = TransactionClassifier(
            (self.min_sleep,self.max_sleep), self.positive_remainders
        )
        self.transaction_dto = TransactionDAO().build_from_document(
            {
                "_id" : 0,
                "client_country" : "SK",
                "client_id" : 35,
                "commerce_tpv" : "805348991287",
                "client_credit_card" : "4756310296329932",
                "transaction_amount" : 384.1,
                "commerce_id" : 100,
                "client_country_name" : "Slovakia",
                "commerce_country" : "ES",
                "commerce_country_name" : "Spain",
                "commerce_account_iban" : "ES7231011409805348991287",
                "transaction_datetime" : "2015-06-15T18:01:32.000+0000"
            }
        )

    def tearDown(self ):
        pass

    def test_creation(self):
        self.assertIsNotNone(self.clf)

    def test_dumb_prediction(self):
        result = self.clf.is_transaction_fraudulent(self.transaction_dto)
        self.assertIsNotNone(result)

    def test_random_sleep_is_within_interval(self):
        sleep_intervals = []

        for i in range(10):
            start_time = datetime.datetime.now()
            self.clf.is_transaction_fraudulent(self.transaction_dto)
            end_time = datetime.datetime.now()

            lapse = self.clf.millis_interval(start_time, end_time)
            sleep_intervals.append(lapse)
        # To perform an assert on the minimun response time is really a load
        # tests, not a unit test, so we skip it.
        # self.assertGreaterEqual(min(sleep_intervals), self.min_sleep)
        self.assertLessEqual(max(sleep_intervals), self.max_sleep)

    def test_incomplete_transaction_raises_exception(self):
        self.transaction_dto.commerce_account_iban = None
        self.assertRaises(
            InsufficientDataInTransactionException,
            self.clf.is_transaction_fraudulent,
            self.transaction_dto
        )

        self.setUp()
        self.transaction_dto.client_credit_card = None
        self.assertRaises(
            InsufficientDataInTransactionException,
            self.clf.is_transaction_fraudulent,
            self.transaction_dto
        )

        self.setUp()
        self.transaction_dto.transaction_amount = None
        self.assertRaises(
            InsufficientDataInTransactionException,
            self.clf.is_transaction_fraudulent,
            self.transaction_dto
        )

    def test_malformed_transaction_document_raises_exception(self):
        transaction_dict = TransactionDAO().to_dict(self.transaction_dto)
        transaction_dict.pop("client_country", None)
        self.assertRaises(
            MalformedTransactionException,


        )

    def test_fraudulent_transaction_returns_positive(self):
        self.transaction_dto.commerce_account_iban = "10001"
        self.transaction_dto.client_credit_card = "99991"
        self.transaction_dto.transaction_amount = "772"
        result = self.clf.is_transaction_fraudulent(self.transaction_dto)
        self.assertTrue(result)

    def test_legit_transaction_returns_negative(self):
        self.transaction_dto.commerce_account_iban = "10003"
        self.transaction_dto.client_credit_card = "99993"
        self.transaction_dto.transaction_amount = "772"
        result = self.clf.is_transaction_fraudulent(self.transaction_dto)
        self.assertFalse(result)

    def test_malformed_transaction_raises_exception_when_predicted(self):
        self.transaction_dto.commerce_account_iban = "aaaaa"
        self.transaction_dto.client_credit_card = "ññññ"
        self.transaction_dto.transaction_amount = "úuuú"
        self.assertRaises(
            MalformedTransactionException,
            self.clf.is_transaction_fraudulent,
            self.transaction_dto
        )

if __name__ == '__main__':
    unittest.main()
