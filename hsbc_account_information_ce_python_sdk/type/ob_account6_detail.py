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
from hsbc_account_information_ce_python_sdk.type.active_or_historic_currency_code0 import ActiveOrHistoricCurrencyCode0
from hsbc_account_information_ce_python_sdk.type.description0 import Description0
from hsbc_account_information_ce_python_sdk.type.nickname import Nickname
from hsbc_account_information_ce_python_sdk.type.ob_account6_detail_account import OBAccount6DetailAccount
from hsbc_account_information_ce_python_sdk.type.ob_account_status1_code import OBAccountStatus1Code
from hsbc_account_information_ce_python_sdk.type.ob_branch_and_financial_institution_identification50 import OBBranchAndFinancialInstitutionIdentification50
from hsbc_account_information_ce_python_sdk.type.ob_external_account_sub_type1_code import OBExternalAccountSubType1Code
from hsbc_account_information_ce_python_sdk.type.ob_external_account_type1_code import OBExternalAccountType1Code
from hsbc_account_information_ce_python_sdk.type.ob_external_switch_status_code import OBExternalSwitchStatusCode

class RequiredOBAccount6Detail(TypedDict):
    AccountId: AccountId

    Currency: ActiveOrHistoricCurrencyCode0

    AccountType: OBExternalAccountType1Code

    AccountSubType: OBExternalAccountSubType1Code

    Account: OBAccount6DetailAccount

class OptionalOBAccount6Detail(TypedDict, total=False):
    Status: OBAccountStatus1Code

    # Date and time at which the resource status was updated.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    StatusUpdateDateTime: datetime

    Description: Description0

    Nickname: Nickname

    # Date on which the account and related basic services are effectively operational for the account owner.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    OpeningDate: datetime

    # Maturity date of the account.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    MaturityDate: datetime

    SwitchStatus: OBExternalSwitchStatusCode

    Servicer: OBBranchAndFinancialInstitutionIdentification50

class OBAccount6Detail(RequiredOBAccount6Detail, OptionalOBAccount6Detail):
    pass
