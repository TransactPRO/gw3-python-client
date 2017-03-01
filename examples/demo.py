#!/usr/bin/env python

from gateway.client import GateWayClient

MY_MERCHANT = {
    'ACCOUNT_ID': 22,
    'SEC_KEY': 'UOJ6sQPByC4fpg5XoZ0txmzniudr3HMc'
}

payment_data_from_ecommerce_web = {
    'card_num': '8888223211313',
    'exp_date': '12/18',
    'cvv': '442',
    'name': 'John Doe'
}

# Init client
GW_TPRO = GateWayClient()

# Set auth
auth = GW_TPRO.create_auth_data()
auth.add_account_id(account_id=MY_MERCHANT['ACCOUNT_ID'])
auth.add_secret_key(secret_key=MY_MERCHANT['SEC_KEY'])

# Build your transaction
sms = GW_TPRO.set_operation().sms()
sms.PaymentMethod.add_pan_number(pan_number=payment_data_from_ecommerce_web['card_num'])
sms.PaymentMethod.add_pan_expiry_date(pan_exp_date=payment_data_from_ecommerce_web['exp_date'])
sms.PaymentMethod.add_pan_cvv_code(pan_cvv=payment_data_from_ecommerce_web['cvv'])
sms.PaymentMethod.add_pan_cardholder_name(pan_cardholder_name=payment_data_from_ecommerce_web['name'])
sms.MoneyData.add_payment_amount(payment_amount=100)
sms.MoneyData.add_payment_currency(payment_currency='EUR')


# Do req
try:
    print(GW_TPRO.build_request())
except (KeyError, ValueError, RuntimeError):
    raise




# print(req)
# for v in (req):
#     for e in v:
#         print(v[e])



# Handle response


