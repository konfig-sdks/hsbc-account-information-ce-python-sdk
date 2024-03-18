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

from hsbc_account_information_ce_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_repayment_repayment_holiday_item_notes import OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemNotes

class OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItem(BaseModel):
    # The maximum length/duration of a Repayment Holiday
    max_holiday_length: typing.Optional[int] = Field(None, alias='MaxHolidayLength')

    # The unit of period (days, weeks, months etc.) of the repayment holiday
    max_holiday_period: typing.Optional[Literal["PACT", "PDAY", "PHYR", "PMTH", "PQTR", "PWEK", "PYER"]] = Field(None, alias='MaxHolidayPeriod')

    notes: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemNotes] = Field(None, alias='Notes')
    class Config:
        arbitrary_types_allowed = True