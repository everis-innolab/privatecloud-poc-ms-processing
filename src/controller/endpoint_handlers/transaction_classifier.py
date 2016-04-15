# -*- encoding: utf8 -*-
import random
from datetime import datetime
from time import sleep

from src.constants import *
from src.controller.exceptions import InsufficientDataInTransactionException, \
    MalformedTransactionException


class TransactionClassifier():

    def __init__(self, random_sleep_bounds_tuple, fraudulent_remainders, logger):
        self.__min_sleep, self.__max_sleep = random_sleep_bounds_tuple
        self.__fraudulent_remainders = fraudulent_remainders
        self.__logger=logger

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
            return random.choice(FRAUDULENT_CODES)

        else:
            self.__logger.info("Classified as Legit transaction")
            return LEGIT_CODE

    def __check_enough_data_to_classify_transaction(self, transaction_dto):
        complete= (
            transaction_dto.commerce_account_iban is not None and \
            transaction_dto.client_credit_card is not None and \
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
        remainder = total % DIVIDER
        return remainder in self.__fraudulent_remainders

    def __sleep_random_amount_if_necessary(self, start_time):
        millis_already_passed = self.millis_interval(start_time, datetime.now())

        sleep_time = \
            random.randint(self.__min_sleep, self.__max_sleep)/ float(1000)
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


