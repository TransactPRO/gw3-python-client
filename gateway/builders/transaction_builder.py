from .payment_data_builder import PaymentDataBuilder
from .money_data_builder import MoneyDataBuilder


class TransactionTypesResources:
    @classmethod
    def payment_method(cls, __data_set):
        return PaymentDataBuilder(__data_set)

    @classmethod
    def money_data(cls, __data_set):
        return MoneyDataBuilder(__data_set)


class SmsBuilder(TransactionTypesResources):
    PaymentMethod = None
    MoneyData = None
    __sms_data_set = None

    def __init__(self, __operation_data_set):
        self.__sms_data_set = __operation_data_set

    def payment_method(self, **kwargs):
        return super().payment_method(self.__sms_data_set)

    def money_data(self, **kwargs):
        return super().money_data(self.__sms_data_set)
