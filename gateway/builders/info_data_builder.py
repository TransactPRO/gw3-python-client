class InfoDataBuilder(object):
    """
    Info Data contains all informational data property's
    """

    __INFO_COMMAND_DATA_KEY = 'command-data'
    __command_data_structure = {
        __INFO_COMMAND_DATA_KEY: None
    }

    def __init__(self, __builder_data_set):
        from gateway.utils.data_structures import DataStructuresUtils
        from gateway.data_sets.request_parameters import RequestParameters
        self.__data_structure_util = DataStructuresUtils
        self.__req_params = RequestParameters
        self.__payment_data_set = __builder_data_set

    def add_gateway_transaction_ids(self, list_of_gate_transaction_id=None):
        """
        Add previously created Transaction IDs

        Example -> ["2d4b377c-648c-432b-a4dc-b386901116d7", "2323377c-548c-4scb-a6dc-b3899kxah520"]

        Args:
            list_of_gate_transaction_id (list): Previously created Transaction IDs
        """
        if list_of_gate_transaction_id is None:
            list_of_gate_transaction_id = []

        self.__data_structure_util.add_to_dict(
            source_dict=self.__payment_data_set,
            working_dict=self.__command_data_structure,
            new_key=self.__INFO_COMMAND_DATA_KEY,
            new_dict={self.__req_params.COMMAND_DATA_GATEWAY_TRANSACTION_IDS: list_of_gate_transaction_id}
        )
