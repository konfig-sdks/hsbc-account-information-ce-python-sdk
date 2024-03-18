import typing_extensions

from hsbc_account_information_ce_python_sdk.apis.tags import TagValues
from hsbc_account_information_ce_python_sdk.apis.tags.account_access_consents_api import AccountAccessConsentsApi
from hsbc_account_information_ce_python_sdk.apis.tags.accounts_api import AccountsApi
from hsbc_account_information_ce_python_sdk.apis.tags.scheduled_payments_api import ScheduledPaymentsApi
from hsbc_account_information_ce_python_sdk.apis.tags.standing_orders_api import StandingOrdersApi
from hsbc_account_information_ce_python_sdk.apis.tags.transactions_api import TransactionsApi
from hsbc_account_information_ce_python_sdk.apis.tags.balances_api import BalancesApi
from hsbc_account_information_ce_python_sdk.apis.tags.beneficiaries_api import BeneficiariesApi
from hsbc_account_information_ce_python_sdk.apis.tags.parties_api import PartiesApi
from hsbc_account_information_ce_python_sdk.apis.tags.products_api import ProductsApi
from hsbc_account_information_ce_python_sdk.apis.tags.direct_debits_api import DirectDebitsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCOUNT_ACCESS_CONSENTS: AccountAccessConsentsApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.SCHEDULED_PAYMENTS: ScheduledPaymentsApi,
        TagValues.STANDING_ORDERS: StandingOrdersApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.BALANCES: BalancesApi,
        TagValues.BENEFICIARIES: BeneficiariesApi,
        TagValues.PARTIES: PartiesApi,
        TagValues.PRODUCTS: ProductsApi,
        TagValues.DIRECT_DEBITS: DirectDebitsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCOUNT_ACCESS_CONSENTS: AccountAccessConsentsApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.SCHEDULED_PAYMENTS: ScheduledPaymentsApi,
        TagValues.STANDING_ORDERS: StandingOrdersApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.BALANCES: BalancesApi,
        TagValues.BENEFICIARIES: BeneficiariesApi,
        TagValues.PARTIES: PartiesApi,
        TagValues.PRODUCTS: ProductsApi,
        TagValues.DIRECT_DEBITS: DirectDebitsApi,
    }
)
