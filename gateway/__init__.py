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

"""
Transact Pro Payment Gateway integration library.
"""

from gateway.client import Client

# Transact PRO API configuration
API_BASE_URL = 'https://api.sandbox.transactpro.io/'
API_VERSION = 'v3.0'

# Transact PRO HTTP transport configuration
# Implemented:
# requests
# pycurl
HTTP_TRANSPORT_IMPLEMENTATION = 'requests'
HTTP_TIME_OUT = 60
HTTP_VERIFY_SSL_CERTS = False
# Example: { 'http': 'http://<user>:<pass>@<proxy>:<port>', 'https': 'http://<user>:<pass>@<proxy>:<port>' }
HTTP_PROXY = None

# Card verification modes
CARD_VERIFICATION_MODE_INIT = 1
CARD_VERIFICATION_MODE_VERIFY = 2

# Payment data sources
DATA_SOURCE_CARDHOLDER = 0
DATA_SOURCE_SAVE_TO_GATEWAY = 1
DATA_SOURCE_USE_GATEWAY_SAVED_CARDHOLDER_INITIATED = 2
DATA_SOURCE_SAVING_BY_MERCHANT = 3
DATA_SOURCE_USE_MERCHANT_SAVED_CARDHOLDER_INITIATED = 4
DATA_SOURCE_USE_GATEWAY_SAVED_MERCHANT_INITIATED = 5
DATA_SOURCE_USE_MERCHANT_SAVED_MERCHANT_INITIATED = 6
