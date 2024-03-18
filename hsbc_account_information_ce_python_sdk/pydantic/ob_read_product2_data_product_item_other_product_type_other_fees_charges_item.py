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

from hsbc_account_information_ce_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_other_fees_charges_item_fee_charge_cap import OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCap
from hsbc_account_information_ce_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail import OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetail
from hsbc_account_information_ce_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_other_fees_charges_item_other_tariff_type import OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemOtherTariffType

class OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItem(BaseModel):
    fee_charge_detail: OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetail = Field(alias='FeeChargeDetail')

    # TariffType which defines the fee and charges.
    tariff_type: typing.Optional[Literal["TTEL", "TTMX", "TTOT"]] = Field(None, alias='TariffType')

    # Name of the tariff
    tariff_name: typing.Optional[str] = Field(None, alias='TariffName')

    other_tariff_type: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemOtherTariffType] = Field(None, alias='OtherTariffType')

    fee_charge_cap: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCap] = Field(None, alias='FeeChargeCap')
    class Config:
        arbitrary_types_allowed = True
