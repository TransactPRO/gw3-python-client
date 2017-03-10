class MoneyDataBuilder(object):
    """
    Money data - information about payment request
    """
    __MONEY_DATA_KEY = 'money-data'
    __money_data_structure = {
        __MONEY_DATA_KEY: None
    }

    def __init__(self, __client_transaction_data_set, __client_mandatory_fields):
        from gateway.utils.data_structures import DataStructuresUtils
        from gateway.data_sets.request_parameters import (
            RequestParameters,
            RequestParametersTypes
        )
        self.__data_structure_util = DataStructuresUtils
        self.__data_types = RequestParametersTypes
        self.__data_sets = RequestParameters
        self.__money_data_set = __client_transaction_data_set
        self.__money_mandatory_fields = __client_mandatory_fields

    def add_payment_amount(self, minor_value=None):
        """
        Add payment money amount in minor units

        Args:
            minor_value (int): Money amount in minor units
        """
        self.__money_mandatory_fields[
            self.__data_sets.MONEY_DATA_AMOUNT
        ] = self.__data_types.MONEY_DATA_AMOUNT

        self.__data_structure_util.add_to_dict(
            source_dict=self.__money_data_set,
            working_dict=self.__money_data_structure,
            new_key=self.__MONEY_DATA_KEY,
            new_dict={self.__data_sets.MONEY_DATA_AMOUNT: minor_value}
        )

    def add_payment_currency(self, iso_4217_ccy=None):
        """
        Add payment currency, ISO-4217 format

        Args:
            iso_4217_ccy (str): Currency, ISO-4217 format
        """
        self.__money_mandatory_fields[
            self.__data_sets.MONEY_DATA_CURRENCY
        ] = self.__data_types.MONEY_DATA_CURRENCY

        self.__data_structure_util.add_to_dict(
            source_dict=self.__money_data_set,
            working_dict=self.__money_data_structure,
            new_key=self.__MONEY_DATA_KEY,
            new_dict={self.__data_sets.MONEY_DATA_CURRENCY: iso_4217_ccy}
        )
