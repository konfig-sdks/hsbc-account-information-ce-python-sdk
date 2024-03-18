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

from hsbc_account_information_ce_python_sdk.pydantic.obpca_data1_other_fees_charges_fee_charge_cap_item_fee_type import OBPCAData1OtherFeesChargesFeeChargeCapItemFeeType
from hsbc_account_information_ce_python_sdk.pydantic.obpca_data1_other_fees_charges_fee_charge_cap_item_notes import OBPCAData1OtherFeesChargesFeeChargeCapItemNotes
from hsbc_account_information_ce_python_sdk.pydantic.obpca_data1_other_fees_charges_fee_charge_cap_item_other_fee_type import OBPCAData1OtherFeesChargesFeeChargeCapItemOtherFeeType

class OBPCAData1OtherFeesChargesFeeChargeCapItem(BaseModel):
    fee_type: OBPCAData1OtherFeesChargesFeeChargeCapItemFeeType = Field(alias='FeeType')

    # Indicates that this is the minimum/ maximum fee/charge that can be applied by the financial institution
    min_max_type: Literal["Minimum", "Maximum"] = Field(alias='MinMaxType')

    # fee/charges are captured dependent on the number of occurrences rather than capped at a particular amount
    fee_cap_occurrence: typing.Optional[typing.Union[int, float]] = Field(None, alias='FeeCapOccurrence')

    # Cap amount charged for a fee/charge (where it is charged in terms of an amount rather than a rate)
    fee_cap_amount: typing.Optional[str] = Field(None, alias='FeeCapAmount')

    # Period e.g. day, week, month etc. for which the fee/charge is capped
    capping_period: typing.Optional[Literal["AcademicTerm", "Day", "Half Year", "Month", "Quarter", "Week", "Year"]] = Field(None, alias='CappingPeriod')

    notes: typing.Optional[OBPCAData1OtherFeesChargesFeeChargeCapItemNotes] = Field(None, alias='Notes')

    other_fee_type: typing.Optional[OBPCAData1OtherFeesChargesFeeChargeCapItemOtherFeeType] = Field(None, alias='OtherFeeType')
    class Config:
        arbitrary_types_allowed = True
