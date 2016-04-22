# -*- encoding: utf8 -*-
import random
from datetime import datetime
from time import sleep
from src.controller.exceptions import InsufficientDataInTransactionException, \
    MalformedTransactionException


class TransactionClassifier():

    def __init__(self,logger,constants_dto):
        self.__logger=logger
        self.__constants_dto=constants_dto

    def get_fraud_code(self, transaction_dto):
        """
        In order to simplify the development a really simple operation is
        going to be used. A random sleep time will be added to resemble the
        performance of a real Classifier

        Those are the only fields taken into consideration:

            * commerce_account_iban
            * client_credit_card
            * transaction_amount

        The las digit of this three fields are added and, if the last digits of
        the result match the ones specified in the constants, the transaction
        is classified as fraudulent.

        :param transaction_dto:
        :return:
        """
        self.__check_enough_data_to_classify_transaction(transaction_dto)
        start_time = datetime.now()
        is_positive = self.__transaction_remainder_in_fraudulent_remainders(
            transaction_dto
        )
        self.__sleep_random_amount_if_necessary(start_time)
        if is_positive:
            self.__logger.info("Classified as Fraudulent transaction")
            return random.choice(self.__constants_dto.fraudulent_codes)

        else:
            self.__logger.info("Classified as Legit transaction")
            return self.__constants_dto.legit_code

    def __check_enough_data_to_classify_transaction(self, transaction_dto):
        complete = (
            transaction_dto.commerce_account_iban is not None and
            transaction_dto.client_credit_card is not None and
            transaction_dto.transaction_amount is not None
        )
        if complete is False:
            raise InsufficientDataInTransactionException()

    def __transaction_remainder_in_fraudulent_remainders(self, transaction_dto):
        try:
            operand1 = int(str(transaction_dto.commerce_account_iban)[-1])
            operand2 = int(str(transaction_dto.client_credit_card)[-1])
            operand3 = int(str(int(transaction_dto.transaction_amount))[-1])
        except:
            raise MalformedTransactionException()
        total = operand1 + operand2 + operand3
        remainder = total % self.__constants_dto.divider
        return remainder in self.__constants_dto.positive_remainders

    def __sleep_random_amount_if_necessary(self, start_time):
        millis_already_passed = self.millis_interval(start_time, datetime.now())
        min, max = self.__constants_dto.random_sleep_bounds_ms
        sleep_time = random.randint(min, max)/ float(1000)
        sleep_time -= millis_already_passed
        # if sleep_time > 0 :
        #     sleep(sleep_time)

    @staticmethod
    def millis_interval(start, end):
        """start and end are datetime instances"""
        diff = end - start
        millis = diff.days * 24 * 60 * 60 * 1000
        millis += diff.seconds * 1000
        millis += diff.microseconds / 1000
        return millis
