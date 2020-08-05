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

from gateway.data_sets.request_parameters import RequestParameters
from gateway.utils.data_structures import DataStructuresUtils


class SystemDataBuilder(object):
    """
    System Data contains IP addresses of cardholders
    """

    __SYSTEM_DATA_KEY = 'system'

    def __init__(self, __client_transaction_data_set):
        self.__system_data_structure = {
            self.__SYSTEM_DATA_KEY: None
        }

        self.__data_structure_util = DataStructuresUtils
        self.__data_sets = RequestParameters
        self.__system_data_set = __client_transaction_data_set

    def add_user_ip(self, cardholder_ipv4=None):
        """
        Add cardholder IPv4 address

        Args:
            cardholder_ipv4 (str): Cardholder IPv4 address
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__system_data_set,
            working_dict=self.__system_data_structure,
            new_key=self.__SYSTEM_DATA_KEY,
            new_dict={self.__data_sets.SYSTEM_USER_IP: cardholder_ipv4}
        )

    def add_x_forwarded_for_ip(self, cardholder_ipv4=None):
        """
        Add cardholder real IPv4 address in case of proxy

        Args:
            cardholder_ipv4 (str): Cardholder real IPv4 address in case of proxy
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__system_data_set,
            working_dict=self.__system_data_structure,
            new_key=self.__SYSTEM_DATA_KEY,
            new_dict={self.__data_sets.SYSTEM_X_FORWARDED_FOR: cardholder_ipv4}
        )

    def add_browser_accept_header(self, browser_accept_header=None):
        """
        Add browser accept header

        Args:
            browser_accept_header (str): Browser accept header
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__system_data_set,
            working_dict=self.__system_data_structure,
            new_key=self.__SYSTEM_DATA_KEY,
            new_dict={self.__data_sets.SYSTEM_BROWSER_ACCEPT_HEADER: browser_accept_header}
        )

    def add_browser_java_enabled(self, value=None):
        """
        Add browser Java enabled flag

        Args:
            value (bool): Flag that shows is Java enabled or not
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__system_data_set,
            working_dict=self.__system_data_structure,
            new_key=self.__SYSTEM_DATA_KEY,
            new_dict={self.__data_sets.SYSTEM_BROWSER_JAVA_ENABLED: value}
        )

    def add_browser_javascript_enabled(self, value=None):
        """
        Add browser JavaScript enabled flag

        Args:
            value (bool): Flag that shows is JavaScript enabled or not
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__system_data_set,
            working_dict=self.__system_data_structure,
            new_key=self.__SYSTEM_DATA_KEY,
            new_dict={self.__data_sets.SYSTEM_BROWSER_JAVASCRIPT_ENABLED: value}
        )

    def add_browser_language(self, language=None):
        """
        Add browser language

        Args:
            language (str): Browser language
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__system_data_set,
            working_dict=self.__system_data_structure,
            new_key=self.__SYSTEM_DATA_KEY,
            new_dict={self.__data_sets.SYSTEM_BROWSER_LANGUAGE: language}
        )

    def add_browser_color_depth(self, browser_color_depth=None):
        """
        Add browser color depth

        Args:
            browser_color_depth (str): Browser color depth
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__system_data_set,
            working_dict=self.__system_data_structure,
            new_key=self.__SYSTEM_DATA_KEY,
            new_dict={self.__data_sets.SYSTEM_BROWSER_COLOR_DEPTH: browser_color_depth}
        )

    def add_browser_screen_height(self, height=None):
        """
        Add browser screen height

        Args:
            height (str): Browser screen height
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__system_data_set,
            working_dict=self.__system_data_structure,
            new_key=self.__SYSTEM_DATA_KEY,
            new_dict={self.__data_sets.SYSTEM_BROWSER_SCREEN_HEIGHT: height}
        )

    def add_browser_screen_width(self, width=None):
        """
        Add browser screen width

        Args:
            width (str): Browser screen width
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__system_data_set,
            working_dict=self.__system_data_structure,
            new_key=self.__SYSTEM_DATA_KEY,
            new_dict={self.__data_sets.SYSTEM_BROWSER_SCREEN_WIDTH: width}
        )

    def add_browser_tz(self, browser_tz=None):
        """
        Add browser timezone

        Args:
            browser_tz (str): Browser timezone offset in minutes
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__system_data_set,
            working_dict=self.__system_data_structure,
            new_key=self.__SYSTEM_DATA_KEY,
            new_dict={self.__data_sets.SYSTEM_BROWSER_TZ: browser_tz}
        )

    def add_user_agent(self, user_agent=None):
        """
        Add browser user agent

        Args:
            user_agent (str): Browser user agent
        """

        self.__data_structure_util.add_to_dict(
            source_dict=self.__system_data_set,
            working_dict=self.__system_data_structure,
            new_key=self.__SYSTEM_DATA_KEY,
            new_dict={self.__data_sets.SYSTEM_BROWSER_USER_AGENT: user_agent}
        )
