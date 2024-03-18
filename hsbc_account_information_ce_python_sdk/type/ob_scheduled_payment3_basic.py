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
from hsbc_account_information_ce_python_sdk.type.debtor_reference import DebtorReference
from hsbc_account_information_ce_python_sdk.type.ob_active_or_historic_currency_and_amount1 import OBActiveOrHistoricCurrencyAndAmount1
from hsbc_account_information_ce_python_sdk.type.ob_external_schedule_type1_code import OBExternalScheduleType1Code
from hsbc_account_information_ce_python_sdk.type.reference import Reference
from hsbc_account_information_ce_python_sdk.type.scheduled_payment_id import ScheduledPaymentId

class RequiredOBScheduledPayment3Basic(TypedDict):
    AccountId: AccountId

    # The date on which the scheduled payment will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    ScheduledPaymentDateTime: datetime

    ScheduledType: OBExternalScheduleType1Code

    InstructedAmount: OBActiveOrHistoricCurrencyAndAmount1

class OptionalOBScheduledPayment3Basic(TypedDict, total=False):
    ScheduledPaymentId: ScheduledPaymentId

    Reference: Reference

    DebtorReference: DebtorReference

class OBScheduledPayment3Basic(RequiredOBScheduledPayment3Basic, OptionalOBScheduledPayment3Basic):
    pass
