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


from gateway.operations.operations import Operations
from unittest import TestCase
from unittest.mock import (
    patch,
    Mock
)


class TestOperations(TestCase):
    OP = None

    def setUp(self):
        self.OP = Operations({}, {}, {})

    def test_call_sms(self):
        new_op = self.OP
        from gateway.builders.transaction_builder import SmsBuilder
        self.assertIsInstance(new_op.sms(), SmsBuilder)

        with patch.object(new_op, 'sms') as mock:
            new_op.sms()

        mock.assert_called_once_with()

    def test_call_dms_hold(self):
        new_op = self.OP
        from gateway.builders.transaction_builder import DmsHoldBuilder
        self.assertIsInstance(new_op.dms_hold(), DmsHoldBuilder)

        with patch.object(new_op, 'dms_hold') as mock:
            new_op.dms_hold()

        mock.assert_called_once_with()

    def test_call_dms_charge(self):
        new_op = self.OP
        from gateway.builders.transaction_builder import DmsChargeBuilder
        self.assertIsInstance(new_op.dms_charge(), DmsChargeBuilder)

        with patch.object(new_op, 'dms_charge') as mock:
            new_op.dms_charge()

        mock.assert_called_once_with()

    def test_call_dms_cancel(self):
        new_op = self.OP
        from gateway.builders.transaction_builder import DmsCancelBuilder
        self.assertIsInstance(new_op.dms_cancel(), DmsCancelBuilder)

        with patch.object(new_op, 'dms_cancel') as mock:
            new_op.dms_cancel()

        mock.assert_called_once_with()

    def test_call_moto_sms(self):
        new_op = self.OP
        from gateway.builders.transaction_builder import MotoSmsBuilder
        self.assertIsInstance(new_op.moto_sms(), MotoSmsBuilder)

        with patch.object(new_op, 'moto_sms') as mock:
            new_op.moto_sms()

        mock.assert_called_once_with()

    def test_call_moto_dms(self):
        new_op = self.OP
        from gateway.builders.transaction_builder import MotoDmsBuilder
        self.assertIsInstance(new_op.moto_dms(), MotoDmsBuilder)

        with patch.object(new_op, 'moto_dms') as mock:
            new_op.moto_dms()

        mock.assert_called_once_with()

    def test_call_recurrent_sms(self):
        new_op = self.OP
        from gateway.builders.transaction_builder import RecurrentSmsBuilder
        self.assertIsInstance(new_op.recurrent_sms(), RecurrentSmsBuilder)

        with patch.object(new_op, 'recurrent_sms') as mock:
            new_op.recurrent_sms()

        mock.assert_called_once_with()

    def test_call_recurrent_dms(self):
        new_op = self.OP
        from gateway.builders.transaction_builder import RecurrentDmsBuilder
        self.assertIsInstance(new_op.recurrent_dms(), RecurrentDmsBuilder)

        with patch.object(new_op, 'recurrent_dms') as mock:
            new_op.recurrent_dms()

        mock.assert_called_once_with()

    def test_call_refund(self):
        new_op = self.OP
        from gateway.builders.transaction_builder import RefundBuilder
        self.assertIsInstance(new_op.refund(), RefundBuilder)

        with patch.object(new_op, 'refund') as mock:
            new_op.refund()

        mock.assert_called_once_with()

    def test_call_reversal(self):
        new_op = self.OP
        from gateway.builders.transaction_builder import ReversalBuilder
        self.assertIsInstance(new_op.reversal(), ReversalBuilder)

        with patch.object(new_op, 'reversal') as mock:
            new_op.reversal()

        mock.assert_called_once_with()

    def test_call_transaction_status(self):
        new_op = self.OP
        from gateway.builders.transaction_builder import TransactionStatusBuilder
        self.assertIsInstance(new_op.transaction_status(), TransactionStatusBuilder)

        with patch.object(new_op, 'transaction_status') as mock:
            new_op.transaction_status()

        mock.assert_called_once_with()

    def test_call_transaction_result(self):
        new_op = self.OP
        from gateway.builders.transaction_builder import TransactionStatusBuilder
        self.assertIsInstance(new_op.transaction_result(), TransactionStatusBuilder)

        with patch.object(new_op, 'transaction_result') as mock:
            new_op.transaction_result()

        mock.assert_called_once_with()

    def test_call_transaction_history(self):
        new_op = self.OP
        from gateway.builders.transaction_builder import TransactionStatusBuilder
        self.assertIsInstance(new_op.transaction_history(), TransactionStatusBuilder)

        with patch.object(new_op, 'transaction_history') as mock:
            new_op.transaction_history()

        mock.assert_called_once_with()

    def test_call_transaction_recurrent_history(self):
        new_op = self.OP
        from gateway.builders.transaction_builder import TransactionStatusBuilder
        self.assertIsInstance(new_op.transaction_recurrent_history(), TransactionStatusBuilder)

        with patch.object(new_op, 'transaction_recurrent_history') as mock:
            new_op.transaction_recurrent_history()

        mock.assert_called_once_with()

    def test_call_transaction_refunds_history(self):
        new_op = self.OP
        from gateway.builders.transaction_builder import TransactionStatusBuilder
        self.assertIsInstance(new_op.transaction_refunds_history(), TransactionStatusBuilder)

        with patch.object(new_op, 'transaction_refunds_history') as mock:
            new_op.transaction_refunds_history()

        mock.assert_called_once_with()
