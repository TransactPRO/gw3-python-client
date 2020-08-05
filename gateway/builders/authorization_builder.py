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

from typing import Dict

from gateway.data_sets.request_parameters import RequestParameters, RequestParametersTypes


class AuthorizationBuilder(object):
    def __init__(self, __client_auth_data_set, __client_mandatory_fields):
        self.__data_sets = RequestParameters
        self.__data_types = RequestParametersTypes
        self.__auth_mandatory_fields = __client_mandatory_fields
        self.__auth_data_set = __client_auth_data_set

    def add_merchant_guid(self, guid=None):
        """
        Transact Pro Merchant GUID.

        Args:
            guid (str): Transact Pro Merchant GUID.
        """
        self.__auth_data_set[self.__data_sets.AUTH_DATA_MERCHANT_GUID] = guid

    def add_account_guid(self, guid=None):
        """
        Transact Pro Merchant Account GUID.

        Args:
            guid (str): Transact Pro Merchant Account GUID.
        """
        self.__auth_data_set[self.__data_sets.AUTH_DATA_ACCOUNT_GUID] = guid

    def add_secret_key(self, value=None):
        """
        Transact Pro Merchant Password

        Args:
            value (str): Transact Pro Merchant Password
        """
        self.__auth_data_set[self.__data_sets.AUTH_DATA_SECRET_KEY] = value

    def add_session_id(self, id_value=None):
        """
        Transact Pro Gateway Session ID

        Args:
            id_value (str): Transact Pro Gateway Session ID
        """
        self.__auth_mandatory_fields[self.__data_sets.AUTH_DATA_SESSION_ID] = self.__data_types.AUTH_DATA_SESSION_ID
        self.__auth_data_set[self.__data_sets.AUTH_DATA_SESSION_ID] = id_value

    @staticmethod
    def get_object_guid(auth_data: Dict) -> str:
        """
        Returns an appropriate object's GUID

        :param auth_data: previously filled authentication data
        :return: appropriate GUID
        """
        return auth_data[RequestParameters.AUTH_DATA_ACCOUNT_GUID] \
            if RequestParameters.AUTH_DATA_ACCOUNT_GUID in auth_data \
            else auth_data[RequestParameters.AUTH_DATA_MERCHANT_GUID]
