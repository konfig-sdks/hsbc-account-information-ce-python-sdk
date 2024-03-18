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


class OBPCAData1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def ProductDetails() -> typing.Type['OBPCAData1ProductDetails']:
                return OBPCAData1ProductDetails
        
            @staticmethod
            def CreditInterest() -> typing.Type['OBPCAData1CreditInterest']:
                return OBPCAData1CreditInterest
        
            @staticmethod
            def Overdraft() -> typing.Type['OBPCAData1Overdraft']:
                return OBPCAData1Overdraft
        
            @staticmethod
            def OtherFeesCharges() -> typing.Type['OBPCAData1OtherFeesCharges']:
                return OBPCAData1OtherFeesCharges
            __annotations__ = {
                "ProductDetails": ProductDetails,
                "CreditInterest": CreditInterest,
                "Overdraft": Overdraft,
                "OtherFeesCharges": OtherFeesCharges,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProductDetails"]) -> 'OBPCAData1ProductDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditInterest"]) -> 'OBPCAData1CreditInterest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Overdraft"]) -> 'OBPCAData1Overdraft': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherFeesCharges"]) -> 'OBPCAData1OtherFeesCharges': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ProductDetails", "CreditInterest", "Overdraft", "OtherFeesCharges", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProductDetails"]) -> typing.Union['OBPCAData1ProductDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditInterest"]) -> typing.Union['OBPCAData1CreditInterest', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Overdraft"]) -> typing.Union['OBPCAData1Overdraft', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherFeesCharges"]) -> typing.Union['OBPCAData1OtherFeesCharges', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ProductDetails", "CreditInterest", "Overdraft", "OtherFeesCharges", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ProductDetails: typing.Union['OBPCAData1ProductDetails', schemas.Unset] = schemas.unset,
        CreditInterest: typing.Union['OBPCAData1CreditInterest', schemas.Unset] = schemas.unset,
        Overdraft: typing.Union['OBPCAData1Overdraft', schemas.Unset] = schemas.unset,
        OtherFeesCharges: typing.Union['OBPCAData1OtherFeesCharges', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBPCAData1':
        return super().__new__(
            cls,
            *args,
            ProductDetails=ProductDetails,
            CreditInterest=CreditInterest,
            Overdraft=Overdraft,
            OtherFeesCharges=OtherFeesCharges,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.obpca_data1_credit_interest import OBPCAData1CreditInterest
from hsbc_account_information_ce_python_sdk.model.obpca_data1_other_fees_charges import OBPCAData1OtherFeesCharges
from hsbc_account_information_ce_python_sdk.model.obpca_data1_overdraft import OBPCAData1Overdraft
from hsbc_account_information_ce_python_sdk.model.obpca_data1_product_details import OBPCAData1ProductDetails