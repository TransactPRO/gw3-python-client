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


# It's not necessary to use it in your implementation
import pprint
# Add library, to make your work easier
import gateway

# Step 0
# Init client class for our work flow
GATEWAY_CLIENT = gateway.Client()
# Step 1
# Add your merchant authorization data
GATEWAY_CLIENT.create_auth_data().add_account_id(id_number=507)
GATEWAY_CLIENT.create_auth_data().add_secret_key(value='IvjBhoeDKUkCMOif58gyxlRNb7QpdmtF')
# Step 2
# Now let's set operation
verify_3d_enrollment = GATEWAY_CLIENT.set_operation().verify_3d_enrollment()
verify_3d_enrollment.input_data_set().add_pan_number("4111111111111111")
verify_3d_enrollment.input_data_set().add_terminal_mid("1234567")
verify_3d_enrollment.input_data_set().add_currency("EUR")

# Step 3
# Construct our transaction request data
api_request = GATEWAY_CLIENT.build_request()
print('Request:')
pprint.pprint(api_request)
print('--------------------')
# Step 4
# Now make our request via Transact pro HTTP transporter
# Or you can use your own HTTP transporter
gw_response = GATEWAY_CLIENT.make_request(request_json=api_request)
print('Response:')
pprint.pprint(gw_response)
print('--------------------')
