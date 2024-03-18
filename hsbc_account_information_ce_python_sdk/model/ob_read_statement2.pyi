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


class OBReadStatement2(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "Data",
        }
        
        class properties:
        
            @staticmethod
            def Data() -> typing.Type['OBReadDataStatement2']:
                return OBReadDataStatement2
        
            @staticmethod
            def Links() -> typing.Type['Links']:
                return Links
        
            @staticmethod
            def Meta() -> typing.Type['Meta']:
                return Meta
            __annotations__ = {
                "Data": Data,
                "Links": Links,
                "Meta": Meta,
            }
    
    Data: 'OBReadDataStatement2'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Data"]) -> 'OBReadDataStatement2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Links"]) -> 'Links': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Meta"]) -> 'Meta': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Data", "Links", "Meta", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Data"]) -> 'OBReadDataStatement2': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Links"]) -> typing.Union['Links', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Meta"]) -> typing.Union['Meta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Data", "Links", "Meta", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Data: 'OBReadDataStatement2',
        Links: typing.Union['Links', schemas.Unset] = schemas.unset,
        Meta: typing.Union['Meta', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadStatement2':
        return super().__new__(
            cls,
            *args,
            Data=Data,
            Links=Links,
            Meta=Meta,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.links import Links
from hsbc_account_information_ce_python_sdk.model.meta import Meta
from hsbc_account_information_ce_python_sdk.model.ob_read_data_statement2 import OBReadDataStatement2
