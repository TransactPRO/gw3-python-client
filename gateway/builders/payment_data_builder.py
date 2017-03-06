class PaymentDataBuilder(object):
    """
    Payment data - information about credit card
    """
    __PAYMENT_METHOD_DATA_KEY = 'payment-method-data'
    __payment_data_structure = {
        __PAYMENT_METHOD_DATA_KEY: None
    }

    def __init__(self, __transaction_data_set):
        from gateway.utils.data_structures_utils import DataStructuresUtils
        from gateway.data_sets.request_parameters import RequestParameters
        self.__data_structure_util = DataStructuresUtils
        self.__req_params = RequestParameters
        self.__payment_data_set = __transaction_data_set

    def add_pan_number(self, pan_number=None):
        """
        Add credit card number

        Args:
            pan_number (str): Credit card number
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__payment_data_set,
            working_dict=self.__payment_data_structure,
            new_key=self.__PAYMENT_METHOD_DATA_KEY,
            new_dict={self.__req_params.PAYMENT_METHOD_DATA_PAN: pan_number}
        )

    def add_pan_expiry_date(self, mm_yy=None):
        """
        Add credit card expiry date in mm/yy format

        Args:
            mm_yy (str): Credit card expiry date in mm/yy format
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__payment_data_set,
            working_dict=self.__payment_data_structure,
            new_key=self.__PAYMENT_METHOD_DATA_KEY,
            new_dict={self.__req_params.PAYMENT_METHOD_DATA_EXPIRE: mm_yy}
        )

    def add_pan_cvv_code(self, cvv_number=None):
        """
        Add credit card protection code

        Args:
            cvv_number (str): Credit card protection code
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__payment_data_set,
            working_dict=self.__payment_data_structure,
            new_key=self.__PAYMENT_METHOD_DATA_KEY,
            new_dict={self.__req_params.PAYMENT_METHOD_DATA_CVV: cvv_number}
        )

    def add_pan_cardholder_name(self, first_last_name=None):
        """
        Add cardholder Name and Surname

        Args:
            first_last_name (str): Cardholder Name and Surname
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__payment_data_set,
            working_dict=self.__payment_data_structure,
            new_key=self.__PAYMENT_METHOD_DATA_KEY,
            new_dict={self.__req_params.PAYMENT_METHOD_DATA_CARDHOLDER_NAME: first_last_name}
        )
