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

from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_product_details_notes import OBBCAData1ProductDetailsNotes
from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_product_details_segment import OBBCAData1ProductDetailsSegment

class OBBCAData1ProductDetails(BaseModel):
    segment: typing.Optional[OBBCAData1ProductDetailsSegment] = Field(None, alias='Segment')

    # The length/duration of the fee free period
    fee_free_length: typing.Optional[typing.Union[int, float]] = Field(None, alias='FeeFreeLength')

    # The unit of period (days, weeks, months etc.) of the promotional length
    fee_free_length_period: typing.Optional[Literal["Day", "Half Year", "Month", "Quarter", "Week", "Year"]] = Field(None, alias='FeeFreeLengthPeriod')

    notes: typing.Optional[OBBCAData1ProductDetailsNotes] = Field(None, alias='Notes')
    class Config:
        arbitrary_types_allowed = True
