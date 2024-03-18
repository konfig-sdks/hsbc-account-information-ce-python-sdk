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


class OBPostalAddress6(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Information that locates and identifies a specific address, as defined by postal services.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def AddressType() -> typing.Type['OBAddressTypeCode']:
                return OBAddressTypeCode
            
            
            class Department(
                schemas.StrSchema
            ):
                pass
            
            
            class SubDepartment(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def StreetName() -> typing.Type['StreetName']:
                return StreetName
        
            @staticmethod
            def BuildingNumber() -> typing.Type['BuildingNumber']:
                return BuildingNumber
        
            @staticmethod
            def PostCode() -> typing.Type['PostCode']:
                return PostCode
        
            @staticmethod
            def TownName() -> typing.Type['TownName']:
                return TownName
            
            
            class CountrySubDivision(
                schemas.StrSchema
            ):
                pass
            
            
            class Country(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def AddressLine() -> typing.Type['OBPostalAddress6AddressLine']:
                return OBPostalAddress6AddressLine
            __annotations__ = {
                "AddressType": AddressType,
                "Department": Department,
                "SubDepartment": SubDepartment,
                "StreetName": StreetName,
                "BuildingNumber": BuildingNumber,
                "PostCode": PostCode,
                "TownName": TownName,
                "CountrySubDivision": CountrySubDivision,
                "Country": Country,
                "AddressLine": AddressLine,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AddressType"]) -> 'OBAddressTypeCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Department"]) -> MetaOapg.properties.Department: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SubDepartment"]) -> MetaOapg.properties.SubDepartment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StreetName"]) -> 'StreetName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BuildingNumber"]) -> 'BuildingNumber': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PostCode"]) -> 'PostCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TownName"]) -> 'TownName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CountrySubDivision"]) -> MetaOapg.properties.CountrySubDivision: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Country"]) -> MetaOapg.properties.Country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AddressLine"]) -> 'OBPostalAddress6AddressLine': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AddressType", "Department", "SubDepartment", "StreetName", "BuildingNumber", "PostCode", "TownName", "CountrySubDivision", "Country", "AddressLine", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AddressType"]) -> typing.Union['OBAddressTypeCode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Department"]) -> typing.Union[MetaOapg.properties.Department, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SubDepartment"]) -> typing.Union[MetaOapg.properties.SubDepartment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StreetName"]) -> typing.Union['StreetName', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BuildingNumber"]) -> typing.Union['BuildingNumber', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PostCode"]) -> typing.Union['PostCode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TownName"]) -> typing.Union['TownName', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CountrySubDivision"]) -> typing.Union[MetaOapg.properties.CountrySubDivision, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Country"]) -> typing.Union[MetaOapg.properties.Country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AddressLine"]) -> typing.Union['OBPostalAddress6AddressLine', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AddressType", "Department", "SubDepartment", "StreetName", "BuildingNumber", "PostCode", "TownName", "CountrySubDivision", "Country", "AddressLine", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        AddressType: typing.Union['OBAddressTypeCode', schemas.Unset] = schemas.unset,
        Department: typing.Union[MetaOapg.properties.Department, str, schemas.Unset] = schemas.unset,
        SubDepartment: typing.Union[MetaOapg.properties.SubDepartment, str, schemas.Unset] = schemas.unset,
        StreetName: typing.Union['StreetName', schemas.Unset] = schemas.unset,
        BuildingNumber: typing.Union['BuildingNumber', schemas.Unset] = schemas.unset,
        PostCode: typing.Union['PostCode', schemas.Unset] = schemas.unset,
        TownName: typing.Union['TownName', schemas.Unset] = schemas.unset,
        CountrySubDivision: typing.Union[MetaOapg.properties.CountrySubDivision, str, schemas.Unset] = schemas.unset,
        Country: typing.Union[MetaOapg.properties.Country, str, schemas.Unset] = schemas.unset,
        AddressLine: typing.Union['OBPostalAddress6AddressLine', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBPostalAddress6':
        return super().__new__(
            cls,
            *args,
            AddressType=AddressType,
            Department=Department,
            SubDepartment=SubDepartment,
            StreetName=StreetName,
            BuildingNumber=BuildingNumber,
            PostCode=PostCode,
            TownName=TownName,
            CountrySubDivision=CountrySubDivision,
            Country=Country,
            AddressLine=AddressLine,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.building_number import BuildingNumber
from hsbc_account_information_ce_python_sdk.model.ob_address_type_code import OBAddressTypeCode
from hsbc_account_information_ce_python_sdk.model.ob_postal_address6_address_line import OBPostalAddress6AddressLine
from hsbc_account_information_ce_python_sdk.model.post_code import PostCode
from hsbc_account_information_ce_python_sdk.model.street_name import StreetName
from hsbc_account_information_ce_python_sdk.model.town_name import TownName
