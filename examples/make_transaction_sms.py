import pprint
from gateway import Client

TPRO_CLI = Client()
TPRO_CLI.create_auth_data().add_account_id(id_number=22)
TPRO_CLI.create_auth_data().add_secret_key(value='Ht93CeOzg5ofmkLJYyiuhpvwRXWIGUxs')

transaction_sms = TPRO_CLI.set_operation().sms()
transaction_sms.payment_method_set().add_pan_cardholder_name(first_last_name='John Doe')
transaction_sms.payment_method_set().add_pan_cvv_code(cvv_number=442)
transaction_sms.payment_method_set().add_pan_expiry_date(mm_yy='12/20')
transaction_sms.payment_method_set().add_pan_number(pan_number='4222222222222')
transaction_sms.money_data_set().add_payment_amount(minor_value=100)
transaction_sms.money_data_set().add_payment_currency(iso_4217_ccy='EUR')
transaction_sms.system_data_set().add_user_ip(cardholder_ipv4='192.168.1.70')
transaction_sms.system_data_set().add_x_forwarded_for_ip(cardholder_ipv4='192.168.1.70')

transaction_request = TPRO_CLI.build_request()
print('Constructed request:')
pprint.pprint(transaction_request)

result = TPRO_CLI.make_request(request_json=transaction_request)
print('Response:')
pprint.pprint(result.json())
