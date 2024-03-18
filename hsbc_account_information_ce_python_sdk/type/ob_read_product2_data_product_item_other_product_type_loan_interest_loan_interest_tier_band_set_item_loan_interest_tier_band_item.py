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

from hsbc_account_information_ce_python_sdk.type.ob_interest_fixed_variable_type1_code import OBInterestFixedVariableType1Code
from hsbc_account_information_ce_python_sdk.type.ob_read_product2_data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges import OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesCharges
from hsbc_account_information_ce_python_sdk.type.ob_read_product2_data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_notes import OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemNotes
from hsbc_account_information_ce_python_sdk.type.ob_read_product2_data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_other_loan_provider_interest_rate_type import OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemOtherLoanProviderInterestRateType

class RequiredOBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem(TypedDict):
    # Minimum loan value for which the loan interest tier applies.
    TierValueMinimum: str

    # Minimum loan term for which the loan interest tier applies.
    TierValueMinTerm: int

    # The unit of period (days, weeks, months etc.) of the Minimum Term
    MinTermPeriod: str

    FixedVariableInterestRateType: OBInterestFixedVariableType1Code

    # The annual equivalent rate (AER) is interest that is calculated under the assumption that any interest paid is combined with the original balance and the next interest payment will be based on the slightly higher account balance. Overall, this means that interest can be compounded several times in a year depending on the number of times that interest payments are made.  For SME Loan, this APR is the representative APR which includes any account fees.
    RepAPR: str

class OptionalOBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem(TypedDict, total=False):
    # Unique and unambiguous identification of a  Tier Band for a SME Loan.
    Identification: str

    # Maximum loan value for which the loan interest tier applies.
    TierValueMaximum: str

    # Maximum loan term for which the loan interest tier applies.
    TierValueMaxTerm: int

    # The unit of period (days, weeks, months etc.) of the Maximum Term
    MaxTermPeriod: str

    # Interest rate types, other than APR, which financial institutions may use to describe the annual interest rate payable for the SME Loan.
    LoanProviderInterestRateType: str

    # Loan provider Interest for the SME Loan product
    LoanProviderInterestRate: str

    Notes: OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemNotes

    OtherLoanProviderInterestRateType: OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemOtherLoanProviderInterestRateType

    LoanInterestFeesCharges: OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesCharges

class OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem(RequiredOBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem, OptionalOBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem):
    pass
