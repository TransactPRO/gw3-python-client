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

from gateway.builders.info_data_builder import InfoDataBuilder


class TestInfoDataBuilder(TestCase):
    BUILDER = None
    DATA = {}
    MANDATORY_FIELDS = {}

    def setUp(self):
        self.DATA = {}
        self.MANDATORY_FIELDS = {}
        self.BUILDER = InfoDataBuilder(self.DATA, self.MANDATORY_FIELDS)

    def tearDown(self):
        del self.DATA
        del self.MANDATORY_FIELDS

    def test_mandatory_and_data_fields(self):
        new = self.BUILDER
        new.add_gateway_transaction_ids([
            '16f462cb-9s32-dsv2-b983-fa14da6421f1'
        ])
        from gateway.data_sets.request_parameters import (RequestParameters, RequestParametersTypes)
        valid_fields = {
            RequestParameters.COMMAND_DATA_GATEWAY_TRANSACTION_IDS:
                RequestParametersTypes.COMMAND_DATA_GATEWAY_TRANSACTION_IDS,
        }
        self.assertDictEqual(valid_fields, self.MANDATORY_FIELDS)
        valid_data_structure = {'command-data': {'gateway-transaction-ids': ['16f462cb-9s32-dsv2-b983-fa14da6421f1']}}
        self.assertDictEqual(valid_data_structure, self.DATA)
