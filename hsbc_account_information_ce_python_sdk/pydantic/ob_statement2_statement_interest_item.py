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
from pydantic import BaseModel, Field, RootModel

from hsbc_account_information_ce_python_sdk.pydantic.description2 import Description2
from hsbc_account_information_ce_python_sdk.pydantic.ob_active_or_historic_currency_and_amount7 import OBActiveOrHistoricCurrencyAndAmount7
from hsbc_account_information_ce_python_sdk.pydantic.ob_credit_debit_code0 import OBCreditDebitCode0
from hsbc_account_information_ce_python_sdk.pydantic.ob_external_statement_interest_frequency1_code import OBExternalStatementInterestFrequency1Code
from hsbc_account_information_ce_python_sdk.pydantic.ob_external_statement_interest_rate_type1_code import OBExternalStatementInterestRateType1Code
from hsbc_account_information_ce_python_sdk.pydantic.ob_external_statement_interest_type1_code import OBExternalStatementInterestType1Code

class OBStatement2StatementInterestItem(BaseModel):
    credit_debit_indicator: OBCreditDebitCode0 = Field(alias='CreditDebitIndicator')

    type: OBExternalStatementInterestType1Code = Field(alias='Type')

    amount: OBActiveOrHistoricCurrencyAndAmount7 = Field(alias='Amount')

    description: typing.Optional[Description2] = Field(None, alias='Description')

    # field representing a percentage (e.g. 0.05 represents 5% and 0.9525 represents 95.25%). Note the number of decimal places may vary.
    rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='Rate')

    rate_type: typing.Optional[OBExternalStatementInterestRateType1Code] = Field(None, alias='RateType')

    frequency: typing.Optional[OBExternalStatementInterestFrequency1Code] = Field(None, alias='Frequency')
    class Config:
        arbitrary_types_allowed = True
