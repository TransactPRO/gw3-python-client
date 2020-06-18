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

from unittest import TestCase

from gateway.builders.transaction_builder import *
from gateway.builders.verify_3d_enrollment_builder import Verify3dEnrollmentBuilder
from gateway.builders.verify_card_data_builder import VerifyCardDataBuilder


class TestTransactionBuilder(TestCase):
    def test_dependency_construction_sms(self):
        new = SmsBuilder({}, {})
        self.assertIsInstance(new, SmsBuilder)
        self.assertIsInstance(new, TransactionBuilder)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.customer_data_set(), CustomerDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertIsInstance(new.payment_method_set(), PaymentDataBuilder)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_dms_hold(self):
        new = DmsHoldBuilder({}, {})
        self.assertIsInstance(new, DmsHoldBuilder)
        self.assertIsInstance(new, TransactionBuilder)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.customer_data_set(), CustomerDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertIsInstance(new.payment_method_set(), PaymentDataBuilder)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_dms_charge(self):
        new = DmsChargeBuilder({}, {})
        self.assertIsInstance(new, DmsChargeBuilder)
        self.assertIsInstance(new, TransactionBuilder)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertRaises(NotImplementedError, new.customer_data_set)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertRaises(NotImplementedError, new.payment_method_set)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_dms_cancel(self):
        new = DmsCancelBuilder({}, {})
        self.assertIsInstance(new, DmsCancelBuilder)
        self.assertIsInstance(new, TransactionBuilder)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertRaises(NotImplementedError, new.customer_data_set)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertRaises(NotImplementedError, new.payment_method_set)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_moto_sms(self):
        new = MotoSmsBuilder({}, {})
        self.assertIsInstance(new, MotoSmsBuilder)
        self.assertIsInstance(new, TransactionBuilder)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.customer_data_set(), CustomerDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertIsInstance(new.payment_method_set(), PaymentDataBuilder)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_moto_dms(self):
        new = MotoDmsBuilder({}, {})
        self.assertIsInstance(new, MotoDmsBuilder)
        self.assertIsInstance(new, TransactionBuilder)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.customer_data_set(), CustomerDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertIsInstance(new.payment_method_set(), PaymentDataBuilder)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_credit(self):
        new = CreditBuilder({}, {})
        self.assertIsInstance(new, CreditBuilder)
        self.assertIsInstance(new, TransactionBuilder)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.customer_data_set(), CustomerDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertIsInstance(new.payment_method_set(), PaymentDataBuilder)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_p2p(self):
        new = P2PBuilder({}, {})
        self.assertIsInstance(new, P2PBuilder)
        self.assertIsInstance(new, TransactionBuilder)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.customer_data_set(), CustomerDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertIsInstance(new.payment_method_set(), PaymentDataBuilder)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_b2p(self):
        new = B2PBuilder({}, {})
        self.assertIsInstance(new, B2PBuilder)
        self.assertIsInstance(new, TransactionBuilder)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.customer_data_set(), CustomerDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertIsInstance(new.payment_method_set(), PaymentDataBuilder)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_recurrent_sms(self):
        new = RecurrentSmsBuilder({}, {})
        self.assertIsInstance(new, RecurrentSmsBuilder)
        self.assertIsInstance(new, TransactionBuilder)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertRaises(NotImplementedError, new.customer_data_set)
        self.assertRaises(NotImplementedError, new.payment_method_set)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_recurrent_dms(self):
        new = RecurrentDmsBuilder({}, {})
        self.assertIsInstance(new, RecurrentDmsBuilder)
        self.assertIsInstance(new, TransactionBuilder)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertRaises(NotImplementedError, new.customer_data_set)
        self.assertRaises(NotImplementedError, new.payment_method_set)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_refund(self):
        new = RefundBuilder({}, {})
        self.assertIsInstance(new, RefundBuilder)
        self.assertIsInstance(new, TransactionBuilder)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertRaises(NotImplementedError, new.customer_data_set)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertRaises(NotImplementedError, new.payment_method_set)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_reversal(self):
        new = ReversalBuilder({}, {})
        self.assertIsInstance(new, ReversalBuilder)
        self.assertIsInstance(new, TransactionBuilder)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertRaises(NotImplementedError, new.customer_data_set)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertRaises(NotImplementedError, new.payment_method_set)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_transaction_status(self):
        new = TransactionStatusBuilder({}, {})
        self.assertIsInstance(new, ExploringBuilder)
        self.assertIsInstance(new.info_command_data_set(), InfoDataBuilder)

    def test_dependency_construction_transaction_result(self):
        new = TransactionResultBuilder({}, {})
        self.assertIsInstance(new, ExploringBuilder)
        self.assertIsInstance(new.info_command_data_set(), InfoDataBuilder)

    def test_dependency_construction_transaction_refunds(self):
        new = TransactionRefundsHistoryBuilder({}, {})
        self.assertIsInstance(new, ExploringBuilder)
        self.assertIsInstance(new.info_command_data_set(), InfoDataBuilder)

    def test_dependency_construction_transaction_recurring(self):
        new = TransactionRecurringHistoryBuilder({}, {})
        self.assertIsInstance(new, ExploringBuilder)
        self.assertIsInstance(new.info_command_data_set(), InfoDataBuilder)

    def test_dependency_construction_transaction_history(self):
        new = TransactionHistoryBuilder({}, {})
        self.assertIsInstance(new, ExploringBuilder)
        self.assertIsInstance(new.info_command_data_set(), InfoDataBuilder)

    def test_dependency_construction_verify_3d_enrollment(self):
        new = Verify3dBuilder({}, {})
        self.assertIsInstance(new, Verify3dBuilder)
        self.assertIsInstance(new.input_data_set(), Verify3dEnrollmentBuilder)

    def test_dependency_construction_verify_card(self):
        new = VerifyCardBuilder({}, {})
        self.assertIsInstance(new, VerifyCardBuilder)
        self.assertIsInstance(new.data_set(), VerifyCardDataBuilder)

    def test_dependency_construction_create_token(self):
        new = CreateTokenBuilder({}, {})
        self.assertIsInstance(new, CreateTokenBuilder)
        self.assertIsInstance(new, TransactionBuilder)
        self.assertIsInstance(new.command_data_set(), CommandDataBuilder)
        self.assertIsInstance(new.merchant_order_data_set(), MerchantOrderBuilder)
        self.assertIsInstance(new.payment_method_set(), PaymentDataBuilder)
        self.assertIsInstance(new.money_data_set(), MoneyDataBuilder)
        self.assertIsInstance(new.system_data_set(), SystemDataBuilder)

    def test_dependency_construction_report(self):
        new = ReportBuilder({}, {})
        self.assertIsInstance(new.filter_data(), ReportFilterDataBuilder)
