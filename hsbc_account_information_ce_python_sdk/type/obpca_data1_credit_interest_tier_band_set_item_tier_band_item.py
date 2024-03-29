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

from hsbc_account_information_ce_python_sdk.type.obpca_data1_credit_interest_tier_band_set_item_tier_band_item_notes import OBPCAData1CreditInterestTierBandSetItemTierBandItemNotes
from hsbc_account_information_ce_python_sdk.type.obpca_data1_credit_interest_tier_band_set_item_tier_band_item_other_application_frequency import OBPCAData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency
from hsbc_account_information_ce_python_sdk.type.obpca_data1_credit_interest_tier_band_set_item_tier_band_item_other_bank_interest_type import OBPCAData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType
from hsbc_account_information_ce_python_sdk.type.obpca_data1_credit_interest_tier_band_set_item_tier_band_item_other_calculation_frequency import OBPCAData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency

class RequiredOBPCAData1CreditInterestTierBandSetItemTierBandItem(TypedDict):
    # Minimum deposit value for which the credit interest tier applies.
    TierValueMinimum: str

    # How often is interest applied to the PCA for this tier/band i.e. how often the financial institution pays accumulated interest to the customer's PCA.
    ApplicationFrequency: str

    # Type of interest rate, Fixed or Variable
    FixedVariableInterestRateType: str

    # The annual equivalent rate (AER) is interest that is calculated under the assumption that any interest paid is combined with the original balance and the next interest payment will be based on the slightly higher account balance. Overall, this means that interest can be compounded several times in a year depending on the number of times that interest payments are made.   Read more: Annual Equivalent Rate (AER) http://www.investopedia.com/terms/a/aer.asp#ixzz4gfR7IO1A
    AER: str

class OptionalOBPCAData1CreditInterestTierBandSetItemTierBandItem(TypedDict, total=False):
    # Unique and unambiguous identification of a  Tier Band for a PCA.
    Identification: str

    # Maximum deposit value for which the credit interest tier applies.
    TierValueMaximum: str

    # How often is credit interest calculated for the account.
    CalculationFrequency: str

    # Amount on which Interest applied.
    DepositInterestAppliedCoverage: str

    # Interest rate types, other than AER, which financial institutions may use to describe the annual interest rate payable to the PCA.
    BankInterestRateType: str

    # Bank Interest for the PCA product
    BankInterestRate: str

    Notes: OBPCAData1CreditInterestTierBandSetItemTierBandItemNotes

    OtherBankInterestType: OBPCAData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType

    OtherApplicationFrequency: OBPCAData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency

    OtherCalculationFrequency: OBPCAData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency

class OBPCAData1CreditInterestTierBandSetItemTierBandItem(RequiredOBPCAData1CreditInterestTierBandSetItemTierBandItem, OptionalOBPCAData1CreditInterestTierBandSetItemTierBandItem):
    pass
