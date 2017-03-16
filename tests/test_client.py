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


import gateway
from gateway.builders.authorization_builder import AuthorizationBuilder
from gateway.operations.operations import Operations
from unittest import TestCase
from unittest.mock import (
    patch,
    Mock
)


class TestClient(TestCase):
    CORRECT_EMPTY_REQUEST = {
        'auth-data': {},
        'data': {}
    }
    CORRECT_AUTH_DATA = {
        'auth-data': {
            'account-id': 1, 'secret-key': 'MySecretKey'
        },
        'data': {}
    }

    def setUp(self):
        self.GATE_CLIENT = gateway.Client()

    def test_create_auth_data_instance(self):
        self.assertIsInstance(self.GATE_CLIENT.create_auth_data(), AuthorizationBuilder)

    def test_set_operation_instance(self):
        self.assertIsInstance(self.GATE_CLIENT.set_operation(), Operations)

    def test_call_add_account_id(self):
        """Will succeed"""
        cli = self.GATE_CLIENT.create_auth_data()
        with patch.object(cli, 'add_account_id') as mock:
            cli.add_account_id(1)

        mock.assert_called_once_with(1)

    def test_call_add_secret_key(self):
        """Will succeed"""
        cli = self.GATE_CLIENT.create_auth_data()
        with patch.object(cli, 'add_secret_key') as mock:
            cli.add_secret_key('MySecretKey')

        mock.assert_called_once_with('MySecretKey')

    def test_call_add_session_id(self):
        """Will succeed"""
        cli = self.GATE_CLIENT.create_auth_data()
        with patch.object(cli, 'add_session_id') as mock:
            cli.add_session_id('SUPER_session_id')

        mock.assert_called_once_with('SUPER_session_id')

    def test_build_empty_request(self):
        """Will succeed"""
        self.assertEquals(self.GATE_CLIENT.build_request(), self.CORRECT_EMPTY_REQUEST)

    def test_create_auth_data(self):
        """Will succeed"""
        self.GATE_CLIENT.create_auth_data().add_account_id(1)
        self.GATE_CLIENT.create_auth_data().add_secret_key('MySecretKey')
        self.assertEquals(self.GATE_CLIENT.build_request(), self.CORRECT_AUTH_DATA)

    def test_make_request(self):
        """Will succeed"""
        cli = self.GATE_CLIENT
        with patch.object(cli, 'make_request') as req_mock:
            cli.make_request(self.CORRECT_AUTH_DATA)

        req_mock.assert_called_once_with(self.CORRECT_AUTH_DATA)
