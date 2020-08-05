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
import datetime

from gateway.responses.constants import ErrorCode, Status
from gateway.responses.response import get_value, parse_date


class Error:
    def __init__(self, data: dict = None) -> None:
        self.error_code = get_value(data, 'code', ErrorCode, get_value(data, 'code', int))  # type: ErrorCode
        self.message = get_value(data, 'message', str)  # type: str


class TransactionInfo:
    def __init__(self, data: dict = None) -> None:
        self.account_guid = get_value(data, 'account-guid', str, '')  # type: str
        self.acq_terminal_id = get_value(data, 'acq-terminal-id', str, '')  # type: str
        self.acq_transaction_id = get_value(data, 'acq-transaction-id', str, '')  # type: str
        self.amount = get_value(data, 'amount', int)  # type: int
        self.approval_code = get_value(data, 'approval-code', str, '')  # type: str
        self.cardholder_name = get_value(data, 'cardholder-name', str, '')  # type: str
        self.currency = get_value(data, 'currency', str, '')  # type: str
        self.eci_sli = get_value(data, 'eci-sli', str, '')  # type: str
        self.gateway_transaction_id = get_value(data, 'gateway-transaction-id', str, '')  # type: str
        self.merchant_transaction_id = get_value(data, 'merchant-transaction-id', str, '')  # type: str
        self.status_code = get_value(data, 'status-code', Status)  # type: Status
        self.status_code_general = get_value(data, 'status-code-general', Status)  # type: Status
        self.status_text = get_value(data, 'status-text', str, '')  # type: str
        self.status_text_general = get_value(data, 'status-text-general', str, '')  # type: str
        self.date_finished = get_value(data, 'date-finished', parse_date)  # type: datetime.datetime
