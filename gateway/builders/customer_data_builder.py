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

from gateway.data_sets.request_parameters import RequestParameters
from gateway.utils.data_structures import DataStructuresUtils


class CustomerDataBuilder(object):
    """
    Customer data - information about customer (cardholder)
    """

    # First layer of that data set
    __GENERAL_DATA_KEY = 'general-data'
    # Nested layer of general data set
    __CUSTOMER_DATA_KEY = 'customer-data'
    # Nested layer of customer data set
    __BILLING_DATA_KEY = 'billing-address'
    # Nested layer of customer data set
    __SHIPPING_DATA_KEY = 'shipping-address'

    def __init__(self, __transaction_data_set):
        # Base structure of customer data
        self.__customer_data_structure = {
            self.__CUSTOMER_DATA_KEY: None
        }

        # Base structure of billing layer
        self.__billing_data_structure = {
            self.__BILLING_DATA_KEY: None
        }

        # Base structure of shipping layer
        self.__shipping_data_structure = {
            self.__SHIPPING_DATA_KEY: None
        }

        self.__data_structure_util = DataStructuresUtils
        self.__req_params = RequestParameters
        self.__general_data_set = __transaction_data_set
        # Set primary nested layer in transaction data set
        if self.__GENERAL_DATA_KEY not in self.__general_data_set:
            self.__general_data_set[self.__GENERAL_DATA_KEY] = self.__customer_data_structure

    def __update_nested_billing_structure(self):
        """
        Update's nested customer data with new billing data
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__general_data_set[self.__GENERAL_DATA_KEY],
            working_dict=self.__customer_data_structure,
            new_key=self.__CUSTOMER_DATA_KEY,
            new_dict=self.__billing_data_structure
        )

    def __update_nested_shipping_structure(self):
        """
        Update's nested customer data with new shipping data
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__general_data_set[self.__GENERAL_DATA_KEY],
            working_dict=self.__customer_data_structure,
            new_key=self.__CUSTOMER_DATA_KEY,
            new_dict=self.__shipping_data_structure
        )

    def add_email(self, cardholder_email=None):
        """
        Add customer (cardholder) email

        Args:
            cardholder_email (str): Customer (cardholder) email
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__general_data_set[self.__GENERAL_DATA_KEY],
            working_dict=self.__customer_data_structure,
            new_key=self.__CUSTOMER_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_EMAIL: cardholder_email
            }
        )

    def add_phone(self, phone=None):
        """
        Add customer (cardholder) phone

        Args:
            phone (str): Customer (cardholder) phone
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__general_data_set[self.__GENERAL_DATA_KEY],
            working_dict=self.__customer_data_structure,
            new_key=self.__CUSTOMER_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_PHONE: phone
            }
        )

    def add_birth_date(self, birth_date=None):
        """
        Add customer (cardholder) birth date

        Args:
            birth_date (str): Customer (cardholder) birth date
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__general_data_set[self.__GENERAL_DATA_KEY],
            working_dict=self.__customer_data_structure,
            new_key=self.__CUSTOMER_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_BIRTH_DATE: birth_date
            }
        )

    def add_billing_country(self, country=None):
        """
        Add billing country

        Args:
            country (str): 	Billing country
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__billing_data_structure,
            working_dict=self.__billing_data_structure,
            new_key=self.__BILLING_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_COUNTRY: country
            }
        )

        self.__update_nested_billing_structure()

    def add_billing_state(self, state=None):
        """
        Add billing state

        Args:
            state (str): 	Billing state
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__billing_data_structure,
            working_dict=self.__billing_data_structure,
            new_key=self.__BILLING_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_STATE: state
            }
        )

        self.__update_nested_billing_structure()

    def add_billing_city(self, city=None):
        """
        Add billing city

        Args:
            city (str): 	Billing city
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__billing_data_structure,
            working_dict=self.__billing_data_structure,
            new_key=self.__BILLING_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_CITY: city
            }
        )

        self.__update_nested_billing_structure()

    def add_billing_street(self, street=None):
        """
        Add billing street

        Args:
            street (str): 	Billing street
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__billing_data_structure,
            working_dict=self.__billing_data_structure,
            new_key=self.__BILLING_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_BILlING_ADDRESS_STREET: street
            }
        )

        self.__update_nested_billing_structure()

    def add_billing_house(self, house_number=None):
        """
        Add billing house number

        Args:
            house_number (str): 	Billing house number
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__billing_data_structure,
            working_dict=self.__billing_data_structure,
            new_key=self.__BILLING_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_HOUSE: house_number
            }
        )

        self.__update_nested_billing_structure()

    def add_billing_flat(self, flat_number=None):
        """
        Add billing flat number

        Args:
            flat_number (str): 	Billing flat number
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__billing_data_structure,
            working_dict=self.__billing_data_structure,
            new_key=self.__BILLING_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_FLAT: flat_number
            }
        )

        self.__update_nested_billing_structure()

    def add_billing_zip(self, zip_code=None):
        """
        Add billing ZIP

        Args:
            zip_code (str): 	Billing ZIP
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__billing_data_structure,
            working_dict=self.__billing_data_structure,
            new_key=self.__BILLING_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_ZIP: zip_code
            }
        )

        self.__update_nested_billing_structure()

    def add_shipping_country(self, country=None):
        """
        Add shipping country

        Args:
            country (str): 	Shipping country
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__shipping_data_structure,
            working_dict=self.__shipping_data_structure,
            new_key=self.__SHIPPING_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_COUNTRY: country
            }
        )

        self.__update_nested_shipping_structure()

    def add_shipping_state(self, state=None):
        """
        Add shipping state

        Args:
            state (str): 	Shipping state
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__shipping_data_structure,
            working_dict=self.__shipping_data_structure,
            new_key=self.__SHIPPING_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_STATE: state
            }
        )

        self.__update_nested_shipping_structure()

    def add_shipping_city(self, city=None):
        """
        Add shipping city

        Args:
            city (str): 	Shipping city
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__shipping_data_structure,
            working_dict=self.__shipping_data_structure,
            new_key=self.__SHIPPING_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_CITY: city
            }
        )

        self.__update_nested_shipping_structure()

    def add_shipping_street(self, street=None):
        """
        Add shipping street

        Args:
            street (str): 	Shipping street
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__shipping_data_structure,
            working_dict=self.__shipping_data_structure,
            new_key=self.__SHIPPING_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_STREET: street
            }
        )

        self.__update_nested_shipping_structure()

    def add_shipping_house(self, house_number=None):
        """
        Add shipping house number

        Args:
            house_number (str): 	Shipping house number
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__shipping_data_structure,
            working_dict=self.__shipping_data_structure,
            new_key=self.__SHIPPING_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_HOUSE: house_number
            }
        )

        self.__update_nested_shipping_structure()

    def add_shipping_flat(self, flat_number=None):
        """
        Add shipping flat number

        Args:
            flat_number (str): 	Shipping flat number
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__shipping_data_structure,
            working_dict=self.__shipping_data_structure,
            new_key=self.__SHIPPING_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_FLAT: flat_number
            }
        )

        self.__update_nested_shipping_structure()

    def add_shipping_zip(self, zip_code=None):
        """
        Add shipping ZIP code

        Args:
            zip_code (str): 	Shipping ZIP code
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__shipping_data_structure,
            working_dict=self.__shipping_data_structure,
            new_key=self.__SHIPPING_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_ZIP: zip_code
            }
        )

        self.__update_nested_shipping_structure()
