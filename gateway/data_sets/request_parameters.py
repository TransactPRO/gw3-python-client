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


class RequestParameters:
    """
    Transact Pro APIs Request Parameters data sets
    """
    # Auth data sets
    AUTH_DATA_ACCOUNT_GUID = 'account-guid'
    AUTH_DATA_SECRET_KEY = 'secret-key'
    AUTH_DATA_SESSION_ID = 'session-id'

    # Command data sets
    COMMAND_DATA_GATEWAY_TRANSACTION_ID = 'gateway-transaction-id'
    COMMAND_DATA_GATEWAY_TRANSACTION_IDS = 'gateway-transaction-ids'
    COMMAND_DATA_MERCHANT_TRANSACTION_IDS = 'merchant-transaction-ids'
    COMMAND_DATA_FORM_ID = 'form-id'
    COMMAND_DATA_TERMINAL_MID = 'terminal-mid'

    # Customer data sets
    GENERAL_DATA_CUSTOMER_DATA_EMAIL = 'email'
    GENERAL_DATA_CUSTOMER_DATA_PHONE = 'phone'
    GENERAL_DATA_CUSTOMER_DATA_BIRTH_DATE = 'birth-date'
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_COUNTRY = 'country'
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_STATE = 'state'
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_CITY = 'city'
    GENERAL_DATA_CUSTOMER_DATA_BILlING_ADDRESS_STREET = 'street'
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_HOUSE = 'house'
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_FLAT = 'flat'
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_ZIP = 'zip'
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_COUNTRY = 'country'
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_STATE = 'state'
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_CITY = 'city'
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_STREET = 'street'
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_HOUSE = 'house'
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_FLAT = 'flat'
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_ZIP = 'zip'

    # Order data sets
    GENERAL_DATA_ORDER_DATA_MERCHANT_TRANSACTION_ID = 'merchant-transaction-id'
    GENERAL_DATA_ORDER_DATA_MERCHANT_USER_ID = 'merchant-user-id'
    GENERAL_DATA_ORDER_DATA_ORDER_ID = 'order-id'
    GENERAL_DATA_ORDER_DATA_ORDER_DESCRIPTION = 'order-description'
    GENERAL_DATA_ORDER_DATA_ORDER_META = 'order-meta'
    GENERAL_DATA_ORDER_DATA_MERCHANT_SIDE_URL = 'merchant-side-url'
    GENERAL_DATA_ORDER_DATA_RECIPIENT_NAME = 'recipient-name'
    GENERAL_DATA_ORDER_DATA_MERCHANT_REFERRING_NAME = 'merchant-referring-name'
    GENERAL_DATA_ORDER_DATA_CUSTOM_3D_RETURN_URL = 'custom-3d-return-url'

    # Payment data sets
    PAYMENT_METHOD_DATA_PAN = 'pan'
    PAYMENT_METHOD_DATA_EXPIRE = 'exp-mm-yy'
    PAYMENT_METHOD_DATA_CVV = 'cvv'
    PAYMENT_METHOD_DATA_CARDHOLDER_NAME = 'cardholder-name'

    # Money data sets
    MONEY_DATA_AMOUNT = 'amount'
    MONEY_DATA_CURRENCY = 'currency'

    # System data sets
    SYSTEM_USER_IP = 'user-ip'
    SYSTEM_X_FORWARDED_FOR = 'x-forwarded-for'

    def __init__(self):
        pass


class RequestParametersTypes(RequestParameters):
    """
    Transact Pro APIs Request Parameters data types
    """
    # Auth data type
    AUTH_DATA_ACCOUNT_GUID = str
    AUTH_DATA_SECRET_KEY = str
    AUTH_DATA_SESSION_ID = str

    # Command data type
    COMMAND_DATA_GATEWAY_TRANSACTION_ID = str
    COMMAND_DATA_GATEWAY_TRANSACTION_IDS = list
    COMMAND_DATA_MERCHANT_TRANSACTION_IDS = list
    COMMAND_DATA_FORM_ID = str
    COMMAND_DATA_TERMINAL_MID = str

    # Customer data sets
    GENERAL_DATA_CUSTOMER_DATA_EMAIL = str
    GENERAL_DATA_CUSTOMER_DATA_PHONE = str
    GENERAL_DATA_CUSTOMER_DATA_BIRTH_DATE = str
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_COUNTRY = str
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_STATE = str
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_CITY = str
    GENERAL_DATA_CUSTOMER_DATA_BILlING_ADDRESS_STREET = str
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_HOUSE = str
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_FLAT = str
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_ZIP = str
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_COUNTRY = str
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_STATE = str
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_CITY = str
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_STREET = str
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_HOUSE = str
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_FLAT = str
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_ZIP = str

    # Order data sets
    GENERAL_DATA_ORDER_DATA_MERCHANT_TRANSACTION_ID = str
    GENERAL_DATA_ORDER_DATA_MERCHANT_USER_ID = str
    GENERAL_DATA_ORDER_DATA_ORDER_ID = str
    GENERAL_DATA_ORDER_DATA_ORDER_DESCRIPTION = str
    GENERAL_DATA_ORDER_DATA_ORDER_META = str
    GENERAL_DATA_ORDER_DATA_MERCHANT_SIDE_URL = str
    GENERAL_DATA_ORDER_DATA_RECIPIENT_NAME = str
    GENERAL_DATA_ORDER_DATA_MERCHANT_REFERRING_NAME = str
    GENERAL_DATA_ORDER_DATA_CUSTOM_3D_RETURN_URL = str

    # Payment data sets
    PAYMENT_METHOD_DATA_PAN = str
    PAYMENT_METHOD_DATA_EXPIRE = str
    PAYMENT_METHOD_DATA_CVV = str
    PAYMENT_METHOD_DATA_CARDHOLDER_NAME = str

    # Money data sets
    MONEY_DATA_AMOUNT = int
    MONEY_DATA_CURRENCY = str

    # System data sets
    SYSTEM_USER_IP = str
    SYSTEM_X_FORWARDED_FOR = str
