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


class MoneyDataBuilder(object):
    """
    Money data - information about payment request
    """
    __MONEY_DATA_KEY = 'money-data'

    def __init__(self, __client_transaction_data_set, __client_mandatory_fields):
        self.__money_data_structure = {
            self.__MONEY_DATA_KEY: None
        }

        self.__data_structure_util = DataStructuresUtils
        self.__data_types = RequestParametersTypes
        self.__data_sets = RequestParameters
        self.__money_data_set = __client_transaction_data_set
        self.__money_mandatory_fields = __client_mandatory_fields

    def add_payment_amount(self, minor_value=None):
        """
        Add payment money amount in minor units

        Args:
            minor_value (int): Money amount in minor units
        """
        self.__money_mandatory_fields[self.__data_sets.MONEY_DATA_AMOUNT] = self.__data_types.MONEY_DATA_AMOUNT

        self.__data_structure_util.add_to_dict(
            source_dict=self.__money_data_set,
            working_dict=self.__money_data_structure,
            new_key=self.__MONEY_DATA_KEY,
            new_dict={self.__data_sets.MONEY_DATA_AMOUNT: minor_value}
        )

    def add_payment_currency(self, iso_4217_ccy=None):
        """
        Add payment currency, ISO-4217 format

        Args:
            iso_4217_ccy (str): Currency, ISO-4217 format
        """
        self.__money_mandatory_fields[self.__data_sets.MONEY_DATA_CURRENCY] = self.__data_types.MONEY_DATA_CURRENCY

        self.__data_structure_util.add_to_dict(
            source_dict=self.__money_data_set,
            working_dict=self.__money_data_structure,
            new_key=self.__MONEY_DATA_KEY,
            new_dict={self.__data_sets.MONEY_DATA_CURRENCY: iso_4217_ccy}
        )
