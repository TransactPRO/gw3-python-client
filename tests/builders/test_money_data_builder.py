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

from gateway.builders.money_data_builder import MoneyDataBuilder
from unittest import TestCase
from unittest.mock import patch


class TestMoneyDataBuilder(TestCase):
    BUILDER = None
    DATA = {}
    MANDATORY_FIELDS = {}

    def setUp(self):
        self.DATA = {}
        self.MANDATORY_FIELDS = {}
        self.BUILDER = MoneyDataBuilder(self.DATA, self.MANDATORY_FIELDS)

    def tearDown(self):
        del self.DATA
        del self.MANDATORY_FIELDS

    def test_create_command_data_builder_instance(self):
        """Will succeed"""
        self.assertIsInstance(self.BUILDER, MoneyDataBuilder)

    def test_build_with_add_payment_amount(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_payment_amount') as mock:
            new.add_payment_amount(60030)
        mock.assert_called_once_with(60030)

    def test_build_with_add_payment_currency(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_payment_currency') as mock:
            new.add_payment_currency('EUR')
        mock.assert_called_once_with('EUR')

    def test_mandatory_and_data_fields(self):
        """Will succeed"""
        new = self.BUILDER
        new.add_payment_amount(minor_value=5000)
        new.add_payment_currency(iso_4217_ccy='USD')
        from gateway.data_sets.request_parameters import (RequestParameters, RequestParametersTypes)
        valid_fields_types = {
            RequestParameters.MONEY_DATA_AMOUNT:
                RequestParametersTypes.MONEY_DATA_AMOUNT,
            RequestParameters.MONEY_DATA_CURRENCY:
                RequestParametersTypes.MONEY_DATA_CURRENCY,
        }
        self.assertDictEqual(valid_fields_types, self.MANDATORY_FIELDS)
        valid_data_structure = {
            'money-data': {
                'currency': 'USD',
                'amount': 5000
            }
        }
        self.assertDictEqual(valid_data_structure, self.DATA)
