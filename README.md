# Transact Pro Gateway v3 Python client library
This library provide ability to make requests to Transact Pro Gateway API v3.


## Requirements
- This library works with Python 3.6 and above.

## Installation
Install the latest version with:

```bash
python3 -m pip install --user transactpro-gw3-client
```

Or from sources:
```bash
python3 -m pip install --user --upgrade setuptools wheel

git clone https://github.com/TransactPRO/gw3-python-client.git
cd gw3-python-client
python3 setup.py sdist bdist_wheel
pip install --user --upgrade ./dist/*.whl
```

## Documentation
This `README` provide introduction to the library usage.

### Supported operations
- Transactions
  - SMS
  - DMS HOLD
  - DMS CHARGE
  - CANCEL
  - MOTO SMS
  - MOTO DMS
  - CREDIT
  - P2P
  - B2P
  - INIT RECURRENT DMS
  - RECURRENT DMS
  - INIT RECURRENT SMS
  - RECURRENT SMS
  - REFUND
  - REVERSAL

- Information
  - HISTORY
  - RECURRENTS
  - REFUNDS
  - RESULT
  - STATUS
  - LIMITS

- Verifications
  - Verify 3-D Secure enrollment
  - Complete card verification

- Tokenization
  - Create payment data token
  
- Callback processing
  - Verify callback data sign

- Reporting
  - Get transactions report in CSV format

### Basic usage

You can find several examples realisation in examples folder:
[ExampleScripts](https://github.com/TransactPRO/gw3-python-client/blob/master/examples/)

Also you can set up base configuration for your workflow.

Config sets:
 - Base API URL address
 - API version
 - HTTP time out sec
 - SSL verification flag
 - Proxy config

Usage in your implementation:
```python
import gateway

# Changing default configuration
gateway.API_BASE_URL = 'https://custom-api.com/'
gateway.API_VERSION = 'v999.0'
gateway.HTTP_TIME_OUT = '200'
gateway.HTTP_PROXY = {
    'http': 'http://ECommerce:SuperSu@api-proxy:8822',
    'https': 'http://ECommerce:SuperSu@api-proxy:8822'
}
gateway.HTTP_VERIFY_SSL_CERTS = False
```

### Errors

Library may throw following errors:
- RuntimeError
- ValueError
- DigestMissingError
- DigestMismatchError

### Card verification

```python
import gateway

# set init card verification mode for a payment
payment.command_data_set().add_card_verification_mode(gateway.CARD_VERIFICATION_MODE_INIT)

# complete card verification
complete_request = GATEWAY_CLIENT.set_operation().verify_card()
complete_request.data_set().add_gateway_transaction_id(initialPaymentGatewayId)
request = GATEWAY_CLIENT.build_request()
response = GATEWAY_CLIENT.make_request(request)
if response.status != 200:
    raise RuntimeError('Verification failed')

# set card verification mode to verify for subsequent payments
new_payment.command_data_set().add_card_verification_mode(gateway.CARD_VERIFICATION_MODE_VERIFY)
```

### Payment data tokenization

```python
import gateway

# option 1: create a payment with flag to save payment data
payment.command_data_set().add_payment_method_data_source(gateway.DATA_SOURCE_SAVE_TO_GATEWAY)

# option 2: send "create token" request with payment data
operation = GATEWAY_CLIENT.set_operation().create_token()

operation.payment_method_set().add_pan_cardholder_name(first_last_name='John Doe')
operation.payment_method_set().add_pan_expiry_date(mm_yy='12/20')
operation.payment_method_set().add_pan_number(pan_number='4222222222222')
operation.money_data_set().add_payment_currency(iso_4217_ccy='EUR')

request = GATEWAY_CLIENT.build_request()
response = GATEWAY_CLIENT.make_request(request)

# send a payment with flag to load payment data by token
new_payment.command_data_set().add_payment_method_data_source(gateway.DATA_SOURCE_USE_GATEWAY_SAVED_CARDHOLDER_INITIATED)
new_payment.command_data_set().add_payment_method_data_token('initial gateway-transaction-id')
```

### Callback validation

```python
import json

from gateway.crypto.digest import ResponseDigest
from gateway.responses.payment import CallbackResult

response_digest = ResponseDigest(signFromPost)
response_digest.set_original_uri(payment_response.digest.get_uri())        # optional, set if available
response_digest.set_original_cnonce(payment_response.digest.get_cnonce())  # optional, set if available
response_digest.set_body(jsonFromPost)
response_digest.verify(GUID, SECRET_KEY)

parsed_callback = CallbackResult(json.loads(jsonFromPost))
print(parsed_callback.gw.status_text)
```

### Transactions report loading

```python
import gateway

# NB. Merchant GUID/secret must be used instead of account GUID/secret!
GATEWAY_CLIENT.create_auth_data().add_merchant_guid(SOME_MERCHANT_GUID)
GATEWAY_CLIENT.create_auth_data().add_secret_key(SOME_SERCET_KEY)

operation = GATEWAY_CLIENT.set_operation().report()
operation.filter_data().add_dt_created_from(time.time() - 86400)
operation.filter_data().add_dt_finished_to(time.time())

request_data = GATEWAY_CLIENT.build_request()
response = GATEWAY_CLIENT.make_request(request_data)
parsed_response = operation.parse(response)

print(parsed_response.get_headers())
for transaction_data in parsed_response:
    print(transaction_data)
```

### Customization

If you need to load an HTML form from Gateway instead of cardholder browser redirect, a special operation type may be used:

```python
import gateway

GATEWAY_CLIENT.set_operation().retrieve_form(parsed_payment_response)
response = GATEWAY_CLIENT.make_request()
html = response.payload
```

### How to run tests

Tests are based on Unit testing framework (unittest).
Then, go to project directory and run all of the tests by executing command in terminal:
```bash
python3 -m unittest tests
```
Or only run one of the suites:
```bash
python3 -m unittest tests/test_client.py
```

## About

### Submit bugs and feature requests

Bugs and feature request are tracked on [GitHub](https://github.com/TransactPRO/gw3-python-client/issues)

### If you wont to make some contributions

Please review code style guideline and try to keep in accordance with it
[CodeStyle](https://github.com/TransactPRO/gw3-python-client/blob/master/CODESTYLE.md)

### License
This library is licensed under the MIT License - see the `LICENSE` file for details.