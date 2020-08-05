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

from gateway.builders.report_filter_data_builder import ReportFilterDataBuilder
from gateway.data_sets.request_parameters import RequestParameters, RequestParametersTypes


class TestReportFilterBuilder(TestCase):
    BUILDER = None
    DATA = {}
    MANDATORY_FIELDS = {}

    def setUp(self):
        self.DATA = {}
        self.MANDATORY_FIELDS = {}
        self.BUILDER = ReportFilterDataBuilder(self.DATA, self.MANDATORY_FIELDS)

    def tearDown(self):
        del self.DATA
        del self.MANDATORY_FIELDS

    def test_mandatory_and_data_fields(self):
        new = self.BUILDER
        new.add_dt_created_from(1)
        new.add_dt_created_to(2)
        new.add_dt_finished_from(3)
        new.add_dt_finished_to(4)

        valid_fields = {
            RequestParameters.FILTER_DATA_DT_CREATED_FROM: RequestParametersTypes.FILTER_DATA_DT_CREATED_FROM,
            RequestParameters.FILTER_DATA_DT_CREATED_TO: RequestParametersTypes.FILTER_DATA_DT_CREATED_TO,
            RequestParameters.FILTER_DATA_DT_FINISHED_FROM: RequestParametersTypes.FILTER_DATA_DT_FINISHED_FROM,
            RequestParameters.FILTER_DATA_DT_FINISHED_TO: RequestParametersTypes.FILTER_DATA_DT_FINISHED_TO,
        }

        self.assertDictEqual(valid_fields, self.MANDATORY_FIELDS)

        valid_data_structure = {
            'dt-created-from': 1,
            'dt-created-to': 2,
            'dt-finished-from': 3,
            'dt-finished-to': 4,
        }
        self.assertDictEqual(valid_data_structure, self.DATA)
