class RequestParameters:
    """
    Transact Pro APIs Request Parameters data sets
    """
    # Auth data sets
    AUTH_DATA_ACCOUNT_ID = 'account-id'
    AUTH_DATA_SECRET_KEY = 'secret-key'
    AUTH_DATA_SESSION_ID = 'session-id'

    # Command data sets
    COMMAND_DATA_GATEWAY_TRANSACTION_ID = 'data.command-data.gateway-transaction-id'
    COMMAND_DATA_FORM_ID = 'data.command-data.form-id'
    COMMAND_DATA_TERMINAL_MID = 'data.command-data.terminal-mid'

    # Customer data sets
    GENERAL_DATA_CUSTOMER_DATA_EMAIL = 'data.general-data.customer-data.email'
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_COUNTRY = 'data.general-data.customer-data.billing-address.country'
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_STATE = 'data.general-data.customer-data.billing-address.state'
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_CITY = 'data.general-data.customer-data.billing-address.city'
    GENERAL_DATA_CUSTOMER_DATA_BILlING_ADDRESS_STREET = 'data.general-data.customer-data.billing-address.street'
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_HOUSE = 'data.general-data.customer-data.billing-address.house'
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_FLAT = 'data.general-data.customer-data.billing-address.flat'
    GENERAL_DATA_CUSTOMER_DATA_BILLING_ADDRESS_ZIP = 'data.general-data.customer-data.billing-address.zip'
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_COUNTRY = 'data.general-data.customer-data.shipping-address.country'
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_STATE = 'data.general-data.customer-data.shipping-address.state'
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_CITY = 'data.general-data.customer-data.shipping-address.city'
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_STREET = 'data.general-data.customer-data.shipping-address.street'
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_HOUSE = 'data.general-data.customer-data.shipping-address.house'
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_FLAT = 'data.general-data.customer-data.shipping-address.flat'
    GENERAL_DATA_CUSTOMER_DATA_SHIPPING_ADDRESS_ZIP = 'data.general-data.customer-data.shipping-address.zip'

    # Order data sets
    GENERAL_DATA_ORDER_DATA_MERCHANT_TRANSACTION_ID = 'data.general-data.order-data.merchant-transaction-id'
    GENERAL_DATA_ORDER_DATA_MERCHANT_USER_ID = 'data.general-data.order-data.merchant-user-id'
    GENERAL_DATA_ORDER_DATA_ORDER_ID = 'data.general-data.order-data.order-id'
    GENERAL_DATA_ORDER_DATA_ORDER_DESCRIPTION = 'data.general-data.order-data.order-description'
    GENERAL_DATA_ORDER_DATA_ORDER_META = 'data.general-data.order-data.order-meta'

    # Payment data sets
    PAYMENT_METHOD_DATA_PAN = 'pan'
    PAYMENT_METHOD_DATA_EXPIRE = 'exp-mm-yy'
    PAYMENT_METHOD_DATA_CVV = 'cvv'
    PAYMENT_METHOD_DATA_CARDHOLDER_NAME = 'cardholder-name'
    PAYMENT_METHOD_DATA_EXTERNAL_MPI_DATA = 'external-mpi-data'

    # Money data sets
    MONEY_DATA_AMOUNT = 'amount'
    MONEY_DATA_CURRENCY = 'currency'

    # System data sets
    SYSTEM_USER_IP = 'user-ip'
    SYSTEM_X_FORWARDED_FOR = 'x-forwarded-for'

    def __init__(self):
        pass
