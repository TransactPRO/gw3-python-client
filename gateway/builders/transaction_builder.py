class TransactionTypesResources:
    """
    Contains all necessary data sets builders for different transaction types constructors
    """

    @classmethod
    def payment_method_set(cls, __transaction_data_set_dict):
        from .payment_data_builder import PaymentDataBuilder
        return PaymentDataBuilder(__transaction_data_set_dict)

    @classmethod
    def money_data_set(cls, __transaction_data_set_dict):
        from .money_data_builder import MoneyDataBuilder
        return MoneyDataBuilder(__transaction_data_set_dict)

    @classmethod
    def system_data_set(cls, __transaction_data_set_dict):
        from gateway.builders.system_data_builder import SystemDataBuilder
        return SystemDataBuilder(__transaction_data_set_dict)

    @classmethod
    def command_data_set(cls, __transaction_data_set_dict):
        from gateway.builders.command_data_builder import CommandDataBuilder
        return CommandDataBuilder(__transaction_data_set_dict)

    @classmethod
    def customer_data_set(cls, __transaction_data_set_dict):
        from gateway.builders.customer_data_builder import CustomerDataBuilder
        return CustomerDataBuilder(__transaction_data_set_dict)


class SmsBuilder(TransactionTypesResources):
    __sms_data_set = None

    def __init__(self, __operation_data_set):
        self.__sms_data_set = __operation_data_set

    def payment_method_set(self, **kwargs):
        return super().payment_method_set(self.__sms_data_set)

    def money_data_set(self, **kwargs):
        return super().money_data_set(self.__sms_data_set)

    def system_data_set(self, **kwargs):
        return super().system_data_set(self.__sms_data_set)

    def customer_data_set(self, **kwargs):
        return super().customer_data_set(self.__sms_data_set)


class DmsHoldBuilder(TransactionTypesResources):
    __dms_hold_set = None

    def __init__(self, __operation_data_set):
        self.__dms_hold_set = __operation_data_set

    def payment_method_set(self, **kwargs):
        return super().payment_method_set(self.__dms_hold_set)

    def money_data_set(self, **kwargs):
        return super().money_data_set(self.__dms_hold_set)

    def system_data_set(self, **kwargs):
        return super().system_data_set(self.__dms_hold_set)

    def customer_data_set(self, **kwargs):
        return super().customer_data_set(self.__dms_hold_set)


class DmsChargeBuilder(TransactionTypesResources):
    __dms_charge_set = None

    def __init__(self, __operation_data_set):
        self.__dms_charge_set = __operation_data_set

    def money_data_set(self, **kwargs):
        return super().money_data_set(self.__dms_charge_set)

    def command_data_set(self, **kwargs):
        return super().command_data_set(self.__dms_charge_set)
