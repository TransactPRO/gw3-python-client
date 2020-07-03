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
import random
import string

import gateway
from gateway.crypto.digest import DigestMissingError, DigestMismatchError

# Step 0
# Init client class for our work flow
GATEWAY_CLIENT = gateway.Client()
# Step 1
# Add your merchant authorization data
GATEWAY_CLIENT.create_auth_data().add_account_guid(guid='3383e58e-9cde-4ffa-85cf-81cd25b2423e')
GATEWAY_CLIENT.create_auth_data().add_secret_key(value='IvjBhoeDKUkCMOif58gyxlRNb7QpdmtF')
# Step 2
# Now let's set operation SMS hold
operation = GATEWAY_CLIENT.set_operation().create_token()
# And fill transaction details as down below
# Add data about cardholder
operation.payment_method_set().add_pan_cardholder_name(first_last_name='John Doe')
operation.payment_method_set().add_pan_expiry_date(mm_yy='12/20')
operation.payment_method_set().add_pan_number(pan_number='4222222222222')
# And about payment
operation.money_data_set().add_payment_currency(iso_4217_ccy='EUR')
# Probably you will needed description of yours transaction
operation.merchant_order_data_set().add_merchant_order_description(
    description='Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
)
# Also you can add your transaction id
operation.merchant_order_data_set().add_merchant_transaction_id(
    transaction_id=''.join(random.choice(string.ascii_lowercase) for t_id in range(random.randrange(0, 50, 2)))
)
# Set our cardholder IP. That's optionally.
operation.system_data_set().add_user_ip(cardholder_ipv4='192.168.1.70')

# Step 3
# Construct our transaction request data
request_data = GATEWAY_CLIENT.build_request()
print('Constructed request:')
pprint.pprint(request_data)
print('--------------------')
# Step 4
# Now make our request via Transact pro HTTP transporter
# Or you can use your own HTTP transporter
try:
    response = GATEWAY_CLIENT.make_request(request_data=request_data)
    parsed_response = operation.parse(response)
except DigestMissingError:
    raise
except DigestMismatchError:
    raise
except RuntimeError:
    raise
print('Response: %s' % parsed_response.__dict__)
print('--------------------')
