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
import hashlib
import json
from unittest import TestCase

from gateway.crypto.digest import Algorithm, RequestDigest, QOP, DigestMissingError, ResponseDigest, DigestMismatchError
from gateway.responses.payment import CallbackResult


class TestAlgorithm(TestCase):
    def test_get_digestmod(self):
        self.assertEqual(hashlib.sha256, Algorithm.SHA256.get_digestmod())


class TestRequestDigest(TestCase):
    def test_create_header(self):
        expected = "Digest username=bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b, uri=\"/v3.0/sms\", algorithm=SHA-256, " \
                   "cnonce=\"MTU5MTYyNTA2MzqydV+lpoF4ZtfSAifxoUretZdAzGaZa97iRogrQ8K/yg==\", qop=auth-int, " \
                   "response=\"a21df219fd9bb2efb71554eb9ebb47f6a7a61769a289f9ab4fcbe41d7544e28d\""

        instance = RequestDigest("bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b", "agHJSthpTPfKEORLDynBuIl07i4sYVmw", "https://some.url/v3.0/sms")
        self.assertEqual(Algorithm.SHA256, instance.get_algorithm())
        self.assertEqual(QOP.AUTH_INT, instance.get_qop())
        self.assertEqual(43, len(instance.get_cnonce()))

        instance.set_body(
            "{\"auth-data\":{},\"data\":{\"command-data\":{},\"general-data\":{\"customer-data\":{\"email\":\"test@test.domain\",\"birth-date\":\"01/00\"," +
            "\"phone\":\"123456789\",\"billing-address\":{\"country\":\"FR\",\"state\":\"FR\",\"city\":\"Chalon-sur-Saône\",\"street\":\"Rue Garibaldi\"," +
            "\"house\":\"10\",\"flat\":\"10\",\"zip\":\"71100\"},\"shipping-address\":{\"country\":\"FR\",\"state\":\"FR\",\"city\":\"Chalon-sur-Saône\"," +
            "\"street\":\"Rue Garibaldi\",\"house\":\"10\",\"flat\":\"10\",\"zip\":\"71100\"}},\"order-data\":{\"merchant-transaction-id\":\"\"," +
            "\"order-id\":\"Order ID\",\"order-description\":\"Payment\",\"merchant-side-url\":\"https://domain.com/custom-url/\"," +
            "\"merchant-referring-name\":\"Test payment\",\"custom3d-return-url\":\"https://domain.com\"}},\"payment-method-data\":" +
            "{\"pan\":\"4111111111111111\",\"exp-mm-yy\":\"09/31\",\"cvv\":\"123\",\"cardholder-name\":\"John Doe\"},\"money-data\":" +
            "{\"amount\":100,\"currency\":\"EUR\"},\"system\":{\"user-ip\":\"127.0.0.1\"}}}"
        )
        instance._cnonce = base64.b64decode("MTU5MTYyNTA2MzqydV+lpoF4ZtfSAifxoUretZdAzGaZa97iRogrQ8K/yg==")
        actual = instance.create_header()

        self.assertEqual(expected, actual)


class TestResponseDigest(TestCase):
    def test_parse_errors(self):
        nonce = str(base64.b64encode(bytes("1:q", "utf-8")), "utf-8")
        no_ts_nonce = str(base64.b64encode(bytes("qqq", "utf-8")), "utf-8")
        wrong_ts_nonce = str(base64.b64encode(bytes("qqq:www", "utf-8")), "utf-8")

        cases = [
            ('', DigestMissingError, 'Digest is missing'),
            (
                "Digest uri=b, algorithm=SHA-256, cnonce=%s, snonce=%s, qop=auth-int, response=e" % (nonce, nonce),
                DigestMismatchError, 'Digest mismatch: empty value for username'
            ),
            (
                "Digest username=a, algorithm=SHA-256, cnonce=%s, snonce=%s, qop=auth-int, response=e" % (nonce, nonce),
                DigestMismatchError, "Digest mismatch: empty value for uri"
            ),
            (
                "Digest username=a, uri=b, cnonce=%s, snonce=%s, qop=auth-int, response=e" % (nonce, nonce),
                DigestMismatchError, "Digest mismatch: empty value for algorithm"
            ),
            (
                "Digest username=a, uri=b, algorithm=SHA-256, snonce=%s, qop=auth-int, response=e" % nonce,
                DigestMismatchError, "Digest mismatch: empty value for cnonce"
            ),
            (
                "Digest username=a, uri=b, algorithm=SHA-256, cnonce=%s, qop=auth-int, response=e" % nonce,
                DigestMismatchError, "Digest mismatch: empty value for snonce"
            ),
            (
                "Digest username=a, uri=b, algorithm=SHA-256, cnonce=%s, snonce=%s, response=e" % (nonce, nonce),
                DigestMismatchError, "Digest mismatch: empty value for qop"
            ),
            (
                "Digest username=a, uri=b, algorithm=SHA-256, cnonce=%s, snonce=%s, qop=auth" % (nonce, nonce),
                DigestMismatchError, "Digest mismatch: empty value for response"
            ),
            (
                "Digest username=a, uri=b, algorithm=SHA-256, cnonce=%s, snonce=%s, qop=aaa, response=x" % (nonce, nonce),
                DigestMismatchError, "Digest mismatch: format error: unknown QOP value"
            ),
            (
                "Digest username=a, uri=b, algorithm=aaa, cnonce=%s, snonce=%s, qop=auth, response=x" % (nonce, nonce),
                DigestMismatchError, "Digest mismatch: format error: unknown algorithm"
            ),
            (
                "Digest username=a, uri=b, algorithm=SHA-256, cnonce=%s, snonce=%s, qop=auth, response=x" % (nonce, no_ts_nonce),
                DigestMismatchError, "Digest mismatch: corrupted value for snonce (missing timestamp)"
            ),
            (
                "Digest username=a, uri=b, algorithm=SHA-256, cnonce=%s, snonce=%s, qop=auth, response=x" % (nonce, wrong_ts_nonce),
                DigestMismatchError, "Digest mismatch: corrupted value for snonce (unexpected timestamp value)"
            ),
        ]

        for i, test_case in enumerate(cases):
            [header, expected_error, expected_message] = test_case

            with self.subTest("#%d" % i):
                with self.assertRaises(expected_error) as cm:
                    ResponseDigest(header)
                self.assertEqual(expected_message, str(cm.exception))

    def test_parse_successful(self):
        header = "Digest username=bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b, uri=\"/v3.0/sms\", algorithm=SHA-256, " \
                 "cnonce=\"MTU5MTYyNTA2MzqydV+lpoF4ZtfSAifxoUretZdAzGaZa97iRogrQ8K/yg==\", " \
                 "snonce=\"MTU5MTYyNDgwNzoUte6YsXIJmUo1EsA4yrYDCVbPrvCrEtqGq6CHTMhImg==\", qop=auth-int, " \
                 "response=\"a21df219fd9bb2efb71554eb9ebb47f6a7a61769a289f9ab4fcbe41d7544e28d\""
        digest = ResponseDigest(header)

        self.assertEqual("bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b", digest.get_username())
        self.assertEqual("/v3.0/sms", digest.get_uri())
        self.assertEqual(Algorithm.SHA256, digest.get_algorithm())
        self.assertEqual(QOP.AUTH_INT, digest.get_qop())
        self.assertEqual("a21df219fd9bb2efb71554eb9ebb47f6a7a61769a289f9ab4fcbe41d7544e28d", digest.get_response())
        self.assertEqual(1591624807, digest.get_timestamp())
        self.assertEqual(base64.b64decode("MTU5MTYyNTA2MzqydV+lpoF4ZtfSAifxoUretZdAzGaZa97iRogrQ8K/yg=="), digest.get_cnonce())
        self.assertEqual(base64.b64decode("MTU5MTYyNDgwNzoUte6YsXIJmUo1EsA4yrYDCVbPrvCrEtqGq6CHTMhImg=="), digest.get_snonce())

    def test_verify_errors(self):
        valid_cnonce = base64.b64decode("MTU5MTg2NjU3Mzo38zMeHvu4qcbhR8X158atP/BB4dDb5DbOMRT656yS7Q==")
        invalid_cnonce = base64.b64decode("MTU5MTg2NjU3MzpvnttqUse7hfrkUHtPS8tWE1jl0D0G/DgMmEFwbk5/jw==")

        cases = [
            ("wrong-guid", "/v3.0/sms", valid_cnonce, "Digest mismatch: username mismatch"),
            ("bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b", "http://another.local", valid_cnonce, "Digest mismatch: uri mismatch"),
            ("bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b", "/v3.0/sms", invalid_cnonce, "Digest mismatch: cnonce mismatch"),
            ("bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b", "/v3.0/sms", valid_cnonce, "Digest mismatch")
        ]

        body = "{\"acquirer-details\":{},\"error\":{},\"gw\":{\"gateway-transaction-id\":\"37b88436-b69c-45f3-ad26-b945153ad9a8\"," \
               "\"redirect-url\":\"http://api.local/4f1f647d10e8296a2ed4d21e3639f1ee\",\"status-code\":30,\"status-text\":" \
               "\"INSIDE FORM URL SENT\"},\"warnings\":[\"Soon counters will be exceeded for the merchant\",\"Soon counters will be exceeded " \
               "for the account\"]}"

        header = "Digest username=bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b, uri=\"/v3.0/sms\", algorithm=SHA-256, " \
                 "cnonce=\"MTU5MTg2NjU3Mzo38zMeHvu4qcbhR8X158atP/BB4dDb5DbOMRT656yS7Q==\", " \
                 "snonce=\"MTU5MTg2NjU3MzpvnttqUse7hfrkUHtPS8tWE1jl0D0G/DgMmEFwbk5/jw==\", qop=auth-int, " \
                 "response=\"624478f45d33bbadc7cf0ae9b34462efd7b9736111f295e6330fe0bc3b20acda\""

        for i, test_case in enumerate(cases):
            with self.subTest("#%d" % i):
                response_digest = ResponseDigest(header)
                response_digest.set_original_uri(test_case[1])
                response_digest.set_original_cnonce(test_case[2])
                response_digest.set_body(body)

                with self.assertRaises(DigestMismatchError) as cm:
                    response_digest.verify(test_case[0], "something wrong")
                self.assertEqual(test_case[3], str(cm.exception))

    def test_verify_success_full_checks(self):
        body = "{\"acquirer-details\":{},\"error\":{},\"gw\":{\"gateway-transaction-id\":\"37b88436-b69c-45f3-ad26-b945153ad9a8\"," \
               "\"redirect-url\":\"http://api.local/4f1f647d10e8296a2ed4d21e3639f1ee\",\"status-code\":30,\"status-text\":" \
               "\"INSIDE FORM URL SENT\"},\"warnings\":[\"Soon counters will be exceeded for the merchant\",\"Soon counters will be exceeded " \
               "for the account\"]}"

        header = "Digest username=bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b, uri=\"/v3.0/sms\", algorithm=SHA-256, " \
                 "cnonce=\"MTU5MTg2NjU3Mzo38zMeHvu4qcbhR8X158atP/BB4dDb5DbOMRT656yS7Q==\", " \
                 "snonce=\"MTU5MTg2NjU3MzpvnttqUse7hfrkUHtPS8tWE1jl0D0G/DgMmEFwbk5/jw==\", qop=auth-int, " \
                 "response=\"dda7026eebbeeee19fda191fd951d470b2064e3e1bc416365835abc775352552\""

        response_digest = ResponseDigest(header)
        response_digest.set_original_uri("/v3.0/sms")
        response_digest.set_original_cnonce(base64.b64decode("MTU5MTg2NjU3Mzo38zMeHvu4qcbhR8X158atP/BB4dDb5DbOMRT656yS7Q=="))
        response_digest.set_body(body)
        response_digest.verify("bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b", "tPMOogw7YBumh6RpXxi2nvGW0C9lJq3L")

    def test_verify_success_minimal_checks(self):
        body = "{\"acquirer-details\":{},\"error\":{},\"gw\":{\"gateway-transaction-id\":\"37b88436-b69c-45f3-ad26-b945153ad9a8\"," \
               "\"redirect-url\":\"http://api.local/4f1f647d10e8296a2ed4d21e3639f1ee\",\"status-code\":30,\"status-text\":" \
               "\"INSIDE FORM URL SENT\"},\"warnings\":[\"Soon counters will be exceeded for the merchant\",\"Soon counters will be exceeded " \
               "for the account\"]}"

        header = "Digest username=bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b, uri=\"/v3.0/sms\", algorithm=SHA-256, " \
                 "cnonce=\"MTU5MTg2NjU3Mzo38zMeHvu4qcbhR8X158atP/BB4dDb5DbOMRT656yS7Q==\", " \
                 "snonce=\"MTU5MTg2NjU3MzpvnttqUse7hfrkUHtPS8tWE1jl0D0G/DgMmEFwbk5/jw==\", qop=auth-int, " \
                 "response=\"dda7026eebbeeee19fda191fd951d470b2064e3e1bc416365835abc775352552\""

        response_digest = ResponseDigest(header)
        response_digest.set_body(body)
        response_digest.verify("bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b", "tPMOogw7YBumh6RpXxi2nvGW0C9lJq3L")

    def test_verify_callback(self):
        json_from_post = "{\"result-data\":{\"gw\":{\"gateway-transaction-id\":\"8d77f986-de7f-4d47-97ef-9de7f8561684\",\"status-code\":7,\"status-text\":\"SUCCESS\"}," \
                         "\"error\":{},\"acquirer-details\":{\"eci-sli\":\"503\",\"terminal-mid\":\"3201210\",\"transaction-id\":\"7146311464333929\"," \
                         "\"result-code\":\"000\",\"status-text\":\"Approved\",\"status-description\":\"Approved\"},\"warnings\":" \
                         "[\"Soon counters will be exceeded for the merchant\",\"Soon counters will be exceeded for the account\"," \
                         "\"Soon counters will be exceeded for the terminal group\",\"Soon counters will be exceeded for the terminal\"]}}"

        sign_from_post = "Digest username=bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b, uri=\"/v3.0/sms\", algorithm=SHA-256, " \
                         "cnonce=\"MTU5MTg2OTQ3OTpbmPfGQxVAh5z7MdWnRjF1cavfwKyxiLVrX4p7IHNwWA==\", " \
                         "snonce=\"MTU5MTg2OTQ4MTqfPxash/0hfNpI/gHuaoSiV+6PwVKYEawxchE0nxHTkA==\", qop=auth-int, " \
                         "response=\"87bd753875e28da54dfcb5e61614e10a7120aba9a3f8bed0e6eaa9acb85aa9f9\""

        response_digest = ResponseDigest(sign_from_post)
        response_digest.set_original_uri("/v3.0/sms")
        response_digest.set_original_cnonce(base64.b64decode("MTU5MTg2OTQ3OTpbmPfGQxVAh5z7MdWnRjF1cavfwKyxiLVrX4p7IHNwWA=="))
        response_digest.set_body(json_from_post)
        response_digest.verify("bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b", "tPMOogw7YBumh6RpXxi2nvGW0C9lJq3L")

        parsed_result = CallbackResult(json.loads(json_from_post))
        self.assertEqual("8d77f986-de7f-4d47-97ef-9de7f8561684", parsed_result.gw.gateway_transaction_id)
