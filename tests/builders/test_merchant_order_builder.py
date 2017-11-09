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

from gateway.builders.merchant_order_builder import MerchantOrderBuilder
from unittest import TestCase
from unittest.mock import patch


class TestMerchantOrderBuilder(TestCase):
    BUILDER = None
    DATA = {}

    def setUp(self):
        self.DATA = {}
        self.BUILDER = MerchantOrderBuilder(self.DATA)

    def tearDown(self):
        del self.DATA

    def test_create_builder_instance(self):
        """Will succeed"""
        self.assertIsInstance(self.BUILDER, MerchantOrderBuilder)

    def test_build_with_add_merchant_transaction_id(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_merchant_transaction_id') as mock:
            new.add_merchant_transaction_id('MyMerchantExampleID#1234567890')
        mock.assert_called_once_with('MyMerchantExampleID#1234567890')

    def test_build_with_add_merchant_order_id(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_merchant_order_id') as mock:
            new.add_merchant_order_id('MyORDER#1234567890')
        mock.assert_called_once_with('MyORDER#1234567890')

    def test_build_with_add_merchant_order_description(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_merchant_order_description') as mock:
            new.add_merchant_order_description(
                'Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
        mock.assert_called_once_with(
            'Lorem Ipsum is simply dummy text of the printing and typesetting industry.')

    def test_build_with_add_merchant_order_meta(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_merchant_order_meta') as mock:
            new.add_merchant_order_meta({
                'f_name': 'Jane',
                'l_name': 'Doe',
                'sequence': '0',
                'title': 'president',
                'url': 'nice.example.com'
            })
        mock.assert_called_once_with({
            'f_name': 'Jane',
            'l_name': 'Doe',
            'sequence': '0',
            'title': 'president',
            'url': 'nice.example.com'
        })

    def test_build_with_add_merchant_side_url(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_merchant_side_url') as mock:
            new.add_merchant_side_url('Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
        mock.assert_called_once_with('Lorem Ipsum is simply dummy text of the printing and typesetting industry.')

    def test_build_with_add_recipient_name(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_recipient_name') as mock:
            new.add_recipient_name('Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
        mock.assert_called_once_with('Lorem Ipsum is simply dummy text of the printing and typesetting industry.')

    def test_merchant_data_structure_build(self):
        valid_data_structure = {
            'general-data': {
                'order-data': {
                    'order-id': 'UnitTestIdOforder_id',
                    'merchant-transaction-id': 'UnitTestIdOftransaction_id',
                    'order-description': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
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
        new.add_merchant_transaction_id(
            transaction_id='UnitTestIdOftransaction_id'
        )
        new.add_merchant_order_id(
            order_id='UnitTestIdOforder_id'
        )
        new.add_merchant_order_description(
            description='Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
        )
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
