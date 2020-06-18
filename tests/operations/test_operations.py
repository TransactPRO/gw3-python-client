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
from urllib.parse import urlparse

from gateway.builders.transaction_builder import *
from gateway.operations.operations import Operations
from gateway.responses.constants import Status, ErrorCode
from gateway.responses.enrollment import EnrollmentStatus
from gateway.responses.lists import RefundsListElement, TransactionResult, TransactionStatus
from gateway.responses.parts import TransactionInfo
from gateway.responses.payment import GW
from gateway.responses.response import parse_date
from gateway.transport.transport import HTTP_GET


class TestOperations(TestCase):
    OP = None

    def setUp(self):
        self.__operation_data = {}
        self.__asked_operation = {}
        self.__operation_mandatory_fields = {}

        self.OP = Operations(self.__operation_data, self.__asked_operation, self.__operation_mandatory_fields)

    def test_sms(self):
        self.assertIsInstance(self.OP.sms(), SmsBuilder)

    def test_dms_hold(self):
        self.assertIsInstance(self.OP.dms_hold(), DmsHoldBuilder)

    def test_dms_charge(self):
        self.assertIsInstance(self.OP.dms_charge(), DmsChargeBuilder)

    def test_dms_cancel(self):
        self.assertIsInstance(self.OP.dms_cancel(), DmsCancelBuilder)

    def test_moto_sms(self):
        self.assertIsInstance(self.OP.moto_sms(), MotoSmsBuilder)

    def test_moto_dms(self):
        self.assertIsInstance(self.OP.moto_dms(), MotoDmsBuilder)

    def test_credit(self):
        self.assertIsInstance(self.OP.credit(), CreditBuilder)

    def test_p2p(self):
        new_op = self.OP
        self.assertIsInstance(new_op.p2p(), P2PBuilder)

    def test_b2p(self):
        self.assertIsInstance(self.OP.b2p(), B2PBuilder)

    def test_init_recurrent_sms(self):
        self.assertIsInstance(self.OP.init_recurrent_sms(), SmsBuilder)

    def test_recurrent_sms(self):
        self.assertIsInstance(self.OP.recurrent_sms(), RecurrentSmsBuilder)

    def test_init_recurrent_dms(self):
        self.assertIsInstance(self.OP.init_recurrent_dms(), DmsHoldBuilder)

    def test_recurrent_dms(self):
        self.assertIsInstance(self.OP.recurrent_dms(), RecurrentDmsBuilder)

    def test_refund(self):
        self.assertIsInstance(self.OP.refund(), RefundBuilder)

    def test_reversal(self):
        self.assertIsInstance(self.OP.reversal(), ReversalBuilder)

    def test_transaction_status(self):
        self.assertIsInstance(self.OP.transaction_status(), TransactionStatusBuilder)

    def test_transaction_result(self):
        self.assertIsInstance(self.OP.transaction_result(), TransactionResultBuilder)

    def test_transaction_history(self):
        self.assertIsInstance(self.OP.transaction_history(), TransactionHistoryBuilder)

    def test_transaction_recurrent_history(self):
        self.assertIsInstance(self.OP.transaction_recurrent_history(), TransactionRecurringHistoryBuilder)

    def test_transaction_refunds_history(self):
        self.assertIsInstance(self.OP.transaction_refunds_history(), TransactionRefundsHistoryBuilder)

    def test_limits(self):
        self.assertIsInstance(self.OP.limits(), LimitsBuilder)

    def test_verify_3d_enrollment(self):
        self.assertIsInstance(self.OP.verify_3d_enrollment(), Verify3dBuilder)

    def test_verify_card(self):
        self.assertIsInstance(self.OP.verify_card(), VerifyCardBuilder)

    def test_create_token(self):
        self.assertIsInstance(self.OP.create_token(), CreateTokenBuilder)

    def test_report(self):
        self.assertIsInstance(self.OP.report(), ReportBuilder)

    def test_retrieve_form(self):
        with self.assertRaises(RuntimeError) as cm:
            self.OP.retrieve_form({})
        self.assertEqual('Payment response has invalid type', str(cm.exception))

        response = PaymentResponse()
        with self.assertRaises(RuntimeError) as cm:
            self.OP.retrieve_form(response)
            self.assertEqual("Response doesn't contain link to an HTML form", str(cm.exception))

        response.gw = GW()
        with self.assertRaises(RuntimeError) as cm:
            self.OP.retrieve_form(response)
        self.assertEqual("Response doesn't contain link to an HTML form", str(cm.exception))

        expected_url = 'http://some.url/with/path'
        response.gw.redirect_url = urlparse(expected_url)
        self.OP.retrieve_form(response)
        self.assertEqual(self.__asked_operation['method'], HTTP_GET)
        self.assertEqual(self.__asked_operation['current'], expected_url)


class TestResponseParsing(TestCase):
    def setUp(self):
        self.operations = Operations({}, {}, {})

    def test_history(self):
        expected_date1 = parse_date("2020-06-09 09:56:53")
        expected_date2 = parse_date("2020-06-09 09:57:53")

        body = b"{\"transactions\":[{\"error\":{\"code\":400,\"message\":\"Failed to fetch data for transaction with gateway id: " \
               b"a2975c68-e235-40a4-87a9-987824c20000\"},\"gateway-transaction-id\":\"a2975c68-e235-40a4-87a9-987824c20000\"}," \
               b"{\"gateway-transaction-id\":\"a2975c68-e235-40a4-87a9-987824c2090a\",\"history\":[{\"date-updated\":\"2020-06-09 09:56:53\"," \
               b"\"status-code-new\":2,\"status-code-old\":1,\"status-text-new\":\"SENT TO BANK\",\"status-text-old\":\"INIT\"}," \
               b"{\"date-updated\":\"2020-06-09 09:57:53\",\"status-code-new\":7,\"status-code-old\":2,\"status-text-new\":\"SUCCESS\"," \
               b"\"status-text-old\":\"SENT TO BANK\"}]}]}"

        response = GatewayResponse(200, body)
        parsed_response = self.operations.transaction_history().parse(response)
        self.assertEqual(2, len(parsed_response.transactions))

        tr1 = parsed_response.transactions[0]
        self.assertEqual("a2975c68-e235-40a4-87a9-987824c20000", tr1.gateway_transaction_id)
        self.assertEqual(400, tr1.error.error_code)
        self.assertEqual("Failed to fetch data for transaction with gateway id: a2975c68-e235-40a4-87a9-987824c20000", tr1.error.message)

        tr2 = parsed_response.transactions[1]
        self.assertEqual("a2975c68-e235-40a4-87a9-987824c2090a", tr2.gateway_transaction_id)
        self.assertEqual(2, len(tr2.history))

        event1 = tr2.history[0]
        self.assertEqual(expected_date1, event1.date_updated)
        self.assertEqual(Status.INIT, event1.status_code_old)
        self.assertEqual(Status.SENT2BANK, event1.status_code_new)
        self.assertEqual("INIT", event1.status_text_old)
        self.assertEqual("SENT TO BANK", event1.status_text_new)

        event2 = tr2.history[1]
        self.assertEqual(expected_date2, event2.date_updated)
        self.assertEqual(Status.SENT2BANK, event2.status_code_old)
        self.assertEqual(Status.SUCCESS, event2.status_code_new)
        self.assertEqual("SENT TO BANK", event2.status_text_old)
        self.assertEqual("SUCCESS", event2.status_text_new)

    def test_limits(self):
        body = b"{\"childs\":[{\"childs\":[{\"childs\":[{\"counters\":[{\"counter-type\":\"TR_SUCCESS_AMOUNT\",\"currency\":\"EUR\"," \
               b"\"limit\":5000000,\"payment-method-subtype\":\"all\",\"payment-method-type\":\"all\",\"value\":28410}," \
               b"{\"counter-type\":\"TR_SUCCESS_COUNT\",\"currency\":\"EUR\",\"limit\":20000,\"payment-method-subtype\":\"all\"," \
               b"\"payment-method-type\":\"all\",\"value\":992}],\"acq-terminal-id\":\"5800978\",\"title\":\"Test T1\",\"type\":\"terminal\"}]," \
               b"\"counters\":[{\"counter-type\":\"TR_SUCCESS_AMOUNT\",\"currency\":\"EUR\",\"limit\":5000000,\"payment-method-subtype\":\"all\"," \
               b"\"payment-method-type\":\"all\",\"value\":2400}],\"title\":\"Test TG\",\"type\":\"terminal-group\"}],\"counters\":" \
               b"[{\"counter-type\":\"TR_SUCCESS_AMOUNT\",\"currency\":\"EUR\",\"limit\":5000000,\"payment-method-subtype\":\"all\"," \
               b"\"payment-method-type\":\"all\",\"value\":2400}],\"title\":\"Test ACC\",\"type\":\"account\"}],\"counters\":" \
               b"[{\"counter-type\":\"TR_SUCCESS_AMOUNT\",\"currency\":\"EUR\",\"limit\":5000000,\"payment-method-subtype\":\"all\"," \
               b"\"payment-method-type\":\"all\",\"value\":2400}],\"title\":\"Test M\",\"type\":\"merchant\"}"

        response = GatewayResponse(200, body)
        merchant = self.operations.limits().parse(response)

        self.assertEqual("merchant", merchant.limits.type)
        self.assertEqual("Test M", merchant.limits.title)
        self.assertIsNone(merchant.limits.acq_terminal_id)
        self.assertEqual(1, len(merchant.limits.children))
        self.assertEqual(1, len(merchant.limits.limits))
        self.assertEqual("TR_SUCCESS_AMOUNT", merchant.limits.limits[0].counter_type)
        self.assertEqual("EUR", merchant.limits.limits[0].currency)
        self.assertEqual(5000000, merchant.limits.limits[0].limit)
        self.assertEqual(2400, merchant.limits.limits[0].value)
        self.assertEqual("all", merchant.limits.limits[0].payment_method_type)
        self.assertEqual("all", merchant.limits.limits[0].payment_method_subtype)

        account = merchant.limits.children[0]
        self.assertEqual("account", account.type)
        self.assertEqual("Test ACC", account.title)
        self.assertIsNone(account.acq_terminal_id)
        self.assertEqual(1, len(account.children))
        self.assertEqual(1, len(account.limits))
        self.assertEqual("TR_SUCCESS_AMOUNT", account.limits[0].counter_type)
        self.assertEqual("EUR", account.limits[0].currency)
        self.assertEqual(5000000, account.limits[0].limit)
        self.assertEqual(2400, account.limits[0].value)
        self.assertEqual("all", account.limits[0].payment_method_type)
        self.assertEqual("all", account.limits[0].payment_method_subtype)

        terminal_group = account.children[0]
        self.assertEqual("terminal-group", terminal_group.type)
        self.assertEqual("Test TG", terminal_group.title)
        self.assertIsNone(terminal_group.acq_terminal_id)
        self.assertEqual(1, len(terminal_group.children))
        self.assertEqual(1, len(terminal_group.limits))
        self.assertEqual("TR_SUCCESS_AMOUNT", terminal_group.limits[0].counter_type)
        self.assertEqual("EUR", terminal_group.limits[0].currency)
        self.assertEqual(5000000, terminal_group.limits[0].limit)
        self.assertEqual(2400, terminal_group.limits[0].value)
        self.assertEqual("all", terminal_group.limits[0].payment_method_type)
        self.assertEqual("all", terminal_group.limits[0].payment_method_subtype)

        terminal = terminal_group.children[0]
        self.assertEqual("terminal", terminal.type)
        self.assertEqual("Test T1", terminal.title)
        self.assertEqual("5800978", terminal.acq_terminal_id)
        self.assertEqual(0, len(terminal.children))
        self.assertEqual(2, len(terminal.limits))

        self.assertEqual("TR_SUCCESS_AMOUNT", terminal.limits[0].counter_type)
        self.assertEqual("EUR", terminal.limits[0].currency)
        self.assertEqual(5000000, terminal.limits[0].limit)
        self.assertEqual(28410, terminal.limits[0].value)
        self.assertEqual("all", terminal.limits[0].payment_method_type)
        self.assertEqual("all", terminal.limits[0].payment_method_subtype)

        self.assertEqual("TR_SUCCESS_COUNT", terminal.limits[1].counter_type)
        self.assertEqual("EUR", terminal.limits[1].currency)
        self.assertEqual(20000, terminal.limits[1].limit)
        self.assertEqual(992, terminal.limits[1].value)
        self.assertEqual("all", terminal.limits[1].payment_method_type)
        self.assertEqual("all", terminal.limits[1].payment_method_subtype)

    def test_recurring_history(self):
        expected_date_finished = parse_date("2020-06-09 09:56:53")

        body = b"{\"transactions\":[{\"error\":{\"code\":400,\"message\":\"Failed to fetch data for transaction with gateway id: " \
               b"9e09bad0-5704-4b78-bf6a-c612f0101900\"},\"gateway-transaction-id\":\"9e09bad0-5704-4b78-bf6a-c612f0101900\"}," \
               b"{\"gateway-transaction-id\":\"9e09bad0-5704-4b78-bf6a-c612f010192a\",\"recurrents\":[{\"account-guid\":" \
               b"\"bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b\",\"account-id\":108,\"acq-terminal-id\":\"5800978\",\"acq-transaction-id\":" \
               b"\"7435540948424227\",\"amount\":100,\"approval-code\":\"4773442\",\"cardholder-name\":\"John Doe\",\"currency\":\"EUR\"," \
               b"\"date-finished\":\"2020-06-09 09:56:53\",\"eci-sli\":\"464\",\"gateway-transaction-id\":\"a2975c68-e235-40a4-87a9-987824c2090a\"," \
               b"\"merchant-transaction-id\":\"52a9990bad03e15417c70ef11a8103e1\",\"status-code\":7,\"status-code-general\":13," \
               b"\"status-text\":\"SUCCESS\",\"status-text-general\":\"REFUND SUCCESS\"}]}]}"

        response = GatewayResponse(200, body)
        parsed_response = self.operations.transaction_recurrent_history().parse(response)
        self.assertEqual(2, len(parsed_response.transactions))

        tr1 = parsed_response.transactions[0]
        self.assertEqual("9e09bad0-5704-4b78-bf6a-c612f0101900", tr1.gateway_transaction_id)
        self.assertEqual(400, tr1.error.error_code)
        self.assertEqual("Failed to fetch data for transaction with gateway id: 9e09bad0-5704-4b78-bf6a-c612f0101900", tr1.error.message)

        tr2 = parsed_response.transactions[1]
        self.assertEqual("9e09bad0-5704-4b78-bf6a-c612f010192a", tr2.gateway_transaction_id)
        self.assertEqual(1, len(tr2.subsequent))

        info1: TransactionInfo = tr2.subsequent[0]
        self.assertEqual("bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b", info1.account_guid)
        self.assertEqual("5800978", info1.acq_terminal_id)
        self.assertEqual("7435540948424227", info1.acq_transaction_id)
        self.assertEqual(100, info1.amount)
        self.assertEqual("4773442", info1.approval_code)
        self.assertEqual("John Doe", info1.cardholder_name)
        self.assertEqual("EUR", info1.currency)
        self.assertEqual(expected_date_finished, info1.date_finished)
        self.assertEqual("464", info1.eci_sli)
        self.assertEqual("a2975c68-e235-40a4-87a9-987824c2090a", info1.gateway_transaction_id)
        self.assertEqual("52a9990bad03e15417c70ef11a8103e1", info1.merchant_transaction_id)
        self.assertEqual(Status.SUCCESS, info1.status_code)
        self.assertEqual(Status.REFUND_SUCCESS, info1.status_code_general)
        self.assertEqual("SUCCESS", info1.status_text)
        self.assertEqual("REFUND SUCCESS", info1.status_text_general)

    def test_refunds(self):
        expected_date_finished1 = parse_date("2020-06-09 10:18:15")
        expected_date_finished2 = parse_date("2020-06-09 10:18:22")

        body = b"{\"transactions\":[{\"gateway-transaction-id\":\"a2975c68-e235-40a4-87a9-987824c2090a\",\"refunds\":" \
               b"[{\"account-guid\":\"bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b\",\"account-id\":108,\"acq-terminal-id\":\"5800978\"," \
               b"\"acq-transaction-id\":\"1128894405863338\",\"amount\":10,\"approval-code\":\"1299034\",\"cardholder-name\":\"John Doe\"," \
               b"\"currency\":\"EUR\",\"date-finished\":\"2020-06-09 10:18:15\",\"eci-sli\":\"960\",\"gateway-transaction-id\":" \
               b"\"508fd8b9-3f78-486b-812b-2756f44e1bc6\",\"merchant-transaction-id\":\"aaa1\",\"status-code\":13,\"status-code-general\":11," \
               b"\"status-text\":\"REFUND SUCCESS\",\"status-text-general\":\"REFUND FAILED\"},{\"account-guid\":" \
               b"\"bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b\",\"account-id\":108,\"acq-terminal-id\":\"5800978\",\"acq-transaction-id\":" \
               b"\"0508080614087693\",\"amount\":20,\"approval-code\":\"7117603\",\"cardholder-name\":\"John Doe\",\"currency\":\"EUR\"," \
               b"\"date-finished\":\"2020-06-09 10:18:22\",\"eci-sli\":\"690\",\"gateway-transaction-id\":\"191228b8-fd2d-47c8-8ff7-d28ba799cdb4\"," \
               b"\"merchant-transaction-id\":\"\",\"status-code\":13,\"status-code-general\":13,\"status-text\":\"REFUND SUCCESS\"," \
               b"\"status-text-general\":\"REFUND SUCCESS\"}]},{\"error\":{\"code\":400,\"message\":" \
               b"\"Failed to fetch data for transaction with gateway id: a2975c68-e235-40a4-87a9-987824c20900\"}," \
               b"\"gateway-transaction-id\":\"a2975c68-e235-40a4-87a9-987824c20900\"}]}"

        response = GatewayResponse(200, body)
        parsed_response = self.operations.transaction_refunds_history().parse(response)
        self.assertEqual(2, len(parsed_response.transactions))

        tr1: RefundsListElement = parsed_response.transactions[0]
        self.assertEqual("a2975c68-e235-40a4-87a9-987824c2090a", tr1.gateway_transaction_id)
        self.assertEqual(2, len(tr1.refunds))

        refund1: TransactionInfo = tr1.refunds[0]
        self.assertEqual("bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b", refund1.account_guid)
        self.assertEqual("5800978", refund1.acq_terminal_id)
        self.assertEqual("1128894405863338", refund1.acq_transaction_id)
        self.assertEqual(10, refund1.amount)
        self.assertEqual("1299034", refund1.approval_code)
        self.assertEqual("John Doe", refund1.cardholder_name)
        self.assertEqual("EUR", refund1.currency)
        self.assertEqual(expected_date_finished1, refund1.date_finished)
        self.assertEqual("960", refund1.eci_sli)
        self.assertEqual("508fd8b9-3f78-486b-812b-2756f44e1bc6", refund1.gateway_transaction_id)
        self.assertEqual("aaa1", refund1.merchant_transaction_id)
        self.assertEqual(Status.REFUND_SUCCESS, refund1.status_code)
        self.assertEqual(Status.REFUND_FAILED, refund1.status_code_general)
        self.assertEqual("REFUND SUCCESS", refund1.status_text)
        self.assertEqual("REFUND FAILED", refund1.status_text_general)

        refund2: TransactionInfo = tr1.refunds[1]
        self.assertEqual("bc501eda-e2a1-4e63-9a1e-7a7f6ff4813b", refund2.account_guid)
        self.assertEqual("5800978", refund2.acq_terminal_id)
        self.assertEqual("0508080614087693", refund2.acq_transaction_id)
        self.assertEqual(20, refund2.amount)
        self.assertEqual("7117603", refund2.approval_code)
        self.assertEqual("John Doe", refund2.cardholder_name)
        self.assertEqual("EUR", refund2.currency)
        self.assertEqual(expected_date_finished2, refund2.date_finished)
        self.assertEqual("690", refund2.eci_sli)
        self.assertEqual("191228b8-fd2d-47c8-8ff7-d28ba799cdb4", refund2.gateway_transaction_id)
        self.assertEqual("", refund2.merchant_transaction_id)
        self.assertEqual(Status.REFUND_SUCCESS, refund2.status_code)
        self.assertEqual(Status.REFUND_SUCCESS, refund2.status_code_general)
        self.assertEqual("REFUND SUCCESS", refund2.status_text)
        self.assertEqual("REFUND SUCCESS", refund2.status_text_general)

        tr2: RefundsListElement = parsed_response.transactions[1]
        self.assertEqual("a2975c68-e235-40a4-87a9-987824c20900", tr2.gateway_transaction_id)
        self.assertEqual(400, tr2.error.error_code)
        self.assertEqual("Failed to fetch data for transaction with gateway id: a2975c68-e235-40a4-87a9-987824c20900", tr2.error.message)

    def test_result(self):
        expected_date_created = parse_date("2020-06-10 08:37:22")
        expected_date_finished = parse_date("2020-06-10 08:37:23")

        body = b"{\"transactions\":[{\"date-created\":\"2020-06-10 08:37:22\",\"date-finished\":\"2020-06-10 08:37:23\"," \
               b"\"gateway-transaction-id\":\"b552fe8c-0fe3-4982-b2d6-9c37fa96dc58\",\"result-data\":{\"acquirer-details\":" \
               b"{\"eci-sli\":\"736\",\"result-code\":\"000\",\"status-description\":\"Approved\",\"status-text\":\"Approved\"," \
               b"\"terminal-mid\":\"5800978\",\"transaction-id\":\"8225174463086463\"},\"error\":{},\"gw\":" \
               b"{\"gateway-transaction-id\":\"b552fe8c-0fe3-4982-b2d6-9c37fa96dc58\",\"original-gateway-transaction-id\":" \
               b"\"096a93f4-c4d9-4b46-bbe9-22e30031f2d2\",\"parent-gateway-transaction-id\":\"096a93f4-c4d9-4b46-bbe9-22e30031f2d2\"," \
               b"\"status-code\":15,\"status-text\":\"CANCELLED\"}}},{\"error\":{\"code\":400,\"message\":" \
               b"\"Failed to get transaction result for transaction with gateway id: 965ffd17-1874-48d0-89f3-f2c2f06bf749\"}," \
               b"\"gateway-transaction-id\":\"965ffd17-1874-48d0-89f3-f2c2f06bf749\"}]}"

        response = GatewayResponse(200, body)
        parsed_response = self.operations.transaction_result().parse(response)
        self.assertEqual(2, len(parsed_response.transactions))

        tr1: TransactionResult = parsed_response.transactions[0]
        self.assertEqual("b552fe8c-0fe3-4982-b2d6-9c37fa96dc58", tr1.gateway_transaction_id)
        self.assertEqual(expected_date_created, tr1.date_created)
        self.assertEqual(expected_date_finished, tr1.date_finished)

        self.assertIsNotNone(tr1.result_data.acquirer_details)
        self.assertIsNone(tr1.result_data.acquirer_details.dynamic_descriptor)
        self.assertEqual("736", tr1.result_data.acquirer_details.eci_sli)
        self.assertEqual("000", tr1.result_data.acquirer_details.result_code)
        self.assertEqual("Approved", tr1.result_data.acquirer_details.status_description)
        self.assertEqual("Approved", tr1.result_data.acquirer_details.status_text)
        self.assertEqual("5800978", tr1.result_data.acquirer_details.terminal_mid)
        self.assertEqual("8225174463086463", tr1.result_data.acquirer_details.transaction_id)

        self.assertIsNotNone(tr1.result_data.gw)
        self.assertEqual("b552fe8c-0fe3-4982-b2d6-9c37fa96dc58", tr1.result_data.gw.gateway_transaction_id)
        self.assertEqual("096a93f4-c4d9-4b46-bbe9-22e30031f2d2", tr1.result_data.gw.original_gateway_transaction_id)
        self.assertEqual("096a93f4-c4d9-4b46-bbe9-22e30031f2d2", tr1.result_data.gw.parent_gateway_transaction_id)
        self.assertEqual(Status.DMS_CANCELED_OK, tr1.result_data.gw.status_code)
        self.assertEqual("CANCELLED", tr1.result_data.gw.status_text)

        tr2: TransactionResult = parsed_response.transactions[1]
        self.assertEqual("965ffd17-1874-48d0-89f3-f2c2f06bf749", tr2.gateway_transaction_id)
        self.assertEqual(400, tr2.error.error_code)
        self.assertEqual("Failed to get transaction result for transaction with gateway id: 965ffd17-1874-48d0-89f3-f2c2f06bf749", tr2.error.message)

    def test_status(self):
        body = b"{\"transactions\":[{\"gateway-transaction-id\":\"cd7b8bdf-3c78-4540-95d0-68018d2aba97\",\"status\":" \
               b"[{\"gateway-transaction-id\":\"cd7b8bdf-3c78-4540-95d0-68018d2aba97\",\"status-code\":7,\"status-code-general\":8," \
               b"\"status-text\":\"SUCCESS\",\"status-text-general\":\"EXPIRED\"}]},{\"gateway-transaction-id\":\"37908991-789b-4d79-8c6a-f90ba0ce12b6\"," \
               b"\"status\":[{\"gateway-transaction-id\":\"37908991-789b-4d79-8c6a-f90ba0ce12b6\",\"status-code\":8,\"status-code-general\":7," \
               b"\"status-text\":\"EXPIRED\",\"status-text-general\":\"SUCCESS\"}]}," \
               b"{\"error\":{\"code\":400,\"message\":\"Failed to fetch data for transaction with gateway id: 99900000-789b-4d79-8c6a-f90ba0ce12b0\"}," \
               b"\"gateway-transaction-id\":\"99900000-789b-4d79-8c6a-f90ba0ce12b0\"}]}"

        response = GatewayResponse(200, body)
        parsed_response = self.operations.transaction_status().parse(response)
        self.assertEqual(3, len(parsed_response.transactions))

        tr1: TransactionStatus = parsed_response.transactions[0]
        self.assertEqual("cd7b8bdf-3c78-4540-95d0-68018d2aba97", tr1.gateway_transaction_id)
        self.assertEqual(Status.SUCCESS, tr1.status_code)
        self.assertEqual(Status.EXPIRED, tr1.status_code_general)
        self.assertEqual("SUCCESS", tr1.status_text)
        self.assertEqual("EXPIRED", tr1.status_text_general)

        tr2: TransactionStatus = parsed_response.transactions[1]
        self.assertEqual("37908991-789b-4d79-8c6a-f90ba0ce12b6", tr2.gateway_transaction_id)
        self.assertEqual(Status.EXPIRED, tr2.status_code)
        self.assertEqual(Status.SUCCESS, tr2.status_code_general)
        self.assertEqual("EXPIRED", tr2.status_text)
        self.assertEqual("SUCCESS", tr2.status_text_general)

        tr3: TransactionStatus = parsed_response.transactions[2]
        self.assertEqual("99900000-789b-4d79-8c6a-f90ba0ce12b0", tr3.gateway_transaction_id)
        self.assertEqual(400, tr3.error.error_code)
        self.assertEqual("Failed to fetch data for transaction with gateway id: 99900000-789b-4d79-8c6a-f90ba0ce12b0", tr3.error.message)

    def test_payment_successful_api(self):
        body = b"{\"acquirer-details\":{\"dynamic-descriptor\":\"test\",\"eci-sli\":\"648\",\"result-code\":\"000\",\"status-description\":\"Approved\"," \
               b"\"status-text\":\"Approved\",\"terminal-mid\":\"5800978\",\"transaction-id\":\"1899493845214315\"},\"error\":{}," \
               b"\"gw\":{\"gateway-transaction-id\":\"8a9bed66-8412-494f-9866-2c26b5ceee62\",\"status-code\":7,\"status-text\":\"SUCCESS\"," \
               b"\"original-gateway-transaction-id\":\"orig-aaa\",\"parent-gateway-transaction-id\":\"parent-aaa\"}," \
               b"\"warnings\":[\"Soon counters will be exceeded for the merchant\",\"Soon counters will be exceeded for the account\"," \
               b"\"Soon counters will be exceeded for the terminal group\",\"Soon counters will be exceeded for the terminal\"]}\n"

        response = GatewayResponse(200, body)
        parsed_response = self.operations.sms().parse(response)

        self.assertIsNotNone(parsed_response.acquirer_details)
        self.assertEqual("test", parsed_response.acquirer_details.dynamic_descriptor)
        self.assertEqual("648", parsed_response.acquirer_details.eci_sli)
        self.assertEqual("000", parsed_response.acquirer_details.result_code)
        self.assertEqual("Approved", parsed_response.acquirer_details.status_description)
        self.assertEqual("Approved", parsed_response.acquirer_details.status_text)
        self.assertEqual("5800978", parsed_response.acquirer_details.terminal_mid)
        self.assertEqual("1899493845214315", parsed_response.acquirer_details.transaction_id)

        self.assertIsNotNone(parsed_response.gw)
        self.assertEqual("8a9bed66-8412-494f-9866-2c26b5ceee62", parsed_response.gw.gateway_transaction_id)
        self.assertEqual("orig-aaa", parsed_response.gw.original_gateway_transaction_id)
        self.assertEqual("parent-aaa", parsed_response.gw.parent_gateway_transaction_id)
        self.assertEqual(Status.SUCCESS, parsed_response.gw.status_code)
        self.assertEqual("SUCCESS", parsed_response.gw.status_text)

        expected_warnings = [
            "Soon counters will be exceeded for the merchant",
            "Soon counters will be exceeded for the account",
            "Soon counters will be exceeded for the terminal group",
            "Soon counters will be exceeded for the terminal",
        ]
        self.assertEqual(expected_warnings, parsed_response.warnings)

    def test_payment_successful_redirect(self):
        operations = [
            self.operations.sms,
            self.operations.dms_hold,
            self.operations.dms_charge,
            self.operations.dms_cancel,
            self.operations.moto_sms,
            self.operations.moto_dms,
            self.operations.credit,
            self.operations.p2p,
            self.operations.b2p,
            self.operations.init_recurrent_sms,
            self.operations.recurrent_sms,
            self.operations.init_recurrent_dms,
            self.operations.recurrent_dms,
            self.operations.refund,
            self.operations.reversal,
            self.operations.create_token,
        ]

        body = b"{\"acquirer-details\": {},\"error\": {},\"gw\": {\"gateway-transaction-id\": \"965ffd17-1874-48d0-89f3-f2c2f06bf749\"," \
               b"\"redirect-url\": \"https://api.url/a4345be5b8a1af9773b8b0642b49ff26\",\"status-code\": 30,\"status-text\": \"INSIDE FORM URL SENT\"}}"

        for i, operation in enumerate(operations):
            with self.subTest("#%d" % i):
                response = GatewayResponse(200, body)
                parsed_response = operation().parse(response)

                self.assertIsNotNone(parsed_response.gw)
                self.assertEqual("965ffd17-1874-48d0-89f3-f2c2f06bf749", parsed_response.gw.gateway_transaction_id)
                self.assertEqual(urlparse("https://api.url/a4345be5b8a1af9773b8b0642b49ff26"), parsed_response.gw.redirect_url)
                self.assertEqual(Status.CARD_FORM_URL_SENT, parsed_response.gw.status_code)
                self.assertEqual("INSIDE FORM URL SENT", parsed_response.gw.status_text)

    def test_payment_error(self):
        body = b"{\"acquirer-details\": {},\"error\": {\"code\": 1102,\"message\": \"Invalid pan number. Failed assertion that pan (false) == true\"}," \
               b"\"gw\":{\"gateway-transaction-id\": \"33f17d34-3796-45e0-9bba-a771e9d3e504\",\"status-code\": 19,\"status-text\": \"BR VALIDATION FAILED\"}," \
               b"\"warnings\": [\"Soon counters will be exceeded for the merchant\",\"Soon counters will be exceeded for the account\"]}"

        response = GatewayResponse(200, body)
        parsed_response = self.operations.sms().parse(response)

        self.assertIsNotNone(parsed_response.error)
        self.assertEqual(ErrorCode.EEC_CC_BAD_NUMBER, parsed_response.error.error_code)
        self.assertEqual("Invalid pan number. Failed assertion that pan (false) == true", parsed_response.error.message)

        self.assertIsNotNone(parsed_response.gw)
        self.assertEqual("33f17d34-3796-45e0-9bba-a771e9d3e504", parsed_response.gw.gateway_transaction_id)
        self.assertEqual(Status.BR_VALIDATION_FAILED, parsed_response.gw.status_code)
        self.assertEqual("BR VALIDATION FAILED", parsed_response.gw.status_text)

        expected_warnings = [
            "Soon counters will be exceeded for the merchant",
            "Soon counters will be exceeded for the account",
        ]
        self.assertEqual(expected_warnings, parsed_response.warnings)

    def test_verify_enrollment(self):
        cases = [
            (b"{\"enrollment\":\"y\"}", EnrollmentStatus.YES),
            (b"{\"enrollment\":\"n\"}", EnrollmentStatus.NO),
            (b"{\"enrollment\":\"abracadabra\"}", None),
        ]

        for i, test_case in enumerate(cases):
            with self.subTest("#%d" % i):
                [body, expected] = test_case

                response = GatewayResponse(200, body)
                parsed_response = self.operations.verify_3d_enrollment().parse(response)

                self.assertEqual(expected, parsed_response.enrollment)

    def test_report(self):
        expected = [
            {"aaa": "1", "bbb": "2", "ccc": "3"},
            {"aaa": "xxx", "bbb": "yyyy", "ccc": "zzz"},
        ]

        body = b"aaa,bbb,ccc\n" \
               b"1,2,3\n" \
               b"xxx,yyyy,zzz\n" \
               b"\n"

        response = GatewayResponse(200, body)
        parsed_response = self.operations.report().parse(response)

        rows = 0
        for record in parsed_response:
            self.assertLess(rows, len(expected), "Missing value for %d in row %s" % (rows, record))
            self.assertDictEqual(expected[rows], record, "Wrong value for %d in row %s" % (rows, record))

            rows += 1

        self.assertEqual(len(expected), rows, "Not all expected values are present")
