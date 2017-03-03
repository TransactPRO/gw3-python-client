from .payment_data_builder import PaymentDataBuilder
from .money_data_builder import MoneyDataBuilder
from gateway.data_sets.request_parameters import RequestParameters


class SmsBuilder(object):
    PaymentMethod = None
    MoneyData = None

    def __init__(self, __operation_data_set):
        self.PaymentMethod = PaymentDataBuilder(__operation_data_set)
        self.MoneyData = MoneyDataBuilder(__operation_data_set)
        self.__data_set = RequestParameters
