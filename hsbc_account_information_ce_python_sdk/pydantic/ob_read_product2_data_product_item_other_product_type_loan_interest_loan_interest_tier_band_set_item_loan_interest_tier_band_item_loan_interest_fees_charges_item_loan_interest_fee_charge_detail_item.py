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

from hsbc_account_information_ce_python_sdk.pydantic.ob_amount13 import OBAmount13
from hsbc_account_information_ce_python_sdk.pydantic.ob_fee_frequency1_code2 import OBFeeFrequency1Code2
from hsbc_account_information_ce_python_sdk.pydantic.ob_fee_frequency1_code3 import OBFeeFrequency1Code3
from hsbc_account_information_ce_python_sdk.pydantic.ob_fee_type1_code import OBFeeType1Code
from hsbc_account_information_ce_python_sdk.pydantic.ob_interest_rate_type1_code1 import OBInterestRateType1Code1
from hsbc_account_information_ce_python_sdk.pydantic.ob_other_code_type15 import OBOtherCodeType15
from hsbc_account_information_ce_python_sdk.pydantic.ob_other_code_type16 import OBOtherCodeType16
from hsbc_account_information_ce_python_sdk.pydantic.ob_other_code_type17 import OBOtherCodeType17
from hsbc_account_information_ce_python_sdk.pydantic.ob_other_fee_charge_detail_type import OBOtherFeeChargeDetailType
from hsbc_account_information_ce_python_sdk.pydantic.ob_rate11 import OBRate11
from hsbc_account_information_ce_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item_loan_interest_fee_charge_detail_item_notes import OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeDetailItemNotes

class OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeDetailItem(BaseModel):
    fee_type: OBFeeType1Code = Field(alias='FeeType')

    application_frequency: OBFeeFrequency1Code2 = Field(alias='ApplicationFrequency')

    calculation_frequency: OBFeeFrequency1Code3 = Field(alias='CalculationFrequency')

    # Fee/charge which is usually negotiable rather than a fixed amount
    negotiable_indicator: typing.Optional[bool] = Field(None, alias='NegotiableIndicator')

    fee_amount: typing.Optional[OBAmount13] = Field(None, alias='FeeAmount')

    fee_rate: typing.Optional[OBRate11] = Field(None, alias='FeeRate')

    fee_rate_type: typing.Optional[OBInterestRateType1Code1] = Field(None, alias='FeeRateType')

    notes: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeDetailItemNotes] = Field(None, alias='Notes')

    other_fee_type: typing.Optional[OBOtherFeeChargeDetailType] = Field(None, alias='OtherFeeType')

    other_fee_rate_type: typing.Optional[OBOtherCodeType15] = Field(None, alias='OtherFeeRateType')

    other_application_frequency: typing.Optional[OBOtherCodeType16] = Field(None, alias='OtherApplicationFrequency')

    other_calculation_frequency: typing.Optional[OBOtherCodeType17] = Field(None, alias='OtherCalculationFrequency')
    class Config:
        arbitrary_types_allowed = True
