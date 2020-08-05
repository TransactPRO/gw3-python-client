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

import base64
import datetime
import hashlib
import hmac
import secrets
from enum import Enum
from urllib.parse import urlparse


class DigestMissingError(RuntimeError):
    def __init__(self, msg="Digest is missing", *args: object) -> None:
        super().__init__(msg, *args)


class DigestMismatchError(RuntimeError):
    def __init__(self, msg="Digest mismatch", *args: object) -> None:
        super().__init__(msg, *args)


class QOP(Enum):
    AUTH = "auth"
    AUTH_INT = "auth-int"


class Algorithm(Enum):
    SHA256 = "SHA-256"

    def get_digestmod(self) -> str:
        digestmods = {
            Algorithm.SHA256: hashlib.sha256
        }

        return digestmods.get(self, hashlib.sha256)


class Digest:
    def __init__(self) -> None:
        self._username = None
        self._uri = None
        self._qop = None
        self._algorithm = None
        self._cnonce = None
        self._response = None

        self._body = None

    def get_username(self) -> str: return self._username

    def get_uri(self) -> str: return self._uri

    def get_qop(self) -> QOP: return self._qop

    def get_algorithm(self) -> Algorithm: return self._algorithm

    def get_cnonce(self) -> bytes: return self._cnonce

    def get_response(self) -> str: return self._response

    def set_body(self, value: str): self._body = value


class RequestDigest(Digest):
    __NONCE_LENGTH = 32

    def __init__(self, username: str, secret: str, full_url: str) -> None:
        super().__init__()

        self._username = username
        self._secret = secret
        self._algorithm = Algorithm.SHA256
        self._qop = QOP.AUTH_INT
        self._cnonce = bytes(str(int(datetime.datetime.now().timestamp())), 'utf8') + b':' + secrets.token_bytes(self.__NONCE_LENGTH)

        url = urlparse(full_url)
        self._uri = url.path

    def create_header(self) -> str:
        data = bytes(self._username, 'utf8') + self._cnonce + bytes(str(self._qop.value), 'utf8') + bytes(self._uri, 'utf8')
        if self._qop == QOP.AUTH_INT:
            data += bytes(self._body, 'utf8')

        self._response = hmac.new(bytes(self._secret, 'utf8'), data, self._algorithm.get_digestmod()).hexdigest()
        return 'Digest username=%s, uri="%s", algorithm=%s, cnonce="%s", qop=%s, response="%s"' % (
            self._username,
            self._uri,
            self._algorithm.value,
            str(base64.b64encode(self._cnonce), "utf-8"),
            self._qop.value,
            self._response
        )


class ResponseDigest(Digest):
    def __init__(self, authorization_header: str) -> None:
        """
        Parse and verify raw value of 'Authorization' header.
        
        :param authorization_header: raw value of 'Authorization' header.
        
        If verification fails, DigestMismatchError will be thrown.
        """
        super().__init__()

        self._timestamp = None
        self._snonce = None
        self._original_uri = None
        self._original_cnonce = None

        if authorization_header == "":
            raise DigestMissingError()

        values = {
            "username": "",
            "uri": "",
            "response": "",
            "algorithm": "",
            "qop": "",
            "cnonce": "",
            "snonce": "",
        }

        elements = authorization_header \
            .replace("\n", "") \
            .replace("\r", "") \
            .split(',')

        for i, key_value in enumerate(elements):
            try:
                key_value = key_value.strip()
                delimiter_pos = key_value.index("=")
                key = key_value[:delimiter_pos]
                if i == 0:
                    key = key.lower().replace("digest ", "", 1)

                if key in values:
                    value = key_value[delimiter_pos + 1:]
                    values[key] = value.strip('"').strip()
            except ValueError:
                raise DigestMismatchError("Digest mismatch: unexpected element '%s'" % key_value)

        for key, value in values.items():
            if value == "":
                raise DigestMismatchError("Digest mismatch: empty value for %s" % key)

            if key == "username":
                self._username = value
            elif key == "uri":
                self._uri = value
            elif key == "response":
                self._response = value
            elif key == "algorithm":
                try:
                    self._algorithm = Algorithm(value)
                except ValueError:
                    raise DigestMismatchError("Digest mismatch: format error: unknown algorithm")
            elif key == "qop":
                try:
                    self._qop = QOP(value)
                except ValueError:
                    raise DigestMismatchError("Digest mismatch: format error: unknown QOP value")
            elif key == "cnonce":
                self._cnonce = base64.b64decode(value)
            elif key == "snonce":
                self._snonce = base64.b64decode(value)

                try:
                    timestamp_delimiter_pos = self._snonce.index(b':')
                except ValueError:
                    raise DigestMismatchError("Digest mismatch: corrupted value for snonce (missing timestamp)")

                timestamp = self._snonce[:timestamp_delimiter_pos]
                if timestamp == "" or not timestamp.isdigit():
                    raise DigestMismatchError('Digest mismatch: corrupted value for snonce (unexpected timestamp value)')
                self._timestamp = int(timestamp, base=10)

    def set_original_uri(self, value: str):
        self._original_uri = value

    def set_original_cnonce(self, value: bytes):
        self._original_cnonce = value

    def get_timestamp(self) -> int:
        return self._timestamp

    def get_snonce(self) -> bytes:
        return self._snonce

    def verify(self, object_guid: str, secret: str) -> None:
        """
        Verify parsed digest against given object_guid/secret.
        
        :param object_guid: object GUID. Should be equal to username from header.
        :param secret: Secret key to calculate HMAC
        
        If verification fails, DigestMismatchError will be thrown.
        
        If original URI/cnonce was set, an additional validation against
        these values will be performed. If values differ, DigestMismatchError will be thrown.
        """
        if object_guid.lower() != self._username.lower():
            raise DigestMismatchError("Digest mismatch: username mismatch")

        if self._original_uri is not None and self._original_uri != self._uri:
            raise DigestMismatchError("Digest mismatch: uri mismatch")

        if self._original_cnonce is not None and self._original_cnonce != self._cnonce:
            raise DigestMismatchError("Digest mismatch: cnonce mismatch")

        data = bytes(self._username, 'utf8') + self._cnonce + self._snonce + bytes(str(self._qop.value), 'utf8') + bytes(self._uri, 'utf8')
        if self._qop == QOP.AUTH_INT:
            data += bytes(self._body, 'utf8')

        expected_digest = hmac.new(bytes(secret, 'utf8'), data, self._algorithm.get_digestmod()).hexdigest()
        if not hmac.compare_digest(expected_digest, self._response):
            raise DigestMismatchError()
