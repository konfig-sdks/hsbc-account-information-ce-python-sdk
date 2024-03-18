# coding: utf-8

"""
    Account Information API

    In this document, you'll find the steps your organization needs to take to use our API services. Included in this guide are details of request and response messages used to support your organization’s integration. The intended audience for this document are **Technical Architects**, **Development Engineers**, **Test Engineers**, and **Operation & Maintenance Engineers** involved in development and support of your organization’s integration. Setting up our API Services is best completed with the assistance of your organization’s IT team, or someone with experience and knowledge of application programming interfaces. This should include experience with **JSON payloads**, **security** and **public key infrastructure (PKI)**. This Document describes the following request and response structure of HSBCnet - Account Information API. For detail implementation guidelines, please refer to the respective section from [develop.hsbc.com](https://develop.hsbc.com/ob-api-documentation/account-information-uk-personal-v319) 

    The version of the OpenAPI document: 3.1.11
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from hsbc_account_information_ce_python_sdk import schemas  # noqa: F401


class OBExternalAccountSubType1Code(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Specifies the sub type of account (product family group).
    """
    
    @schemas.classproperty
    def CHARGE_CARD(cls):
        return cls("ChargeCard")
    
    @schemas.classproperty
    def CREDIT_CARD(cls):
        return cls("CreditCard")
    
    @schemas.classproperty
    def CURRENT_ACCOUNT(cls):
        return cls("CurrentAccount")
    
    @schemas.classproperty
    def EMONEY(cls):
        return cls("EMoney")
    
    @schemas.classproperty
    def LOAN(cls):
        return cls("Loan")
    
    @schemas.classproperty
    def MORTGAGE(cls):
        return cls("Mortgage")
    
    @schemas.classproperty
    def PRE_PAID_CARD(cls):
        return cls("PrePaidCard")
    
    @schemas.classproperty
    def SAVINGS(cls):
        return cls("Savings")