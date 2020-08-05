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

from gateway.builders.system_data_builder import SystemDataBuilder


class TestSystemDataBuilder(TestCase):
    BUILDER = None
    DATA = {}

    def setUp(self):
        self.DATA = {}
        self.BUILDER = SystemDataBuilder(self.DATA)

    def tearDown(self):
        del self.DATA

    def test_mandatory_and_data_fields(self):
        new = self.BUILDER
        new.add_user_ip(cardholder_ipv4='192.168.1.70')
        new.add_x_forwarded_for_ip(cardholder_ipv4='192.168.1.70')
        new.add_browser_accept_header("application/json, text/javascript, */*; q=0.01")
        new.add_browser_java_enabled(True)
        new.add_browser_javascript_enabled(True)
        new.add_browser_language("en-US")
        new.add_browser_color_depth("24")
        new.add_browser_screen_height("1080")
        new.add_browser_screen_width("1920")
        new.add_browser_tz("+300")
        new.add_user_agent("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36")

        valid_data_structure = {'system': {
            'user-ip': '192.168.1.70',
            'x-forwarded-for': '192.168.1.70',
            'browser-accept-header': "application/json, text/javascript, */*; q=0.01",
            'browser-java-enabled': True,
            'browser-javascript-enabled': True,
            'browser-language': "en-US",
            'browser-color-depth': "24",
            'browser-screen-height': "1080",
            'browser-screen-width': "1920",
            'browser-tz': "+300",
            'browser-user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        }}
        self.assertDictEqual(valid_data_structure, self.DATA)
