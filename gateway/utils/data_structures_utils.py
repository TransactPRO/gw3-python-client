class DataStructuresUtils:
    """Contains all usefully methods for work with different data structures
    """

    @staticmethod
    def add_to_dict(source_dict=None, working_dict=None, new_key=None, new_dict=None):
        """
        Staticmethod will helps correctly update dict with nested data structure
        Examples:
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
