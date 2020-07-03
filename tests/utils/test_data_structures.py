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

from gateway.utils import data_structures


class TestUtils(TestCase):
    def setUp(self):
        self.SAMPLE_SOURCE_DICT = {
            'FIRST_LAYER': {}
        }

    def test_add_to_dict(self):

        new_dict = {
            'NESTED_KEY': None
        }

        data_structures.DataStructuresUtils.add_to_dict(
            source_dict=self.SAMPLE_SOURCE_DICT,
            working_dict=new_dict,
            new_key='NESTED_KEY',
            new_dict={'SAY_KEY': 'hello world'}
        )

        self.assertTrue('SAY_KEY' in self.SAMPLE_SOURCE_DICT['NESTED_KEY'])
