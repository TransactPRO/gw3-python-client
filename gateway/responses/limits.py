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

from gateway.responses.generic import GenericResponse
from gateway.responses.response import get_value


class Limit:
    def __init__(self, data: dict = None) -> None:
        self.counter_type = get_value(data, 'counter-type', str, '')  # type: str
        self.currency = get_value(data, 'currency', str, '')  # type: str
        self.limit = get_value(data, 'limit', int, 0)  # type: int
        self.payment_method_subtype = get_value(data, 'payment-method-subtype', str, '')  # type: str
        self.payment_method_type = get_value(data, 'payment-method-type', str, '')  # type: str
        self.value = get_value(data, 'value', int, 0)  # type: int


class ObjectLimits:
    def __init__(self, data: dict = None) -> None:
        self.type = get_value(data, 'type', str, '')   # type: str
        self.title = get_value(data, 'title', str, '')   # type: str
        self.acq_terminal_id = get_value(data, 'acq-terminal-id', str)   # type: str
        self.limits = get_value(data, 'counters', lambda x: [Limit(v) for v in x], [])   # type: Sequence[Limit]
        self.children = get_value(data, 'childs', lambda x: [ObjectLimits(v) for v in x], [])   # type: Sequence[ObjectLimits]


class LimitsResponse(GenericResponse):
    def __init__(self, data: dict = None) -> None:
        super().__init__(data)
        self.limits = ObjectLimits(data)
