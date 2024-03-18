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


class OBFeeFrequency1Code1(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    How often is the overdraft fee/charge calculated for the account.
    """


    class MetaOapg:
        enum_value_to_name = {
            "FEAC": "FEAC",
            "FEAO": "FEAO",
            "FECP": "FECP",
            "FEDA": "FEDA",
            "FEHO": "FEHO",
            "FEI": "FEI",
            "FEMO": "FEMO",
            "FEOA": "FEOA",
            "FEOT": "FEOT",
            "FEPC": "FEPC",
            "FEPH": "FEPH",
            "FEPO": "FEPO",
            "FEPS": "FEPS",
            "FEPT": "FEPT",
            "FEPTA": "FEPTA",
            "FEPTP": "FEPTP",
            "FEQU": "FEQU",
            "FESM": "FESM",
            "FEST": "FEST",
            "FEWE": "FEWE",
            "FEYE": "FEYE",
        }
    
    @schemas.classproperty
    def FEAC(cls):
        return cls("FEAC")
    
    @schemas.classproperty
    def FEAO(cls):
        return cls("FEAO")
    
    @schemas.classproperty
    def FECP(cls):
        return cls("FECP")
    
    @schemas.classproperty
    def FEDA(cls):
        return cls("FEDA")
    
    @schemas.classproperty
    def FEHO(cls):
        return cls("FEHO")
    
    @schemas.classproperty
    def FEI(cls):
        return cls("FEI")
    
    @schemas.classproperty
    def FEMO(cls):
        return cls("FEMO")
    
    @schemas.classproperty
    def FEOA(cls):
        return cls("FEOA")
    
    @schemas.classproperty
    def FEOT(cls):
        return cls("FEOT")
    
    @schemas.classproperty
    def FEPC(cls):
        return cls("FEPC")
    
    @schemas.classproperty
    def FEPH(cls):
        return cls("FEPH")
    
    @schemas.classproperty
    def FEPO(cls):
        return cls("FEPO")
    
    @schemas.classproperty
    def FEPS(cls):
        return cls("FEPS")
    
    @schemas.classproperty
    def FEPT(cls):
        return cls("FEPT")
    
    @schemas.classproperty
    def FEPTA(cls):
        return cls("FEPTA")
    
    @schemas.classproperty
    def FEPTP(cls):
        return cls("FEPTP")
    
    @schemas.classproperty
    def FEQU(cls):
        return cls("FEQU")
    
    @schemas.classproperty
    def FESM(cls):
        return cls("FESM")
    
    @schemas.classproperty
    def FEST(cls):
        return cls("FEST")
    
    @schemas.classproperty
    def FEWE(cls):
        return cls("FEWE")
    
    @schemas.classproperty
    def FEYE(cls):
        return cls("FEYE")