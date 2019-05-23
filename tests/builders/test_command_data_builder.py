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

from gateway.builders.command_data_builder import CommandDataBuilder
from unittest import TestCase
from unittest.mock import patch


class TestCommandDataBuilder(TestCase):
    BUILDER = None
    DATA = {}
    MANDATORY_FIELDS = {}

    def setUp(self):
        self.DATA = {}
        self.MANDATORY_FIELDS = {}
        self.BUILDER = CommandDataBuilder(self.DATA, self.MANDATORY_FIELDS)

    def tearDown(self):
        del self.DATA
        del self.MANDATORY_FIELDS

    def test_create_builder_instance(self):
        """Will succeed"""
        self.assertIsInstance(self.BUILDER, CommandDataBuilder)

    def test_build_with_form_id(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_form_id') as mock:
            new.add_form_id('#Delta789')
        mock.assert_called_once_with('#Delta789')

    def test_build_with_gateway_transaction_id(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_gateway_transaction_id') as mock:
            new.add_gateway_transaction_id('16f462cb-9s32-dsv2-b983-fa14da6421f1')
        mock.assert_called_once_with('16f462cb-9s32-dsv2-b983-fa14da6421f1')

    def test_build_with_terminal_mid(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_terminal_mid') as mock:
            new.add_terminal_mid('77299421')
        mock.assert_called_once_with('77299421')

    def test_build_with_card_verification_mode(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_card_verification_mode') as mock:
            new.add_card_verification_mode(123)
        mock.assert_called_once_with(123)

    def test_build_with_payment_method_data_source(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_payment_method_data_source') as mock:
            new.add_payment_method_data_source(123)
        mock.assert_called_once_with(123)

    def test_build_with_payment_method_data_token(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_payment_method_data_token') as mock:
            new.add_payment_method_data_token('qwerty')
        mock.assert_called_once_with('qwerty')

    def test_mandatory_and_data_fields(self):
        """Will succeed"""
        new = self.BUILDER
        new.add_terminal_mid('3321552')
        new.add_gateway_transaction_id('16f463xf-9s32-dsv2-b983-fSD2234598f1')
        new.add_form_id('#Bravo345')
        new.add_card_verification_mode(321)
        new.add_payment_method_data_source(456)
        new.add_payment_method_data_token('mega-token')
        from gateway.data_sets.request_parameters import (RequestParameters, RequestParametersTypes)
        valid_fields_types = {
            RequestParameters.COMMAND_DATA_GATEWAY_TRANSACTION_ID:
                RequestParametersTypes.COMMAND_DATA_GATEWAY_TRANSACTION_ID,
        }
        self.assertDictEqual(valid_fields_types, self.MANDATORY_FIELDS)
        valid_data_structure = {
            'command-data': {
                'terminal-mid': '3321552',
                'gateway-transaction-id': '16f463xf-9s32-dsv2-b983-fSD2234598f1',
                'form-id': '#Bravo345',
                'card-verification': 321,
                'payment-method-data-source': 456,
                'payment-method-data-token': 'mega-token'
            }
        }
        self.assertDictEqual(valid_data_structure, self.DATA)
