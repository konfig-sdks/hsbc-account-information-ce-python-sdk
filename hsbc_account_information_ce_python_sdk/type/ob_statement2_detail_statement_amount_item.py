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

from hsbc_account_information_ce_python_sdk.type.ob_active_or_historic_currency_and_amount8 import OBActiveOrHistoricCurrencyAndAmount8
from hsbc_account_information_ce_python_sdk.type.ob_credit_debit_code0 import OBCreditDebitCode0
from hsbc_account_information_ce_python_sdk.type.ob_external_statement_amount_type1_code import OBExternalStatementAmountType1Code

class RequiredOBStatement2DetailStatementAmountItem(TypedDict):
    CreditDebitIndicator: OBCreditDebitCode0

    Type: OBExternalStatementAmountType1Code

    Amount: OBActiveOrHistoricCurrencyAndAmount8

class OptionalOBStatement2DetailStatementAmountItem(TypedDict, total=False):
    pass

class OBStatement2DetailStatementAmountItem(RequiredOBStatement2DetailStatementAmountItem, OptionalOBStatement2DetailStatementAmountItem):
    pass
