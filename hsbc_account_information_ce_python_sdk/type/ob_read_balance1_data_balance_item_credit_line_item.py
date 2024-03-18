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

from hsbc_account_information_ce_python_sdk.type.ob_read_balance1_data_balance_item_credit_line_item_amount import OBReadBalance1DataBalanceItemCreditLineItemAmount

class RequiredOBReadBalance1DataBalanceItemCreditLineItem(TypedDict):
    # Indicates whether or not the credit line is included in the balance of the account. Usage: If not present, credit line is not included in the balance amount of the account.
    Included: bool

class OptionalOBReadBalance1DataBalanceItemCreditLineItem(TypedDict, total=False):
    # Limit type, in a coded form.
    Type: str

    Amount: OBReadBalance1DataBalanceItemCreditLineItemAmount

class OBReadBalance1DataBalanceItemCreditLineItem(RequiredOBReadBalance1DataBalanceItemCreditLineItem, OptionalOBReadBalance1DataBalanceItemCreditLineItem):
    pass
