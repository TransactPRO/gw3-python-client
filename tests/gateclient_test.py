import unittest
from gateway.client import Client


class TestGateWayClient(unittest.TestCase):
    GATEWAY_CLIENT = None

    def setUp(self):
        self.GATEWAY_CLIENT = Client()

    def test_auth_builder_account_id_and_secret_key(self):
        """Will succeed"""
        new_auth_data = self.GATEWAY_CLIENT.create_auth_data()
        new_auth_data.add_account_id(123)
        new_auth_data.add_secret_key('ExtraordinarySecKey')
        new_auth_data.add_session_id('TheSession:1sad885asd1gf32asg3f')

        self.assertDictEqual(new_auth_data.get_data_set(), {'auth-data.secret-key': 'ExtraordinarySecKey',
                                                            'auth-data.account-id': 123,
                                                            'auth-data.session-id': 'TheSession:1sad885asd1gf32asg3f'
                                                            })

    # def test_set_operation_create_sms(self):
    #     """Will succeed"""
    #     new_sms_op = self.GATEWAY_CLIENT.set_operation().sms()
    #     new_sms_op.PaymentDataBuilder.add_pan_number('8888223211313')
    #     new_sms_op.PaymentDataBuilder.add_pan_expiry_date('12/28')
    #     new_sms_op.PaymentDataBuilder.add_pan_cvv_code('442')
    #     new_sms_op.PaymentDataBuilder.add_pan_cardholder_name('John Doe Tester')
    #
    #     self.assertDictEqual(new_sms_op.get_sms_data(), {'data.payment-method-data.cardholder-name': 'John Doe Tester',
    #                                                      'data.payment-method-data.cvv': '442',
    #                                                      'data.payment-method-data.exp-mm-yy': '12/28',
    #                                                      'data.payment-method-data.pan': '8888223211313'
    #                                                      })
