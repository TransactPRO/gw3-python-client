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
from typing import Sequence

from gateway.responses.constants import Status
from gateway.responses.generic import GenericResponse
from gateway.responses.parts import Error, TransactionInfo
from gateway.responses.payment import PaymentResponse
from gateway.responses.response import get_value, parse_date


class TransactionsListElement:
    def __init__(self, data: dict = None) -> None:
        self.error = get_value(data, "error", Error)  # type: Error
        self.gateway_transaction_id = get_value(data, "gateway-transaction-id", str, "")  # type: str


class TransactionsList(GenericResponse):
    def __init__(self, collection_type, data: dict = None) -> None:
        super().__init__(data)
        self.transactions = get_value(data, "transactions", lambda x: [collection_type(v) for v in x], [])  # type: Sequence


class RefundsListElement(TransactionsListElement):
    def __init__(self, data: dict = None) -> None:
        super().__init__(data)
        self.refunds = get_value(data, "refunds", lambda x: [TransactionInfo(v) for v in x], [])  # type: Sequence[TransactionInfo]


class RefundsResponse(TransactionsList):
    def __init__(self, data: dict = None) -> None:
        super().__init__(RefundsListElement, data)


class InitialRecurringTransaction(TransactionsListElement):
    def __init__(self, data: dict = None) -> None:
        super().__init__(data)
        self.subsequent = get_value(data, "recurrents", lambda x: [TransactionInfo(v) for v in x], [])  # type: Sequence[TransactionInfo]


class RecurringTransactionsResponse(TransactionsList):
    def __init__(self, data: dict = None) -> None:
        super().__init__(InitialRecurringTransaction, data)


class HistoryEvent:
    def __init__(self, data: dict = None) -> None:
        self.date_updated = get_value(data, 'date-updated', parse_date)  # type: datetime.datetime
        self.status_code_new = get_value(data, 'status-code-new', Status)  # type: Status
        self.status_code_old = get_value(data, 'status-code-old', Status)  # type: Status
        self.status_text_new = get_value(data, 'status-text-new', str, '')  # type: str
        self.status_text_old = get_value(data, 'status-text-old', str, '')  # type: str


class HistoryListElement(TransactionsListElement):
    def __init__(self, data: dict = None) -> None:
        super().__init__(data)
        self.history = get_value(data, "history", lambda x: [HistoryEvent(v) for v in x], [])  # type: Sequence[HistoryEvent]


class HistoryResponse(TransactionsList):
    def __init__(self, data: dict = None) -> None:
        super().__init__(HistoryListElement, data)


class TransactionResult(TransactionsListElement):
    def __init__(self, data: dict = None) -> None:
        super().__init__(data)
        self.date_created = get_value(data, 'date-created', parse_date)  # type: datetime.datetime
        self.date_finished = get_value(data, 'date-finished', parse_date)  # type: datetime.datetime
        self.result_data = get_value(data, 'result-data', PaymentResponse)  # type: PaymentResponse


class ResultResponse(TransactionsList):
    def __init__(self, data: dict = None) -> None:
        super().__init__(TransactionResult, data)


class TransactionStatus(TransactionsListElement):
    def __init__(self, data: dict = None) -> None:
        super().__init__(data)
        status_data = {}
        status_list = get_value(data, 'status') # type: list
        if status_list is not None and len(status_list) == 1:
            status_data = status_list[0]

        self.status_code = get_value(status_data, 'status-code', Status)
        self.status_code_general = get_value(status_data, 'status-code-general', Status)
        self.status_text = get_value(status_data, 'status-text', str, '')
        self.status_text_general = get_value(status_data, 'status-text-general', str, '')


class StatusResponse(TransactionsList):
    def __init__(self, data: dict = None) -> None:
        super().__init__(TransactionStatus, data)
