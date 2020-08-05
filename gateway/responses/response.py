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
import json

from requests.structures import CaseInsensitiveDict

from gateway.crypto.digest import ResponseDigest
from gateway.responses.csv_response import CsvResponse


class GatewayResponse:
    """
    Gateway response wrapper with access to response status, headers, payload and digest
    """

    def __init__(self, status: int, payload: bytes, headers: CaseInsensitiveDict = None) -> None:
        self.status = status
        self.payload = payload.decode("utf-8")
        self.headers = headers
        self.digest = None  # type: ResponseDigest

    def is_successful(self) -> bool:
        return (200 <= self.status < 400) or self.status == 402

    def parse_json(self, target_class) -> any:
        return target_class(json.loads(self.payload))

    def parse_csv(self) -> CsvResponse:
        return CsvResponse(self.payload)


def get_value(data: dict, key: str, output_post_process: any = None, default: any = None) -> any:
    if data is not None and key in data:
        value = data[key]
        try:
            return output_post_process(value) if output_post_process is not None and value is not None else value
        except ValueError:
            return default
    else:
        return default


def parse_date(raw: str) -> datetime.datetime:
    return datetime.datetime.strptime(raw, '%Y-%m-%d %H:%M:%S').replace(tzinfo=datetime.timezone.utc)
