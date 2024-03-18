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


class OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about any caps (maximum charges) that apply to a particular or group of fee/charge
    """


    class MetaOapg:
        required = {
            "FeeType",
            "MinMaxType",
        }
        
        class properties:
        
            @staticmethod
            def FeeType() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemFeeType']:
                return OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemFeeType
        
            @staticmethod
            def MinMaxType() -> typing.Type['OBMinMaxType1Code']:
                return OBMinMaxType1Code
            FeeCapOccurrence = schemas.IntSchema
        
            @staticmethod
            def FeeCapAmount() -> typing.Type['OBAmount14']:
                return OBAmount14
        
            @staticmethod
            def CappingPeriod() -> typing.Type['OBPeriod1Code']:
                return OBPeriod1Code
        
            @staticmethod
            def Notes() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemNotes']:
                return OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemNotes
        
            @staticmethod
            def OtherFeeType() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemOtherFeeType']:
                return OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemOtherFeeType
            __annotations__ = {
                "FeeType": FeeType,
                "MinMaxType": MinMaxType,
                "FeeCapOccurrence": FeeCapOccurrence,
                "FeeCapAmount": FeeCapAmount,
                "CappingPeriod": CappingPeriod,
                "Notes": Notes,
                "OtherFeeType": OtherFeeType,
            }
    
    FeeType: 'OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemFeeType'
    MinMaxType: 'OBMinMaxType1Code'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeType"]) -> 'OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemFeeType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MinMaxType"]) -> 'OBMinMaxType1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeCapOccurrence"]) -> MetaOapg.properties.FeeCapOccurrence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeCapAmount"]) -> 'OBAmount14': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CappingPeriod"]) -> 'OBPeriod1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemNotes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherFeeType"]) -> 'OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemOtherFeeType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["FeeType", "MinMaxType", "FeeCapOccurrence", "FeeCapAmount", "CappingPeriod", "Notes", "OtherFeeType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeType"]) -> 'OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemFeeType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MinMaxType"]) -> 'OBMinMaxType1Code': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeCapOccurrence"]) -> typing.Union[MetaOapg.properties.FeeCapOccurrence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeCapAmount"]) -> typing.Union['OBAmount14', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CappingPeriod"]) -> typing.Union['OBPeriod1Code', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherFeeType"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemOtherFeeType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["FeeType", "MinMaxType", "FeeCapOccurrence", "FeeCapAmount", "CappingPeriod", "Notes", "OtherFeeType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        FeeType: 'OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemFeeType',
        MinMaxType: 'OBMinMaxType1Code',
        FeeCapOccurrence: typing.Union[MetaOapg.properties.FeeCapOccurrence, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        FeeCapAmount: typing.Union['OBAmount14', schemas.Unset] = schemas.unset,
        CappingPeriod: typing.Union['OBPeriod1Code', schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemNotes', schemas.Unset] = schemas.unset,
        OtherFeeType: typing.Union['OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemOtherFeeType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItem':
        return super().__new__(
            cls,
            *args,
            FeeType=FeeType,
            MinMaxType=MinMaxType,
            FeeCapOccurrence=FeeCapOccurrence,
            FeeCapAmount=FeeCapAmount,
            CappingPeriod=CappingPeriod,
            Notes=Notes,
            OtherFeeType=OtherFeeType,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.ob_amount14 import OBAmount14
from hsbc_account_information_ce_python_sdk.model.ob_min_max_type1_code import OBMinMaxType1Code
from hsbc_account_information_ce_python_sdk.model.ob_period1_code import OBPeriod1Code
from hsbc_account_information_ce_python_sdk.model.ob_read_product2_data_product_item_other_product_type_other_fees_charges_item_fee_charge_cap_item_fee_type import OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemFeeType
from hsbc_account_information_ce_python_sdk.model.ob_read_product2_data_product_item_other_product_type_other_fees_charges_item_fee_charge_cap_item_notes import OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemNotes
from hsbc_account_information_ce_python_sdk.model.ob_read_product2_data_product_item_other_product_type_other_fees_charges_item_fee_charge_cap_item_other_fee_type import OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItemOtherFeeType
