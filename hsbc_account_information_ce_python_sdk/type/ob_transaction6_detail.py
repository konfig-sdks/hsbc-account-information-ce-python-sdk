# coding: utf-8

"""
    Account Information API

    In this document, you'll find the steps your organization needs to take to use our API services. Included in this guide are details of request and response messages used to support your organization’s integration. The intended audience for this document are **Technical Architects**, **Development Engineers**, **Test Engineers**, and **Operation & Maintenance Engineers** involved in development and support of your organization’s integration. Setting up our API Services is best completed with the assistance of your organization’s IT team, or someone with experience and knowledge of application programming interfaces. This should include experience with **JSON payloads**, **security** and **public key infrastructure (PKI)**. This Document describes the following request and response structure of HSBCnet - Account Information API. For detail implementation guidelines, please refer to the respective section from [develop.hsbc.com](https://develop.hsbc.com/ob-api-documentation/account-information-uk-personal-v319) 

    The version of the OpenAPI document: 3.1.11
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from hsbc_account_information_ce_python_sdk.type.account_id import AccountId
from hsbc_account_information_ce_python_sdk.type.address_line import AddressLine
from hsbc_account_information_ce_python_sdk.type.ob_active_or_historic_currency_and_amount10 import OBActiveOrHistoricCurrencyAndAmount10
from hsbc_account_information_ce_python_sdk.type.ob_active_or_historic_currency_and_amount9 import OBActiveOrHistoricCurrencyAndAmount9
from hsbc_account_information_ce_python_sdk.type.ob_bank_transaction_code_structure1 import OBBankTransactionCodeStructure1
from hsbc_account_information_ce_python_sdk.type.ob_branch_and_financial_institution_identification61 import OBBranchAndFinancialInstitutionIdentification61
from hsbc_account_information_ce_python_sdk.type.ob_branch_and_financial_institution_identification62 import OBBranchAndFinancialInstitutionIdentification62
from hsbc_account_information_ce_python_sdk.type.ob_cash_account60 import OBCashAccount60
from hsbc_account_information_ce_python_sdk.type.ob_cash_account61 import OBCashAccount61
from hsbc_account_information_ce_python_sdk.type.ob_credit_debit_code1 import OBCreditDebitCode1
from hsbc_account_information_ce_python_sdk.type.ob_currency_exchange5 import OBCurrencyExchange5
from hsbc_account_information_ce_python_sdk.type.ob_entry_status1_code import OBEntryStatus1Code
from hsbc_account_information_ce_python_sdk.type.ob_merchant_details1 import OBMerchantDetails1
from hsbc_account_information_ce_python_sdk.type.ob_supplementary_data1 import OBSupplementaryData1
from hsbc_account_information_ce_python_sdk.type.ob_transaction_card_instrument1 import OBTransactionCardInstrument1
from hsbc_account_information_ce_python_sdk.type.ob_transaction_cash_balance import OBTransactionCashBalance
from hsbc_account_information_ce_python_sdk.type.ob_transaction_mutability1_code import OBTransactionMutability1Code
from hsbc_account_information_ce_python_sdk.type.proprietary_bank_transaction_code_structure1 import ProprietaryBankTransactionCodeStructure1
from hsbc_account_information_ce_python_sdk.type.statement_reference import StatementReference
from hsbc_account_information_ce_python_sdk.type.transaction_id import TransactionId
from hsbc_account_information_ce_python_sdk.type.transaction_information import TransactionInformation
from hsbc_account_information_ce_python_sdk.type.transaction_reference import TransactionReference

class RequiredOBTransaction6Detail(TypedDict):
    AccountId: AccountId

    CreditDebitIndicator: OBCreditDebitCode1

    Status: OBEntryStatus1Code

    # Date and time when a transaction entry is posted to an account on the account servicer's books. Usage: Booking date is the expected booking date, unless the status is booked, in which case it is the actual booking date.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    BookingDateTime: datetime

    Amount: OBActiveOrHistoricCurrencyAndAmount9

class OptionalOBTransaction6Detail(TypedDict, total=False):
    TransactionId: TransactionId

    TransactionReference: TransactionReference

    StatementReference: typing.List[StatementReference]

    TransactionMutability: OBTransactionMutability1Code

    # Date and time at which assets become available to the account owner in case of a credit entry, or cease to be available to the account owner in case of a debit transaction entry. Usage: If transaction entry status is pending and value date is present, then the value date refers to an expected/requested value date. For transaction entries subject to availability/float and for which availability information is provided, the value date must not be used. In this case the availability component identifies the number of availability days.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    ValueDateTime: datetime

    TransactionInformation: TransactionInformation

    AddressLine: AddressLine

    ChargeAmount: OBActiveOrHistoricCurrencyAndAmount10

    CurrencyExchange: OBCurrencyExchange5

    BankTransactionCode: OBBankTransactionCodeStructure1

    ProprietaryBankTransactionCode: ProprietaryBankTransactionCodeStructure1

    Balance: OBTransactionCashBalance

    MerchantDetails: OBMerchantDetails1

    CreditorAgent: OBBranchAndFinancialInstitutionIdentification61

    CreditorAccount: OBCashAccount60

    DebtorAgent: OBBranchAndFinancialInstitutionIdentification62

    DebtorAccount: OBCashAccount61

    CardInstrument: OBTransactionCardInstrument1

    SupplementaryData: OBSupplementaryData1

class OBTransaction6Detail(RequiredOBTransaction6Detail, OptionalOBTransaction6Detail):
    pass
