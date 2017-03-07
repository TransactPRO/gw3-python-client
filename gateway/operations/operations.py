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
    __RECURRENTS = '/recurrent/dms'

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
