"""
Transact Pro Payment Gateway integration library.
"""

import requests
import gateway


class Client:
    """
    Main Gate client class for using TransactPro API

    Before starting you need to have a valid Account ID and a Secret Key.
    This information must be provided after successful registration in Transact Pro system.
    """

    # Request structure
    __AUTH_KEY = 'auth-data'
    __DATA_KEY = 'data'
    __gate_client_request = {
        __AUTH_KEY: None,
        __DATA_KEY: None
    }

    __client_operation = None

    def __init__(self):
        self.__dict_of_auth_data_set = {}
        self.__dict_of_operation_data_set = {}
        pass

    def create_auth_data(self):
        from gateway.builders.authorization_builder import AuthorizationBuilder
        return AuthorizationBuilder(self.__dict_of_auth_data_set)

    def set_operation(self):
        from gateway.operations.operations import Operations
        return Operations(self.__dict_of_operation_data_set, self.__client_operation)

    def build_request(self):
        self.__gate_client_request[self.__AUTH_KEY] = self.__dict_of_auth_data_set
        self.__gate_client_request[self.__DATA_KEY] = self.__dict_of_operation_data_set

        # TODO Add validation scheme
        return self.__gate_client_request

    def make_request(self, request_json=None):
        # TODO Add http client
        """
        Request data  in json format, for Transact Pro API

        Args:
            request_json (string): Transact Pro Merchant Account ID.
        Returns:
            :return: :class:`Response <Response>` object
        """
        r = requests.post(gateway.API_BASE_URL + self.__client_operation, json=request_json)
        return r
