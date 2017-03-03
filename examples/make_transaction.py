import pprint
from gateway import Client

TPRO_CLI = Client()
TPRO_CLI.create_auth_data().add_account_id(22)
TPRO_CLI.create_auth_data().add_secret_key('UOJ6sQPByC4fpg5XoZ0txmzniudr3HMc')

transaction_sms = TPRO_CLI.set_operation().sms()
transaction_sms.PaymentMethod.add_pan_cardholder_name('John Doe')
transaction_sms.PaymentMethod.add_pan_cvv_code('442')
transaction_sms.PaymentMethod.add_pan_expiry_date('12/18')
transaction_sms.PaymentMethod.add_pan_number('8888223211313')

transaction_request = TPRO_CLI.build_request()
print('Constructed request:')
pprint.pprint(transaction_request)


result = TPRO_CLI.make_request(request_json=transaction_request)
print('Response:')
pprint.pprint(result.json())
