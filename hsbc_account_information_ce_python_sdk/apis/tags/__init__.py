# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from hsbc_account_information_ce_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ACCOUNT_ACCESS_CONSENTS = "Account Access Consents"
    ACCOUNTS = "Accounts"
    SCHEDULED_PAYMENTS = "Scheduled Payments"
    STANDING_ORDERS = "Standing Orders"
    TRANSACTIONS = "Transactions"
    BALANCES = "Balances"
    BENEFICIARIES = "Beneficiaries"
    PARTIES = "Parties"
    PRODUCTS = "Products"
    DIRECT_DEBITS = "Direct Debits"
