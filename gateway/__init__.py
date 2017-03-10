"""
Transact Pro Payment Gateway integration library.
"""

from gateway.client import Client

# Transact PRO API configuration
API_BASE_URL = 'http://uriel.sk.fpngw3.env/'
API_VERSION = 'v3.0'

# Transact PRO HTTP transport configuration
TIME_OUT = 10
VERIFY_SSL_CERTS = True
# Example: { 'http': 'http://<user>:<pass>@<proxy>:<port>', 'https': 'http://<user>:<pass>@<proxy>:<port>' }
PROXY = None
