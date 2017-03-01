from gateway.data_sets.request_parameters import RequestParameters


class AuthorizationBuilder(object):
    __data_sets = None
    __auth_data_set = {}

    def __init__(self, __gate_auth_data_set, __gate_validation_list):
        self.__data_sets = RequestParameters
        self.__auth_data_set = __gate_auth_data_set

        # Add mandatory fields to validate it
        self.__add_mandatory_fields(__gate_validation_list)

    def __add_mandatory_fields(self, mandatory_list):
        mandatory_list.append(self.__data_sets.AUTH_DATA_ACCOUNT_ID)
        mandatory_list.append(self.__data_sets.AUTH_DATA_SECRET_KEY)

    def add_account_id(self, account_id=None):
        """
        Transact Pro Merchant Account ID.

        Args:
            account_id (int): Transact Pro Merchant Account ID.
        """
        self.__auth_data_set[self.__data_sets.AUTH_DATA_ACCOUNT_ID] = account_id

    def add_secret_key(self, secret_key=None):
        """
        Transact Pro Merchant Password

        Args:
            secret_key (str): Transact Pro Merchant Password
        """
        self.__auth_data_set[self.__data_sets.AUTH_DATA_SECRET_KEY] = secret_key

    def add_session_id(self, session_id=None):
        """
        Transact Pro Gateway Session ID

        Args:
            session_id (str): Transact Pro Gateway Session ID
        """
        self.__auth_data_set[self.__data_sets.AUTH_DATA_SECRET_KEY] = session_id

    def get_data_set(self):
        """
        Returns prepared auth data set

        Returns:
        Dicts: Auth data set
        """

        return self.__auth_data_set
