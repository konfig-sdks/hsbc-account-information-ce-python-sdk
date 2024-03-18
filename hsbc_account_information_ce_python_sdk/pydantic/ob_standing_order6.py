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
from hsbc_account_information_ce_python_sdk.pydantic.frequency1 import Frequency1
from hsbc_account_information_ce_python_sdk.pydantic.number_of_payments import NumberOfPayments
from hsbc_account_information_ce_python_sdk.pydantic.ob_active_or_historic_currency_and_amount11 import OBActiveOrHistoricCurrencyAndAmount11
from hsbc_account_information_ce_python_sdk.pydantic.ob_active_or_historic_currency_and_amount2 import OBActiveOrHistoricCurrencyAndAmount2
from hsbc_account_information_ce_python_sdk.pydantic.ob_active_or_historic_currency_and_amount3 import OBActiveOrHistoricCurrencyAndAmount3
from hsbc_account_information_ce_python_sdk.pydantic.ob_active_or_historic_currency_and_amount4 import OBActiveOrHistoricCurrencyAndAmount4
from hsbc_account_information_ce_python_sdk.pydantic.ob_branch_and_financial_institution_identification51 import OBBranchAndFinancialInstitutionIdentification51
from hsbc_account_information_ce_python_sdk.pydantic.ob_cash_account51 import OBCashAccount51
from hsbc_account_information_ce_python_sdk.pydantic.ob_external_standing_order_status1_code import OBExternalStandingOrderStatus1Code
from hsbc_account_information_ce_python_sdk.pydantic.ob_supplementary_data1 import OBSupplementaryData1
from hsbc_account_information_ce_python_sdk.pydantic.reference import Reference
from hsbc_account_information_ce_python_sdk.pydantic.standing_order_id import StandingOrderId

class OBStandingOrder6(BaseModel):
    account_id: AccountId = Field(alias='AccountId')

    frequency: Frequency1 = Field(alias='Frequency')

    standing_order_id: typing.Optional[StandingOrderId] = Field(None, alias='StandingOrderId')

    reference: typing.Optional[Reference] = Field(None, alias='Reference')

    # The date on which the first payment for a Standing Order schedule will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    first_payment_date_time: typing.Optional[datetime] = Field(None, alias='FirstPaymentDateTime')

    # The date on which the next payment for a Standing Order schedule will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    next_payment_date_time: typing.Optional[datetime] = Field(None, alias='NextPaymentDateTime')

    # The date on which the last (most recent) payment for a Standing Order schedule was made.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    last_payment_date_time: typing.Optional[datetime] = Field(None, alias='LastPaymentDateTime')

    # The date on which the final payment for a Standing Order schedule will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    final_payment_date_time: typing.Optional[datetime] = Field(None, alias='FinalPaymentDateTime')

    number_of_payments: typing.Optional[NumberOfPayments] = Field(None, alias='NumberOfPayments')

    standing_order_status_code: typing.Optional[OBExternalStandingOrderStatus1Code] = Field(None, alias='StandingOrderStatusCode')

    first_payment_amount: typing.Optional[OBActiveOrHistoricCurrencyAndAmount2] = Field(None, alias='FirstPaymentAmount')

    next_payment_amount: typing.Optional[OBActiveOrHistoricCurrencyAndAmount3] = Field(None, alias='NextPaymentAmount')

    last_payment_amount: typing.Optional[OBActiveOrHistoricCurrencyAndAmount11] = Field(None, alias='LastPaymentAmount')

    final_payment_amount: typing.Optional[OBActiveOrHistoricCurrencyAndAmount4] = Field(None, alias='FinalPaymentAmount')

    creditor_agent: typing.Optional[OBBranchAndFinancialInstitutionIdentification51] = Field(None, alias='CreditorAgent')

    creditor_account: typing.Optional[OBCashAccount51] = Field(None, alias='CreditorAccount')

    supplementary_data: typing.Optional[OBSupplementaryData1] = Field(None, alias='SupplementaryData')
    class Config:
        arbitrary_types_allowed = True
