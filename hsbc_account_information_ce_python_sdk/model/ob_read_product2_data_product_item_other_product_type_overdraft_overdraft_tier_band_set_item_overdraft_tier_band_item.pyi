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


class OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItem(
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
                pass
            
            
            class Identification(
                schemas.StrSchema
            ):
                pass
            
            
            class TierValueMax(
                schemas.StrSchema
            ):
                pass
            
            
            class EAR(
                schemas.StrSchema
            ):
                pass
            AgreementLengthMin = schemas.IntSchema
            AgreementLengthMax = schemas.IntSchema
            
            
            class AgreementPeriod(
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
            
            
            class OverdraftInterestChargingCoverage(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INBA(cls):
                    return cls("INBA")
                
                @schemas.classproperty
                def INTI(cls):
                    return cls("INTI")
                
                @schemas.classproperty
                def INWH(cls):
                    return cls("INWH")
            BankGuaranteedIndicator = schemas.BoolSchema
        
            @staticmethod
            def Notes() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes']:
                return OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes
        
            @staticmethod
            def OverdraftFeesCharges() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges']:
                return OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges
            __annotations__ = {
                "TierValueMin": TierValueMin,
                "Identification": Identification,
                "TierValueMax": TierValueMax,
                "EAR": EAR,
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
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OverdraftFeesCharges"]) -> 'OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["TierValueMin", "Identification", "TierValueMax", "EAR", "AgreementLengthMin", "AgreementLengthMax", "AgreementPeriod", "OverdraftInterestChargingCoverage", "BankGuaranteedIndicator", "Notes", "OverdraftFeesCharges", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OverdraftFeesCharges"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["TierValueMin", "Identification", "TierValueMax", "EAR", "AgreementLengthMin", "AgreementLengthMax", "AgreementPeriod", "OverdraftInterestChargingCoverage", "BankGuaranteedIndicator", "Notes", "OverdraftFeesCharges", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        TierValueMin: typing.Union[MetaOapg.properties.TierValueMin, str, ],
        Identification: typing.Union[MetaOapg.properties.Identification, str, schemas.Unset] = schemas.unset,
        TierValueMax: typing.Union[MetaOapg.properties.TierValueMax, str, schemas.Unset] = schemas.unset,
        EAR: typing.Union[MetaOapg.properties.EAR, str, schemas.Unset] = schemas.unset,
        AgreementLengthMin: typing.Union[MetaOapg.properties.AgreementLengthMin, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        AgreementLengthMax: typing.Union[MetaOapg.properties.AgreementLengthMax, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        AgreementPeriod: typing.Union[MetaOapg.properties.AgreementPeriod, str, schemas.Unset] = schemas.unset,
        OverdraftInterestChargingCoverage: typing.Union[MetaOapg.properties.OverdraftInterestChargingCoverage, str, schemas.Unset] = schemas.unset,
        BankGuaranteedIndicator: typing.Union[MetaOapg.properties.BankGuaranteedIndicator, bool, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes', schemas.Unset] = schemas.unset,
        OverdraftFeesCharges: typing.Union['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItem':
        return super().__new__(
            cls,
            *args,
            TierValueMin=TierValueMin,
            Identification=Identification,
            TierValueMax=TierValueMax,
            EAR=EAR,
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

from hsbc_account_information_ce_python_sdk.model.ob_read_product2_data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_notes import OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes
from hsbc_account_information_ce_python_sdk.model.ob_read_product2_data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges import OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges
