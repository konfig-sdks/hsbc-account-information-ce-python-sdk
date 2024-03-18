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


class OBBCAData1CreditInterestTierBandSetItemTierBandItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Tier Band Details
    """


    class MetaOapg:
        required = {
            "FixedVariableInterestRateType",
            "TierValueMinimum",
            "ApplicationFrequency",
            "AER",
        }
        
        class properties:
            
            
            class TierValueMinimum(
                schemas.StrSchema
            ):
                pass
            
            
            class ApplicationFrequency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DAILY(cls):
                    return cls("Daily")
                
                @schemas.classproperty
                def HALF_YEARLY(cls):
                    return cls("HalfYearly")
                
                @schemas.classproperty
                def MONTHLY(cls):
                    return cls("Monthly")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
                
                @schemas.classproperty
                def QUARTERLY(cls):
                    return cls("Quarterly")
                
                @schemas.classproperty
                def PER_STATEMENT_DATE(cls):
                    return cls("PerStatementDate")
                
                @schemas.classproperty
                def WEEKLY(cls):
                    return cls("Weekly")
                
                @schemas.classproperty
                def YEARLY(cls):
                    return cls("Yearly")
            
            
            class FixedVariableInterestRateType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FIXED(cls):
                    return cls("Fixed")
                
                @schemas.classproperty
                def VARIABLE(cls):
                    return cls("Variable")
            
            
            class AER(
                schemas.StrSchema
            ):
                pass
            
            
            class Identification(
                schemas.StrSchema
            ):
                pass
            
            
            class TierValueMaximum(
                schemas.StrSchema
            ):
                pass
            
            
            class CalculationFrequency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DAILY(cls):
                    return cls("Daily")
                
                @schemas.classproperty
                def HALF_YEARLY(cls):
                    return cls("HalfYearly")
                
                @schemas.classproperty
                def MONTHLY(cls):
                    return cls("Monthly")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
                
                @schemas.classproperty
                def QUARTERLY(cls):
                    return cls("Quarterly")
                
                @schemas.classproperty
                def PER_STATEMENT_DATE(cls):
                    return cls("PerStatementDate")
                
                @schemas.classproperty
                def WEEKLY(cls):
                    return cls("Weekly")
                
                @schemas.classproperty
                def YEARLY(cls):
                    return cls("Yearly")
            
            
            class DepositInterestAppliedCoverage(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BANDED(cls):
                    return cls("Banded")
                
                @schemas.classproperty
                def TIERED(cls):
                    return cls("Tiered")
                
                @schemas.classproperty
                def WHOLE(cls):
                    return cls("Whole")
            
            
            class BankInterestRateType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def GROSS(cls):
                    return cls("Gross")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
            
            
            class BankInterestRate(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def Notes() -> typing.Type['OBBCAData1CreditInterestTierBandSetItemTierBandItemNotes']:
                return OBBCAData1CreditInterestTierBandSetItemTierBandItemNotes
        
            @staticmethod
            def OtherBankInterestType() -> typing.Type['OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType']:
                return OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType
        
            @staticmethod
            def OtherApplicationFrequency() -> typing.Type['OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency']:
                return OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency
        
            @staticmethod
            def OtherCalculationFrequency() -> typing.Type['OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency']:
                return OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency
            __annotations__ = {
                "TierValueMinimum": TierValueMinimum,
                "ApplicationFrequency": ApplicationFrequency,
                "FixedVariableInterestRateType": FixedVariableInterestRateType,
                "AER": AER,
                "Identification": Identification,
                "TierValueMaximum": TierValueMaximum,
                "CalculationFrequency": CalculationFrequency,
                "DepositInterestAppliedCoverage": DepositInterestAppliedCoverage,
                "BankInterestRateType": BankInterestRateType,
                "BankInterestRate": BankInterestRate,
                "Notes": Notes,
                "OtherBankInterestType": OtherBankInterestType,
                "OtherApplicationFrequency": OtherApplicationFrequency,
                "OtherCalculationFrequency": OtherCalculationFrequency,
            }
    
    FixedVariableInterestRateType: MetaOapg.properties.FixedVariableInterestRateType
    TierValueMinimum: MetaOapg.properties.TierValueMinimum
    ApplicationFrequency: MetaOapg.properties.ApplicationFrequency
    AER: MetaOapg.properties.AER
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TierValueMinimum"]) -> MetaOapg.properties.TierValueMinimum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ApplicationFrequency"]) -> MetaOapg.properties.ApplicationFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FixedVariableInterestRateType"]) -> MetaOapg.properties.FixedVariableInterestRateType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AER"]) -> MetaOapg.properties.AER: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Identification"]) -> MetaOapg.properties.Identification: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TierValueMaximum"]) -> MetaOapg.properties.TierValueMaximum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CalculationFrequency"]) -> MetaOapg.properties.CalculationFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DepositInterestAppliedCoverage"]) -> MetaOapg.properties.DepositInterestAppliedCoverage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankInterestRateType"]) -> MetaOapg.properties.BankInterestRateType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankInterestRate"]) -> MetaOapg.properties.BankInterestRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBBCAData1CreditInterestTierBandSetItemTierBandItemNotes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherBankInterestType"]) -> 'OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherApplicationFrequency"]) -> 'OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherCalculationFrequency"]) -> 'OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["TierValueMinimum", "ApplicationFrequency", "FixedVariableInterestRateType", "AER", "Identification", "TierValueMaximum", "CalculationFrequency", "DepositInterestAppliedCoverage", "BankInterestRateType", "BankInterestRate", "Notes", "OtherBankInterestType", "OtherApplicationFrequency", "OtherCalculationFrequency", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TierValueMinimum"]) -> MetaOapg.properties.TierValueMinimum: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ApplicationFrequency"]) -> MetaOapg.properties.ApplicationFrequency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FixedVariableInterestRateType"]) -> MetaOapg.properties.FixedVariableInterestRateType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AER"]) -> MetaOapg.properties.AER: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Identification"]) -> typing.Union[MetaOapg.properties.Identification, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TierValueMaximum"]) -> typing.Union[MetaOapg.properties.TierValueMaximum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CalculationFrequency"]) -> typing.Union[MetaOapg.properties.CalculationFrequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DepositInterestAppliedCoverage"]) -> typing.Union[MetaOapg.properties.DepositInterestAppliedCoverage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankInterestRateType"]) -> typing.Union[MetaOapg.properties.BankInterestRateType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankInterestRate"]) -> typing.Union[MetaOapg.properties.BankInterestRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBBCAData1CreditInterestTierBandSetItemTierBandItemNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherBankInterestType"]) -> typing.Union['OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherApplicationFrequency"]) -> typing.Union['OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherCalculationFrequency"]) -> typing.Union['OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["TierValueMinimum", "ApplicationFrequency", "FixedVariableInterestRateType", "AER", "Identification", "TierValueMaximum", "CalculationFrequency", "DepositInterestAppliedCoverage", "BankInterestRateType", "BankInterestRate", "Notes", "OtherBankInterestType", "OtherApplicationFrequency", "OtherCalculationFrequency", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        FixedVariableInterestRateType: typing.Union[MetaOapg.properties.FixedVariableInterestRateType, str, ],
        TierValueMinimum: typing.Union[MetaOapg.properties.TierValueMinimum, str, ],
        ApplicationFrequency: typing.Union[MetaOapg.properties.ApplicationFrequency, str, ],
        AER: typing.Union[MetaOapg.properties.AER, str, ],
        Identification: typing.Union[MetaOapg.properties.Identification, str, schemas.Unset] = schemas.unset,
        TierValueMaximum: typing.Union[MetaOapg.properties.TierValueMaximum, str, schemas.Unset] = schemas.unset,
        CalculationFrequency: typing.Union[MetaOapg.properties.CalculationFrequency, str, schemas.Unset] = schemas.unset,
        DepositInterestAppliedCoverage: typing.Union[MetaOapg.properties.DepositInterestAppliedCoverage, str, schemas.Unset] = schemas.unset,
        BankInterestRateType: typing.Union[MetaOapg.properties.BankInterestRateType, str, schemas.Unset] = schemas.unset,
        BankInterestRate: typing.Union[MetaOapg.properties.BankInterestRate, str, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBBCAData1CreditInterestTierBandSetItemTierBandItemNotes', schemas.Unset] = schemas.unset,
        OtherBankInterestType: typing.Union['OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType', schemas.Unset] = schemas.unset,
        OtherApplicationFrequency: typing.Union['OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency', schemas.Unset] = schemas.unset,
        OtherCalculationFrequency: typing.Union['OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBBCAData1CreditInterestTierBandSetItemTierBandItem':
        return super().__new__(
            cls,
            *args,
            FixedVariableInterestRateType=FixedVariableInterestRateType,
            TierValueMinimum=TierValueMinimum,
            ApplicationFrequency=ApplicationFrequency,
            AER=AER,
            Identification=Identification,
            TierValueMaximum=TierValueMaximum,
            CalculationFrequency=CalculationFrequency,
            DepositInterestAppliedCoverage=DepositInterestAppliedCoverage,
            BankInterestRateType=BankInterestRateType,
            BankInterestRate=BankInterestRate,
            Notes=Notes,
            OtherBankInterestType=OtherBankInterestType,
            OtherApplicationFrequency=OtherApplicationFrequency,
            OtherCalculationFrequency=OtherCalculationFrequency,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.obbca_data1_credit_interest_tier_band_set_item_tier_band_item_notes import OBBCAData1CreditInterestTierBandSetItemTierBandItemNotes
from hsbc_account_information_ce_python_sdk.model.obbca_data1_credit_interest_tier_band_set_item_tier_band_item_other_application_frequency import OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency
from hsbc_account_information_ce_python_sdk.model.obbca_data1_credit_interest_tier_band_set_item_tier_band_item_other_bank_interest_type import OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType
from hsbc_account_information_ce_python_sdk.model.obbca_data1_credit_interest_tier_band_set_item_tier_band_item_other_calculation_frequency import OBBCAData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency
