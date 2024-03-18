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

from hsbc_account_information_ce_python_sdk.type.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeType
from hsbc_account_information_ce_python_sdk.type.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_notes import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemNotes
from hsbc_account_information_ce_python_sdk.type.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeType

class RequiredOBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem(TypedDict):
    FeeType: OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeType

    # Indicates that this is the minimum/ maximum fee/charge that can be applied by the financial institution
    MinMaxType: str

class OptionalOBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem(TypedDict, total=False):
    # Specifies for the overdraft control feature/benefit
    OverdraftControlIndicator: bool

    # fee/charges are captured dependent on the number of occurrences rather than capped at a particular amount
    FeeCapOccurrence: typing.Union[int, float]

    # Cap amount charged for a fee/charge
    FeeCapAmount: str

    # Period e.g. day, week, month etc. for which the fee/charge is capped
    CappingPeriod: str

    Notes: OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemNotes

    OtherFeeType: OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeType

class OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem(RequiredOBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem, OptionalOBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem):
    pass