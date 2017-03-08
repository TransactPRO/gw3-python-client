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
        """
        Make HTTP request via Transact Pro Client

        Args:
            request_json (string): Transact Pro request structure
        Returns:
            :return: :class:`Response <Response>` object
        """
        req_url = gateway.API_BASE_URL + gateway.API_VERSION + self.__client_operations['current']
        if req_url is None:
            raise RuntimeError('Transact PRO API URL empty!')

        from gateway.http_clients.transport import new_http_client

        response = new_http_client().request(
            url=req_url,
            request_data=request_json
        )

        return response
