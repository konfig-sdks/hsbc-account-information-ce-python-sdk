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


class OBTransactionCardInstrument1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Set of elements to describe the card instrument used in the transaction.
    """


    class MetaOapg:
        required = {
            "CardSchemeName",
        }
        
        class properties:
            
            
            class CardSchemeName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AMERICAN_EXPRESS(cls):
                    return cls("AmericanExpress")
                
                @schemas.classproperty
                def DINERS(cls):
                    return cls("Diners")
                
                @schemas.classproperty
                def DISCOVER(cls):
                    return cls("Discover")
                
                @schemas.classproperty
                def MASTER_CARD(cls):
                    return cls("MasterCard")
                
                @schemas.classproperty
                def VISA(cls):
                    return cls("VISA")
            
            
            class AuthorisationType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CONSUMER_DEVICE(cls):
                    return cls("ConsumerDevice")
                
                @schemas.classproperty
                def CONTACTLESS(cls):
                    return cls("Contactless")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("None")
                
                @schemas.classproperty
                def PIN(cls):
                    return cls("PIN")
            
            
            class Name(
                schemas.StrSchema
            ):
                pass
            
            
            class Identification(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "CardSchemeName": CardSchemeName,
                "AuthorisationType": AuthorisationType,
                "Name": Name,
                "Identification": Identification,
            }
    
    CardSchemeName: MetaOapg.properties.CardSchemeName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CardSchemeName"]) -> MetaOapg.properties.CardSchemeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AuthorisationType"]) -> MetaOapg.properties.AuthorisationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Identification"]) -> MetaOapg.properties.Identification: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["CardSchemeName", "AuthorisationType", "Name", "Identification", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CardSchemeName"]) -> MetaOapg.properties.CardSchemeName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AuthorisationType"]) -> typing.Union[MetaOapg.properties.AuthorisationType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Identification"]) -> typing.Union[MetaOapg.properties.Identification, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["CardSchemeName", "AuthorisationType", "Name", "Identification", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        CardSchemeName: typing.Union[MetaOapg.properties.CardSchemeName, str, ],
        AuthorisationType: typing.Union[MetaOapg.properties.AuthorisationType, str, schemas.Unset] = schemas.unset,
        Name: typing.Union[MetaOapg.properties.Name, str, schemas.Unset] = schemas.unset,
        Identification: typing.Union[MetaOapg.properties.Identification, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBTransactionCardInstrument1':
        return super().__new__(
            cls,
            *args,
            CardSchemeName=CardSchemeName,
            AuthorisationType=AuthorisationType,
            Name=Name,
            Identification=Identification,
            _configuration=_configuration,
            **kwargs,
        )
