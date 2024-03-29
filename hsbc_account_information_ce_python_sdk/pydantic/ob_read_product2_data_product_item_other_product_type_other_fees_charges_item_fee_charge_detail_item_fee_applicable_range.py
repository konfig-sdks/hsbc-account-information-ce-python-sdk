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


class OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange(BaseModel):
    # Minimum Amount on which fee/charge is applicable (where it is expressed as an amount)
    minimum_amount: typing.Optional[str] = Field(None, alias='MinimumAmount')

    # Maximum Amount on which fee is applicable (where it is expressed as an amount)
    maximum_amount: typing.Optional[str] = Field(None, alias='MaximumAmount')

    # Minimum rate on which fee/charge is applicable(where it is expressed as an rate)
    minimum_rate: typing.Optional[str] = Field(None, alias='MinimumRate')

    # Maximum rate on which fee/charge is applicable(where it is expressed as an rate)
    maximum_rate: typing.Optional[str] = Field(None, alias='MaximumRate')
    class Config:
        arbitrary_types_allowed = True
