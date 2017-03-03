"""
TransactPro Gateway 3 API s operations
"""

from gateway.builders.transaction_builder import SmsBuilder


class Operations(object):
    __data_sets = None
    __operation_data = {}
    __asked_operation = None

    # Transactions types
    SMS = '/sms'
    HOLD_DMS = '/hold-dms'
    CHARGE_DMS = '/charge-dms'
    CANCEL = '/cancel'
    MOTO_SMS = '/moto/sms'
    MOTO_DMS = '/moto/dms'

    def __init__(self, __gate_operation_data_set, __client_operations):
        self.__asked_operations_dict = __client_operations
        self.__operation_data = __gate_operation_data_set
        pass

    def sms(self):
        self.__asked_operations_dict['current'] = self.SMS
        return SmsBuilder(self.__operation_data)

