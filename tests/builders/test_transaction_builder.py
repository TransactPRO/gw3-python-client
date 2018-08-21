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

from gateway.builders.transaction_builder import (
    TransactionTypesResources,
    ExploringTypesResources,
    SmsBuilder,
    DmsHoldBuilder,
    DmsChargeBuilder,
    DmsCancelBuilder,
    MotoSmsBuilder,
    MotoDmsBuilder,
    CreditBuilder,
    P2PBuilder,
    B2PBuilder,
    RecurrentSmsBuilder,
    RecurrentDmsBuilder,
    RefundBuilder,
    ReversalBuilder,
    TransactionStatusBuilder,
    Verify3dBuilder
)
from gateway.builders.command_data_builder import CommandDataBuilder
from gateway.builders.customer_data_builder import CustomerDataBuilder
from gateway.builders.merchant_order_builder import MerchantOrderBuilder
from gateway.builders.payment_data_builder import PaymentDataBuilder
from gateway.builders.system_data_builder import SystemDataBuilder
from gateway.builders.money_data_builder import MoneyDataBuilder
from gateway.builders.info_data_builder import InfoDataBuilder
from gateway.builders.data_builder import DataBuilder
from unittest import TestCase


class TestTransactionBuilder(TestCase):
    def test_dependency_construction_sms(self):
        new = SmsBuilder({}, {})
        self.assertIsInstance(new, SmsBuilder)
        self.assertIsInstance(new, TransactionTypesResources)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.customer_data_set(), CustomerDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertIsInstance(new.payment_method_set(), PaymentDataBuilder)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_dms_hold(self):
        new = DmsHoldBuilder({}, {})
        self.assertIsInstance(new, DmsHoldBuilder)
        self.assertIsInstance(new, TransactionTypesResources)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.customer_data_set(), CustomerDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertIsInstance(new.payment_method_set(), PaymentDataBuilder)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_dms_charge(self):
        new = DmsChargeBuilder({}, {})
        self.assertIsInstance(new, DmsChargeBuilder)
        self.assertIsInstance(new, TransactionTypesResources)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertRaises(NotImplementedError, new.customer_data_set)
        self.assertRaises(NotImplementedError, new.merchant_order_data_set)
        self.assertRaises(NotImplementedError, new.payment_method_set)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_dms_cancel(self):
        new = DmsCancelBuilder({}, {})
        self.assertIsInstance(new, DmsCancelBuilder)
        self.assertIsInstance(new, TransactionTypesResources)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertRaises(NotImplementedError, new.customer_data_set)
        self.assertRaises(NotImplementedError, new.merchant_order_data_set)
        self.assertRaises(NotImplementedError, new.payment_method_set)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_moto_sms(self):
        new = MotoSmsBuilder({}, {})
        self.assertIsInstance(new, MotoSmsBuilder)
        self.assertIsInstance(new, TransactionTypesResources)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.customer_data_set(), CustomerDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertIsInstance(new.payment_method_set(), PaymentDataBuilder)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_moto_dms(self):
        new = MotoDmsBuilder({}, {})
        self.assertIsInstance(new, MotoDmsBuilder)
        self.assertIsInstance(new, TransactionTypesResources)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.customer_data_set(), CustomerDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertIsInstance(new.payment_method_set(), PaymentDataBuilder)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_credit(self):
        new = CreditBuilder({}, {})
        self.assertIsInstance(new, CreditBuilder)
        self.assertIsInstance(new, TransactionTypesResources)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.customer_data_set(), CustomerDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertIsInstance(new.payment_method_set(), PaymentDataBuilder)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_p2p(self):
        new = P2PBuilder({}, {})
        self.assertIsInstance(new, P2PBuilder)
        self.assertIsInstance(new, TransactionTypesResources)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.customer_data_set(), CustomerDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertIsInstance(new.payment_method_set(), PaymentDataBuilder)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_b2p(self):
        new = B2PBuilder({}, {})
        self.assertIsInstance(new, B2PBuilder)
        self.assertIsInstance(new, TransactionTypesResources)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.customer_data_set(), CustomerDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertIsInstance(new.payment_method_set(), PaymentDataBuilder)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_recurrent_sms(self):
        new = RecurrentSmsBuilder({}, {})
        self.assertIsInstance(new, RecurrentSmsBuilder)
        self.assertIsInstance(new, TransactionTypesResources)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertRaises(NotImplementedError, new.customer_data_set)
        self.assertRaises(NotImplementedError, new.payment_method_set)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_recurrent_dms(self):
        new = RecurrentDmsBuilder({}, {})
        self.assertIsInstance(new, RecurrentDmsBuilder)
        self.assertIsInstance(new, TransactionTypesResources)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertRaises(NotImplementedError, new.customer_data_set)
        self.assertRaises(NotImplementedError, new.payment_method_set)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_refund(self):
        new = RefundBuilder({}, {})
        self.assertIsInstance(new, RefundBuilder)
        self.assertIsInstance(new, TransactionTypesResources)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertRaises(NotImplementedError, new.customer_data_set)
        self.assertRaises(NotImplementedError, new.merchant_order_data_set)
        self.assertRaises(NotImplementedError, new.payment_method_set)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_reversal(self):
        new = ReversalBuilder({}, {})
        self.assertIsInstance(new, ReversalBuilder)
        self.assertIsInstance(new, TransactionTypesResources)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertRaises(NotImplementedError, new.customer_data_set)
        self.assertRaises(NotImplementedError, new.merchant_order_data_set)
        self.assertRaises(NotImplementedError, new.payment_method_set)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_transaction_status(self):
        new = TransactionStatusBuilder({}, {})
        self.assertIsInstance(new, TransactionStatusBuilder)
        self.assertIsInstance(new, TransactionTypesResources)
        self.assertIsInstance(new, ExploringTypesResources)
        self.assertIsInstance(new.info_command_data_set(), InfoDataBuilder)
        self.assertRaises(NotImplementedError, new.command_data_set)
        self.assertRaises(NotImplementedError, new.customer_data_set)
        self.assertRaises(NotImplementedError, new.merchant_order_data_set)
        self.assertRaises(NotImplementedError, new.payment_method_set)
        self.assertRaises(NotImplementedError, new.money_data_set)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_verify_3d_enrollment(self):
        new = Verify3dBuilder({}, {})
        self.assertIsInstance(new, Verify3dBuilder)
        self.assertIsInstance(new, TransactionTypesResources)
        self.assertIsInstance(new, ExploringTypesResources)
        self.assertIsInstance(new.input_data_set(), DataBuilder)
