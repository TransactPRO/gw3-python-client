class SystemDataBuilder(object):
    """
    System Data contains IP addresses of cardholders
    """

    __SYSTEM_DATA_KEY = 'system'
    __system_data_structure = {
        __SYSTEM_DATA_KEY: None
    }

    def __init__(self, __client_transaction_data_set, __client_mandatory_fields):
        from gateway.utils.data_structures import DataStructuresUtils
        from gateway.data_sets.request_parameters import (
            RequestParameters,
            RequestParametersTypes
        )
        self.__data_structure_util = DataStructuresUtils
        self.__data_types = RequestParametersTypes
        self.__data_sets = RequestParameters
        self.__system_data_set = __client_transaction_data_set
        self.__system_mandatory_fields = __client_mandatory_fields

    def add_user_ip(self, cardholder_ipv4=None):
        """
        Add cardholder IPv4 address

        Args:
            cardholder_ipv4 (str): Cardholder IPv4 address
        """
        self.__system_mandatory_fields[
            self.__data_sets.SYSTEM_USER_IP
        ] = self.__data_types.SYSTEM_USER_IP

        self.__data_structure_util.add_to_dict(
            source_dict=self.__system_data_set,
            working_dict=self.__system_data_structure,
            new_key=self.__SYSTEM_DATA_KEY,
            new_dict={self.__data_sets.SYSTEM_USER_IP: cardholder_ipv4}
        )

    def add_x_forwarded_for_ip(self, cardholder_ipv4=None):
        """
        Add cardholder real IPv4 address in case of proxy

        Args:
            cardholder_ipv4 (str): Cardholder real IPv4 address in case of proxy
        """
        self.__system_mandatory_fields[
            self.__data_sets.SYSTEM_USER_IP
        ] = self.__data_types.SYSTEM_USER_IP

        self.__data_structure_util.add_to_dict(
            source_dict=self.__system_data_set,
            working_dict=self.__system_data_structure,
            new_key=self.__SYSTEM_DATA_KEY,
            new_dict={self.__data_sets.SYSTEM_X_FORWARDED_FOR: cardholder_ipv4}
        )
