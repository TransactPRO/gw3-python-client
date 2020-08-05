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

from gateway.utils.data_validator import DataValidator


class TestDataValidator(TestCase):
    required_data_list = {
        'Key1': int,
        'tiny_key': str
    }

    invalid_test_data_list = {
        'Key1': 42,
        'Other_dor': {
            'tiny_key': 22
        }
    }

    valid_test_data_list = {
        'Key1': 42,
        'Other_dor': {
            'tiny_key': 'the id 22'
        }
    }

    def test_invalid_request_data(self):
        response = DataValidator().validate_request_data(
            request_data=self.invalid_test_data_list,
            required_data=self.required_data_list
        )
        # The structure invalid, as response we got key and type
        self.assertEqual({'tiny_key': str}, response)

    def test_valid_request_data(self):
        response = DataValidator().validate_request_data(
            request_data=self.valid_test_data_list,
            required_data=self.required_data_list
        )
        # The structure valid, as response empty list
        self.assertEqual({}, response)

