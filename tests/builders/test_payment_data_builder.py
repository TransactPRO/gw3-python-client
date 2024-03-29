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

from gateway.builders.payment_data_builder import PaymentDataBuilder


class TestPaymentDataBuilder(TestCase):
    BUILDER = None
    DATA = {}
    MANDATORY_FIELDS = {}

    def setUp(self):
        self.DATA = {}
        self.MANDATORY_FIELDS = {}
        self.BUILDER = PaymentDataBuilder(self.DATA, self.MANDATORY_FIELDS)

    def tearDown(self):
        del self.DATA
        del self.MANDATORY_FIELDS

    def test_mandatory_and_data_fields(self):
        new = self.BUILDER
        new.add_pan_cardholder_name(first_last_name='Jane Doe')
        new.add_pan_cvv_code(cvv_number='442')
        new.add_pan_expiry_date(mm_yy='12/30')
        new.add_pan_number(pan_number='4222222222222')
        from gateway.data_sets.request_parameters import (RequestParameters, RequestParametersTypes)
        valid_fields_types = {
            RequestParameters.PAYMENT_METHOD_DATA_PAN:
                RequestParametersTypes.PAYMENT_METHOD_DATA_PAN,
        }
        self.assertDictEqual(valid_fields_types, self.MANDATORY_FIELDS)
        valid_data_structure = {
            'payment-method-data': {
                'cvv': '442',
                'pan': '4222222222222',
                'cardholder-name': 'Jane Doe',
                'exp-mm-yy': '12/30'
            }
        }
        self.assertDictEqual(valid_data_structure, self.DATA)

    def test_additional_data_fields(self):
        new = self.BUILDER
        new.add_pan_cardholder_name(first_last_name='Jane Doe')
        new.add_pan_cvv_code(cvv_number='442')
        new.add_pan_expiry_date(mm_yy='12/30')
        new.add_pan_number(pan_number='4222222222222')

        new.add_external_mpi_protocol_version('2.2.0')
        new.add_external_mpi_ds_trans_id('26221368-1c3d-4f3c-ba34-2efb76644c320')
        new.add_external_mpi_xid('b+f8duAy8jNTQ0DB4U3mSmPyp8s=')
        new.add_external_mpi_cavv('kBMI/uGZvlKCygBkcQIlLJeBTPLG')
        new.add_external_mpi_trans_status('Y')

        from gateway.data_sets.request_parameters import (RequestParameters, RequestParametersTypes)
        valid_fields_types = {
            RequestParameters.PAYMENT_METHOD_DATA_PAN:
                RequestParametersTypes.PAYMENT_METHOD_DATA_PAN,
        }
        self.assertDictEqual(valid_fields_types, self.MANDATORY_FIELDS)
        valid_data_structure = {
            'payment-method-data': {
                'cvv': '442',
                'pan': '4222222222222',
                'cardholder-name': 'Jane Doe',
                'exp-mm-yy': '12/30',
                'external-mpi-data': {
                    'protocolVersion': '2.2.0',
                    'dsTransID': '26221368-1c3d-4f3c-ba34-2efb76644c320',
                    'xid': 'b+f8duAy8jNTQ0DB4U3mSmPyp8s=',
                    'cavv': 'kBMI/uGZvlKCygBkcQIlLJeBTPLG',
                    'transStatus': 'Y'
                }
            }
        }
        self.assertDictEqual(valid_data_structure, self.DATA)
