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
from gateway.builders.command_data_builder import CommandDataBuilder
from gateway.builders.customer_data_builder import CustomerDataBuilder
from gateway.builders.info_data_builder import InfoDataBuilder
from gateway.builders.merchant_order_builder import MerchantOrderBuilder
from gateway.builders.money_data_builder import MoneyDataBuilder
from gateway.builders.payment_data_builder import PaymentDataBuilder
from gateway.builders.report_filter_data_builder import ReportFilterDataBuilder
from gateway.builders.system_data_builder import SystemDataBuilder
from gateway.builders.verify_3d_enrollment_builder import Verify3dEnrollmentBuilder
from gateway.builders.verify_card_data_builder import VerifyCardDataBuilder
from gateway.responses.csv_response import CsvResponse
from gateway.responses.enrollment import EnrollmentResponse
from gateway.responses.limits import LimitsResponse
from gateway.responses.lists import RefundsResponse, HistoryResponse, RecurringTransactionsResponse, ResultResponse, StatusResponse
from gateway.responses.payment import PaymentResponse
from gateway.responses.response import GatewayResponse


class TransactionBuilder:
    """
    Contains all necessary data sets builders for different transaction types constructors
    """

    def __init__(self, __operation_data_set, __operation_mandatory_fields_set) -> None:
        self.__command_data_builder = CommandDataBuilder(__operation_data_set, __operation_mandatory_fields_set)
        self.__customer_data_builder = CustomerDataBuilder(__operation_data_set)
        self.__merchant_order_builder = MerchantOrderBuilder(__operation_data_set)
        self.__payment_data_builder = PaymentDataBuilder(__operation_data_set, __operation_mandatory_fields_set)
        self.__money_data_builder = MoneyDataBuilder(__operation_data_set, __operation_mandatory_fields_set)
        self.__system_data_builder = SystemDataBuilder(__operation_data_set)

    def command_data_set(self) -> CommandDataBuilder:
        return self.__command_data_builder

    def customer_data_set(self) -> CustomerDataBuilder:
        return self.__customer_data_builder

    def merchant_order_data_set(self) -> MerchantOrderBuilder:
        return self.__merchant_order_builder

    def payment_method_set(self) -> PaymentDataBuilder:
        return self.__payment_data_builder

    def money_data_set(self) -> MoneyDataBuilder:
        return self.__money_data_builder

    def system_data_set(self) -> SystemDataBuilder:
        return self.__system_data_builder

    @staticmethod
    def parse(response: GatewayResponse) -> PaymentResponse:
        return response.parse_json(PaymentResponse)


class ExploringBuilder:
    """
    Contains all necessary data sets builders for construction exploring past payments operations
    """

    def __init__(self, __operation_data_set, __operation_mandatory_fields_set) -> None:
        self.__info_data_builder = InfoDataBuilder(__operation_data_set, __operation_mandatory_fields_set)

    def info_command_data_set(self) -> InfoDataBuilder:
        return self.__info_data_builder


"""
Transaction Types builders
"""


class SmsBuilder(TransactionBuilder):
    pass


class DmsHoldBuilder(TransactionBuilder):
    pass


class DmsChargeBuilder(TransactionBuilder):
    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in DMS CHARGE operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in DMS CHARGE operation!')


class DmsCancelBuilder(TransactionBuilder):
    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in DMS CANCEL operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in DMS CANCEL operation!')


class MotoSmsBuilder(TransactionBuilder):
    pass


class MotoDmsBuilder(TransactionBuilder):
    pass


class CreditBuilder(TransactionBuilder):
    pass


class P2PBuilder(TransactionBuilder):
    pass


class B2PBuilder(TransactionBuilder):
    pass


class RecurrentSmsBuilder(TransactionBuilder):
    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Recurrent SMS operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Recurrent SMS operation!')


class RecurrentDmsBuilder(TransactionBuilder):
    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Recurrent DMS operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Recurrent DMS operation!')


class RefundBuilder(TransactionBuilder):
    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Refund operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Refund operation!')


class ReversalBuilder(TransactionBuilder):
    def customer_data_set(self):
        raise NotImplementedError('Customer data set unavailable in Reversal operation!')

    def payment_method_set(self):
        raise NotImplementedError('Payment method data set unavailable in Reversal operation!')


class CreateTokenBuilder(TransactionBuilder):
    pass


class Verify3dBuilder:
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__verify_enrollment_builder = Verify3dEnrollmentBuilder(__operation_data_set, __operation_mandatory_fields)

    def input_data_set(self) -> Verify3dEnrollmentBuilder:
        return self.__verify_enrollment_builder

    @staticmethod
    def parse(response: GatewayResponse) -> EnrollmentResponse:
        return response.parse_json(EnrollmentResponse)


class VerifyCardBuilder:
    def __init__(self, __operation_data_set, __operation_mandatory_fields):
        self.__verify_card_builder = VerifyCardDataBuilder(__operation_data_set, __operation_mandatory_fields)

    def data_set(self) -> VerifyCardDataBuilder:
        return self.__verify_card_builder


class TransactionRefundsHistoryBuilder(ExploringBuilder):
    @staticmethod
    def parse(response: GatewayResponse) -> RefundsResponse:
        return response.parse_json(RefundsResponse)


class TransactionRecurringHistoryBuilder(ExploringBuilder):
    @staticmethod
    def parse(response: GatewayResponse) -> RecurringTransactionsResponse:
        return response.parse_json(RecurringTransactionsResponse)


class TransactionHistoryBuilder(ExploringBuilder):
    @staticmethod
    def parse(response: GatewayResponse) -> HistoryResponse:
        return response.parse_json(HistoryResponse)


class TransactionResultBuilder(ExploringBuilder):
    @staticmethod
    def parse(response: GatewayResponse) -> ResultResponse:
        return response.parse_json(ResultResponse)


class TransactionStatusBuilder(ExploringBuilder):
    @staticmethod
    def parse(response: GatewayResponse) -> StatusResponse:
        return response.parse_json(StatusResponse)


class LimitsBuilder:
    @staticmethod
    def parse(response: GatewayResponse) -> LimitsResponse:
        return response.parse_json(LimitsResponse)


class ReportBuilder:
    """
    Contains all necessary data sets builders for construction transaction report retrieval operations
    """

    def __init__(self, __operation_data_set, __operation_mandatory_fields_set) -> None:
        self.__filter_data_builder = ReportFilterDataBuilder(__operation_data_set, __operation_mandatory_fields_set)

    def filter_data(self) -> ReportFilterDataBuilder:
        return self.__filter_data_builder

    @staticmethod
    def parse(response: GatewayResponse) -> CsvResponse:
        return response.parse_csv()
