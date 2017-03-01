from .payment_data_builder import PaymentDataBuilder
from .money_data_builder import MoneyDataBuilder
from gateway.data_sets.request_parameters import RequestParameters


class SmsBuilder(object):
    PaymentMethod = None
    MoneyData = None

    def __init__(self, __operation_data_set, __validation_list):
        self.PaymentMethod = PaymentDataBuilder(__operation_data_set)
        self.MoneyData = MoneyDataBuilder(__operation_data_set)
        self.__data_set = RequestParameters
        self.__add_mandatory_fields(__validation_list)

    def __add_mandatory_fields(self, mandatory_list):
        mandatory_list.append(self.__data_set.PAYMENT_METHOD_DATA_PAN)
        mandatory_list.append(self.__data_set.PAYMENT_METHOD_DATA_EXPIRE)
        mandatory_list.append(self.__data_set.PAYMENT_METHOD_DATA_CVV)
        mandatory_list.append(self.__data_set.MONEY_DATA_AMOUNT)
        mandatory_list.append(self.__data_set.MONEY_DATA_CURRENCY)
