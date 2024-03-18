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

from hsbc_account_information_ce_python_sdk.type.account_id import AccountId
from hsbc_account_information_ce_python_sdk.type.ob_read_product2_data_product_item_other_product_type import OBReadProduct2DataProductItemOtherProductType
from hsbc_account_information_ce_python_sdk.type.obbca_data1 import OBBCAData1
from hsbc_account_information_ce_python_sdk.type.obpca_data1 import OBPCAData1

class RequiredOBReadProduct2DataProductItem(TypedDict):
    AccountId: AccountId

    # Product type : Personal Current Account, Business Current Account
    ProductType: str

class OptionalOBReadProduct2DataProductItem(TypedDict, total=False):
    # The name of the Product used for marketing purposes from a customer perspective. I.e. what the customer would recognise.
    ProductName: str

    # The unique ID that has been internally assigned by the financial institution to each of the current account banking products they market to their retail and/or small to medium enterprise (SME) customers.
    ProductId: str

    # Any secondary Identification which  supports Product Identifier to uniquely identify the current account banking products.
    SecondaryProductId: str

    # Unique and unambiguous identification of a  Product Marketing State.
    MarketingStateId: str

    OtherProductType: OBReadProduct2DataProductItemOtherProductType

    BCA: OBBCAData1

    PCA: OBPCAData1

class OBReadProduct2DataProductItem(RequiredOBReadProduct2DataProductItem, OptionalOBReadProduct2DataProductItem):
    pass