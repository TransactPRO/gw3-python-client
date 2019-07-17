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


class Operations(object):
    """
    TransactPro Gateway 3 API s operations
    """

    __operation_data = {}
    __asked_operation = None

    # Transactions types routes
    __SMS = '/sms'
    __DMS_HOLD = '/hold-dms'
    __DMS_CHARGE = '/charge-dms'
    __CANCEL = '/cancel'
    __MOTO_SMS = '/moto/sms'
    __MOTO_DMS = '/moto/dms'
    __CREDIT = '/credit'
    __P2P = '/p2p'
    __B2P = '/b2p'
    __INIT_RECURRENTS_SMS = '/recurrent/sms/init'
    __RECURRENTS_SMS = '/recurrent/sms'
    __INIT_RECURRENTS_DMS = '/recurrent/dms/init'
    __RECURRENTS_DMS = '/recurrent/dms'
    __REFUND = '/refund'
    __REVERSAL = '/reversal'
    __TRAN_STATUS = '/status'
    __TRAN_RESULT = '/result'
    __TRAN_HISTORY = '/history'
    __TRAN_RECURRENT_HISTORY = '/recurrents'
    __TRAN_REFUNDS_HISTORY = '/refunds'
    __VERIFY_3D_ENROLLMENT = '/verify/3d-enrollment'
    __VERIFY_CARD = '/verify/card'
    __TOKEN_CREATE = '/token/create'

    def __init__(self, __gate_operation_data_set, __client_operation, __client_mandatory_fields):
        self.__asked_operation = __client_operation
        self.__operation_data = __gate_operation_data_set
        # @TODO __client_mandatory_fields Must be prepare before builders, to avoid missing fields if they not called
        self.__operation_mandatory_fields = __client_mandatory_fields
        pass

    def sms(self):
        """
        Single-Message transactions are used for immediate charge.
        """
        self.__asked_operation['current'] = self.__SMS
        from gateway.builders.transaction_builder import SmsBuilder
        return SmsBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def dms_hold(self):
        """
        This transaction freezes (reserves\hold) funds on cardholder account for feature charge.
        """
        self.__asked_operation['current'] = self.__DMS_HOLD
        from gateway.builders.transaction_builder import DmsHoldBuilder
        return DmsHoldBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def dms_charge(self):
        """
        Immediate charge of previously frozen (reserved\holded)funds.
        """
        self.__asked_operation['current'] = self.__DMS_CHARGE
        from gateway.builders.transaction_builder import DmsChargeBuilder
        return DmsChargeBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def dms_cancel(self):
        """
        Unfreeze previously reserved funds in DMS hold stage
        """
        self.__asked_operation['current'] = self.__CANCEL
        from gateway.builders.transaction_builder import DmsCancelBuilder
        return DmsCancelBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def moto_sms(self):
        """
        MOTO transaction (Mail Order \ Telephone Order) is a type of transaction.
        This is identical as SMS transaction, but requires no CVV code for processing.
        """
        self.__asked_operation['current'] = self.__MOTO_SMS
        from gateway.builders.transaction_builder import MotoSmsBuilder
        return MotoSmsBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def moto_dms(self):
        """
        MOTO transaction (Mail Order \ Telephone Order) is a type of transaction.
        This is identical as DMS-HOLD transaction, but requires no CVV code for processing.
        """
        self.__asked_operation['current'] = self.__MOTO_DMS
        from gateway.builders.transaction_builder import MotoDmsBuilder
        return MotoDmsBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def credit(self):
        """
        Credit transaction is a type of transaction for money send.
        """
        self.__asked_operation['current'] = self.__CREDIT
        from gateway.builders.transaction_builder import CreditBuilder
        return CreditBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def p2p(self):
        """
        P2P transaction is a type of transaction for money send.
        """
        self.__asked_operation['current'] = self.__P2P
        from gateway.builders.transaction_builder import P2PBuilder
        return P2PBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def b2p(self):
        """
        B2P transaction is a type of transaction for money send (Business To Person).
        """
        self.__asked_operation['current'] = self.__B2P
        from gateway.builders.transaction_builder import B2PBuilder
        return B2PBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def init_recurrent_sms(self):
        """
        Init recurrent SMS.
        """
        self.__asked_operation['current'] = self.__INIT_RECURRENTS_SMS
        from gateway.builders.transaction_builder import SmsBuilder
        return SmsBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def recurrent_sms(self):
        """
        Creates a double of previously created and successfully processed transaction
        (either from SMS or DMS-CHARGE) as DMS transaction.
        """
        self.__asked_operation['current'] = self.__RECURRENTS_SMS
        from gateway.builders.transaction_builder import RecurrentSmsBuilder
        return RecurrentSmsBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def init_recurrent_dms(self):
        """
        Init recurrent DMS Hold.
        """
        self.__asked_operation['current'] = self.__INIT_RECURRENTS_DMS
        from gateway.builders.transaction_builder import DmsHoldBuilder
        return DmsHoldBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def recurrent_dms(self):
        """
        Creates a double of previously created and successfully processed transaction
        (either from SMS or DMS-CHARGE) as DMS transaction.
        """
        self.__asked_operation['current'] = self.__RECURRENTS_DMS
        from gateway.builders.transaction_builder import RecurrentDmsBuilder
        return RecurrentDmsBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def refund(self):
        """
        Refund previously successfully executed SMS or DMS-CHARGE transaction.
        """
        self.__asked_operation['current'] = self.__REFUND
        from gateway.builders.transaction_builder import RefundBuilder
        return RefundBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def reversal(self):
        """
        Reverse previously successfully executed SMS or DMS-CHARGE transaction.
        """
        self.__asked_operation['current'] = self.__REVERSAL
        from gateway.builders.transaction_builder import ReversalBuilder
        return ReversalBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def transaction_status(self):
        """
        Returns transaction current status.
        """
        self.__asked_operation['current'] = self.__TRAN_STATUS
        from gateway.builders.transaction_builder import TransactionStatusBuilder
        return TransactionStatusBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def transaction_result(self):
        """
        Returns final result for provided transactions.
        """
        self.__asked_operation['current'] = self.__TRAN_RESULT
        from gateway.builders.transaction_builder import TransactionStatusBuilder
        return TransactionStatusBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def transaction_history(self):
        """
        Returns status history for provided transactions.
        """
        self.__asked_operation['current'] = self.__TRAN_HISTORY
        from gateway.builders.transaction_builder import TransactionStatusBuilder
        return TransactionStatusBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def transaction_recurrent_history(self):
        """
        Returns list of child RECURRENT transactions for provided list of parent transactions.
        """
        self.__asked_operation['current'] = self.__TRAN_RECURRENT_HISTORY
        from gateway.builders.transaction_builder import TransactionStatusBuilder
        return TransactionStatusBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def transaction_refunds_history(self):
        """
        Returns list of child REFUND transactions for provided list of parent transactions.
        """
        self.__asked_operation['current'] = self.__TRAN_REFUNDS_HISTORY
        from gateway.builders.transaction_builder import TransactionStatusBuilder
        return TransactionStatusBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def verify_3d_enrollment(self):
        """
        Verify card 3-D Secure enrollment.
        """
        self.__asked_operation['current'] = self.__VERIFY_3D_ENROLLMENT
        from gateway.builders.transaction_builder import Verify3dBuilder
        return Verify3dBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def verify_card(self):
        """
        Verify card completion request.
        """
        self.__asked_operation['current'] = self.__VERIFY_CARD
        from gateway.builders.transaction_builder import VerifyCardBuilder
        return VerifyCardBuilder(self.__operation_data, self.__operation_mandatory_fields)

    def create_token(self):
        """
        Payment data tokenization request.
        """
        self.__asked_operation['current'] = self.__TOKEN_CREATE
        from gateway.builders.transaction_builder import CreateTokenBuilder
        return CreateTokenBuilder(self.__operation_data, self.__operation_mandatory_fields)
