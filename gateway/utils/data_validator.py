class DataValidator:
    EXCLUDED_DATA_KEYS = [
        'general-data'
    ]

    def validate_request_data(self, required_data, request_data):
        """

        Args:
            required_data (dict): Money amount in minor units
            Example {'Key1': int, 'tiny_key': str}

            request_data (dict): Data set for validation
            Example {'Key1': int, 'Other_dor': {'tiny_key': str}}
        Returns (dict):  Invalid data
        """
        return list(self.__search_and_validate(req_struct=required_data, source_struct=request_data))

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
