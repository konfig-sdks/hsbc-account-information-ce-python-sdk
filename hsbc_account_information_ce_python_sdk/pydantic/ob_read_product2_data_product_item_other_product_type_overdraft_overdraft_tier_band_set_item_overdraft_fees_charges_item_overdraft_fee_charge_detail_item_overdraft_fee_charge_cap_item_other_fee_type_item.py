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

from hsbc_account_information_ce_python_sdk.pydantic.description3 import Description3
from hsbc_account_information_ce_python_sdk.pydantic.name4 import Name4
from hsbc_account_information_ce_python_sdk.pydantic.ob_code_mnemonic import OBCodeMnemonic

class OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem(BaseModel):
    name: Name4 = Field(alias='Name')

    description: Description3 = Field(alias='Description')

    code: typing.Optional[OBCodeMnemonic] = Field(None, alias='Code')
    class Config:
        arbitrary_types_allowed = True
