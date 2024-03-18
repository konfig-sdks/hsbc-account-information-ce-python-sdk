import typing_extensions

from hsbc_account_information_ce_python_sdk.paths import PathValues
from hsbc_account_information_ce_python_sdk.apis.paths.account_access_consents import AccountAccessConsents
from hsbc_account_information_ce_python_sdk.apis.paths.account_access_consents_consent_id import AccountAccessConsentsConsentId
from hsbc_account_information_ce_python_sdk.apis.paths.accounts import Accounts
from hsbc_account_information_ce_python_sdk.apis.paths.accounts_account_id import AccountsAccountId
from hsbc_account_information_ce_python_sdk.apis.paths.accounts_account_id_balances import AccountsAccountIdBalances
from hsbc_account_information_ce_python_sdk.apis.paths.accounts_account_id_direct_debits import AccountsAccountIdDirectDebits
from hsbc_account_information_ce_python_sdk.apis.paths.accounts_account_id_scheduled_payments import AccountsAccountIdScheduledPayments
from hsbc_account_information_ce_python_sdk.apis.paths.accounts_account_id_standing_orders import AccountsAccountIdStandingOrders
from hsbc_account_information_ce_python_sdk.apis.paths.accounts_account_id_transactions import AccountsAccountIdTransactions
from hsbc_account_information_ce_python_sdk.apis.paths.accounts_account_id_beneficiaries import AccountsAccountIdBeneficiaries
from hsbc_account_information_ce_python_sdk.apis.paths.accounts_account_id_parties import AccountsAccountIdParties
from hsbc_account_information_ce_python_sdk.apis.paths.accounts_account_id_product import AccountsAccountIdProduct

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACCOUNTACCESSCONSENTS: AccountAccessConsents,
        PathValues.ACCOUNTACCESSCONSENTS_CONSENT_ID: AccountAccessConsentsConsentId,
        PathValues.ACCOUNTS: Accounts,
        PathValues.ACCOUNTS_ACCOUNT_ID: AccountsAccountId,
        PathValues.ACCOUNTS_ACCOUNT_ID_BALANCES: AccountsAccountIdBalances,
        PathValues.ACCOUNTS_ACCOUNT_ID_DIRECTDEBITS: AccountsAccountIdDirectDebits,
        PathValues.ACCOUNTS_ACCOUNT_ID_SCHEDULEDPAYMENTS: AccountsAccountIdScheduledPayments,
        PathValues.ACCOUNTS_ACCOUNT_ID_STANDINGORDERS: AccountsAccountIdStandingOrders,
        PathValues.ACCOUNTS_ACCOUNT_ID_TRANSACTIONS: AccountsAccountIdTransactions,
        PathValues.ACCOUNTS_ACCOUNT_ID_BENEFICIARIES: AccountsAccountIdBeneficiaries,
        PathValues.ACCOUNTS_ACCOUNT_ID_PARTIES: AccountsAccountIdParties,
        PathValues.ACCOUNTS_ACCOUNT_ID_PRODUCT: AccountsAccountIdProduct,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACCOUNTACCESSCONSENTS: AccountAccessConsents,
        PathValues.ACCOUNTACCESSCONSENTS_CONSENT_ID: AccountAccessConsentsConsentId,
        PathValues.ACCOUNTS: Accounts,
        PathValues.ACCOUNTS_ACCOUNT_ID: AccountsAccountId,
        PathValues.ACCOUNTS_ACCOUNT_ID_BALANCES: AccountsAccountIdBalances,
        PathValues.ACCOUNTS_ACCOUNT_ID_DIRECTDEBITS: AccountsAccountIdDirectDebits,
        PathValues.ACCOUNTS_ACCOUNT_ID_SCHEDULEDPAYMENTS: AccountsAccountIdScheduledPayments,
        PathValues.ACCOUNTS_ACCOUNT_ID_STANDINGORDERS: AccountsAccountIdStandingOrders,
        PathValues.ACCOUNTS_ACCOUNT_ID_TRANSACTIONS: AccountsAccountIdTransactions,
        PathValues.ACCOUNTS_ACCOUNT_ID_BENEFICIARIES: AccountsAccountIdBeneficiaries,
        PathValues.ACCOUNTS_ACCOUNT_ID_PARTIES: AccountsAccountIdParties,
        PathValues.ACCOUNTS_ACCOUNT_ID_PRODUCT: AccountsAccountIdProduct,
    }
)
