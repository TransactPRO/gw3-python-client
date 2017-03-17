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

from gateway.builders.authorization_builder import AuthorizationBuilder
from unittest import TestCase
from unittest.mock import patch


class TestAuthorizationBuilder(TestCase):
    AUTH_BUILDER = None
    AUTH_DATA = None
    AUTH_MANDATORY_FIELDS = None

    def setUp(self):
        self.AUTH_DATA = {}
        self.AUTH_MANDATORY_FIELDS = {}
        self.AUTH_BUILDER = AuthorizationBuilder(self.AUTH_DATA, self.AUTH_MANDATORY_FIELDS)

    def tearDown(self):
        del self.AUTH_DATA
        del self.AUTH_MANDATORY_FIELDS

    def test_create_authorization_builder_instance(self):
        """Will succeed"""
        self.assertIsInstance(self.AUTH_BUILDER, AuthorizationBuilder)

    def test_build_with_account_id(self):
        """Will succeed"""
        new_auth = self.AUTH_BUILDER
        with patch.object(new_auth, 'add_account_id') as mock:
            new_auth.add_account_id(42)
        mock.assert_called_once_with(42)

    def test_build_with_secret_key(self):
        """Will succeed"""
        new_auth = self.AUTH_BUILDER
        with patch.object(new_auth, 'add_secret_key') as mock:
            new_auth.add_secret_key('TheKey')
        mock.assert_called_once_with('TheKey')

    def test_build_with_session(self):
        """Will succeed"""
        new_auth = self.AUTH_BUILDER
        with patch.object(new_auth, 'add_session_id') as mock:
            new_auth.add_session_id('TheXSession')
        mock.assert_called_once_with('TheXSession')

