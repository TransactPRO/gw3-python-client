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

from unittest import TestCase

from gateway.builders.command_data_builder import CommandDataBuilder


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

    def test_mandatory_and_data_fields(self):
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
