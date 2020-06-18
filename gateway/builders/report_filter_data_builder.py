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
from gateway.data_sets.request_parameters import RequestParameters, RequestParametersTypes


class ReportFilterDataBuilder(object):
    """
    Info Data contains all informational data property's
    """

    def __init__(self, __client_transaction_data_set, __client_mandatory_fields):
        self.__data_set = __client_transaction_data_set
        self.__mandatory_fields = __client_mandatory_fields

    def add_dt_created_from(self, timestamp: int) -> None:
        """
        Add filtration by transaction creation date (interval start)

        Example -> add_dt_created_from(1593159762)

        Args:
            timestamp (int): Transaction creation date (interval start)
        """
        self.__data_set[RequestParameters.FILTER_DATA_DT_CREATED_FROM] = int(timestamp)
        self.__mandatory_fields[RequestParameters.FILTER_DATA_DT_CREATED_FROM] = RequestParametersTypes.FILTER_DATA_DT_CREATED_FROM

    def add_dt_created_to(self, timestamp: int) -> None:
        """
        Add filtration by transaction creation date (interval end)

        Example -> add_dt_created_from(1593159762)

        Args:
            timestamp (int): Transaction creation date (interval end)
        """
        self.__data_set[RequestParameters.FILTER_DATA_DT_CREATED_TO] = int(timestamp)
        self.__mandatory_fields[RequestParameters.FILTER_DATA_DT_CREATED_TO] = RequestParametersTypes.FILTER_DATA_DT_CREATED_TO

    def add_dt_finished_from(self, timestamp: int) -> None:
        """
        Add filtration by transaction finish date (interval start)

        Example -> add_dt_finished_from(1593159762)

        Args:
            timestamp (int): Transaction finish date (interval start)
        """
        self.__data_set[RequestParameters.FILTER_DATA_DT_FINISHED_FROM] = int(timestamp)
        self.__mandatory_fields[RequestParameters.FILTER_DATA_DT_FINISHED_FROM] = RequestParametersTypes.FILTER_DATA_DT_FINISHED_FROM

    def add_dt_finished_to(self, timestamp: int) -> None:
        """
        Add filtration by transaction finish date (interval end)

        Example -> add_dt_finished_from(1593159762)

        Args:
            timestamp (int): Transaction finish date (interval end)
        """
        self.__data_set[RequestParameters.FILTER_DATA_DT_FINISHED_TO] = int(timestamp)
        self.__mandatory_fields[RequestParameters.FILTER_DATA_DT_FINISHED_TO] = RequestParametersTypes.FILTER_DATA_DT_FINISHED_TO
