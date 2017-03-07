# It's not necessary to use it in your implementation
import pprint
import random
import string
# Add library, to make your work easier
from gateway import Client

# Step 0
# Init client class for our work flow
TPRO_CLI = Client()
# Step 1
# Add your merchant authorization data
TPRO_CLI.create_auth_data().add_account_id(id_number=22)
TPRO_CLI.create_auth_data().add_secret_key(value='Ht93CeOzg5ofmkLJYyiuhpvwRXWIGUxs')
# Step 2
# Now let's set operation SMS hold
transaction_sms = TPRO_CLI.set_operation().sms()
# And fill transaction details as down below
# Add data about cardholder
transaction_sms.payment_method_set().add_pan_cardholder_name(first_last_name='John Doe')
transaction_sms.payment_method_set().add_pan_cvv_code(cvv_number=442)
transaction_sms.payment_method_set().add_pan_expiry_date(mm_yy='12/20')
transaction_sms.payment_method_set().add_pan_number(pan_number='4222222222222')
# And about payment
transaction_sms.money_data_set().add_payment_amount(minor_value=100)
transaction_sms.money_data_set().add_payment_currency(iso_4217_ccy='EUR')
# Probably you will needed description of yours transaction
transaction_sms.merchant_order_data_set.add_merchant_order_description(
    description='Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
)
# And setup your own order ID
transaction_sms.merchant_order_data_set.add_merchant_order_id(
    order_id=''.join(random.choice(string.ascii_lowercase) for o_id in range(random.randrange(0, 255, 2)))
)
# Also you can add your transaction id

transaction_sms.merchant_order_data_set.add_merchant_transaction_id(
    transaction_id=''.join(random.choice(string.ascii_lowercase) for t_id in range(random.randrange(0, 50, 2)))
)
# Set our cardholder IP. That's optionally.
transaction_sms.system_data_set().add_user_ip(cardholder_ipv4='192.168.1.70')
transaction_sms.system_data_set().add_x_forwarded_for_ip(cardholder_ipv4='192.168.1.70')

# Step 3
# Construct our transaction request data
# TODO Add try catch validator exception
sms_transaction = TPRO_CLI.build_request()
print('Constructed SMS request:')
pprint.pprint(sms_transaction)
print('--------------------')
# Step 4
# Now make our request via Transact pro HTTP transporter
# Or you can use your own HTTP transporter
result = TPRO_CLI.make_request(request_json=sms_transaction)
print('Response:')
gw_response = result
if gw_response.text is '' or gw_response.text is None:
    raise RuntimeError("Critical can't continue: Gateway response empty!")
gw_response = gw_response.json()
pprint.pprint(gw_response)
print('--------------------')
