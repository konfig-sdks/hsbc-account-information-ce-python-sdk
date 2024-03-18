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

from hsbc_account_information_ce_python_sdk.pydantic.ob_other_code_type10 import OBOtherCodeType10
from hsbc_account_information_ce_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_product_details_notes import OBReadProduct2DataProductItemOtherProductTypeProductDetailsNotes
from hsbc_account_information_ce_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_product_details_segment import OBReadProduct2DataProductItemOtherProductTypeProductDetailsSegment

class OBReadProduct2DataProductItemOtherProductTypeProductDetails(BaseModel):
    segment: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeProductDetailsSegment] = Field(None, alias='Segment')

    # The length/duration of the fee free period
    fee_free_length: typing.Optional[int] = Field(None, alias='FeeFreeLength')

    # The unit of period (days, weeks, months etc.) of the promotional length
    fee_free_length_period: typing.Optional[Literal["PACT", "PDAY", "PHYR", "PMTH", "PQTR", "PWEK", "PYER"]] = Field(None, alias='FeeFreeLengthPeriod')

    # The maximum relevant charges that could accrue as defined fully in Part 7 of the CMA order
    monthly_maximum_charge: typing.Optional[str] = Field(None, alias='MonthlyMaximumCharge')

    notes: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeProductDetailsNotes] = Field(None, alias='Notes')

    other_segment: typing.Optional[OBOtherCodeType10] = Field(None, alias='OtherSegment')
    class Config:
        arbitrary_types_allowed = True