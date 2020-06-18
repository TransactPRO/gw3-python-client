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

import gateway
from gateway.builders.authorization_builder import AuthorizationBuilder
from gateway.operations.operations import Operations


class TestClient(TestCase):
    CORRECT_EMPTY_REQUEST = {
        'data': {}
    }
    CORRECT_AUTH_DATA = {
        'data': {}
    }
    CORRECT_AUTH_DATA_WITH_SESSION = {
        'auth-data': {
            'session-id': 'super-session'
        },
        'data': {}
    }

    def setUp(self):
        self.GATE_CLIENT = gateway.Client()

    def test_create_auth_data_instance(self):
        self.assertIsInstance(self.GATE_CLIENT.create_auth_data(), AuthorizationBuilder)

    def test_set_operation_instance(self):
        self.assertIsInstance(self.GATE_CLIENT.set_operation(), Operations)

    def test_build_empty_request(self):
        self.assertEqual(self.CORRECT_EMPTY_REQUEST, self.GATE_CLIENT.build_request())

    def test_create_auth_data(self):
        self.GATE_CLIENT.create_auth_data().add_account_guid('3383e58e-9cde-4ffa-85cf-81cd25b2423e')
        self.GATE_CLIENT.create_auth_data().add_secret_key('MySecretKey')
        self.assertEqual(self.CORRECT_AUTH_DATA, self.GATE_CLIENT.build_request())

    def test_create_auth_data_with_session(self):
        self.GATE_CLIENT.create_auth_data().add_account_guid('3383e58e-9cde-4ffa-85cf-81cd25b2423e')
        self.GATE_CLIENT.create_auth_data().add_secret_key('MySecretKey')
        self.GATE_CLIENT.create_auth_data().add_session_id('super-session')
        self.assertEqual(self.CORRECT_AUTH_DATA_WITH_SESSION, self.GATE_CLIENT.build_request())
