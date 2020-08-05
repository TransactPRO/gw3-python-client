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
import csv


class CsvResponse:
    def __init__(self, data: str) -> None:
        self.__data = data
        self.__init_reader()
        self.__headers = next(self.__csv_reader)
        if len(self.__headers) == 0:
            raise RuntimeError('Cannot parse CSV data: no headers line')

    def __init_reader(self):
        self.__csv_reader = csv.reader(list(iter(self.__data.splitlines())))

    def get_headers(self) -> list:
        return self.__headers

    def __iter__(self):
        self.__init_reader()
        next(self.__csv_reader)  # skip headers line
        return self

    def __next__(self) -> dict:
        data = []
        while len(data) == 0:
            data = next(self.__csv_reader)
        return dict(zip(self.__headers, data))
