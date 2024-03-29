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

from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_notes import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes
from hsbc_account_information_ce_python_sdk.pydantic.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges

class OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem(BaseModel):
    # Minimum value of Overdraft Tier/Band
    tier_value_min: str = Field(alias='TierValueMin')

    # Unique and unambiguous identification of a  Tier Band for a overdraft.
    identification: typing.Optional[str] = Field(None, alias='Identification')

    # Maximum value of Overdraft Tier/Band
    tier_value_max: typing.Optional[str] = Field(None, alias='TierValueMax')

    # EAR means Effective Annual Rate and/or Equivalent Annual Rate (frequently used interchangeably), being the actual annual interest rate of an Overdraft.
    e_a_r: typing.Optional[str] = Field(None, alias='EAR')

    # An annual percentage rate (APR) is the annual rate charged for borrowing or earned through an investment. APR is expressed as a percentage that represents the actual yearly cost of funds over the term of a loan. This includes any fees or additional costs associated with the transaction but does not take compounding into account.
    representative_a_p_r: typing.Optional[str] = Field(None, alias='RepresentativeAPR')

    # Specifies the minimum length of a band for a fixed overdraft agreement
    agreement_length_min: typing.Optional[typing.Union[int, float]] = Field(None, alias='AgreementLengthMin')

    # Specifies the maximum length of a band for a fixed overdraft agreement
    agreement_length_max: typing.Optional[typing.Union[int, float]] = Field(None, alias='AgreementLengthMax')

    # Specifies the period of a fixed length overdraft agreement
    agreement_period: typing.Optional[Literal["Day", "Half Year", "Month", "Quarter", "Week", "Year"]] = Field(None, alias='AgreementPeriod')

    # Refers to which interest rate is applied when interests are tiered. For example, if an overdraft balance is £2k and the interest tiers are:- 0-£500 0.1%, 500-1000 0.2%, 1000-10000 0.5%, then the applicable interest rate could either be 0.5% of the entire balance (since the account balance sits in the top interest tier) or (0.1%*500)+(0.2%*500)+(0.5%*1000). In the 1st situation, we say the interest is applied to the ‘Whole’ of the account balance,  and in the 2nd that it is ‘Tiered’.
    overdraft_interest_charging_coverage: typing.Optional[Literal["Banded", "Tiered", "Whole"]] = Field(None, alias='OverdraftInterestChargingCoverage')

    # Indicates whether the advertised overdraft rate is guaranteed to be offered to a borrower by the bank e.g. if it’s part of a government scheme, or whether the rate may vary dependent on the applicant’s circumstances.
    bank_guaranteed_indicator: typing.Optional[bool] = Field(None, alias='BankGuaranteedIndicator')

    notes: typing.Optional[OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes] = Field(None, alias='Notes')

    overdraft_fees_charges: typing.Optional[OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges] = Field(None, alias='OverdraftFeesCharges')
    class Config:
        arbitrary_types_allowed = True
