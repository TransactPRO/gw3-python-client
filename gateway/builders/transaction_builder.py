# The MIT License
#
# Copyright (c) 2017 Transact Pro.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


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
        from gateway.builders.payment_data_builder import PaymentDataBuilder
        return PaymentDataBuilder(__transaction_data_set_dict, __operation_mandatory_fields_set_dict)

    @classmethod
    def money_data_set(cls, __transaction_data_set_dict, __operation_mandatory_fields_set_dict):
        from gateway.builders.money_data_builder import MoneyDataBuilder
        return MoneyDataBuilder(__transaction_data_set_dict, __operation_mandatory_fields_set_dict)

    @classmethod
    def system_data_set(cls, __transaction_data_set_dict):
        from gateway.builders.system_data_builder import SystemDataBuilder
        return SystemDataBuilder(__transaction_data_set_dict)


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
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(SmsBuilder, self).command_data_set(self.__operation_data_set,
                                                        self.__operation_mandatory_fields_set)

    def customer_data_set(self):
        return super(SmsBuilder, self).customer_data_set(self.__operation_data_set)

    def merchant_order_data_set(self):
        return super(SmsBuilder, self).merchant_order_data_set(self.__operation_data_set)

    def payment_method_set(self):
        return super(SmsBuilder, self).payment_method_set(self.__operation_data_set,
                                                          self.__operation_mandatory_fields_set)

    def money_data_set(self):
        return super(SmsBuilder, self).money_data_set(self.__operation_data_set, self.__operation_mandatory_fields_set)

    def system_data_set(self):
        return super(SmsBuilder, self).system_data_set(self.__operation_data_set)


class DmsHoldBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(DmsHoldBuilder, self).command_data_set(self.__operation_data_set,
                                                            self.__operation_mandatory_fields_set)

    def customer_data_set(self):
        return super(DmsHoldBuilder, self).customer_data_set(self.__operation_data_set)

    def merchant_order_data_set(self):
        return super(DmsHoldBuilder, self).merchant_order_data_set(self.__operation_data_set, )

    def payment_method_set(self):
        return super(DmsHoldBuilder, self).payment_method_set(self.__operation_data_set,
                                                              self.__operation_mandatory_fields_set)

    def money_data_set(self):
        return super(DmsHoldBuilder, self).money_data_set(self.__operation_data_set,
                                                          self.__operation_mandatory_fields_set)

    def system_data_set(self):
        return super(DmsHoldBuilder, self).system_data_set(self.__operation_data_set)


class DmsChargeBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(DmsChargeBuilder, self).command_data_set(self.__operation_data_set,
                                                              self.__operation_mandatory_fields_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in DMS CHARGE operation!')

    def merchant_order_data_set(self):
        return super(DmsChargeBuilder, self).merchant_order_data_set(self.__operation_data_set)

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in DMS CHARGE operation!')

    def money_data_set(self):
        return super(DmsChargeBuilder, self).money_data_set(self.__operation_data_set,
                                                            self.__operation_mandatory_fields_set)

    def system_data_set(self):
        return super(DmsChargeBuilder, self).system_data_set(self.__operation_data_set)


class DmsCancelBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(DmsCancelBuilder, self).command_data_set(self.__operation_data_set,
                                                              self.__operation_mandatory_fields_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in DMS CANCEL operation!')

    def merchant_order_data_set(self):
        return super(DmsCancelBuilder, self).merchant_order_data_set(self.__operation_data_set)

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in DMS CANCEL operation!')

    def money_data_set(self):
        return super(DmsCancelBuilder, self).money_data_set(self.__operation_data_set,
                                                            self.__operation_mandatory_fields_set)

    def system_data_set(self):
        return super(DmsCancelBuilder, self).system_data_set(self.__operation_data_set)


class MotoSmsBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(MotoSmsBuilder, self).command_data_set(self.__operation_data_set,
                                                            self.__operation_mandatory_fields_set)

    def customer_data_set(self):
        return super(MotoSmsBuilder, self).customer_data_set(self.__operation_data_set)

    def merchant_order_data_set(self):
        return super(MotoSmsBuilder, self).merchant_order_data_set(self.__operation_data_set)

    def payment_method_set(self):
        return super(MotoSmsBuilder, self).payment_method_set(self.__operation_data_set,
                                                              self.__operation_mandatory_fields_set)

    def money_data_set(self):
        return super(MotoSmsBuilder, self).money_data_set(self.__operation_data_set,
                                                          self.__operation_mandatory_fields_set)

    def system_data_set(self):
        return super(MotoSmsBuilder, self).system_data_set(self.__operation_data_set)


class MotoDmsBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(MotoDmsBuilder, self).command_data_set(self.__operation_data_set,
                                                            self.__operation_mandatory_fields_set)

    def customer_data_set(self):
        return super(MotoDmsBuilder, self).customer_data_set(self.__operation_data_set)

    def merchant_order_data_set(self):
        return super(MotoDmsBuilder, self).merchant_order_data_set(self.__operation_data_set)

    def payment_method_set(self):
        return super(MotoDmsBuilder, self).payment_method_set(self.__operation_data_set,
                                                              self.__operation_mandatory_fields_set)

    def money_data_set(self):
        return super(MotoDmsBuilder, self).money_data_set(self.__operation_data_set,
                                                          self.__operation_mandatory_fields_set)

    def system_data_set(self):
        return super(MotoDmsBuilder, self).system_data_set(self.__operation_data_set)


class CreditBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(CreditBuilder, self).command_data_set(self.__operation_data_set,
                                                           self.__operation_mandatory_fields_set)

    def customer_data_set(self):
        return super(CreditBuilder, self).customer_data_set(self.__operation_data_set)

    def merchant_order_data_set(self):
        return super(CreditBuilder, self).merchant_order_data_set(self.__operation_data_set)

    def payment_method_set(self):
        return super(CreditBuilder, self).payment_method_set(self.__operation_data_set,
                                                             self.__operation_mandatory_fields_set)

    def money_data_set(self):
        return super(CreditBuilder, self).money_data_set(self.__operation_data_set,
                                                         self.__operation_mandatory_fields_set)

    def system_data_set(self):
        return super(CreditBuilder, self).system_data_set(self.__operation_data_set)


class P2PBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(P2PBuilder, self).command_data_set(self.__operation_data_set,
                                                        self.__operation_mandatory_fields_set)

    def customer_data_set(self):
        return super(P2PBuilder, self).customer_data_set(self.__operation_data_set)

    def merchant_order_data_set(self):
        return super(P2PBuilder, self).merchant_order_data_set(self.__operation_data_set)

    def payment_method_set(self):
        return super(P2PBuilder, self).payment_method_set(self.__operation_data_set,
                                                          self.__operation_mandatory_fields_set)

    def money_data_set(self):
        return super(P2PBuilder, self).money_data_set(self.__operation_data_set,
                                                      self.__operation_mandatory_fields_set)

    def system_data_set(self):
        return super(P2PBuilder, self).system_data_set(self.__operation_data_set)

class B2PBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(B2PBuilder, self).command_data_set(self.__operation_data_set,
                                                        self.__operation_mandatory_fields_set)

    def customer_data_set(self):
        return super(B2PBuilder, self).customer_data_set(self.__operation_data_set)

    def merchant_order_data_set(self):
        return super(B2PBuilder, self).merchant_order_data_set(self.__operation_data_set)

    def payment_method_set(self):
        return super(B2PBuilder, self).payment_method_set(self.__operation_data_set,
                                                          self.__operation_mandatory_fields_set)

    def money_data_set(self):
        return super(B2PBuilder, self).money_data_set(self.__operation_data_set,
                                                      self.__operation_mandatory_fields_set)

    def system_data_set(self):
        return super(B2PBuilder, self).system_data_set(self.__operation_data_set)

class RecurrentSmsBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(RecurrentSmsBuilder, self).command_data_set(self.__operation_data_set,
                                                                 self.__operation_mandatory_fields_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Recurrent SMS operation!')

    def merchant_order_data_set(self):
        return super(RecurrentSmsBuilder, self).merchant_order_data_set(self.__operation_data_set)

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Recurrent SMS operation!')

    def money_data_set(self):
        return super(RecurrentSmsBuilder, self).money_data_set(self.__operation_data_set,
                                                               self.__operation_mandatory_fields_set)

    def system_data_set(self):
        return super(RecurrentSmsBuilder, self).system_data_set(self.__operation_data_set)


class RecurrentDmsBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(RecurrentDmsBuilder, self).command_data_set(self.__operation_data_set,
                                                                 self.__operation_mandatory_fields_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Recurrent DMS operation!')

    def merchant_order_data_set(self):
        return super(RecurrentDmsBuilder, self).merchant_order_data_set(self.__operation_data_set)

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Recurrent DMS operation!')

    def money_data_set(self):
        return super(RecurrentDmsBuilder, self).money_data_set(self.__operation_data_set,
                                                               self.__operation_mandatory_fields_set)

    def system_data_set(self):
        return super(RecurrentDmsBuilder, self).system_data_set(self.__operation_data_set)


class RefundBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(RefundBuilder, self).command_data_set(self.__operation_data_set,
                                                           self.__operation_mandatory_fields_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Refund operation!')

    def merchant_order_data_set(self):
        return super(RefundBuilder, self).merchant_order_data_set(self.__operation_data_set)

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Refund operation!')

    def money_data_set(self):
        return super(RefundBuilder, self).money_data_set(self.__operation_data_set,
                                                         self.__operation_mandatory_fields_set)

    def system_data_set(self):
        return super(RefundBuilder, self).system_data_set(self.__operation_data_set)


class ReversalBuilder(TransactionTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def command_data_set(self):
        return super(ReversalBuilder, self).command_data_set(self.__operation_data_set,
                                                             self.__operation_mandatory_fields_set)

    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Reversal operation!')

    def merchant_order_data_set(self):
        return super(ReversalBuilder, self).merchant_order_data_set(self.__operation_data_set)

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Reversal operation!')

    def money_data_set(self):
        return super(ReversalBuilder, self).money_data_set(self.__operation_data_set,
                                                           self.__operation_mandatory_fields_set)

    def system_data_set(self):
        return super(ReversalBuilder, self).system_data_set(self.__operation_data_set)


"""
Exploring Past Payments builders
"""


class TransactionStatusBuilder(TransactionTypesResources, ExploringTypesResources):
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def info_command_data_set(self):
        return super(TransactionStatusBuilder, self).info_command_data_set(self.__operation_data_set,
                                                                           self.__operation_mandatory_fields_set)

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
        return super(TransactionStatusBuilder, self).system_data_set(self.__operation_data_set)


class Verify3dBuilder:
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def input_data_set(self):
        from gateway.builders.verify_3d_enrollment_builder import Verify3dEnrollmentBuilder
        return Verify3dEnrollmentBuilder(self.__operation_data_set, self.__operation_mandatory_fields_set)


class VerifyCardBuilder:
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__operation_data_set = __operation_data_set
        self.__operation_mandatory_fields_set = __operation_mandatory_fields

    def data_set(self):
        from gateway.builders.verify_card_data_builder import VerifyCardDataBuilder
        return VerifyCardDataBuilder(self.__operation_data_set, self.__operation_mandatory_fields_set)

