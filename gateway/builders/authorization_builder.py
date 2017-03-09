class AuthorizationBuilder(object):
    def __init__(self, __client_auth_data_set, __client_mandatory_fields):
        from gateway.data_sets.request_parameters import (
            RequestParameters,
            RequestParametersTypes
        )
        self.__data_sets = RequestParameters
        self.__data_types = RequestParametersTypes
        self.__auth_mandatory_fields = __client_mandatory_fields
        self.__auth_data_set = __client_auth_data_set

    def add_account_id(self, id_number=None):
        """
        Transact Pro Merchant Account ID.

        Args:
            id_number (int): Transact Pro Merchant Account ID.
        """
        self.__auth_mandatory_fields[self.__data_sets.AUTH_DATA_ACCOUNT_ID] = self.__data_types.AUTH_DATA_ACCOUNT_ID
        self.__auth_data_set[self.__data_sets.AUTH_DATA_ACCOUNT_ID] = id_number

    def add_secret_key(self, value=None):
        """
        Transact Pro Merchant Password

        Args:
            value (str): Transact Pro Merchant Password
        """
        self.__auth_mandatory_fields[self.__data_sets.AUTH_DATA_SECRET_KEY] = self.__data_types.AUTH_DATA_SECRET_KEY
        self.__auth_data_set[self.__data_sets.AUTH_DATA_SECRET_KEY] = value

    def add_session_id(self, id_value=None):
        """
        Transact Pro Gateway Session ID

        Args:
            id_value (str): Transact Pro Gateway Session ID
        """
        self.__auth_data_set[self.__data_sets.AUTH_DATA_SECRET_KEY] = id_value
