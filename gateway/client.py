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

    __client_operations = {'current': None}

    def __init__(self):
        self.__gate_client_base_structure = {
            self.__AUTH_KEY: None,
            self.__DATA_KEY: None
        }
        self.__dict_of_auth_data_set = {}
        self.__dict_of_operation_data_set = {}
        pass

    def create_auth_data(self):
        """
        Transact Pro Authorization
        Returns:AuthorizationBuilder
          - add_account_id()
          - add_secret_key()
          - add_session_id()
        """
        from gateway.builders.authorization_builder import AuthorizationBuilder
        return AuthorizationBuilder(self.__dict_of_auth_data_set)

    def set_operation(self):
        """
        Transact Pro Gateway 3 APIs operations

        Transactions
          - sms()
          - dms_hold()
          - dms_charge()
          - cancel()
          - moto_sms()
          - moto_dms()
          - recurrent_dms()
          - recurrent_sms()
          - refund()
          - reversal()

        Exploring operations
            - transaction_status()
            - transaction_result()
            - transaction_history()
            - transaction_recurrent_history()
            - transaction_refunds_history()
            - transaction_refunds_history

        Returns:Operations
        """
        from gateway.operations.operations import Operations
        return Operations(self.__dict_of_operation_data_set, self.__client_operations)

    def build_request(self):
        """
        Methods constructs and validate operation data structure for Transact Pro Gateway 3.
        Returns: Dict

        """
        self.__gate_client_base_structure[self.__AUTH_KEY] = self.__dict_of_auth_data_set
        self.__gate_client_base_structure[self.__DATA_KEY] = self.__dict_of_operation_data_set

        # TODO Add validation scheme
        return self.__gate_client_base_structure

    def make_request(self, request_json=None):
        # TODO Add http client
        """
        Transact Pro HTTP Client

        Args:
            request_json (string): Transact Pro request structure
        Returns:
            :return: :class:`Response <Response>` object
        """
        r = requests.post(gateway.API_BASE_URL + self.__client_operations['current'], json=request_json)
        return r
