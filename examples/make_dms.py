# pprint for nice printing of dict or json etc.
# It's not necessary to use it in your implementation
import pprint
import random
import string
# Add library, to make your work easier
import gateway

# Step 0
# Init client class for our work flow
GATEWAY_CLIENT = gateway.Client()

# Step 1
# Add your merchant authorization data
GATEWAY_CLIENT.create_auth_data().add_account_id(id_number=22)
GATEWAY_CLIENT.create_auth_data().add_secret_key(value='Ht93CeOzg5ofmkLJYyiuhpvwRXWIGUxs')

# Step 2
# Ok, now build our transaction request
# Set operation DMS hold
transaction_dms_hold = GATEWAY_CLIENT.set_operation().dms_hold()

# Add our credit card (PAN) values, cvv, names, pan number
transaction_dms_hold.payment_method_set().add_pan_cardholder_name(first_last_name='Jane Doe')
transaction_dms_hold.payment_method_set().add_pan_cvv_code(cvv_number=442)
transaction_dms_hold.payment_method_set().add_pan_expiry_date(mm_yy='12/30')
transaction_dms_hold.payment_method_set().add_pan_number(pan_number='4222222222222')

# Now we settings, how much we must take off money from our cardholder
transaction_dms_hold.money_data_set().add_payment_amount(minor_value=5000)
transaction_dms_hold.money_data_set().add_payment_currency(iso_4217_ccy='USD')

# If need you can setup customer data information of that transaction, but it's optional
transaction_dms_hold.customer_data_set().add_email('jane_doe@nice.example.com')
# In our case billing data and shipping data will be same
# First set billing
transaction_dms_hold.customer_data_set().add_billing_country(country='Latvia')
transaction_dms_hold.customer_data_set().add_billing_state(state='Riga')
transaction_dms_hold.customer_data_set().add_billing_city(city='Riga')
transaction_dms_hold.customer_data_set().add_billing_street(street='Gustava Zemgala gatve')
transaction_dms_hold.customer_data_set().add_billing_house(house_number='76')
transaction_dms_hold.customer_data_set().add_billing_flat(flat_number='12')
transaction_dms_hold.customer_data_set().add_billing_zip(zip_code='LV-1039')

# Now set shipping data for our transaction
transaction_dms_hold.customer_data_set().add_shipping_country(country='Latvia')
transaction_dms_hold.customer_data_set().add_shipping_state(state='Riga')
transaction_dms_hold.customer_data_set().add_shipping_city(city='Riga')
transaction_dms_hold.customer_data_set().add_shipping_street(street='Gustava Zemgala gatve')
transaction_dms_hold.customer_data_set().add_shipping_house(house_number='76')
transaction_dms_hold.customer_data_set().add_shipping_flat(flat_number='12')
transaction_dms_hold.customer_data_set().add_shipping_zip(zip_code='LV-1039')

# Don't forget to fill your merchant data in your transaction, like this one
transaction_dms_hold.merchant_order_data_set.add_merchant_transaction_id(
    transaction_id=''.join(random.choice(string.ascii_lowercase) for t_id in range(random.randrange(0, 50, 2)))
)
transaction_dms_hold.merchant_order_data_set.add_merchant_order_id(
    order_id=''.join(random.choice(string.ascii_lowercase) for o_id in range(random.randrange(0, 255, 2)))
)
transaction_dms_hold.merchant_order_data_set.add_merchant_order_description(
    description='Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
)
transaction_dms_hold.merchant_order_data_set.add_merchant_order_meta(
    json_object={'f_name': 'Jane', 'l_name': 'Doe', 'sequence': '0', 'title': 'president', 'url': 'nice.example.com'}
)
# So, all almost done. Set our cardholder IP. That's optionally.
transaction_dms_hold.system_data_set().add_user_ip(cardholder_ipv4='192.168.1.70')
transaction_dms_hold.system_data_set().add_x_forwarded_for_ip(cardholder_ipv4='192.168.1.70')

# Step 3
# Construct our transaction request data
# TODO Add try catch validator exception
dms_hold_transaction = GATEWAY_CLIENT.build_request()
print('Constructed DMS HOLD request:')
pprint.pprint(dms_hold_transaction)
print('--------------------')

# Step 4
# Now make our request via Transact pro HTTP transporter
# Or you can use your own HTTP transporter
result = GATEWAY_CLIENT.make_request(request_json=dms_hold_transaction)
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
# Step 0
# Init client class for our work flow
GATEWAY_CLIENT = gateway.Client()
# Step 1
# Add your merchant authorization data
GATEWAY_CLIENT.create_auth_data().add_account_id(id_number=22)
GATEWAY_CLIENT.create_auth_data().add_secret_key(value='Ht93CeOzg5ofmkLJYyiuhpvwRXWIGUxs')
# Step 2
transaction_dms_charge = GATEWAY_CLIENT.set_operation().dms_charge()
# As we do in DMS HOLD, set needed data sets.
# For DMS CHARGE need provide gate_transaction_id form last operation DMS HOLD
transaction_dms_charge.command_data_set().add_gateway_transaction_id(gate_transaction_id=gateway_transaction_id)
# And we can charge holded data part of it or full.
# As in example:
# First payment was for the shipment in the e-commerce shop and holded 50$ from your cardholder
# But cardholder received half of goods, so we charge 20$ form hold
transaction_dms_charge.money_data_set().add_payment_amount(minor_value=2000)

# Step 3
# As usual build our request for needed operation
# TODO Try catch exception of validator
dms_charge_transaction = GATEWAY_CLIENT.build_request()
print('Constructed DMS CHARGE request:')
pprint.pprint(dms_charge_transaction)
print('--------------------')

# Ok, let's send request via Transact Pro HTTP transporter
result = GATEWAY_CLIENT.make_request(request_json=dms_charge_transaction)
print('Response:')
gw_response = result
if gw_response.text is '' or gw_response.text is None:
    raise RuntimeError("Critical can't continue: Gateway response empty!")
gw_response = gw_response.json()
pprint.pprint(gw_response)
print('--------------------')
# That's it, happy coding
