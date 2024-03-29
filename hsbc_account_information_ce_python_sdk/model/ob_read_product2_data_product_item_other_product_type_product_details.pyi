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


class OBReadProduct2DataProductItemOtherProductTypeProductDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def Segment() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeProductDetailsSegment']:
                return OBReadProduct2DataProductItemOtherProductTypeProductDetailsSegment
            FeeFreeLength = schemas.IntSchema
            
            
            class FeeFreeLengthPeriod(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PACT(cls):
                    return cls("PACT")
                
                @schemas.classproperty
                def PDAY(cls):
                    return cls("PDAY")
                
                @schemas.classproperty
                def PHYR(cls):
                    return cls("PHYR")
                
                @schemas.classproperty
                def PMTH(cls):
                    return cls("PMTH")
                
                @schemas.classproperty
                def PQTR(cls):
                    return cls("PQTR")
                
                @schemas.classproperty
                def PWEK(cls):
                    return cls("PWEK")
                
                @schemas.classproperty
                def PYER(cls):
                    return cls("PYER")
            
            
            class MonthlyMaximumCharge(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def Notes() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeProductDetailsNotes']:
                return OBReadProduct2DataProductItemOtherProductTypeProductDetailsNotes
        
            @staticmethod
            def OtherSegment() -> typing.Type['OBOtherCodeType10']:
                return OBOtherCodeType10
            __annotations__ = {
                "Segment": Segment,
                "FeeFreeLength": FeeFreeLength,
                "FeeFreeLengthPeriod": FeeFreeLengthPeriod,
                "MonthlyMaximumCharge": MonthlyMaximumCharge,
                "Notes": Notes,
                "OtherSegment": OtherSegment,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Segment"]) -> 'OBReadProduct2DataProductItemOtherProductTypeProductDetailsSegment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeFreeLength"]) -> MetaOapg.properties.FeeFreeLength: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeFreeLengthPeriod"]) -> MetaOapg.properties.FeeFreeLengthPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MonthlyMaximumCharge"]) -> MetaOapg.properties.MonthlyMaximumCharge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBReadProduct2DataProductItemOtherProductTypeProductDetailsNotes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherSegment"]) -> 'OBOtherCodeType10': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Segment", "FeeFreeLength", "FeeFreeLengthPeriod", "MonthlyMaximumCharge", "Notes", "OtherSegment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Segment"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeProductDetailsSegment', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeFreeLength"]) -> typing.Union[MetaOapg.properties.FeeFreeLength, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeFreeLengthPeriod"]) -> typing.Union[MetaOapg.properties.FeeFreeLengthPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MonthlyMaximumCharge"]) -> typing.Union[MetaOapg.properties.MonthlyMaximumCharge, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeProductDetailsNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherSegment"]) -> typing.Union['OBOtherCodeType10', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Segment", "FeeFreeLength", "FeeFreeLengthPeriod", "MonthlyMaximumCharge", "Notes", "OtherSegment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Segment: typing.Union['OBReadProduct2DataProductItemOtherProductTypeProductDetailsSegment', schemas.Unset] = schemas.unset,
        FeeFreeLength: typing.Union[MetaOapg.properties.FeeFreeLength, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        FeeFreeLengthPeriod: typing.Union[MetaOapg.properties.FeeFreeLengthPeriod, str, schemas.Unset] = schemas.unset,
        MonthlyMaximumCharge: typing.Union[MetaOapg.properties.MonthlyMaximumCharge, str, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBReadProduct2DataProductItemOtherProductTypeProductDetailsNotes', schemas.Unset] = schemas.unset,
        OtherSegment: typing.Union['OBOtherCodeType10', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadProduct2DataProductItemOtherProductTypeProductDetails':
        return super().__new__(
            cls,
            *args,
            Segment=Segment,
            FeeFreeLength=FeeFreeLength,
            FeeFreeLengthPeriod=FeeFreeLengthPeriod,
            MonthlyMaximumCharge=MonthlyMaximumCharge,
            Notes=Notes,
            OtherSegment=OtherSegment,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.ob_other_code_type10 import OBOtherCodeType10
from hsbc_account_information_ce_python_sdk.model.ob_read_product2_data_product_item_other_product_type_product_details_notes import OBReadProduct2DataProductItemOtherProductTypeProductDetailsNotes
from hsbc_account_information_ce_python_sdk.model.ob_read_product2_data_product_item_other_product_type_product_details_segment import OBReadProduct2DataProductItemOtherProductTypeProductDetailsSegment
