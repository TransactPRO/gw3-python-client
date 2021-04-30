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
from gateway.crypto.digest import DigestMismatchError, DigestMissingError
from gateway.responses.constants import Status

# Step 0
# Init client class for our work flow
GATEWAY_CLIENT = gateway.Client()
# Step 1
# Add your merchant authorization data
GATEWAY_CLIENT.create_auth_data().add_account_guid(guid='3383e58e-9cde-4ffa-85cf-81cd25b2423e')
GATEWAY_CLIENT.create_auth_data().add_secret_key(value='IvjBhoeDKUkCMOif58gyxlRNb7QpdmtF')
# Step 2
# Now let's set operation SMS hold
transaction_sms = GATEWAY_CLIENT.set_operation().sms()
# And fill transaction details as down below
# Add data about cardholder
transaction_sms.command_data_set().add_form_id(inside_form_id='22')
transaction_sms.payment_method_set().add_pan_cardholder_name(first_last_name='John Doe')
transaction_sms.payment_method_set().add_pan_cvv_code(cvv_number='442')
transaction_sms.payment_method_set().add_pan_expiry_date(mm_yy='12/20')
transaction_sms.payment_method_set().add_pan_number(pan_number='4222222222222')
# And about payment
transaction_sms.money_data_set().add_payment_amount(minor_value=100)
transaction_sms.money_data_set().add_payment_currency(iso_4217_ccy='EUR')
# Probably you will needed description of yours transaction
transaction_sms.merchant_order_data_set().add_merchant_side_url(url='http://example.com')
transaction_sms.merchant_order_data_set().add_merchant_order_description(
    description='Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
)
# And setup your own order ID
transaction_sms.merchant_order_data_set().add_merchant_order_id(
    order_id=''.join(random.choice(string.ascii_lowercase) for o_id in range(random.randrange(0, 255, 2)))
)
# Also you can add your transaction id

transaction_sms.merchant_order_data_set().add_merchant_transaction_id(
    transaction_id=''.join(random.choice(string.ascii_lowercase) for t_id in range(random.randrange(0, 50, 2)))
)
# Set our cardholder IP. That's optionally.
transaction_sms.system_data_set().add_user_ip(cardholder_ipv4='192.168.1.70')
transaction_sms.system_data_set().add_x_forwarded_for_ip(cardholder_ipv4='192.168.1.70')

# Step 3
# Construct our transaction request data
request_data = GATEWAY_CLIENT.build_request()
print('Constructed SMS request:')
pprint.pprint(request_data)
print('--------------------')
# Step 4
# Now make our request via Transact pro HTTP transporter
# Or you can use your own HTTP transporter
try:
    response = GATEWAY_CLIENT.make_request(request_data=request_data)
    parsed_response = transaction_sms.parse(response)

    if parsed_response.error.error_code:
        raise RuntimeError("GW error: %s" % parsed_response.error.message)
    elif parsed_response.gw.redirect_url:
        pass  # redirect cardholder to parsed_response.gw.redirect_url
except DigestMissingError:
    raise
except DigestMismatchError:
    raise
except RuntimeError:
    raise
print('Response: %s' % parsed_response.__dict__)
print('--------------------')
