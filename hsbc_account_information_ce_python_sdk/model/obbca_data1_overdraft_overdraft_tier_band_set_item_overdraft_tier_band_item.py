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


class OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Provides overdraft details for a specific tier or band
    """


    class MetaOapg:
        required = {
            "TierValueMin",
        }
        
        class properties:
            
            
            class TierValueMin(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^(-?\d{1,14}){1}(\.\d{1,4}){0,1}$',
                    }]
            
            
            class Identification(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 35
                    min_length = 1
            
            
            class TierValueMax(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^(-?\d{1,14}){1}(\.\d{1,4}){0,1}$',
                    }]
            
            
            class EAR(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^(-?\d{1,3}){1}(\.\d{1,4}){0,1}$',
                    }]
            
            
            class RepresentativeAPR(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^(-?\d{1,3}){1}(\.\d{1,4}){0,1}$',
                    }]
            AgreementLengthMin = schemas.Float32Schema
            AgreementLengthMax = schemas.Float32Schema
            
            
            class AgreementPeriod(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Day": "DAY",
                        "Half Year": "HALF_YEAR",
                        "Month": "MONTH",
                        "Quarter": "QUARTER",
                        "Week": "WEEK",
                        "Year": "YEAR",
                    }
                
                @schemas.classproperty
                def DAY(cls):
                    return cls("Day")
                
                @schemas.classproperty
                def HALF_YEAR(cls):
                    return cls("Half Year")
                
                @schemas.classproperty
                def MONTH(cls):
                    return cls("Month")
                
                @schemas.classproperty
                def QUARTER(cls):
                    return cls("Quarter")
                
                @schemas.classproperty
                def WEEK(cls):
                    return cls("Week")
                
                @schemas.classproperty
                def YEAR(cls):
                    return cls("Year")
            
            
            class OverdraftInterestChargingCoverage(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Banded": "BANDED",
                        "Tiered": "TIERED",
                        "Whole": "WHOLE",
                    }
                
                @schemas.classproperty
                def BANDED(cls):
                    return cls("Banded")
                
                @schemas.classproperty
                def TIERED(cls):
                    return cls("Tiered")
                
                @schemas.classproperty
                def WHOLE(cls):
                    return cls("Whole")
            BankGuaranteedIndicator = schemas.BoolSchema
        
            @staticmethod
            def Notes() -> typing.Type['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes']:
                return OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes
        
            @staticmethod
            def OverdraftFeesCharges() -> typing.Type['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges']:
                return OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges
            __annotations__ = {
                "TierValueMin": TierValueMin,
                "Identification": Identification,
                "TierValueMax": TierValueMax,
                "EAR": EAR,
                "RepresentativeAPR": RepresentativeAPR,
                "AgreementLengthMin": AgreementLengthMin,
                "AgreementLengthMax": AgreementLengthMax,
                "AgreementPeriod": AgreementPeriod,
                "OverdraftInterestChargingCoverage": OverdraftInterestChargingCoverage,
                "BankGuaranteedIndicator": BankGuaranteedIndicator,
                "Notes": Notes,
                "OverdraftFeesCharges": OverdraftFeesCharges,
            }
    
    TierValueMin: MetaOapg.properties.TierValueMin
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TierValueMin"]) -> MetaOapg.properties.TierValueMin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Identification"]) -> MetaOapg.properties.Identification: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TierValueMax"]) -> MetaOapg.properties.TierValueMax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EAR"]) -> MetaOapg.properties.EAR: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RepresentativeAPR"]) -> MetaOapg.properties.RepresentativeAPR: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AgreementLengthMin"]) -> MetaOapg.properties.AgreementLengthMin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AgreementLengthMax"]) -> MetaOapg.properties.AgreementLengthMax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AgreementPeriod"]) -> MetaOapg.properties.AgreementPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OverdraftInterestChargingCoverage"]) -> MetaOapg.properties.OverdraftInterestChargingCoverage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankGuaranteedIndicator"]) -> MetaOapg.properties.BankGuaranteedIndicator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OverdraftFeesCharges"]) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["TierValueMin", "Identification", "TierValueMax", "EAR", "RepresentativeAPR", "AgreementLengthMin", "AgreementLengthMax", "AgreementPeriod", "OverdraftInterestChargingCoverage", "BankGuaranteedIndicator", "Notes", "OverdraftFeesCharges", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TierValueMin"]) -> MetaOapg.properties.TierValueMin: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Identification"]) -> typing.Union[MetaOapg.properties.Identification, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TierValueMax"]) -> typing.Union[MetaOapg.properties.TierValueMax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EAR"]) -> typing.Union[MetaOapg.properties.EAR, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RepresentativeAPR"]) -> typing.Union[MetaOapg.properties.RepresentativeAPR, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AgreementLengthMin"]) -> typing.Union[MetaOapg.properties.AgreementLengthMin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AgreementLengthMax"]) -> typing.Union[MetaOapg.properties.AgreementLengthMax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AgreementPeriod"]) -> typing.Union[MetaOapg.properties.AgreementPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OverdraftInterestChargingCoverage"]) -> typing.Union[MetaOapg.properties.OverdraftInterestChargingCoverage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankGuaranteedIndicator"]) -> typing.Union[MetaOapg.properties.BankGuaranteedIndicator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OverdraftFeesCharges"]) -> typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["TierValueMin", "Identification", "TierValueMax", "EAR", "RepresentativeAPR", "AgreementLengthMin", "AgreementLengthMax", "AgreementPeriod", "OverdraftInterestChargingCoverage", "BankGuaranteedIndicator", "Notes", "OverdraftFeesCharges", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        TierValueMin: typing.Union[MetaOapg.properties.TierValueMin, str, ],
        Identification: typing.Union[MetaOapg.properties.Identification, str, schemas.Unset] = schemas.unset,
        TierValueMax: typing.Union[MetaOapg.properties.TierValueMax, str, schemas.Unset] = schemas.unset,
        EAR: typing.Union[MetaOapg.properties.EAR, str, schemas.Unset] = schemas.unset,
        RepresentativeAPR: typing.Union[MetaOapg.properties.RepresentativeAPR, str, schemas.Unset] = schemas.unset,
        AgreementLengthMin: typing.Union[MetaOapg.properties.AgreementLengthMin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        AgreementLengthMax: typing.Union[MetaOapg.properties.AgreementLengthMax, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        AgreementPeriod: typing.Union[MetaOapg.properties.AgreementPeriod, str, schemas.Unset] = schemas.unset,
        OverdraftInterestChargingCoverage: typing.Union[MetaOapg.properties.OverdraftInterestChargingCoverage, str, schemas.Unset] = schemas.unset,
        BankGuaranteedIndicator: typing.Union[MetaOapg.properties.BankGuaranteedIndicator, bool, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes', schemas.Unset] = schemas.unset,
        OverdraftFeesCharges: typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem':
        return super().__new__(
            cls,
            *args,
            TierValueMin=TierValueMin,
            Identification=Identification,
            TierValueMax=TierValueMax,
            EAR=EAR,
            RepresentativeAPR=RepresentativeAPR,
            AgreementLengthMin=AgreementLengthMin,
            AgreementLengthMax=AgreementLengthMax,
            AgreementPeriod=AgreementPeriod,
            OverdraftInterestChargingCoverage=OverdraftInterestChargingCoverage,
            BankGuaranteedIndicator=BankGuaranteedIndicator,
            Notes=Notes,
            OverdraftFeesCharges=OverdraftFeesCharges,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_notes import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes
from hsbc_account_information_ce_python_sdk.model.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges
