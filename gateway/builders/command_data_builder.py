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

from gateway.data_sets.request_parameters import (
    RequestParameters,
    RequestParametersTypes
)
from gateway.utils.data_structures import DataStructuresUtils


class CommandDataBuilder(object):
    """
    Command data - Transact Pro gateway command data for work with (gateway-transaction-id, form-id, terminal-id)
    """

    __COMMAND_DATA_KEY = 'command-data'

    def __init__(self, __client_transaction_data_set, __client_mandatory_fields):
        self.__command_data_nested_structure = {
            self.__COMMAND_DATA_KEY: None
        }

        self.__data_structure_util = DataStructuresUtils
        self.__data_sets = RequestParameters
        self.__data_types = RequestParametersTypes
        self.__command_mandatory_fields = __client_mandatory_fields
        self.__command_data_set = __client_transaction_data_set

    def add_gateway_transaction_id(self, gate_transaction_id=None):
        """
        Add previously created Transaction ID

        Args:
            gate_transaction_id (str): Previously created Transaction ID
        """
        self.__command_mandatory_fields[self.__data_sets.COMMAND_DATA_GATEWAY_TRANSACTION_ID] = self.__data_types.COMMAND_DATA_GATEWAY_TRANSACTION_ID

        self.__data_structure_util.add_to_dict(
            source_dict=self.__command_data_set,
            working_dict=self.__command_data_nested_structure,
            new_key=self.__COMMAND_DATA_KEY,
            new_dict={self.__data_sets.COMMAND_DATA_GATEWAY_TRANSACTION_ID: gate_transaction_id}
        )

    def add_form_id(self, inside_form_id=None):
        """
        Add inside form ID when selecting non-default form manually

        Args:
            inside_form_id (str): Inside form ID when selecting non-default form manually
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__command_data_set,
            working_dict=self.__command_data_nested_structure,
            new_key=self.__COMMAND_DATA_KEY,
            new_dict={self.__data_sets.COMMAND_DATA_FORM_ID: inside_form_id}
        )

    def add_terminal_mid(self, terminal_id=None):
        """
        Add terminal MID when selecting terminal manually

        Args:
            terminal_id (str): Terminal MID when selecting terminal manually
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__command_data_set,
            working_dict=self.__command_data_nested_structure,
            new_key=self.__COMMAND_DATA_KEY,
            new_dict={self.__data_sets.COMMAND_DATA_TERMINAL_MID: terminal_id}
        )

    def add_card_verification_mode(self, mode=None):
        """
        Add card verification mode

        Args:
            mode (int): card verification mode
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__command_data_set,
            working_dict=self.__command_data_nested_structure,
            new_key=self.__COMMAND_DATA_KEY,
            new_dict={self.__data_sets.COMMAND_DATA_CARDS_VERIFICATION: mode}
        )

    def add_payment_method_data_source(self, data_source=None):
        """
        Add payment method data source

        Args:
            data_source (int): payment method data source
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__command_data_set,
            working_dict=self.__command_data_nested_structure,
            new_key=self.__COMMAND_DATA_KEY,
            new_dict={self.__data_sets.COMMAND_DATA_PAYMENT_METHOD_DATA_SOURCE: data_source}
        )

    def add_payment_method_data_token(self, token=None):
        """
        Add payment method data token

        Args:
            token (str): payment method data source
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__command_data_set,
            working_dict=self.__command_data_nested_structure,
            new_key=self.__COMMAND_DATA_KEY,
            new_dict={self.__data_sets.COMMAND_DATA_PAYMENT_METHOD_DATA_TOKEN: token}
        )
