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


class OBCurrencyExchange5(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Set of elements used to provide details on the currency exchange.
    """


    class MetaOapg:
        required = {
            "SourceCurrency",
            "ExchangeRate",
        }
        
        class properties:
            
            
            class SourceCurrency(
                schemas.StrSchema
            ):
                pass
            ExchangeRate = schemas.NumberSchema
            
            
            class TargetCurrency(
                schemas.StrSchema
            ):
                pass
            
            
            class UnitCurrency(
                schemas.StrSchema
            ):
                pass
            
            
            class ContractIdentification(
                schemas.StrSchema
            ):
                pass
            QuotationDate = schemas.DateTimeSchema
        
            @staticmethod
            def InstructedAmount() -> typing.Type['OBCurrencyExchange5InstructedAmount']:
                return OBCurrencyExchange5InstructedAmount
            __annotations__ = {
                "SourceCurrency": SourceCurrency,
                "ExchangeRate": ExchangeRate,
                "TargetCurrency": TargetCurrency,
                "UnitCurrency": UnitCurrency,
                "ContractIdentification": ContractIdentification,
                "QuotationDate": QuotationDate,
                "InstructedAmount": InstructedAmount,
            }
    
    SourceCurrency: MetaOapg.properties.SourceCurrency
    ExchangeRate: MetaOapg.properties.ExchangeRate
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SourceCurrency"]) -> MetaOapg.properties.SourceCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ExchangeRate"]) -> MetaOapg.properties.ExchangeRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TargetCurrency"]) -> MetaOapg.properties.TargetCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UnitCurrency"]) -> MetaOapg.properties.UnitCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ContractIdentification"]) -> MetaOapg.properties.ContractIdentification: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["QuotationDate"]) -> MetaOapg.properties.QuotationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["InstructedAmount"]) -> 'OBCurrencyExchange5InstructedAmount': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["SourceCurrency", "ExchangeRate", "TargetCurrency", "UnitCurrency", "ContractIdentification", "QuotationDate", "InstructedAmount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SourceCurrency"]) -> MetaOapg.properties.SourceCurrency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ExchangeRate"]) -> MetaOapg.properties.ExchangeRate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TargetCurrency"]) -> typing.Union[MetaOapg.properties.TargetCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UnitCurrency"]) -> typing.Union[MetaOapg.properties.UnitCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ContractIdentification"]) -> typing.Union[MetaOapg.properties.ContractIdentification, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["QuotationDate"]) -> typing.Union[MetaOapg.properties.QuotationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["InstructedAmount"]) -> typing.Union['OBCurrencyExchange5InstructedAmount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["SourceCurrency", "ExchangeRate", "TargetCurrency", "UnitCurrency", "ContractIdentification", "QuotationDate", "InstructedAmount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        SourceCurrency: typing.Union[MetaOapg.properties.SourceCurrency, str, ],
        ExchangeRate: typing.Union[MetaOapg.properties.ExchangeRate, decimal.Decimal, int, float, ],
        TargetCurrency: typing.Union[MetaOapg.properties.TargetCurrency, str, schemas.Unset] = schemas.unset,
        UnitCurrency: typing.Union[MetaOapg.properties.UnitCurrency, str, schemas.Unset] = schemas.unset,
        ContractIdentification: typing.Union[MetaOapg.properties.ContractIdentification, str, schemas.Unset] = schemas.unset,
        QuotationDate: typing.Union[MetaOapg.properties.QuotationDate, str, datetime, schemas.Unset] = schemas.unset,
        InstructedAmount: typing.Union['OBCurrencyExchange5InstructedAmount', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBCurrencyExchange5':
        return super().__new__(
            cls,
            *args,
            SourceCurrency=SourceCurrency,
            ExchangeRate=ExchangeRate,
            TargetCurrency=TargetCurrency,
            UnitCurrency=UnitCurrency,
            ContractIdentification=ContractIdentification,
            QuotationDate=QuotationDate,
            InstructedAmount=InstructedAmount,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.ob_currency_exchange5_instructed_amount import OBCurrencyExchange5InstructedAmount
