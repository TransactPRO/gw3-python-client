"""
Transact Pro Payment Gateway integration library.
"""

from gateway.client import Client

# Transact PRO API configuration
API_BASE_URL = 'https://api.transactpro.lv/v3.0'
API_VERSION = 'v3.0'

# Transact PRO HTTP transport configuration
HTTP_TIME_OUT = 60
HTTP_VERIFY_SSL_CERTS = True
# Example: { 'http': 'http://<user>:<pass>@<proxy>:<port>', 'https': 'http://<user>:<pass>@<proxy>:<port>' }
HTTP_PROXY = None
