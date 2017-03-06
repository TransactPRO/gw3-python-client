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

    def __init__(self, __gate_operation_data_set, __client_operations):
        self.__asked_operation = __client_operations
        self.__operation_data = __gate_operation_data_set
        pass

    def sms(self):
        """
        Single-Message transactions are used for immediate charge.

        Callable public methods

        payment_method_set()
        money_data_set()
        system_data_set()
        """
        self.__asked_operation = self.__SMS
        from gateway.builders.transaction_builder import SmsBuilder
        return SmsBuilder(self.__operation_data)

    def dms_hold(self):
        """
        This transaction freezes (reserves\hold) funds on cardholder account for feature charge.

        Callable public methods

        payment_method_set()
        money_data_set()
        system_data_set()
        """
        self.__asked_operation = self.__DMS_HOLD
        from gateway.builders.transaction_builder import DmsHoldBuilder
        return DmsHoldBuilder(self.__operation_data)

    def dms_charge(self):
        """
        Immediate charge of previously frozen (reserved\holded)funds.

        Callable public methods

        command_data_set()
        money_data_set()
        """
        self.__asked_operation = self.__DMS_CHARGE
        from gateway.builders.transaction_builder import DmsChargeBuilder
        return DmsChargeBuilder(self.__operation_data)
