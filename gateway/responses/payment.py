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
from typing import Sequence
from urllib.parse import urlparse, ParseResult

from gateway.responses.constants import Status
from gateway.responses.generic import GenericResponse
from gateway.responses.response import get_value


class AcquirerDetails:
    def __init__(self, data: dict = None) -> None:
        self.dynamic_descriptor = get_value(data, "dynamic-descriptor", str)  # type: str
        self.eci_sli = get_value(data, "eci-sli", str, "")  # type: str
        self.result_code = get_value(data, "result-code", str, "")  # type: str
        self.status_description = get_value(data, "status-description", str, "")  # type: str
        self.status_text = get_value(data, "status-text", str, "")  # type: str
        self.terminal_mid = get_value(data, "terminal-mid", str, "")  # type: str
        self.transaction_id = get_value(data, "transaction-id", str, "")  # type: str


class GW:
    def __init__(self, data: dict = None) -> None:
        self.gateway_transaction_id = get_value(data, "gateway-transaction-id", str, "")  # type: str
        self.original_gateway_transaction_id = get_value(data, "original-gateway-transaction-id", str)  # type: str
        self.parent_gateway_transaction_id = get_value(data, "parent-gateway-transaction-id", str)  # type: str
        self.status_code = get_value(data, "status-code", Status)  # type: Status
        self.status_text = get_value(data, "status-text", str, "")  # type: str
        self.redirect_url = get_value(data, "redirect-url", lambda x: urlparse(x))  # type: ParseResult


class PaymentResponse(GenericResponse):
    def __init__(self, data: dict = None) -> None:
        super().__init__(data)
        self.acquirer_details = get_value(data, "acquirer-details", AcquirerDetails)  #type: AcquirerDetails
        self.gw = get_value(data, "gw", GW)  # type: GW
        self.warnings = get_value(data, "warnings")  # type: Sequence[str]


class CallbackResult(PaymentResponse):
    def __init__(self, data: dict = None) -> None:
        super().__init__(get_value(data, "result-data"))
