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


class DataStructuresUtils:
    """Contains all usefully methods for work with different data structures
    """

    @staticmethod
    def add_to_dict(source_dict=None, working_dict=None, new_key=None, new_dict=None):
        """
        Staticmethod will helps correctly update dict with nested data structure
        Example
            source_dict : {
                'working_dict' : {
                    'new_key' : {
                        'hello_world' : 'Hello mate'
                    }
                }
            }

        Args:
            source_dict (dict): Main dict where will be added new dict inside
            working_dict(dict): Nested dict of source_dict
            new_key(str): The key of nested dict in working_dict
            new_dict(dict): Nested dict of working_dict
        Returns:
            dict: Updated source_dict
        """
        if source_dict is None or working_dict is None or new_key is None or new_dict is None:
            raise RuntimeError("Invalid arguments passed, one of is == None.")

        if working_dict[new_key] is None:
            working_dict[new_key] = new_dict
        else:
            working_dict[new_key].update(new_dict)

        return source_dict.update(working_dict)
