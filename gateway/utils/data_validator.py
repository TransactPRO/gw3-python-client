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


class DataValidator:
    EXCLUDED_DATA_KEYS = [
        'general-data'
    ]

    def validate_request_data(self, required_data, request_data):
        """
        Validate all dict (json) structure with given dict of keys and class types

        Args:
            required_data (dict): Money amount in minor units
            Example {'Key1': int, 'tiny_key': str}

            request_data (dict): Data set for validation
            Example {'Key1': int, 'Other_dor': {'tiny_key': str}}
        Returns (dict):  Invalid data
        """
        result = {}
        yielded_list = list(self.__search_and_validate(req_struct=required_data, source_struct=request_data))

        try:
            if len(yielded_list[-1]) > 0:
                result = yielded_list[-1]
        except IndexError:
            if len(yielded_list) > 0:
                result = yielded_list[0]
        except:
            raise

        return result

    def __search_and_validate(self, req_struct, source_struct):
        """

        Args:
            req_struct (dict): Required keys with data types
            Example {'Key1': int, 'tiny_key': str}

            source_struct (dict): Dict data whose must be validated with req_struct
            Example {'Key1': int, 'Other_dor': {'tiny_key': str}}
        """
        __required_params = req_struct.copy()
        if hasattr(source_struct, 'items'):
            for key, value in source_struct.items():
                for data_key, data_value_type in __required_params.items():
                    for excluded_key in self.EXCLUDED_DATA_KEYS:
                        if key == excluded_key:
                            continue
                    if key == data_key:
                        if type(value) is data_value_type:
                            del req_struct[key]
                            yield req_struct

                # Make recursion if contains nested structures
                if isinstance(value, dict):
                    nested_dict = value
                    for result in self.__search_and_validate(req_struct, nested_dict):
                        yield result
                elif isinstance(value, list):
                    nested_list = value
                    for nested_object in nested_list:
                        for result in self.__search_and_validate(req_struct, nested_object):
                            yield result
