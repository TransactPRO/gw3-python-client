# It's not necessary to use it in your implementation
import pprint
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
# Now let's set operation SMS hold
transaction_status = GATEWAY_CLIENT.set_operation().transaction_status()
transaction_status.info_command_data_set().add_gateway_transaction_ids(
    list_of_gate_transaction_id=[
        '16f462cb-9c08-4c14-b983-fa14da6421f1',
        'a0f61a3d-3837-48e8-89de-757dcc14d907',
        'efd3718b-95d2-4f33-95d3-452e3c99e6ae'
    ]
)
# Set our cardholder IP. That's optionally.
transaction_status.system_data_set().add_user_ip(cardholder_ipv4='192.168.1.70')
transaction_status.system_data_set().add_x_forwarded_for_ip(cardholder_ipv4='192.168.1.70')

# Step 3
# Construct our transaction request data
# TODO Add try catch validator exception
sms_transaction = GATEWAY_CLIENT.build_request()
print('Constructed SMS request:')
pprint.pprint(sms_transaction)
print('--------------------')
# Step 4
# Now make our request via Transact pro HTTP transporter
# Or you can use your own HTTP transporter
result = GATEWAY_CLIENT.make_request(request_json=sms_transaction)
print('Response:')
gw_response = result
if gw_response.text is '' or gw_response.text is None:
    raise RuntimeError("Critical can't continue: Gateway response empty!")
gw_response = gw_response.json()
pprint.pprint(gw_response)
print('--------------------')
