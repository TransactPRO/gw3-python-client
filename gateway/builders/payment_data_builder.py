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


class PaymentDataBuilder(object):
    """
    Payment data - information about credit card
    """
    __PAYMENT_METHOD_DATA_KEY = 'payment-method-data'

    def __init__(self, __client_transaction_data_set, __client_mandatory_fields):
        self.__payment_data_structure = {
            self.__PAYMENT_METHOD_DATA_KEY: None
        }

        self.__data_structure_util = DataStructuresUtils
        self.__data_sets = RequestParameters
        self.__data_types = RequestParametersTypes
        self.__payment_data_set = __client_transaction_data_set
        self.__payment_mandatory_fields = __client_mandatory_fields

    def add_pan_number(self, pan_number=None):
        """
        Add credit card number

        Args:
            pan_number (str): Credit card number
        """
        self.__payment_mandatory_fields[self.__data_sets.PAYMENT_METHOD_DATA_PAN] = self.__data_types.PAYMENT_METHOD_DATA_PAN

        self.__data_structure_util.add_to_dict(
            source_dict=self.__payment_data_set,
            working_dict=self.__payment_data_structure,
            new_key=self.__PAYMENT_METHOD_DATA_KEY,
            new_dict={self.__data_sets.PAYMENT_METHOD_DATA_PAN: pan_number}
        )

    def add_pan_expiry_date(self, mm_yy=None):
        """
        Add credit card expiry date in mm/yy format

        Args:
            mm_yy (str): Credit card expiry date in mm/yy format
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__payment_data_set,
            working_dict=self.__payment_data_structure,
            new_key=self.__PAYMENT_METHOD_DATA_KEY,
            new_dict={self.__data_sets.PAYMENT_METHOD_DATA_EXPIRE: mm_yy}
        )

    def add_pan_cvv_code(self, cvv_number=None):
        """
        Add credit card protection code

        Args:
            cvv_number (str): Credit card protection code
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__payment_data_set,
            working_dict=self.__payment_data_structure,
            new_key=self.__PAYMENT_METHOD_DATA_KEY,
            new_dict={self.__data_sets.PAYMENT_METHOD_DATA_CVV: cvv_number}
        )

    def add_pan_cardholder_name(self, first_last_name=None):
        """
        Add cardholder Name and Surname

        Args:
            first_last_name (str): Cardholder Name and Surname
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__payment_data_set,
            working_dict=self.__payment_data_structure,
            new_key=self.__PAYMENT_METHOD_DATA_KEY,
            new_dict={self.__data_sets.PAYMENT_METHOD_DATA_CARDHOLDER_NAME: first_last_name}
        )
