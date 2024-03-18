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

from hsbc_account_information_ce_python_sdk.pydantic.identification1 import Identification1
from hsbc_account_information_ce_python_sdk.pydantic.name1 import Name1
from hsbc_account_information_ce_python_sdk.pydantic.ob_external_financial_institution_identification4_code import OBExternalFinancialInstitutionIdentification4Code
from hsbc_account_information_ce_python_sdk.pydantic.ob_postal_address6 import OBPostalAddress6

class OBBranchAndFinancialInstitutionIdentification60(BaseModel):
    scheme_name: typing.Optional[OBExternalFinancialInstitutionIdentification4Code] = Field(None, alias='SchemeName')

    identification: typing.Optional[Identification1] = Field(None, alias='Identification')

    name: typing.Optional[Name1] = Field(None, alias='Name')

    postal_address: typing.Optional[OBPostalAddress6] = Field(None, alias='PostalAddress')
    class Config:
        arbitrary_types_allowed = True
