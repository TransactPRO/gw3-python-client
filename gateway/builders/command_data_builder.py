class CommandDataBuilder(object):
    """
    Command data - Transact Pro gateway command data for work with (gateway-transaction-id, form-id, terminal-id)
    """

    __COMMAND_DATA_KEY = 'command-data'
    __command_data_nested_structure = {
        __COMMAND_DATA_KEY: None
    }

    def __init__(self, __client_transaction_data_set, __client_mandatory_fields):
        from gateway.utils.data_structures import DataStructuresUtils
        from gateway.data_sets.request_parameters import (
            RequestParameters,
            RequestParametersTypes
        )
        self.__data_structure_util = DataStructuresUtils
        self.__data_sets = RequestParameters
        self.__data_types = RequestParametersTypes
        self.__command_mandatory_fields = __client_mandatory_fields
        self.__command_data_set = __client_transaction_data_set

    def add_gateway_transaction_id(self, gate_transaction_id=None):
        """
        Add previously created Transaction ID

        Args:
            gate_transaction_id (str): Previously created Transaction ID
        """
        self.__command_mandatory_fields[
            self.__data_sets.COMMAND_DATA_GATEWAY_TRANSACTION_ID
        ] = self.__data_types.COMMAND_DATA_GATEWAY_TRANSACTION_ID

        self.__data_structure_util.add_to_dict(
            source_dict=self.__command_data_set,
            working_dict=self.__command_data_nested_structure,
            new_key=self.__COMMAND_DATA_KEY,
            new_dict={self.__data_sets.COMMAND_DATA_GATEWAY_TRANSACTION_ID: gate_transaction_id}
        )

    def add_form_id(self, inside_form_id=None):
        """
        Add inside form ID when selecting non-default form manually

        Args:
            inside_form_id (str): Inside form ID when selecting non-default form manually
        """
        self.__command_mandatory_fields[
            self.__data_sets.COMMAND_DATA_FORM_ID
        ] = self.__data_types.COMMAND_DATA_FORM_ID

        self.__data_structure_util.add_to_dict(
            source_dict=self.__command_data_set,
            working_dict=self.__command_data_nested_structure,
            new_key=self.__COMMAND_DATA_KEY,
            new_dict={self.__data_sets.COMMAND_DATA_FORM_ID: inside_form_id}
        )

    def add_terminal_mid(self, terminal_id=None):
        """
        Add terminal MID when selecting terminal manually

        Args:
            terminal_id (str): Terminal MID when selecting terminal manually
        """
        self.__command_mandatory_fields[
            self.__data_sets.COMMAND_DATA_FORM_ID
        ] = self.__data_types.COMMAND_DATA_FORM_ID

        self.__data_structure_util.add_to_dict(
            source_dict=self.__command_data_set,
            working_dict=self.__command_data_nested_structure,
            new_key=self.__COMMAND_DATA_KEY,
            new_dict={self.__data_sets.COMMAND_DATA_TERMINAL_MID: terminal_id}
        )
