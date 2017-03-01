"""
TransactPro Gateway 3 API s operations
"""

from gateway.builders.transaction_builder import SmsBuilder


class Operations(object):
    __data_sets = None
    __operation_data = {}
    __gate_validation_list = {}

    def __init__(self, __gate_operation_data_set, __gate_validation_list):
        self.__operation_data = __gate_operation_data_set
        self.__gate_validation_list = __gate_validation_list
        pass

    def sms(self):
        return SmsBuilder(self.__operation_data, self.__gate_validation_list)

