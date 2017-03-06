# pprint for nice printing of dict or json etc.
# It's not necessary to use it in your implementation
import pprint
# # Must have, response all in json format
# import json
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
# Ok, now build our transaction request
# Set operation DMS hold
transaction_dms_hold = TPRO_CLI.set_operation().dms_hold()

# Add our credit card (PAN) values, cvv, names, pan number
transaction_dms_hold.payment_method_set().add_pan_cardholder_name(first_last_name='Jane Doe')
transaction_dms_hold.payment_method_set().add_pan_cvv_code(cvv_number=442)
transaction_dms_hold.payment_method_set().add_pan_expiry_date(mm_yy='12/30')
transaction_dms_hold.payment_method_set().add_pan_number(pan_number='4222222222222')

# Now we settings, how much we must take off money from our cardholder
transaction_dms_hold.money_data_set().add_payment_amount(minor_value=5000)
transaction_dms_hold.money_data_set().add_payment_currency(iso_4217_ccy='USD')

# So, all done, almost. Set our cardholder IP. That's is optionally, you can not report that information
transaction_dms_hold.system_data_set().add_user_ip(cardholder_ipv4='192.168.1.70')
transaction_dms_hold.system_data_set().add_x_forwarded_for_ip(cardholder_ipv4='192.168.1.70')

# Step 3
# Build prepared transaction data
# TODO Add try catch validator exception
dms_hold_request = TPRO_CLI.build_request()
print('Constructed request:')
pprint.pprint(dms_hold_request)
print('--------------------')

# Step 4
# Now make our request via Transact pro HTTP transporter
result = TPRO_CLI.make_request(request_json=dms_hold_request)
print('Response:')
gw_response = result
if gw_response.text is '' or gw_response.text is None:
    raise RuntimeError("Critical can't continue: Gateway response empty!")
gw_response = gw_response.json()
pprint.pprint(gw_response)
print('--------------------')


# Nice let's try get our new gateway transaction id from response.
# It's needed to charge transaction to next stage, it's called DMS CHARGE
if 'gw' not in gw_response:
    raise RuntimeError("Critical can't continue: Gateway isn't provided (gw) data!")
tmp_dict_space = gw_response['gw']
if 'gateway-transaction-id' not in tmp_dict_space:
    raise RuntimeError("Critical can't continue: Gateway isn't provided (gateway-transaction-id) data field!")
gateway_transaction_id = tmp_dict_space['gateway-transaction-id']

# Awesome we extracted our id for next step, so prepare TO CHARGE our transaction.
# Or even just save that stuff in your database for future using

# DMS charge time
# Step 1 (Auth we done constructed) so set operation DMS CHARGE
transaction_dms_charge = TPRO_CLI.set_operation().dms_charge()
# As we do in DMS HOLD, set needed data sets.
# For DMS CHARGE need provide gate_transaction_id form last operation DMS HOLD
transaction_dms_charge.command_data_set().add_gateway_transaction_id(gate_transaction_id=gateway_transaction_id)
# And we can charge holded data part of it or full.
# As in example:
# First payment was for the fuel in the gas station and holded 50$ from your cardholder
# But cardholder filled for 20$ so DMS charge must be 20$
transaction_dms_charge.money_data_set().add_payment_amount(minor_value=2000)

# As usual build our request for needed operation
# TODO Try catch exception of validator
dms_charge_request = TPRO_CLI.build_request()
print('Constructed request:')
pprint.pprint(dms_charge_request)
print('--------------------')

# Ok, let's send request via Transact Pro HTTP transporter
result = TPRO_CLI.make_request(request_json=dms_hold_request)
print('Response:')
gw_response = result
if gw_response.text is '' or gw_response.text is None:
    raise RuntimeError("Critical can't continue: Gateway response empty!")
gw_response = gw_response.json()
pprint.pprint(gw_response)
print('--------------------')
# That's it, happy coding
