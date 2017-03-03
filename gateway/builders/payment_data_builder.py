from gateway.data_sets.request_parameters import RequestParameters


class PaymentDataBuilder(object):
    __data_sets = None

    __PAYMENT_METHOD_DATA_KEY = 'payment-method-data'
    __payment_data_structure = {
        __PAYMENT_METHOD_DATA_KEY: None
    }

    def __init__(self, __builder_data_set):
        self.__payment_data_set = __builder_data_set
        self.__data_sets = RequestParameters

    def __update_structure(self, new_data_set):
        if self.__payment_data_structure[self.__PAYMENT_METHOD_DATA_KEY] is None:
            self.__payment_data_structure[self.__PAYMENT_METHOD_DATA_KEY] = new_data_set
        else:
            self.__payment_data_structure[self.__PAYMENT_METHOD_DATA_KEY].update(new_data_set)

        self.__payment_data_set.update(self.__payment_data_structure)

    def add_pan_number(self, pan_number=None):
        """
        Add credit card number

        Args:
            pan_number (str): Credit card number
        """
        self.__update_structure({self.__data_sets.PAYMENT_METHOD_DATA_PAN: pan_number})

    def add_pan_expiry_date(self, mm_yy=None):
        """
        Add credit card expiry date in mm/yy format

        Args:
            mm_yy (str): Credit card expiry date in mm/yy format
        """
        self.__update_structure({self.__data_sets.PAYMENT_METHOD_DATA_EXPIRE: mm_yy})

    def add_pan_cvv_code(self, cvv_number=None):
        """
        Add credit card protection code

        Args:
            cvv_number (str): Credit card protection code
        """
        self.__update_structure({self.__data_sets.PAYMENT_METHOD_DATA_CVV: cvv_number})

    def add_pan_cardholder_name(self, first_last_name=None):
        """
        Add cardholder Name and Surname

        Args:
            first_last_name (str): Cardholder Name and Surname
        """
        self.__update_structure({self.__data_sets.PAYMENT_METHOD_DATA_CARDHOLDER_NAME: first_last_name})
