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


class Verify3dEnrollmentBuilder(object):
    """
    Payment data - information about credit card
    """

    def __init__(self, __client_transaction_data_set, __client_mandatory_fields):
        self.__input_data_structure = {}

        self.__data_structure_util = DataStructuresUtils
        self.__data_sets = RequestParameters
        self.__data_types = RequestParametersTypes
        self.__input_data_set = __client_transaction_data_set
        self.__input_mandatory_fields = __client_mandatory_fields

    def add_pan_number(self, pan_number=None):
        """
        Add credit card number

        Args:
            pan_number (str): Credit card number
        """
        self.__input_mandatory_fields[self.__data_sets.PAYMENT_METHOD_DATA_PAN] = self.__data_types.PAYMENT_METHOD_DATA_PAN

        self.__input_data_structure.update({self.__data_sets.PAYMENT_METHOD_DATA_PAN: pan_number})
        self.__input_data_set.update(self.__input_data_structure)

    def add_terminal_mid(self, terminal_id=None):
        """
        Add terminal MID when selecting terminal manually

        Args:
            terminal_id (str): Terminal MID when selecting terminal manually
        """
        self.__input_mandatory_fields[self.__data_sets.COMMAND_DATA_TERMINAL_MID] = self.__data_types.COMMAND_DATA_TERMINAL_MID

        self.__input_data_structure.update({self.__data_sets.COMMAND_DATA_TERMINAL_MID: terminal_id})
        self.__input_data_set.update(self.__input_data_structure)

    def add_currency(self, iso_4217_ccy=None):
        """
        Add payment currency, ISO-4217 format

        Args:
            iso_4217_ccy (str): Currency, ISO-4217 format
        """
        self.__input_mandatory_fields[self.__data_sets.MONEY_DATA_CURRENCY] = self.__data_types.MONEY_DATA_CURRENCY

        self.__input_data_structure.update({self.__data_sets.MONEY_DATA_CURRENCY: iso_4217_ccy})
        self.__input_data_set.update(self.__input_data_structure)
