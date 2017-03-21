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

from gateway.builders.customer_data_builder import CustomerDataBuilder
from unittest import TestCase
from unittest.mock import patch


class TestCustomerDataBuilder(TestCase):
    BUILDER = None
    DATA = {}

    def setUp(self):
        self.DATA = {}
        self.BUILDER = CustomerDataBuilder(self.DATA)

    def tearDown(self):
        del self.DATA

    def test_create_command_data_builder_instance(self):
        """Will succeed"""
        self.assertIsInstance(self.BUILDER, CustomerDataBuilder)

    def test_build_add_email(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_email') as mock:
            new.add_email('unit@test.exmaple')
        mock.assert_called_once_with('unit@test.exmaple')

    def test_build_add_billing_country(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_billing_country') as mock:
            new.add_billing_country('Latvia')
        mock.assert_called_once_with('Latvia')

    def test_build_add_billing_state(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_billing_state') as mock:
            new.add_billing_state('Riga')
        mock.assert_called_once_with('Riga')

    def test_build_add_billing_city(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_billing_city') as mock:
            new.add_billing_city('Riga')
        mock.assert_called_once_with('Riga')

    def test_build_add_billing_street(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_billing_street') as mock:
            new.add_billing_street('Gustava Zemgala gatve')
        mock.assert_called_once_with('Gustava Zemgala gatve')

    def test_build_add_billing_house(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_billing_house') as mock:
            new.add_billing_house('76')
        mock.assert_called_once_with('76')

    def test_build_add_billing_flat(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_billing_flat') as mock:
            new.add_billing_flat('12')
        mock.assert_called_once_with('12')

    def test_build_add_billing_zip(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_billing_flat') as mock:
            new.add_billing_flat('LV-1039')
        mock.assert_called_once_with('LV-1039')

    def test_build_add_shipping_country(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_shipping_country') as mock:
            new.add_shipping_country('Latvia')
        mock.assert_called_once_with('Latvia')

    def test_build_add_shipping_state(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_shipping_state') as mock:
            new.add_shipping_state('Riga')
        mock.assert_called_once_with('Riga')

    def test_build_add_shipping_city(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_shipping_city') as mock:
            new.add_shipping_city('Riga')
        mock.assert_called_once_with('Riga')

    def test_build_add_shipping_street(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_shipping_street') as mock:
            new.add_shipping_street('Gustava Zemgala gatve')
        mock.assert_called_once_with('Gustava Zemgala gatve')

    def test_build_add_shipping_house(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_shipping_house') as mock:
            new.add_shipping_house('76')
        mock.assert_called_once_with('76')

    def test_build_add_shipping_flat(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_shipping_flat') as mock:
            new.add_shipping_flat('12')
        mock.assert_called_once_with('12')

    def test_build_add_shipping_zip(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_shipping_flat') as mock:
            new.add_shipping_flat('LV-1039')
        mock.assert_called_once_with('LV-1039')

    def test_customer_data_structure_build(self):
        valid_data_structure = {
            'general-data': {
                'customer-data': {
                    'email': 'jane_doe@nice.example.com',
                    'shipping-address': {
                        'house': '76', 'zip': 'LV-1039',
                        'flat': '12', 'country': 'Latvia',
                        'city': 'Riga',
                        'state': 'Gustava Zemgala gatve'
                    },
                    'billing-address': {
                        'street': 'Gustava Zemgala gatve',
                        'house': '76', 'zip': 'LV-1039',
                        'flat': '12', 'country': 'Latvia',
                        'city': 'Riga', 'state': 'Riga'
                    }
                }
            }
        }

        new = self.BUILDER
        new.add_email(cardholder_email='jane_doe@nice.example.com')
        new.add_billing_country(country='Latvia')
        new.add_billing_state(state='Riga')
        new.add_billing_city(city='Riga')
        new.add_billing_street(street='Gustava Zemgala gatve')
        new.add_billing_house(house_number='76')
        new.add_billing_flat(flat_number='12')
        new.add_billing_zip(zip_code='LV-1039')
        new.add_shipping_country(country='Latvia')
        new.add_shipping_state(state='Riga')
        new.add_shipping_city(city='Riga')
        new.add_shipping_street(street='Gustava Zemgala gatve')
        new.add_shipping_house(house_number='76')
        new.add_shipping_flat(flat_number='12')
        new.add_shipping_zip(zip_code='LV-1039')
        self.assertDictEqual(valid_data_structure, self.DATA)
