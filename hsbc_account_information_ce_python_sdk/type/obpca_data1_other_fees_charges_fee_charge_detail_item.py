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

from hsbc_account_information_ce_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_fee_applicable_range import OBPCAData1OtherFeesChargesFeeChargeDetailItemFeeApplicableRange
from hsbc_account_information_ce_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_fee_charge_cap import OBPCAData1OtherFeesChargesFeeChargeDetailItemFeeChargeCap
from hsbc_account_information_ce_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_notes import OBPCAData1OtherFeesChargesFeeChargeDetailItemNotes
from hsbc_account_information_ce_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_other_application_frequency import OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherApplicationFrequency
from hsbc_account_information_ce_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_other_calculation_frequency import OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherCalculationFrequency
from hsbc_account_information_ce_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_other_fee_category_type import OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherFeeCategoryType
from hsbc_account_information_ce_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_other_fee_rate_type import OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherFeeRateType
from hsbc_account_information_ce_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_other_fee_type import OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherFeeType

class RequiredOBPCAData1OtherFeesChargesFeeChargeDetailItem(TypedDict):
    # Categorisation of fees and charges into standard categories.
    FeeCategory: str

    # Fee/Charge Type
    FeeType: str

    # How frequently the fee/charge is applied to the account
    ApplicationFrequency: str

class OptionalOBPCAData1OtherFeesChargesFeeChargeDetailItem(TypedDict, total=False):
    # Fee Amount charged for a fee/charge (where it is charged in terms of an amount rather than a rate)
    FeeAmount: str

    # Rate charged for Fee/Charge (where it is charged in terms of a rate rather than an amount)
    FeeRate: str

    # Rate type for Fee/Charge (where it is charged in terms of a rate rather than an amount)
    FeeRateType: str

    # How frequently the fee/charge is calculated
    CalculationFrequency: str

    Notes: OBPCAData1OtherFeesChargesFeeChargeDetailItemNotes

    OtherFeeCategoryType: OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherFeeCategoryType

    OtherFeeType: OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherFeeType

    OtherFeeRateType: OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherFeeRateType

    OtherApplicationFrequency: OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherApplicationFrequency

    OtherCalculationFrequency: OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherCalculationFrequency

    FeeChargeCap: OBPCAData1OtherFeesChargesFeeChargeDetailItemFeeChargeCap

    FeeApplicableRange: OBPCAData1OtherFeesChargesFeeChargeDetailItemFeeApplicableRange

class OBPCAData1OtherFeesChargesFeeChargeDetailItem(RequiredOBPCAData1OtherFeesChargesFeeChargeDetailItem, OptionalOBPCAData1OtherFeesChargesFeeChargeDetailItem):
    pass