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


class InfoDataBuilder(object):
    """
    Info Data contains all informational data property's
    """

    __INFO_COMMAND_DATA_KEY = 'command-data'

    def __init__(self, __client_transaction_data_set, __client_mandatory_fields):
        self.__command_data_structure = {
            self.__INFO_COMMAND_DATA_KEY: None
        }

        self.__data_structure_util = DataStructuresUtils
        self.__data_sets = RequestParameters
        self.__data_types = RequestParametersTypes
        self.__payment_data_set = __client_transaction_data_set
        self.__payment_mandatory_fields = __client_mandatory_fields

    def add_gateway_transaction_ids(self, list_of_gate_transaction_id=None):
        """
        Add previously created Transaction IDs

        Example -> ["2d4b377c-648c-432b-a4dc-b386901116d7", "2323377c-548c-4scb-a6dc-b3899kxah520"]

        Args:
            list_of_gate_transaction_id (list): Previously created Transaction IDs
        """
        if list_of_gate_transaction_id is None:
            list_of_gate_transaction_id = []

        self.__payment_mandatory_fields[self.__data_sets.COMMAND_DATA_GATEWAY_TRANSACTION_IDS] = self.__data_types.COMMAND_DATA_GATEWAY_TRANSACTION_IDS

        self.__data_structure_util.add_to_dict(
            source_dict=self.__payment_data_set,
            working_dict=self.__command_data_structure,
            new_key=self.__INFO_COMMAND_DATA_KEY,
            new_dict={self.__data_sets.COMMAND_DATA_GATEWAY_TRANSACTION_IDS: list_of_gate_transaction_id}
        )
