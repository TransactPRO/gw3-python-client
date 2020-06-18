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

from gateway.builders.verify_3d_enrollment_builder import Verify3dEnrollmentBuilder


class TestVerify3dEnrollmentBuilder(TestCase):
    BUILDER = None
    DATA = {}
    MANDATORY_FIELDS = {}

    def setUp(self):
        self.DATA = {}
        self.MANDATORY_FIELDS = {}
        self.BUILDER = Verify3dEnrollmentBuilder(self.DATA, self.MANDATORY_FIELDS)

    def tearDown(self):
        del self.DATA
        del self.MANDATORY_FIELDS

    def test_mandatory_and_data_fields(self):
        new = self.BUILDER
        new.add_pan_number(pan_number='4222222222222')
        new.add_terminal_mid(terminal_id='0123456')
        new.add_currency(iso_4217_ccy='EUR')
        from gateway.data_sets.request_parameters import (RequestParameters, RequestParametersTypes)
        valid_fields_types = {
            RequestParameters.PAYMENT_METHOD_DATA_PAN: RequestParametersTypes.PAYMENT_METHOD_DATA_PAN,
            RequestParameters.COMMAND_DATA_TERMINAL_MID: RequestParametersTypes.COMMAND_DATA_TERMINAL_MID,
            RequestParameters.MONEY_DATA_CURRENCY: RequestParametersTypes.MONEY_DATA_CURRENCY,
        }
        self.assertDictEqual(valid_fields_types, self.MANDATORY_FIELDS)
        valid_data_structure = {
            'pan': '4222222222222',
            'terminal-mid': '0123456',
            'currency': 'EUR'
        }
        self.assertDictEqual(valid_data_structure, self.DATA)
