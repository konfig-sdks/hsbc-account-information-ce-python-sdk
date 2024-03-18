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


class OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about the fees/charges
    """


    class MetaOapg:
        required = {
            "ApplicationFrequency",
            "FeeType",
        }
        
        class properties:
            
            
            class FeeType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ArrangedOverdraft": "ARRANGED_OVERDRAFT",
                        "EmergencyBorrowing": "EMERGENCY_BORROWING",
                        "BorrowingItem": "BORROWING_ITEM",
                        "OverdraftRenewal": "OVERDRAFT_RENEWAL",
                        "AnnualReview": "ANNUAL_REVIEW",
                        "OverdraftSetup": "OVERDRAFT_SETUP",
                        "Surcharge": "SURCHARGE",
                        "TempOverdraft": "TEMP_OVERDRAFT",
                        "UnauthorisedBorrowing": "UNAUTHORISED_BORROWING",
                        "UnauthorisedPaidTrans": "UNAUTHORISED_PAID_TRANS",
                        "Other": "OTHER",
                        "UnauthorisedUnpaidTrans": "UNAUTHORISED_UNPAID_TRANS",
                    }
                
                @schemas.classproperty
                def ARRANGED_OVERDRAFT(cls):
                    return cls("ArrangedOverdraft")
                
                @schemas.classproperty
                def EMERGENCY_BORROWING(cls):
                    return cls("EmergencyBorrowing")
                
                @schemas.classproperty
                def BORROWING_ITEM(cls):
                    return cls("BorrowingItem")
                
                @schemas.classproperty
                def OVERDRAFT_RENEWAL(cls):
                    return cls("OverdraftRenewal")
                
                @schemas.classproperty
                def ANNUAL_REVIEW(cls):
                    return cls("AnnualReview")
                
                @schemas.classproperty
                def OVERDRAFT_SETUP(cls):
                    return cls("OverdraftSetup")
                
                @schemas.classproperty
                def SURCHARGE(cls):
                    return cls("Surcharge")
                
                @schemas.classproperty
                def TEMP_OVERDRAFT(cls):
                    return cls("TempOverdraft")
                
                @schemas.classproperty
                def UNAUTHORISED_BORROWING(cls):
                    return cls("UnauthorisedBorrowing")
                
                @schemas.classproperty
                def UNAUTHORISED_PAID_TRANS(cls):
                    return cls("UnauthorisedPaidTrans")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
                
                @schemas.classproperty
                def UNAUTHORISED_UNPAID_TRANS(cls):
                    return cls("UnauthorisedUnpaidTrans")
            
            
            class ApplicationFrequency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "AccountClosing": "ACCOUNT_CLOSING",
                        "AccountOpening": "ACCOUNT_OPENING",
                        "AcademicTerm": "ACADEMIC_TERM",
                        "ChargingPeriod": "CHARGING_PERIOD",
                        "Daily": "DAILY",
                        "PerItem": "PER_ITEM",
                        "Monthly": "MONTHLY",
                        "OnAccountAnniversary": "ON_ACCOUNT_ANNIVERSARY",
                        "Other": "OTHER",
                        "PerHour": "PER_HOUR",
                        "PerOccurrence": "PER_OCCURRENCE",
                        "PerSheet": "PER_SHEET",
                        "PerTransaction": "PER_TRANSACTION",
                        "PerTransactionAmount": "PER_TRANSACTION_AMOUNT",
                        "PerTransactionPercentage": "PER_TRANSACTION_PERCENTAGE",
                        "Quarterly": "QUARTERLY",
                        "SixMonthly": "SIX_MONTHLY",
                        "StatementMonthly": "STATEMENT_MONTHLY",
                        "Weekly": "WEEKLY",
                        "Yearly": "YEARLY",
                    }
                
                @schemas.classproperty
                def ACCOUNT_CLOSING(cls):
                    return cls("AccountClosing")
                
                @schemas.classproperty
                def ACCOUNT_OPENING(cls):
                    return cls("AccountOpening")
                
                @schemas.classproperty
                def ACADEMIC_TERM(cls):
                    return cls("AcademicTerm")
                
                @schemas.classproperty
                def CHARGING_PERIOD(cls):
                    return cls("ChargingPeriod")
                
                @schemas.classproperty
                def DAILY(cls):
                    return cls("Daily")
                
                @schemas.classproperty
                def PER_ITEM(cls):
                    return cls("PerItem")
                
                @schemas.classproperty
                def MONTHLY(cls):
                    return cls("Monthly")
                
                @schemas.classproperty
                def ON_ACCOUNT_ANNIVERSARY(cls):
                    return cls("OnAccountAnniversary")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
                
                @schemas.classproperty
                def PER_HOUR(cls):
                    return cls("PerHour")
                
                @schemas.classproperty
                def PER_OCCURRENCE(cls):
                    return cls("PerOccurrence")
                
                @schemas.classproperty
                def PER_SHEET(cls):
                    return cls("PerSheet")
                
                @schemas.classproperty
                def PER_TRANSACTION(cls):
                    return cls("PerTransaction")
                
                @schemas.classproperty
                def PER_TRANSACTION_AMOUNT(cls):
                    return cls("PerTransactionAmount")
                
                @schemas.classproperty
                def PER_TRANSACTION_PERCENTAGE(cls):
                    return cls("PerTransactionPercentage")
                
                @schemas.classproperty
                def QUARTERLY(cls):
                    return cls("Quarterly")
                
                @schemas.classproperty
                def SIX_MONTHLY(cls):
                    return cls("SixMonthly")
                
                @schemas.classproperty
                def STATEMENT_MONTHLY(cls):
                    return cls("StatementMonthly")
                
                @schemas.classproperty
                def WEEKLY(cls):
                    return cls("Weekly")
                
                @schemas.classproperty
                def YEARLY(cls):
                    return cls("Yearly")
            OverdraftControlIndicator = schemas.BoolSchema
            
            
            class IncrementalBorrowingAmount(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^(-?\d{1,14}){1}(\.\d{1,4}){0,1}$',
                    }]
            
            
            class FeeAmount(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^(-?\d{1,14}){1}(\.\d{1,4}){0,1}$',
                    }]
            
            
            class FeeRate(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^(-?\d{1,3}){1}(\.\d{1,4}){0,1}$',
                    }]
            
            
            class FeeRateType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "LinkedBaseRate": "LINKED_BASE_RATE",
                        "Gross": "GROSS",
                        "Net": "NET",
                        "Other": "OTHER",
                    }
                
                @schemas.classproperty
                def LINKED_BASE_RATE(cls):
                    return cls("LinkedBaseRate")
                
                @schemas.classproperty
                def GROSS(cls):
                    return cls("Gross")
                
                @schemas.classproperty
                def NET(cls):
                    return cls("Net")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
            
            
            class CalculationFrequency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "AccountClosing": "ACCOUNT_CLOSING",
                        "AccountOpening": "ACCOUNT_OPENING",
                        "AcademicTerm": "ACADEMIC_TERM",
                        "ChargingPeriod": "CHARGING_PERIOD",
                        "Daily": "DAILY",
                        "PerItem": "PER_ITEM",
                        "Monthly": "MONTHLY",
                        "OnAccountAnniversary": "ON_ACCOUNT_ANNIVERSARY",
                        "Other": "OTHER",
                        "PerHour": "PER_HOUR",
                        "PerOccurrence": "PER_OCCURRENCE",
                        "PerSheet": "PER_SHEET",
                        "PerTransaction": "PER_TRANSACTION",
                        "PerTransactionAmount": "PER_TRANSACTION_AMOUNT",
                        "PerTransactionPercentage": "PER_TRANSACTION_PERCENTAGE",
                        "Quarterly": "QUARTERLY",
                        "SixMonthly": "SIX_MONTHLY",
                        "StatementMonthly": "STATEMENT_MONTHLY",
                        "Weekly": "WEEKLY",
                        "Yearly": "YEARLY",
                    }
                
                @schemas.classproperty
                def ACCOUNT_CLOSING(cls):
                    return cls("AccountClosing")
                
                @schemas.classproperty
                def ACCOUNT_OPENING(cls):
                    return cls("AccountOpening")
                
                @schemas.classproperty
                def ACADEMIC_TERM(cls):
                    return cls("AcademicTerm")
                
                @schemas.classproperty
                def CHARGING_PERIOD(cls):
                    return cls("ChargingPeriod")
                
                @schemas.classproperty
                def DAILY(cls):
                    return cls("Daily")
                
                @schemas.classproperty
                def PER_ITEM(cls):
                    return cls("PerItem")
                
                @schemas.classproperty
                def MONTHLY(cls):
                    return cls("Monthly")
                
                @schemas.classproperty
                def ON_ACCOUNT_ANNIVERSARY(cls):
                    return cls("OnAccountAnniversary")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
                
                @schemas.classproperty
                def PER_HOUR(cls):
                    return cls("PerHour")
                
                @schemas.classproperty
                def PER_OCCURRENCE(cls):
                    return cls("PerOccurrence")
                
                @schemas.classproperty
                def PER_SHEET(cls):
                    return cls("PerSheet")
                
                @schemas.classproperty
                def PER_TRANSACTION(cls):
                    return cls("PerTransaction")
                
                @schemas.classproperty
                def PER_TRANSACTION_AMOUNT(cls):
                    return cls("PerTransactionAmount")
                
                @schemas.classproperty
                def PER_TRANSACTION_PERCENTAGE(cls):
                    return cls("PerTransactionPercentage")
                
                @schemas.classproperty
                def QUARTERLY(cls):
                    return cls("Quarterly")
                
                @schemas.classproperty
                def SIX_MONTHLY(cls):
                    return cls("SixMonthly")
                
                @schemas.classproperty
                def STATEMENT_MONTHLY(cls):
                    return cls("StatementMonthly")
                
                @schemas.classproperty
                def WEEKLY(cls):
                    return cls("Weekly")
                
                @schemas.classproperty
                def YEARLY(cls):
                    return cls("Yearly")
        
            @staticmethod
            def Notes() -> typing.Type['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes']:
                return OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes
        
            @staticmethod
            def OtherFeeType() -> typing.Type['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType']:
                return OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType
        
            @staticmethod
            def OtherFeeRateType() -> typing.Type['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType']:
                return OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType
        
            @staticmethod
            def OtherApplicationFrequency() -> typing.Type['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency']:
                return OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency
        
            @staticmethod
            def OtherCalculationFrequency() -> typing.Type['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency']:
                return OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency
        
            @staticmethod
            def OverdraftFeeChargeCap() -> typing.Type['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap']:
                return OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap
            __annotations__ = {
                "FeeType": FeeType,
                "ApplicationFrequency": ApplicationFrequency,
                "OverdraftControlIndicator": OverdraftControlIndicator,
                "IncrementalBorrowingAmount": IncrementalBorrowingAmount,
                "FeeAmount": FeeAmount,
                "FeeRate": FeeRate,
                "FeeRateType": FeeRateType,
                "CalculationFrequency": CalculationFrequency,
                "Notes": Notes,
                "OtherFeeType": OtherFeeType,
                "OtherFeeRateType": OtherFeeRateType,
                "OtherApplicationFrequency": OtherApplicationFrequency,
                "OtherCalculationFrequency": OtherCalculationFrequency,
                "OverdraftFeeChargeCap": OverdraftFeeChargeCap,
            }
    
    ApplicationFrequency: MetaOapg.properties.ApplicationFrequency
    FeeType: MetaOapg.properties.FeeType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeType"]) -> MetaOapg.properties.FeeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ApplicationFrequency"]) -> MetaOapg.properties.ApplicationFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OverdraftControlIndicator"]) -> MetaOapg.properties.OverdraftControlIndicator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IncrementalBorrowingAmount"]) -> MetaOapg.properties.IncrementalBorrowingAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeAmount"]) -> MetaOapg.properties.FeeAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeRate"]) -> MetaOapg.properties.FeeRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeRateType"]) -> MetaOapg.properties.FeeRateType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CalculationFrequency"]) -> MetaOapg.properties.CalculationFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherFeeType"]) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherFeeRateType"]) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherApplicationFrequency"]) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherCalculationFrequency"]) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OverdraftFeeChargeCap"]) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["FeeType", "ApplicationFrequency", "OverdraftControlIndicator", "IncrementalBorrowingAmount", "FeeAmount", "FeeRate", "FeeRateType", "CalculationFrequency", "Notes", "OtherFeeType", "OtherFeeRateType", "OtherApplicationFrequency", "OtherCalculationFrequency", "OverdraftFeeChargeCap", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeType"]) -> MetaOapg.properties.FeeType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ApplicationFrequency"]) -> MetaOapg.properties.ApplicationFrequency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OverdraftControlIndicator"]) -> typing.Union[MetaOapg.properties.OverdraftControlIndicator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IncrementalBorrowingAmount"]) -> typing.Union[MetaOapg.properties.IncrementalBorrowingAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeAmount"]) -> typing.Union[MetaOapg.properties.FeeAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeRate"]) -> typing.Union[MetaOapg.properties.FeeRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeRateType"]) -> typing.Union[MetaOapg.properties.FeeRateType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CalculationFrequency"]) -> typing.Union[MetaOapg.properties.CalculationFrequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherFeeType"]) -> typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherFeeRateType"]) -> typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherApplicationFrequency"]) -> typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherCalculationFrequency"]) -> typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OverdraftFeeChargeCap"]) -> typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["FeeType", "ApplicationFrequency", "OverdraftControlIndicator", "IncrementalBorrowingAmount", "FeeAmount", "FeeRate", "FeeRateType", "CalculationFrequency", "Notes", "OtherFeeType", "OtherFeeRateType", "OtherApplicationFrequency", "OtherCalculationFrequency", "OverdraftFeeChargeCap", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ApplicationFrequency: typing.Union[MetaOapg.properties.ApplicationFrequency, str, ],
        FeeType: typing.Union[MetaOapg.properties.FeeType, str, ],
        OverdraftControlIndicator: typing.Union[MetaOapg.properties.OverdraftControlIndicator, bool, schemas.Unset] = schemas.unset,
        IncrementalBorrowingAmount: typing.Union[MetaOapg.properties.IncrementalBorrowingAmount, str, schemas.Unset] = schemas.unset,
        FeeAmount: typing.Union[MetaOapg.properties.FeeAmount, str, schemas.Unset] = schemas.unset,
        FeeRate: typing.Union[MetaOapg.properties.FeeRate, str, schemas.Unset] = schemas.unset,
        FeeRateType: typing.Union[MetaOapg.properties.FeeRateType, str, schemas.Unset] = schemas.unset,
        CalculationFrequency: typing.Union[MetaOapg.properties.CalculationFrequency, str, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes', schemas.Unset] = schemas.unset,
        OtherFeeType: typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType', schemas.Unset] = schemas.unset,
        OtherFeeRateType: typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType', schemas.Unset] = schemas.unset,
        OtherApplicationFrequency: typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency', schemas.Unset] = schemas.unset,
        OtherCalculationFrequency: typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency', schemas.Unset] = schemas.unset,
        OverdraftFeeChargeCap: typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem':
        return super().__new__(
            cls,
            *args,
            ApplicationFrequency=ApplicationFrequency,
            FeeType=FeeType,
            OverdraftControlIndicator=OverdraftControlIndicator,
            IncrementalBorrowingAmount=IncrementalBorrowingAmount,
            FeeAmount=FeeAmount,
            FeeRate=FeeRate,
            FeeRateType=FeeRateType,
            CalculationFrequency=CalculationFrequency,
            Notes=Notes,
            OtherFeeType=OtherFeeType,
            OtherFeeRateType=OtherFeeRateType,
            OtherApplicationFrequency=OtherApplicationFrequency,
            OtherCalculationFrequency=OtherCalculationFrequency,
            OverdraftFeeChargeCap=OverdraftFeeChargeCap,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_notes import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes
from hsbc_account_information_ce_python_sdk.model.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency
from hsbc_account_information_ce_python_sdk.model.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency
from hsbc_account_information_ce_python_sdk.model.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType
from hsbc_account_information_ce_python_sdk.model.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType
from hsbc_account_information_ce_python_sdk.model.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap
