class Operations(object):
    """
    TransactPro Gateway 3 API s operations
    """

    __operation_data = {}
    __asked_operation = None

    # Transactions types
    SMS = '/sms'
    DMS_HOLD = '/hold-dms'
    DMS_CHARGE = '/charge-dms'
    CANCEL = '/cancel'
    MOTO_SMS = '/moto/sms'
    MOTO_DMS = '/moto/dms'

    def __init__(self, __gate_operation_data_set, __client_operations):
        self.__asked_operations_dict = __client_operations
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
        self.__asked_operations_dict['current'] = self.SMS
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
        self.__asked_operations_dict['current'] = self.DMS_HOLD
        from gateway.builders.transaction_builder import DmsHoldBuilder
        return DmsHoldBuilder(self.__operation_data)

    def dms_charge(self):
        """
        Immediate charge of previously frozen (reserved\holded)funds.

        Callable public methods

        command_data_set()
        money_data_set()
        """
        self.__asked_operations_dict['current'] = self.DMS_CHARGE
        from gateway.builders.transaction_builder import DmsChargeBuilder
        return DmsChargeBuilder(self.__operation_data)
