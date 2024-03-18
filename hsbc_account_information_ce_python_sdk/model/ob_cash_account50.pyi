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


class OBCashAccount50(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Provides the details to identify the beneficiary account.
    """


    class MetaOapg:
        required = {
            "Identification",
            "SchemeName",
        }
        
        class properties:
            
            
            class SchemeName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BBAN(cls):
                    return cls("UK.OBIE.BBAN")
                
                @schemas.classproperty
                def IBAN(cls):
                    return cls("UK.OBIE.IBAN")
                
                @schemas.classproperty
                def PAN(cls):
                    return cls("UK.OBIE.PAN")
                
                @schemas.classproperty
                def PAYM(cls):
                    return cls("UK.OBIE.Paym")
                
                @schemas.classproperty
                def SORT_CODE_ACCOUNT_NUMBER(cls):
                    return cls("UK.OBIE.SortCodeAccountNumber")
                
                @schemas.classproperty
                def WALLET(cls):
                    return cls("UK.OBIE.Wallet")
        
            @staticmethod
            def Identification() -> typing.Type['Identification0']:
                return Identification0
        
            @staticmethod
            def Name() -> typing.Type['Name0']:
                return Name0
        
            @staticmethod
            def SecondaryIdentification() -> typing.Type['SecondaryIdentification']:
                return SecondaryIdentification
            __annotations__ = {
                "SchemeName": SchemeName,
                "Identification": Identification,
                "Name": Name,
                "SecondaryIdentification": SecondaryIdentification,
            }
    
    Identification: 'Identification0'
    SchemeName: MetaOapg.properties.SchemeName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SchemeName"]) -> MetaOapg.properties.SchemeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Identification"]) -> 'Identification0': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> 'Name0': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SecondaryIdentification"]) -> 'SecondaryIdentification': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["SchemeName", "Identification", "Name", "SecondaryIdentification", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SchemeName"]) -> MetaOapg.properties.SchemeName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Identification"]) -> 'Identification0': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union['Name0', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SecondaryIdentification"]) -> typing.Union['SecondaryIdentification', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["SchemeName", "Identification", "Name", "SecondaryIdentification", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Identification: 'Identification0',
        SchemeName: typing.Union[MetaOapg.properties.SchemeName, str, ],
        Name: typing.Union['Name0', schemas.Unset] = schemas.unset,
        SecondaryIdentification: typing.Union['SecondaryIdentification', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBCashAccount50':
        return super().__new__(
            cls,
            *args,
            Identification=Identification,
            SchemeName=SchemeName,
            Name=Name,
            SecondaryIdentification=SecondaryIdentification,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.identification0 import Identification0
from hsbc_account_information_ce_python_sdk.model.name0 import Name0
from hsbc_account_information_ce_python_sdk.model.secondary_identification import SecondaryIdentification
