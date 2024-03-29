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


class OBPCAData1ProductDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def Segment() -> typing.Type['OBPCAData1ProductDetailsSegment']:
                return OBPCAData1ProductDetailsSegment
            
            
            class MonthlyMaximumCharge(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^(-?\d{1,14}){1}(\.\d{1,4}){0,1}$',
                    }]
        
            @staticmethod
            def Notes() -> typing.Type['OBPCAData1ProductDetailsNotes']:
                return OBPCAData1ProductDetailsNotes
            __annotations__ = {
                "Segment": Segment,
                "MonthlyMaximumCharge": MonthlyMaximumCharge,
                "Notes": Notes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Segment"]) -> 'OBPCAData1ProductDetailsSegment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MonthlyMaximumCharge"]) -> MetaOapg.properties.MonthlyMaximumCharge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBPCAData1ProductDetailsNotes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Segment", "MonthlyMaximumCharge", "Notes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Segment"]) -> typing.Union['OBPCAData1ProductDetailsSegment', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MonthlyMaximumCharge"]) -> typing.Union[MetaOapg.properties.MonthlyMaximumCharge, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBPCAData1ProductDetailsNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Segment", "MonthlyMaximumCharge", "Notes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Segment: typing.Union['OBPCAData1ProductDetailsSegment', schemas.Unset] = schemas.unset,
        MonthlyMaximumCharge: typing.Union[MetaOapg.properties.MonthlyMaximumCharge, str, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBPCAData1ProductDetailsNotes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBPCAData1ProductDetails':
        return super().__new__(
            cls,
            *args,
            Segment=Segment,
            MonthlyMaximumCharge=MonthlyMaximumCharge,
            Notes=Notes,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.obpca_data1_product_details_notes import OBPCAData1ProductDetailsNotes
from hsbc_account_information_ce_python_sdk.model.obpca_data1_product_details_segment import OBPCAData1ProductDetailsSegment
