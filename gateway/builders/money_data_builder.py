from gateway.data_sets.request_parameters import RequestParameters


class MoneyDataBuilder(object):
    __data_sets = None

    __MONEY_DATA_KEY = 'money-data'
    __payment_data_structure = {
        __MONEY_DATA_KEY: None
    }

    def __init__(self, __builder_data_set):
        self.__payment_data_set = __builder_data_set
        self.__data_sets = RequestParameters

    def __update_structure(self, new_data_set):
        if self.__payment_data_structure[self.__MONEY_DATA_KEY] is None:
            self.__payment_data_structure[self.__MONEY_DATA_KEY] = new_data_set
        else:
            self.__payment_data_structure[self.__MONEY_DATA_KEY].update(new_data_set)

        self.__payment_data_set.update(self.__payment_data_structure)

    def add_payment_amount(self, payment_amount=None):
        """
        Add payment money amount in minor units

        Args:
            payment_amount (str): Money amount in minor units
        """
        self.__update_structure({self.__data_sets.MONEY_DATA_AMOUNT: payment_amount})

    def add_payment_currency(self, payment_currency=None):
        """
        Add payment currency, ISO-4217 format

        Args:
            payment_currency (int): Currency, ISO-4217 format
        """
        self.__update_structure({self.__data_sets.MONEY_DATA_CURRENCY: payment_currency})
