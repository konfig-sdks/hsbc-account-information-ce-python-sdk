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
from hsbc_account_information_ce_python_sdk.type.ob_external_statement_type1_code import OBExternalStatementType1Code
from hsbc_account_information_ce_python_sdk.type.ob_statement2_statement_amount import OBStatement2StatementAmount
from hsbc_account_information_ce_python_sdk.type.ob_statement2_statement_benefit import OBStatement2StatementBenefit
from hsbc_account_information_ce_python_sdk.type.ob_statement2_statement_date_time import OBStatement2StatementDateTime
from hsbc_account_information_ce_python_sdk.type.ob_statement2_statement_description import OBStatement2StatementDescription
from hsbc_account_information_ce_python_sdk.type.ob_statement2_statement_fee import OBStatement2StatementFee
from hsbc_account_information_ce_python_sdk.type.ob_statement2_statement_interest import OBStatement2StatementInterest
from hsbc_account_information_ce_python_sdk.type.ob_statement2_statement_rate import OBStatement2StatementRate
from hsbc_account_information_ce_python_sdk.type.ob_statement2_statement_value import OBStatement2StatementValue
from hsbc_account_information_ce_python_sdk.type.statement_id import StatementId
from hsbc_account_information_ce_python_sdk.type.statement_reference import StatementReference

class RequiredOBStatement2(TypedDict):
    AccountId: AccountId

    Type: OBExternalStatementType1Code

    # Date and time at which the statement period starts.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    StartDateTime: datetime

    # Date and time at which the statement period ends.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    EndDateTime: datetime

    # Date and time at which the resource was created.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    CreationDateTime: datetime

class OptionalOBStatement2(TypedDict, total=False):
    StatementId: StatementId

    StatementReference: StatementReference

    StatementDescription: OBStatement2StatementDescription

    StatementBenefit: OBStatement2StatementBenefit

    StatementFee: OBStatement2StatementFee

    StatementInterest: OBStatement2StatementInterest

    StatementAmount: OBStatement2StatementAmount

    StatementDateTime: OBStatement2StatementDateTime

    StatementRate: OBStatement2StatementRate

    StatementValue: OBStatement2StatementValue

class OBStatement2(RequiredOBStatement2, OptionalOBStatement2):
    pass