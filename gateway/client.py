# The MIT License
#
# Copyright (c) 2017 Transact Pro.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import json

import gateway
from gateway.builders.authorization_builder import AuthorizationBuilder
from gateway.crypto.digest import RequestDigest, ResponseDigest
from gateway.data_sets.request_parameters import RequestParameters
from gateway.transport.transport import HTTP_POST, new_http_client, HTTP_GET
from gateway.operations.operations import Operations
from gateway.responses.response import GatewayResponse


class Client:
    """
    Main Gate client class for using TransactPro API

    Before starting you need to have a valid GUID and a Secret Key.
    This information must be provided after successful registration in Transact Pro system.

    NB. Client instance cannot be used asynchronously as it saves its internal state through an operation!
    """

    # Request structure
    __AUTH_KEY = 'auth-data'
    __DATA_KEY = 'data'
    __FILTER_DATA_KEY = 'filter-data'

    def __init__(self):
        # Stores's collected auth data
        self.__dict_of_auth_data_set = {}
        self.__reset_data()
        self.__authorization_builder = AuthorizationBuilder(self.__dict_of_auth_data_set, self.__required_parameters_for_operation)

    def __reset_data(self):
        # Stores's asked operation
        self.__client_operations = {'current': None, 'method': HTTP_POST}
        # Stores's collected required parameters for valid request
        self.__required_parameters_for_operation = {}
        # Base request structure
        self.__gate_client_base_structure = {}
        # Stores's collected operation data sets
        self.__dict_of_operation_data_set = {}

    def create_auth_data(self) -> AuthorizationBuilder:
        """
        Transact Pro Authorization
        Returns: AuthorizationBuilder
          - add_merchant_guid()
          - add_account_guid()
          - add_secret_key()
          - add_session_id()
        """
        return self.__authorization_builder

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
          - credit()
          - p2p()
          - b2p()
          - init_recurrent_dms()
          - recurrent_dms()
          - init_recurrent_sms()
          - recurrent_sms()
          - refund()
          - reversal()

        Exploring operations
            - transaction_status()
            - transaction_result()
            - transaction_history()
            - transaction_recurrent_history()
            - transaction_refunds_history()
            - limits()

        Verifications:
            - verify_3d_enrollment()
            - verify_card()

        Tokenization:
            - create_token()

        Reporting:
            - report()

        Helpers:
            - retrieve_form()

        Returns: Operations
        """
        self.__reset_data()
        return Operations(self.__dict_of_operation_data_set, self.__client_operations, self.__required_parameters_for_operation)

    def build_request(self):
        """
        Methods constructs and validate operation data structure for Transact Pro Gateway 3.
        Returns: Dict
        """
        from gateway.data_sets.request_parameters import RequestParameters
        if RequestParameters.AUTH_DATA_SESSION_ID in self.__dict_of_auth_data_set:
            self.__gate_client_base_structure[self.__AUTH_KEY] = {
                RequestParameters.AUTH_DATA_SESSION_ID: self.__dict_of_auth_data_set[RequestParameters.AUTH_DATA_SESSION_ID]
            }

        if self.__client_operations['current'] == '/report':
            self.__gate_client_base_structure[self.__FILTER_DATA_KEY] = self.__dict_of_operation_data_set
        else:
            self.__gate_client_base_structure[self.__DATA_KEY] = self.__dict_of_operation_data_set

        from gateway.utils.data_validator import DataValidator
        validator_response = DataValidator().validate_request_data(
            required_data=self.__required_parameters_for_operation,
            request_data=self.__gate_client_base_structure
        )

        if validator_response:
            raise RuntimeError('Validation failed in request data:', validator_response)

        return self.__gate_client_base_structure

    def make_request(self, request_data=None) -> GatewayResponse:
        """
        Make HTTP request via Transact Pro HttpTransport

        Args:
            request_data (dict): Transact Pro request structure

        Response tuple (HTTP Content, HTTP Status code, HTTP Headers)

        Returns:
            GatewayResponse
        """
        if self.__client_operations['current'] == '/report':
            req_url = gateway.API_BASE_URL.rstrip('/') + self.__client_operations['current']
        elif str(self.__client_operations['current']).startswith('http'):
            req_url = self.__client_operations['current']
        else:
            req_url = gateway.API_BASE_URL + gateway.API_VERSION + self.__client_operations['current']

        if req_url is None:
            raise RuntimeError('Transact PRO API URL Empty!')

        if self.__client_operations['method'] != HTTP_GET:
            if request_data is None or len(request_data) < 1:
                raise RuntimeError("Request data invalid, is empty")

            if type(request_data) is not dict:
                raise RuntimeError('Request data invalid, must be dict')

        guid = AuthorizationBuilder.get_object_guid(self.__dict_of_auth_data_set)
        secret = self.__dict_of_auth_data_set[RequestParameters.AUTH_DATA_SECRET_KEY]
        digest = RequestDigest(username=guid, secret=secret, full_url=req_url)
        digest.set_body(json.dumps(request_data))

        # Setup config for HTTP transport
        # And make request via HTTP implemented Client
        [content, status_code, headers] = new_http_client(
            cli_name=gateway.HTTP_TRANSPORT_IMPLEMENTATION,
            verify_ssl=gateway.HTTP_VERIFY_SSL_CERTS,
            proxy=gateway.HTTP_PROXY,
            timeout=gateway.HTTP_TIME_OUT
        ).request(
            http_method=self.__client_operations['method'],
            http_url=req_url,
            authorization_header=digest.create_header(),
            request_data=request_data
        )

        gw_response = GatewayResponse(status_code, content, headers)
        if gw_response.is_successful():
            response_digest = ResponseDigest(gw_response.headers.get('authorization'))
            gw_response.digest = response_digest

            response_digest.set_original_uri(digest.get_uri())
            response_digest.set_original_cnonce(digest.get_cnonce())
            response_digest.set_body(gw_response.payload)
            response_digest.verify(guid, secret)

        return gw_response
