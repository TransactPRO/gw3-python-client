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

from gateway.builders.merchant_order_builder import MerchantOrderBuilder


class TestMerchantOrderBuilder(TestCase):
    BUILDER = None
    DATA = {}

    def setUp(self):
        self.DATA = {}
        self.BUILDER = MerchantOrderBuilder(self.DATA)

    def tearDown(self):
        del self.DATA

    def test_merchant_data_structure_build(self):
        valid_data_structure = {
            'general-data': {
                'order-data': {
                    'order-id': 'UnitTestIdOforder_id',
                    'merchant-transaction-id': 'UnitTestIdOftransaction_id',
                    'order-description': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
                    'merchant-side-url': 'http://side.url',
                    'recipient-name': 'Jone Doe',
                    'merchant-referring-name': 'REF NAME',
                    'custom-3d-return-url': 'https://example.com',
                    'custom-return-url': 'https://another-example.com',
                    'order-meta': {
                        'url': 'nice.example.com',
                        'sequence': '0',
                        'f_name': 'Jane',
                        'title': 'president',
                        'l_name': 'Doe'
                    }
                }
            }
        }

        new = self.BUILDER
        new.add_merchant_transaction_id('UnitTestIdOftransaction_id')
        new.add_merchant_order_id('UnitTestIdOforder_id')
        new.add_merchant_order_description('Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
        new.add_merchant_side_url('http://side.url')
        new.add_recipient_name('Jone Doe')
        new.add_merchant_referring_name('REF NAME')
        new.add_custom_3d_return_url('https://example.com')
        new.add_custom_return_url('https://another-example.com')
        new.add_merchant_order_meta(
            json_object={
                'f_name': 'Jane',
                'l_name': 'Doe',
                'sequence': '0',
                'title': 'president',
                'url': 'nice.example.com'
            }
        )
        self.assertDictEqual(valid_data_structure, self.DATA)
