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

from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_other_fees_charges_item_fee_charge_detail_item_fee_applicable_range import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange
from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCap
from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_other_fees_charges_item_fee_charge_detail_item_notes import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemNotes
from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_other_fees_charges_item_fee_charge_detail_item_other_application_frequency import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherApplicationFrequency
from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_other_fees_charges_item_fee_charge_detail_item_other_calculation_frequency import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherCalculationFrequency
from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_other_fees_charges_item_fee_charge_detail_item_other_fee_category_type import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeCategoryType
from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_other_fees_charges_item_fee_charge_detail_item_other_fee_rate_type import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeRateType
from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_other_fees_charges_item_fee_charge_detail_item_other_fee_type import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType

class OBBCAData1OtherFeesChargesItemFeeChargeDetailItem(BaseModel):
    # Categorisation of fees and charges into standard categories.
    fee_category: Literal["Other", "Servicing"] = Field(alias='FeeCategory')

    # Fee/Charge Type
    fee_type: Literal["Other", "ServiceCAccountFee", "ServiceCAccountFeeMonthly", "ServiceCAccountFeeQuarterly", "ServiceCFixedTariff", "ServiceCBusiDepAccBreakage", "ServiceCMinimumMonthlyFee", "ServiceCOther"] = Field(alias='FeeType')

    # How frequently the fee/charge is applied to the account
    application_frequency: Literal["OnClosing", "OnOpening", "ChargingPeriod", "Daily", "PerItem", "Monthly", "OnAnniversary", "Other", "PerHundredPounds", "PerHour", "PerOccurrence", "PerSheet", "PerTransaction", "PerTransactionAmount", "PerTransactionPercentage", "Quarterly", "SixMonthly", "StatementMonthly", "Weekly", "Yearly"] = Field(alias='ApplicationFrequency')

    # Fee/charge which is usually negotiable rather than a fixed amount
    negotiable_indicator: typing.Optional[bool] = Field(None, alias='NegotiableIndicator')

    # Fee Amount charged for a fee/charge (where it is charged in terms of an amount rather than a rate)
    fee_amount: typing.Optional[str] = Field(None, alias='FeeAmount')

    # Rate charged for Fee/Charge (where it is charged in terms of a rate rather than an amount)
    fee_rate: typing.Optional[str] = Field(None, alias='FeeRate')

    # Rate type for Fee/Charge (where it is charged in terms of a rate rather than an amount)
    fee_rate_type: typing.Optional[Literal["Gross", "Other"]] = Field(None, alias='FeeRateType')

    # How frequently the fee/charge is calculated
    calculation_frequency: typing.Optional[Literal["OnClosing", "OnOpening", "ChargingPeriod", "Daily", "PerItem", "Monthly", "OnAnniversary", "Other", "PerHundredPounds", "PerHour", "PerOccurrence", "PerSheet", "PerTransaction", "PerTransactionAmount", "PerTransactionPercentage", "Quarterly", "SixMonthly", "StatementMonthly", "Weekly", "Yearly"]] = Field(None, alias='CalculationFrequency')

    notes: typing.Optional[OBBCAData1OtherFeesChargesItemFeeChargeDetailItemNotes] = Field(None, alias='Notes')

    fee_charge_cap: typing.Optional[OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCap] = Field(None, alias='FeeChargeCap')

    other_fee_category_type: typing.Optional[OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeCategoryType] = Field(None, alias='OtherFeeCategoryType')

    other_fee_type: typing.Optional[OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType] = Field(None, alias='OtherFeeType')

    other_fee_rate_type: typing.Optional[OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeRateType] = Field(None, alias='OtherFeeRateType')

    other_application_frequency: typing.Optional[OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherApplicationFrequency] = Field(None, alias='OtherApplicationFrequency')

    other_calculation_frequency: typing.Optional[OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherCalculationFrequency] = Field(None, alias='OtherCalculationFrequency')

    fee_applicable_range: typing.Optional[OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange] = Field(None, alias='FeeApplicableRange')
    class Config:
        arbitrary_types_allowed = True
