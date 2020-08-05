#!/usr/bin/env python3

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
import pprint

import gateway

# Step 0
# Init client class for our work flow
GATEWAY_CLIENT = gateway.Client()
# Step 1
# Add your merchant authorization data
GATEWAY_CLIENT.create_auth_data().add_account_guid(guid='3383e58e-9cde-4ffa-85cf-81cd25b2423e')
GATEWAY_CLIENT.create_auth_data().add_secret_key(value='IvjBhoeDKUkCMOif58gyxlRNb7QpdmtF')
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
sms_transaction = GATEWAY_CLIENT.build_request()
print('Constructed Transaction status request:')
pprint.pprint(sms_transaction)
print('--------------------')
# Step 4
# Now make our request via Transact pro HTTP transporter
# Or you can use your own HTTP transporter
gw_response = GATEWAY_CLIENT.make_request(request_data=sms_transaction)
parsed_gw_response = transaction_status.parse(gw_response)
print('Transaction status Response: %s' % parsed_gw_response.__dict__)
print('--------------------')
