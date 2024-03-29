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

from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_notes import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes
from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency
from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency
from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType
from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType
from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap

class OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem(BaseModel):
    # Overdraft fee type
    fee_type: Literal["ArrangedOverdraft", "AnnualReview", "EmergencyBorrowing", "BorrowingItem", "OverdraftRenewal", "OverdraftSetup", "Surcharge", "TempOverdraft", "UnauthorisedBorrowing", "UnauthorisedPaidTrans", "Other", "UnauthorisedUnpaidTrans"] = Field(alias='FeeType')

    # Frequency at which the overdraft charge is applied to the account
    application_frequency: Literal["OnClosing", "OnOpening", "ChargingPeriod", "Daily", "PerItem", "Monthly", "OnAnniversary", "Other", "PerHundredPounds", "PerHour", "PerOccurrence", "PerSheet", "PerTransaction", "PerTransactionAmount", "PerTransactionPercentage", "Quarterly", "SixMonthly", "StatementMonthly", "Weekly", "Yearly"] = Field(alias='ApplicationFrequency')

    # Indicates whether fee and charges are negotiable
    negotiable_indicator: typing.Optional[bool] = Field(None, alias='NegotiableIndicator')

    # Indicates if the fee/charge is already covered by an 'Overdraft Control' fee or not.
    overdraft_control_indicator: typing.Optional[bool] = Field(None, alias='OverdraftControlIndicator')

    # Every additional tranche of an overdraft balance to which an overdraft fee is applied
    incremental_borrowing_amount: typing.Optional[str] = Field(None, alias='IncrementalBorrowingAmount')

    # Amount charged for an overdraft fee/charge (where it is charged in terms of an amount rather than a rate)
    fee_amount: typing.Optional[str] = Field(None, alias='FeeAmount')

    # Rate charged for overdraft fee/charge (where it is charged in terms of a rate rather than an amount)
    fee_rate: typing.Optional[str] = Field(None, alias='FeeRate')

    # Rate type for overdraft fee/charge (where it is charged in terms of a rate rather than an amount)
    fee_rate_type: typing.Optional[Literal["Gross", "Other"]] = Field(None, alias='FeeRateType')

    # How often is the overdraft fee/charge calculated for the account.
    calculation_frequency: typing.Optional[Literal["OnClosing", "OnOpening", "ChargingPeriod", "Daily", "PerItem", "Monthly", "OnAnniversary", "Other", "PerHundredPounds", "PerHour", "PerOccurrence", "PerSheet", "PerTransaction", "PerTransactionAmount", "PerTransactionPercentage", "Quarterly", "SixMonthly", "StatementMonthly", "Weekly", "Yearly"]] = Field(None, alias='CalculationFrequency')

    notes: typing.Optional[OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes] = Field(None, alias='Notes')

    overdraft_fee_charge_cap: typing.Optional[OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap] = Field(None, alias='OverdraftFeeChargeCap')

    other_fee_type: typing.Optional[OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType] = Field(None, alias='OtherFeeType')

    other_fee_rate_type: typing.Optional[OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType] = Field(None, alias='OtherFeeRateType')

    other_application_frequency: typing.Optional[OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency] = Field(None, alias='OtherApplicationFrequency')

    other_calculation_frequency: typing.Optional[OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency] = Field(None, alias='OtherCalculationFrequency')
    class Config:
        arbitrary_types_allowed = True
