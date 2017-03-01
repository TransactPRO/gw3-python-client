"""
Transact Pro Payment Gateway integration library.
"""

import requests
# import json
from gateway.builders.authorization_builder import AuthorizationBuilder
from gateway.operations.operations import Operations


class GateWayClient:
    """
    Main Gate client class for using TransactPro API

    Before starting you need to have a valid Account ID and a Secret Key.
    This information must be provided after successful registration in Transact Pro system.
    """

    # Request structure
    __AUTH_KEY = 'auth-data'
    __DATA_KEY = 'data'
    __gate_client_request = {
        __AUTH_KEY: None,
        __DATA_KEY: None
    }

    def __init__(self):
        # TODO ADD better validation system, mb in builder
        self.__validation_list = []
        self.__dict_of_auth_data_set = {}
        self.__dict_of_operation_data_set = {}
        pass

    def create_auth_data(self):
        return AuthorizationBuilder(self.__dict_of_auth_data_set, self.__validation_list)

    def set_operation(self):
        return Operations(self.__dict_of_operation_data_set, self.__validation_list)

    def build_request(self):
        # TODO Think about validation in builder or in building req
        # self.__validate_request_data(self.__dict_of_auth_data_set)
        # self.__validate_request_data(self.__dict_of_operation_data_set)
        # TODO ADD Custom exception raise
        # json_payload = self.__wrap_to_json()
        # print(json_payload)
        self.__gate_client_request[self.__AUTH_KEY] = self.__dict_of_auth_data_set
        self.__gate_client_request[self.__DATA_KEY] = self.__dict_of_operation_data_set

        r = requests.post('http://uriel.sk.fpngw3.env/v3.0/sms', json=self.__gate_client_request)
        return r.json()

    # def __wrap_to_json(self):
    #     self.__gate_client_request[self.__AUTH_KEY] = self.__dict_of_auth_data_set
    #     self.__gate_client_request[self.__DATA_KEY] = self.__dict_of_operation_data_set
    #
    #     try:
    #         return json.dumps(self.__gate_client_request)
    #     except:
    #         raise

    def __validate_request_data(self, data_set):
        passed_fields = []
        for field_name in self.__validation_list:
            if field_name in data_set:
                passed_fields.append(field_name)
            else:
                raise RuntimeError('Field (' + field_name + ') are empty in your request!')

        try:
            for v in passed_fields:
                self.__validation_list.remove(v)
        except:
            raise
