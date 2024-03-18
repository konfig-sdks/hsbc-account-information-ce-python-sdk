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

from hsbc_account_information_ce_python_sdk.pydantic.account_id import AccountId
from hsbc_account_information_ce_python_sdk.pydantic.debtor_reference import DebtorReference
from hsbc_account_information_ce_python_sdk.pydantic.ob_active_or_historic_currency_and_amount1 import OBActiveOrHistoricCurrencyAndAmount1
from hsbc_account_information_ce_python_sdk.pydantic.ob_branch_and_financial_institution_identification51 import OBBranchAndFinancialInstitutionIdentification51
from hsbc_account_information_ce_python_sdk.pydantic.ob_cash_account51 import OBCashAccount51
from hsbc_account_information_ce_python_sdk.pydantic.ob_external_schedule_type1_code import OBExternalScheduleType1Code
from hsbc_account_information_ce_python_sdk.pydantic.reference import Reference
from hsbc_account_information_ce_python_sdk.pydantic.scheduled_payment_id import ScheduledPaymentId

class OBScheduledPayment3(BaseModel):
    account_id: AccountId = Field(alias='AccountId')

    # The date on which the scheduled payment will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    scheduled_payment_date_time: datetime = Field(alias='ScheduledPaymentDateTime')

    scheduled_type: OBExternalScheduleType1Code = Field(alias='ScheduledType')

    instructed_amount: OBActiveOrHistoricCurrencyAndAmount1 = Field(alias='InstructedAmount')

    scheduled_payment_id: typing.Optional[ScheduledPaymentId] = Field(None, alias='ScheduledPaymentId')

    reference: typing.Optional[Reference] = Field(None, alias='Reference')

    debtor_reference: typing.Optional[DebtorReference] = Field(None, alias='DebtorReference')

    creditor_agent: typing.Optional[OBBranchAndFinancialInstitutionIdentification51] = Field(None, alias='CreditorAgent')

    creditor_account: typing.Optional[OBCashAccount51] = Field(None, alias='CreditorAccount')
    class Config:
        arbitrary_types_allowed = True
