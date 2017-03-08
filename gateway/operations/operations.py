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
    __RECURRENTS_SMS = '/recurrent/sms'
    __RECURRENTS_DMS = '/recurrent/dms'
    __REFUND = '/refund'
    __REVERSAL = '/reversal'
    __TRAN_STATUS = '/status'
    __TRAN_RESULT = '/result'
    __TRAN_HISTORY = '/history'
    __TRAN_RECURRENT_HISTORY = '/recurrents'
    __TRAN_REFUNDS_HISTORY = '/history'

    def __init__(self, __gate_operation_data_set, __client_operation):
        self.__asked_operation = __client_operation
        self.__operation_data = __gate_operation_data_set
        pass

    def sms(self):
        """
        Single-Message transactions are used for immediate charge.
        """
        self.__asked_operation['current'] = self.__SMS
        from gateway.builders.transaction_builder import SmsBuilder
        return SmsBuilder(self.__operation_data)

    def dms_hold(self):
        """
        This transaction freezes (reserves\hold) funds on cardholder account for feature charge.
        """
        self.__asked_operation['current'] = self.__DMS_HOLD
        from gateway.builders.transaction_builder import DmsHoldBuilder
        return DmsHoldBuilder(self.__operation_data)

    def dms_charge(self):
        """
        Immediate charge of previously frozen (reserved\holded)funds.
        """
        self.__asked_operation['current'] = self.__DMS_CHARGE
        from gateway.builders.transaction_builder import DmsChargeBuilder
        return DmsChargeBuilder(self.__operation_data)

    def dms_cancel(self):
        """
        Unfreeze previously reserved funds in DMS hold stage
        """
        self.__asked_operation['current'] = self.__CANCEL
        from gateway.builders.transaction_builder import DmsCancelBuilder
        return DmsCancelBuilder(self.__operation_data)

    def moto_sms(self):
        """
        MOTO transaction (Mail Order \ Telephone Order) is a type of transaction.
        This is identical as SMS transaction, but requires no CVV code for processing.
        """
        self.__asked_operation['current'] = self.__MOTO_SMS
        from gateway.builders.transaction_builder import MotoSmsBuilder
        return MotoSmsBuilder(self.__operation_data)

    def moto_dms(self):
        """
        MOTO transaction (Mail Order \ Telephone Order) is a type of transaction.
        This is identical as DMS-HOLD transaction, but requires no CVV code for processing.
        """
        self.__asked_operation['current'] = self.__MOTO_DMS
        from gateway.builders.transaction_builder import MotoDmsBuilder
        return MotoDmsBuilder(self.__operation_data)

    def recurrent_sms(self):
        """
        Creates a double of previously created and successfully processed transaction
        (either from SMS or DMS-CHARGE) as DMS transaction.
        """
        self.__asked_operation['current'] = self.__RECURRENTS_DMS
        from gateway.builders.transaction_builder import RecurrentSmsBuilder
        return RecurrentSmsBuilder(self.__operation_data)

    def recurrent_dms(self):
        """
        Creates a double of previously created and successfully processed transaction
        (either from SMS or DMS-CHARGE) as DMS transaction.
        """
        self.__asked_operation['current'] = self.__RECURRENTS_SMS
        from gateway.builders.transaction_builder import RecurrentDmsBuilder
        return RecurrentDmsBuilder(self.__operation_data)

    def refund(self):
        """
        Refund previously successfully executed SMS or DMS-CHARGE transaction.
        """
        self.__asked_operation['current'] = self.__REFUND
        from gateway.builders.transaction_builder import RefundBuilder
        return RefundBuilder(self.__operation_data)

    def reversal(self):
        """
        Reverse previously successfully executed SMS or DMS-CHARGE transaction.
        """
        self.__asked_operation['current'] = self.__REVERSAL
        from gateway.builders.transaction_builder import ReversalBuilder
        return ReversalBuilder(self.__operation_data)

    def transaction_status(self):
        """
        Returns transaction current status.
        """
        self.__asked_operation['current'] = self.__TRAN_STATUS
        from gateway.builders.transaction_builder import TransactionStatusBuilder
        return TransactionStatusBuilder(self.__operation_data)

    def transaction_result(self):
        """
        Returns final result for provided transactions.
        """
        self.__asked_operation['current'] = self.__TRAN_RESULT
        from gateway.builders.transaction_builder import TransactionStatusBuilder
        return TransactionStatusBuilder(self.__operation_data)

    def transaction_history(self):
        """
        Returns status history for provided transactions.
        """
        self.__asked_operation['current'] = self.__TRAN_HISTORY
        from gateway.builders.transaction_builder import TransactionStatusBuilder
        return TransactionStatusBuilder(self.__operation_data)

    def transaction_recurrent_history(self):
        """
        Returns list of child RECURRENT transactions for provided list of parent transactions.
        """
        self.__asked_operation['current'] = self.__TRAN_RECURRENT_HISTORY
        from gateway.builders.transaction_builder import TransactionStatusBuilder
        return TransactionStatusBuilder(self.__operation_data)

    def transaction_refunds_history(self):
        """
        Returns list of child REFUND transactions for provided list of parent transactions.
        """
        self.__asked_operation['current'] = self.__TRAN_REFUNDS_HISTORY
        from gateway.builders.transaction_builder import TransactionStatusBuilder
        return TransactionStatusBuilder(self.__operation_data)
