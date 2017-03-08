class TransactionTypesResources:
    """
    Contains all necessary data sets builders for different transaction types constructors
    """

    @classmethod
    def command_data_set(cls, __transaction_data_set_dict):
        from gateway.builders.command_data_builder import CommandDataBuilder
        return CommandDataBuilder(__transaction_data_set_dict)

    @classmethod
    def customer_data_set(cls, __transaction_data_set_dict):
        from gateway.builders.customer_data_builder import CustomerDataBuilder
        return CustomerDataBuilder(__transaction_data_set_dict)

    @classmethod
    def merchant_order_data_set(cls, __transaction_data_set_dict):
        from gateway.builders.merchant_order_builder import MerchantOrderBuilder
        return MerchantOrderBuilder(__transaction_data_set_dict)

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


class ExploringTypesResources:
    """
    Contains all necessary data sets builders for construction exploring past payments operations
    """

    @classmethod
    def info_command_data_set(cls, __info_data_set_dict):
        from gateway.builders.info_data_builder import InfoDataBuilder
        return InfoDataBuilder(__info_data_set_dict)


"""
Transaction Types builders
"""


class SmsBuilder(TransactionTypesResources):
    __sms_data_set = None

    def __init__(self, __operation_data_set):
        self.__sms_data_set = __operation_data_set

    def command_data_set(self):
        return super().command_data_set(self.__sms_data_set)

    def customer_data_set(self):
        return super().customer_data_set(self.__sms_data_set)

    def merchant_order_data_set(self):
        return super().merchant_order_data_set(self.__sms_data_set)

    def payment_method_set(self):
        return super().payment_method_set(self.__sms_data_set)

    def money_data_set(self):
        return super().money_data_set(self.__sms_data_set)

    def system_data_set(self):
        return super().system_data_set(self.__sms_data_set)


class DmsHoldBuilder(TransactionTypesResources):
    __dms_hold_set = None

    def __init__(self, __operation_data_set):
        self.__dms_hold_set = __operation_data_set

    def command_data_set(self):
        return super().command_data_set(self.__dms_hold_set)

    def customer_data_set(self):
        return super().customer_data_set(self.__dms_hold_set)

    def merchant_order_data_set(self):
        return super().merchant_order_data_set(self.__dms_hold_set)

    def payment_method_set(self):
        return super().payment_method_set(self.__dms_hold_set)

    def money_data_set(self):
        return super().money_data_set(self.__dms_hold_set)

    def system_data_set(self):
        return super().system_data_set(self.__dms_hold_set)


class DmsChargeBuilder(TransactionTypesResources):
    __dms_charge_set = None

    def __init__(self, __operation_data_set):
        self.__dms_charge_set = __operation_data_set

    def command_data_set(self):
        return super().command_data_set(self.__dms_charge_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in DMS CHARGE operation!')

    def merchant_order_data_set(self):
        raise NotImplementedError('Merchant order data set unavailable in DMS CHARGE operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in DMS CHARGE operation!')

    def money_data_set(self):
        return super().money_data_set(self.__dms_charge_set)

    def system_data_set(self):
        return super().system_data_set(self.__dms_charge_set)


class DmsCancelBuilder(TransactionTypesResources):
    __dms_cancel_set = None

    def __init__(self, __operation_data_set):
        self.__dms_cancel_set = __operation_data_set

    def command_data_set(self):
        return super().command_data_set(self.__dms_cancel_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in DMS CANCEL operation!')

    def merchant_order_data_set(self):
        raise NotImplementedError('Merchant order data set unavailable in DMS CANCEL operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in DMS CANCEL operation!')

    def money_data_set(self):
        return super().money_data_set(self.__dms_cancel_set)

    def system_data_set(self):
        return super().system_data_set(self.__dms_cancel_set)


class MotoSmsBuilder(TransactionTypesResources):
    __moto_sms_set = None

    def __init__(self, __operation_data_set):
        self.__moto_sms_set = __operation_data_set

    def command_data_set(self):
        return super().command_data_set(self.__moto_sms_set)

    def customer_data_set(self):
        return super().customer_data_set(self.__moto_sms_set)

    def merchant_order_data_set(self):
        return super().merchant_order_data_set(self.__moto_sms_set)

    def payment_method_set(self):
        return super().payment_method_set(self.__moto_sms_set)

    def money_data_set(self):
        return super().money_data_set(self.__moto_sms_set)

    def system_data_set(self):
        return super().system_data_set(self.__moto_sms_set)


class MotoDmsBuilder(TransactionTypesResources):
    __moto_dms_set = None

    def __init__(self, __operation_data_set):
        self.__moto_dms_set = __operation_data_set

    def command_data_set(self):
        return super().command_data_set(self.__moto_dms_set)

    def customer_data_set(self):
        return super().customer_data_set(self.__moto_dms_set)

    def merchant_order_data_set(self):
        return super().merchant_order_data_set(self.__moto_dms_set)

    def payment_method_set(self):
        return super().payment_method_set(self.__moto_dms_set)

    def money_data_set(self):
        return super().money_data_set(self.__moto_dms_set)

    def system_data_set(self):
        return super().system_data_set(self.__moto_dms_set)


class RecurrentSmsBuilder(TransactionTypesResources):
    __recurrent_sms_set = None

    def __init__(self, __operation_data_set):
        self.__recurrent_sms_set = __operation_data_set

    def command_data_set(self):
        return super().command_data_set(self.__recurrent_sms_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Recurrent SMS operation!')

    def merchant_order_data_set(self):
        raise NotImplementedError('Merchant order data set unavailable in Recurrent SMS operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Recurrent SMS operation!')

    def money_data_set(self):
        return super().money_data_set(self.__recurrent_sms_set)

    def system_data_set(self):
        return super().system_data_set(self.__recurrent_sms_set)


class RecurrentDmsBuilder(TransactionTypesResources):
    __recurrent_dms_set = None

    def __init__(self, __operation_data_set):
        self.__recurrent_dms_set = __operation_data_set

    def command_data_set(self):
        return super().command_data_set(self.__recurrent_dms_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Recurrent DMS operation!')

    def merchant_order_data_set(self):
        raise NotImplementedError('Merchant order data set unavailable in Recurrent DMS operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Recurrent DMS operation!')

    def money_data_set(self):
        return super().money_data_set(self.__recurrent_dms_set)

    def system_data_set(self):
        return super().system_data_set(self.__recurrent_dms_set)


class RefundBuilder(TransactionTypesResources):
    __refund_set = None

    def __init__(self, __operation_data_set):
        self.__refund_set = __operation_data_set

    def command_data_set(self):
        return super().command_data_set(self.__refund_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Refund operation!')

    def merchant_order_data_set(self):
        raise NotImplementedError('Merchant order data set unavailable in Refund operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Refund operation!')

    def money_data_set(self):
        return super().money_data_set(self.__refund_set)

    def system_data_set(self):
        return super().system_data_set(self.__refund_set)


class ReversalBuilder(TransactionTypesResources):
    __reversal_set = None

    def __init__(self, __operation_data_set):
        self.__reversal_set = __operation_data_set

    def command_data_set(self):
        return super().command_data_set(self.__reversal_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Reversal operation!')

    def merchant_order_data_set(self):
        raise NotImplementedError('Merchant order data set unavailable in Reversal operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Reversal operation!')

    def money_data_set(self):
        return super().money_data_set(self.__reversal_set)

    def system_data_set(self):
        return super().system_data_set(self.__reversal_set)


"""
Exploring Past Payments builders
"""


class TransactionStatusBuilder(TransactionTypesResources, ExploringTypesResources):
    __transaction_status_set = None

    def __init__(self, __operation_data_set):
        self.__transaction_status_set = __operation_data_set

    def info_command_data_set(self):
        return super().info_command_data_set(self.__transaction_status_set)

    def command_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Transaction Status operation!')

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Transaction Status operation!')

    def merchant_order_data_set(self):
        raise NotImplementedError('Merchant order data set unavailable in Transaction Status operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Transaction Status operation!')

    def money_data_set(self):
        raise NotImplementedError('Money data set unavailable in Transaction Status operation!')

    def system_data_set(self):
        return super().system_data_set(self.__transaction_status_set)
