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


class OBExternalAccountRole1Code(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A party’s role with respect to the related account.
    """


    class MetaOapg:
        enum_value_to_name = {
            "UK.OBIE.Administrator": "ADMINISTRATOR",
            "UK.OBIE.Beneficiary": "BENEFICIARY",
            "UK.OBIE.CustodianForMinor": "CUSTODIAN_FOR_MINOR",
            "UK.OBIE.Granter": "GRANTER",
            "UK.OBIE.LegalGuardian": "LEGAL_GUARDIAN",
            "UK.OBIE.OtherParty": "OTHER_PARTY",
            "UK.OBIE.PowerOfAttorney": "POWER_OF_ATTORNEY",
            "UK.OBIE.Principal": "PRINCIPAL",
            "UK.OBIE.Protector": "PROTECTOR",
            "UK.OBIE.RegisteredShareholderName": "REGISTERED_SHAREHOLDER_NAME",
            "UK.OBIE.SecondaryOwner": "SECONDARY_OWNER",
            "UK.OBIE.SeniorManagingOfficial": "SENIOR_MANAGING_OFFICIAL",
            "UK.OBIE.Settlor": "SETTLOR",
            "UK.OBIE.SuccessorOnDeath": "SUCCESSOR_ON_DEATH",
        }
    
    @schemas.classproperty
    def ADMINISTRATOR(cls):
        return cls("UK.OBIE.Administrator")
    
    @schemas.classproperty
    def BENEFICIARY(cls):
        return cls("UK.OBIE.Beneficiary")
    
    @schemas.classproperty
    def CUSTODIAN_FOR_MINOR(cls):
        return cls("UK.OBIE.CustodianForMinor")
    
    @schemas.classproperty
    def GRANTER(cls):
        return cls("UK.OBIE.Granter")
    
    @schemas.classproperty
    def LEGAL_GUARDIAN(cls):
        return cls("UK.OBIE.LegalGuardian")
    
    @schemas.classproperty
    def OTHER_PARTY(cls):
        return cls("UK.OBIE.OtherParty")
    
    @schemas.classproperty
    def POWER_OF_ATTORNEY(cls):
        return cls("UK.OBIE.PowerOfAttorney")
    
    @schemas.classproperty
    def PRINCIPAL(cls):
        return cls("UK.OBIE.Principal")
    
    @schemas.classproperty
    def PROTECTOR(cls):
        return cls("UK.OBIE.Protector")
    
    @schemas.classproperty
    def REGISTERED_SHAREHOLDER_NAME(cls):
        return cls("UK.OBIE.RegisteredShareholderName")
    
    @schemas.classproperty
    def SECONDARY_OWNER(cls):
        return cls("UK.OBIE.SecondaryOwner")
    
    @schemas.classproperty
    def SENIOR_MANAGING_OFFICIAL(cls):
        return cls("UK.OBIE.SeniorManagingOfficial")
    
    @schemas.classproperty
    def SETTLOR(cls):
        return cls("UK.OBIE.Settlor")
    
    @schemas.classproperty
    def SUCCESSOR_ON_DEATH(cls):
        return cls("UK.OBIE.SuccessorOnDeath")
