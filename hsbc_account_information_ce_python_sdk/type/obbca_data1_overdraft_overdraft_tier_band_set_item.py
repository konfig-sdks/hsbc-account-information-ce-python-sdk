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

from hsbc_account_information_ce_python_sdk.type.obbca_data1_overdraft_overdraft_tier_band_set_item_notes import OBBCAData1OverdraftOverdraftTierBandSetItemNotes
from hsbc_account_information_ce_python_sdk.type.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesCharges
from hsbc_account_information_ce_python_sdk.type.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBand

class RequiredOBBCAData1OverdraftOverdraftTierBandSetItem(TypedDict):
    # The methodology of how overdraft is charged. It can be: 'Whole'  Where the same charge/rate is applied to the entirety of the overdraft balance (where charges are applicable).  'Tiered' Where different charges/rates are applied dependent on overdraft maximum and minimum balance amount tiers defined by the lending financial organisation 'Banded' Where different charges/rates are applied dependent on overdraft maximum and minimum balance amount bands defined by a government organisation.
    TierBandMethod: str

    OverdraftTierBand: OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBand

class OptionalOBBCAData1OverdraftOverdraftTierBandSetItem(TypedDict, total=False):
    # An overdraft can either be 'committed' which means that the facility cannot be withdrawn without reasonable notification before it's agreed end date, or 'on demand' which means that the financial institution can demand repayment at any point in time.
    OverdraftType: str

    # Unique and unambiguous identification of a  Tier Band for a overdraft product.
    Identification: str

    # Indicates if the Overdraft is authorised (Y) or unauthorised (N)
    AuthorisedIndicator: bool

    # When a customer exceeds their credit limit, a financial institution will not charge the customer unauthorised overdraft charges if they do not exceed by more than the buffer amount. Note: Authorised overdraft charges may still apply.
    BufferAmount: str

    Notes: OBBCAData1OverdraftOverdraftTierBandSetItemNotes

    OverdraftFeesCharges: OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesCharges

class OBBCAData1OverdraftOverdraftTierBandSetItem(RequiredOBBCAData1OverdraftOverdraftTierBandSetItem, OptionalOBBCAData1OverdraftOverdraftTierBandSetItem):
    pass
