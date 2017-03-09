from gateway.utils import data_structures
from unittest import TestCase


class TestUtils(TestCase):
    def setUp(self):
        self.SAMPLE_SOURCE_DICT = {
            'FIRST_LAYER': {}
        }

    def test_add_to_dict(self):
        """Will succeed"""

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
