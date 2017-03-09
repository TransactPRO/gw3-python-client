class SystemDataBuilder(object):
    """
    System Data contains IP addresses of cardholders
    """

    __SYSTEM_DATA_KEY = 'system'
    __system_data_structure = {
        __SYSTEM_DATA_KEY: None
    }

    def __init__(self, __builder_data_set):
        from gateway.utils.data_structures import DataStructuresUtils
        from gateway.data_sets.request_parameters import RequestParameters
        self.__data_structure_util = DataStructuresUtils
        self.__req_params = RequestParameters
        self.__payment_data_set = __builder_data_set

    def add_user_ip(self, cardholder_ipv4=None):
        """
        Add cardholder IPv4 address

        Args:
            cardholder_ipv4 (str): Cardholder IPv4 address
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__payment_data_set,
            working_dict=self.__system_data_structure,
            new_key=self.__SYSTEM_DATA_KEY,
            new_dict={self.__req_params.SYSTEM_USER_IP: cardholder_ipv4}
        )

    def add_x_forwarded_for_ip(self, cardholder_ipv4=None):
        """
        Add cardholder real IPv4 address in case of proxy

        Args:
            cardholder_ipv4 (str): Cardholder real IPv4 address in case of proxy
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__payment_data_set,
            working_dict=self.__system_data_structure,
            new_key=self.__SYSTEM_DATA_KEY,
            new_dict={self.__req_params.SYSTEM_X_FORWARDED_FOR: cardholder_ipv4}
        )
