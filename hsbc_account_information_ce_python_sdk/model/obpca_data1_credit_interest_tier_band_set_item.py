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


class OBPCAData1CreditInterestTierBandSetItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The group of tiers or bands for which credit interest can be applied.
    """


    class MetaOapg:
        required = {
            "TierBandMethod",
            "TierBand",
        }
        
        class properties:
            
            
            class TierBandMethod(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Tiered": "TIERED",
                        "Whole": "WHOLE",
                    }
                
                @schemas.classproperty
                def TIERED(cls):
                    return cls("Tiered")
                
                @schemas.classproperty
                def WHOLE(cls):
                    return cls("Whole")
        
            @staticmethod
            def TierBand() -> typing.Type['OBPCAData1CreditInterestTierBandSetItemTierBand']:
                return OBPCAData1CreditInterestTierBandSetItemTierBand
            
            
            class CalculationMethod(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Compound": "COMPOUND",
                        "SimpleInterest": "SIMPLE_INTEREST",
                    }
                
                @schemas.classproperty
                def COMPOUND(cls):
                    return cls("Compound")
                
                @schemas.classproperty
                def SIMPLE_INTEREST(cls):
                    return cls("SimpleInterest")
            
            
            class Destination(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PayAway": "PAY_AWAY",
                        "SelfCredit": "SELF_CREDIT",
                    }
                
                @schemas.classproperty
                def PAY_AWAY(cls):
                    return cls("PayAway")
                
                @schemas.classproperty
                def SELF_CREDIT(cls):
                    return cls("SelfCredit")
        
            @staticmethod
            def Notes() -> typing.Type['OBPCAData1CreditInterestTierBandSetItemNotes']:
                return OBPCAData1CreditInterestTierBandSetItemNotes
            __annotations__ = {
                "TierBandMethod": TierBandMethod,
                "TierBand": TierBand,
                "CalculationMethod": CalculationMethod,
                "Destination": Destination,
                "Notes": Notes,
            }
    
    TierBandMethod: MetaOapg.properties.TierBandMethod
    TierBand: 'OBPCAData1CreditInterestTierBandSetItemTierBand'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TierBandMethod"]) -> MetaOapg.properties.TierBandMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TierBand"]) -> 'OBPCAData1CreditInterestTierBandSetItemTierBand': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CalculationMethod"]) -> MetaOapg.properties.CalculationMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Destination"]) -> MetaOapg.properties.Destination: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBPCAData1CreditInterestTierBandSetItemNotes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["TierBandMethod", "TierBand", "CalculationMethod", "Destination", "Notes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TierBandMethod"]) -> MetaOapg.properties.TierBandMethod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TierBand"]) -> 'OBPCAData1CreditInterestTierBandSetItemTierBand': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CalculationMethod"]) -> typing.Union[MetaOapg.properties.CalculationMethod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Destination"]) -> typing.Union[MetaOapg.properties.Destination, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBPCAData1CreditInterestTierBandSetItemNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["TierBandMethod", "TierBand", "CalculationMethod", "Destination", "Notes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        TierBandMethod: typing.Union[MetaOapg.properties.TierBandMethod, str, ],
        TierBand: 'OBPCAData1CreditInterestTierBandSetItemTierBand',
        CalculationMethod: typing.Union[MetaOapg.properties.CalculationMethod, str, schemas.Unset] = schemas.unset,
        Destination: typing.Union[MetaOapg.properties.Destination, str, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBPCAData1CreditInterestTierBandSetItemNotes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBPCAData1CreditInterestTierBandSetItem':
        return super().__new__(
            cls,
            *args,
            TierBandMethod=TierBandMethod,
            TierBand=TierBand,
            CalculationMethod=CalculationMethod,
            Destination=Destination,
            Notes=Notes,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.obpca_data1_credit_interest_tier_band_set_item_notes import OBPCAData1CreditInterestTierBandSetItemNotes
from hsbc_account_information_ce_python_sdk.model.obpca_data1_credit_interest_tier_band_set_item_tier_band import OBPCAData1CreditInterestTierBandSetItemTierBand
