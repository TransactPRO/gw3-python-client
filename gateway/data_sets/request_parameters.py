class RequestParameters:
    """
    Transact Pro APIs Request Parameters data sets
    """
    # Auth data sets
    AUTH_DATA_ACCOUNT_ID = 'account-id'
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
    AUTH_DATA_ACCOUNT_ID = int
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
