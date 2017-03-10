class TransactionTypesResources(object):
    """
    Contains all necessary data sets builders for different transaction types constructors
    """

    @classmethod
    def command_data_set(cls, __transaction_data_set_dict, __operation_mandatory_fields_set_dict):
        from gateway.builders.command_data_builder import CommandDataBuilder
        return CommandDataBuilder(__transaction_data_set_dict, __operation_mandatory_fields_set_dict)

    @classmethod
    def customer_data_set(cls, __transaction_data_set_dict):
        from gateway.builders.customer_data_builder import CustomerDataBuilder
        return CustomerDataBuilder(__transaction_data_set_dict)

    @classmethod
    def merchant_order_data_set(cls, __transaction_data_set_dict):
        from gateway.builders.merchant_order_builder import MerchantOrderBuilder
        return MerchantOrderBuilder(__transaction_data_set_dict)

    @classmethod
    def payment_method_set(cls, __transaction_data_set_dict, __operation_mandatory_fields_set_dict):
        from .payment_data_builder import PaymentDataBuilder
        return PaymentDataBuilder(__transaction_data_set_dict, __operation_mandatory_fields_set_dict)

    @classmethod
    def money_data_set(cls, __transaction_data_set_dict, __operation_mandatory_fields_set_dict):
        from .money_data_builder import MoneyDataBuilder
        return MoneyDataBuilder(__transaction_data_set_dict, __operation_mandatory_fields_set_dict)

    @classmethod
    def system_data_set(cls, __transaction_data_set_dict, __operation_mandatory_fields_set_dict):
        from gateway.builders.system_data_builder import SystemDataBuilder
        return SystemDataBuilder(__transaction_data_set_dict, __operation_mandatory_fields_set_dict)


class ExploringTypesResources:
    """
    Contains all necessary data sets builders for construction exploring past payments operations
    """

    @classmethod
    def info_command_data_set(cls, __transaction_data_set_dict, __operation_mandatory_fields_set_dict):
        from gateway.builders.info_data_builder import InfoDataBuilder
        return InfoDataBuilder(__transaction_data_set_dict, __operation_mandatory_fields_set_dict)


"""
Transaction Types builders
"""


class SmsBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.operation_data_set = __operation_data_set
        self.operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(SmsBuilder, self).command_data_set(self.operation_data_set, self.operation_mandatory_fields_set)

    def customer_data_set(self):
        return super(SmsBuilder, self).customer_data_set(self.operation_data_set)

    def merchant_order_data_set(self):
        return super(SmsBuilder, self).merchant_order_data_set(self.operation_data_set)

    def payment_method_set(self):
        return super(SmsBuilder, self).payment_method_set(self.operation_data_set, self.operation_mandatory_fields_set)

    def money_data_set(self):
        return super(SmsBuilder, self).money_data_set(self.operation_data_set, self.operation_mandatory_fields_set)

    def system_data_set(self):
        return super(SmsBuilder, self).system_data_set(self.operation_data_set, self.operation_mandatory_fields_set)


class DmsHoldBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.operation_data_set = __operation_data_set
        self.operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(DmsHoldBuilder, self).command_data_set(self.operation_data_set,
                                                            self.operation_mandatory_fields_set)

    def customer_data_set(self):
        return super(DmsHoldBuilder, self).customer_data_set(self.operation_data_set)

    def merchant_order_data_set(self):
        return super(DmsHoldBuilder, self).merchant_order_data_set(self.operation_data_set, )

    def payment_method_set(self):
        return super(DmsHoldBuilder, self).payment_method_set(self.operation_data_set,
                                                              self.operation_mandatory_fields_set)

    def money_data_set(self):
        return super(DmsHoldBuilder, self).money_data_set(self.operation_data_set, self.operation_mandatory_fields_set)

    def system_data_set(self):
        return super(DmsHoldBuilder, self).system_data_set(self.operation_data_set, self.operation_mandatory_fields_set)


class DmsChargeBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.operation_data_set = __operation_data_set
        self.operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(DmsChargeBuilder, self).command_data_set(self.operation_data_set,
                                                              self.operation_mandatory_fields_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in DMS CHARGE operation!')

    def merchant_order_data_set(self):
        raise NotImplementedError('Merchant order data set unavailable in DMS CHARGE operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in DMS CHARGE operation!')

    def money_data_set(self):
        return super(DmsChargeBuilder, self).money_data_set(self.operation_data_set,
                                                            self.operation_mandatory_fields_set)

    def system_data_set(self):
        return super(DmsChargeBuilder, self).system_data_set(self.operation_data_set,
                                                             self.operation_mandatory_fields_set)


class DmsCancelBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.operation_data_set = __operation_data_set
        self.operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(DmsCancelBuilder, self).command_data_set(self.operation_data_set,
                                                              self.operation_mandatory_fields_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in DMS CANCEL operation!')

    def merchant_order_data_set(self):
        raise NotImplementedError('Merchant order data set unavailable in DMS CANCEL operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in DMS CANCEL operation!')

    def money_data_set(self):
        return super(DmsCancelBuilder, self).money_data_set(self.operation_data_set,
                                                            self.operation_mandatory_fields_set)

    def system_data_set(self):
        return super(DmsCancelBuilder, self).system_data_set(self.operation_data_set,
                                                             self.operation_mandatory_fields_set)


class MotoSmsBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.operation_data_set = __operation_data_set
        self.operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(MotoSmsBuilder, self).command_data_set(self.operation_data_set,
                                                            self.operation_mandatory_fields_set)

    def customer_data_set(self):
        return super(MotoSmsBuilder, self).customer_data_set(self.operation_data_set)

    def merchant_order_data_set(self):
        return super(MotoSmsBuilder, self).merchant_order_data_set(self.operation_data_set)

    def payment_method_set(self):
        return super(MotoSmsBuilder, self).payment_method_set(self.operation_data_set,
                                                              self.operation_mandatory_fields_set)

    def money_data_set(self):
        return super(MotoSmsBuilder, self).money_data_set(self.operation_data_set, self.operation_mandatory_fields_set)

    def system_data_set(self):
        return super(MotoSmsBuilder, self).system_data_set(self.operation_data_set, self.operation_mandatory_fields_set)


class MotoDmsBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.operation_data_set = __operation_data_set
        self.operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(MotoDmsBuilder, self).command_data_set(self.operation_data_set,
                                                            self.operation_mandatory_fields_set)

    def customer_data_set(self):
        return super(MotoDmsBuilder, self).customer_data_set(self.operation_data_set)

    def merchant_order_data_set(self):
        return super(MotoDmsBuilder, self).merchant_order_data_set(self.operation_data_set)

    def payment_method_set(self):
        return super(MotoDmsBuilder, self).payment_method_set(self.operation_data_set,
                                                              self.operation_mandatory_fields_set)

    def money_data_set(self):
        return super(MotoDmsBuilder, self).money_data_set(self.operation_data_set, self.operation_mandatory_fields_set)

    def system_data_set(self):
        return super(MotoDmsBuilder, self).system_data_set(self.operation_data_set, self.operation_mandatory_fields_set)


class RecurrentSmsBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.operation_data_set = __operation_data_set
        self.operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(RecurrentSmsBuilder, self).command_data_set(self.operation_data_set,
                                                                 self.operation_mandatory_fields_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Recurrent SMS operation!')

    def merchant_order_data_set(self):
        raise NotImplementedError('Merchant order data set unavailable in Recurrent SMS operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Recurrent SMS operation!')

    def money_data_set(self):
        return super(RecurrentSmsBuilder, self).money_data_set(self.operation_data_set,
                                                               self.operation_mandatory_fields_set)

    def system_data_set(self):
        return super(RecurrentSmsBuilder, self).system_data_set(self.operation_data_set,
                                                                self.operation_mandatory_fields_set)


class RecurrentDmsBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.operation_data_set = __operation_data_set
        self.operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(RecurrentDmsBuilder, self).command_data_set(self.operation_data_set,
                                                                 self.operation_mandatory_fields_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Recurrent DMS operation!')

    def merchant_order_data_set(self):
        raise NotImplementedError('Merchant order data set unavailable in Recurrent DMS operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Recurrent DMS operation!')

    def money_data_set(self):
        return super(RecurrentDmsBuilder, self).money_data_set(self.operation_data_set,
                                                               self.operation_mandatory_fields_set)

    def system_data_set(self):
        return super(RecurrentDmsBuilder, self).system_data_set(self.operation_data_set,
                                                                self.operation_mandatory_fields_set)


class RefundBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.operation_data_set = __operation_data_set
        self.operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(RefundBuilder, self).command_data_set(self.operation_data_set, self.operation_mandatory_fields_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Refund operation!')

    def merchant_order_data_set(self):
        raise NotImplementedError('Merchant order data set unavailable in Refund operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Refund operation!')

    def money_data_set(self):
        return super(RefundBuilder, self).money_data_set(self.operation_data_set, self.operation_mandatory_fields_set)

    def system_data_set(self):
        return super(RefundBuilder, self).system_data_set(self.operation_data_set, self.operation_mandatory_fields_set)


class ReversalBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.operation_data_set = __operation_data_set
        self.operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(ReversalBuilder, self).command_data_set(self.operation_data_set,
                                                             self.operation_mandatory_fields_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Reversal operation!')

    def merchant_order_data_set(self):
        raise NotImplementedError('Merchant order data set unavailable in Reversal operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Reversal operation!')

    def money_data_set(self):
        return super(ReversalBuilder, self).money_data_set(self.operation_data_set, self.operation_mandatory_fields_set)

    def system_data_set(self):
        return super(ReversalBuilder, self).system_data_set(self.operation_data_set,
                                                            self.operation_mandatory_fields_set)


"""
Exploring Past Payments builders
"""


class TransactionStatusBuilder(TransactionTypesResources, ExploringTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.operation_data_set = __operation_data_set
        self.operation_mandatory_fields_set = __operation_mandatory_fields

    def info_command_data_set(self):
        return super(TransactionStatusBuilder, self).info_command_data_set(self.operation_data_set,
                                                                           self.operation_mandatory_fields_set)

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
        return super(TransactionStatusBuilder, self).system_data_set(self.operation_data_set,
                                                                     self.operation_mandatory_fields_set)
