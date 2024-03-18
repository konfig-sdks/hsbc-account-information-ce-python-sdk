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

from hsbc_account_information_ce_python_sdk.type.ob_amount14 import OBAmount14
from hsbc_account_information_ce_python_sdk.type.ob_min_max_type1_code import OBMinMaxType1Code
from hsbc_account_information_ce_python_sdk.type.ob_period1_code import OBPeriod1Code
from hsbc_account_information_ce_python_sdk.type.ob_read_product2_data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_cap_item_fee_type import OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemFeeType
from hsbc_account_information_ce_python_sdk.type.ob_read_product2_data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_cap_item_notes import OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemNotes
from hsbc_account_information_ce_python_sdk.type.ob_read_product2_data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_cap_item_other_fee_type import OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemOtherFeeType

class RequiredOBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItem(TypedDict):
    FeeType: OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemFeeType

    MinMaxType: OBMinMaxType1Code

class OptionalOBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItem(TypedDict, total=False):
    # fee/charges are captured dependent on the number of occurrences rather than capped at a particular amount
    FeeCapOccurrence: int

    FeeCapAmount: OBAmount14

    CappingPeriod: OBPeriod1Code

    Notes: OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemNotes

    OtherFeeType: OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemOtherFeeType

class OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItem(RequiredOBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItem, OptionalOBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItem):
    pass
