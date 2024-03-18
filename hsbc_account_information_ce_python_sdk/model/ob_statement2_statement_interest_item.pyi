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


class OBStatement2StatementInterestItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Set of elements used to provide details of a generic interest amount related to the statement resource.
    """


    class MetaOapg:
        required = {
            "Type",
            "Amount",
            "CreditDebitIndicator",
        }
        
        class properties:
        
            @staticmethod
            def CreditDebitIndicator() -> typing.Type['OBCreditDebitCode0']:
                return OBCreditDebitCode0
        
            @staticmethod
            def Type() -> typing.Type['OBExternalStatementInterestType1Code']:
                return OBExternalStatementInterestType1Code
        
            @staticmethod
            def Amount() -> typing.Type['OBActiveOrHistoricCurrencyAndAmount7']:
                return OBActiveOrHistoricCurrencyAndAmount7
        
            @staticmethod
            def Description() -> typing.Type['Description2']:
                return Description2
            Rate = schemas.NumberSchema
        
            @staticmethod
            def RateType() -> typing.Type['OBExternalStatementInterestRateType1Code']:
                return OBExternalStatementInterestRateType1Code
        
            @staticmethod
            def Frequency() -> typing.Type['OBExternalStatementInterestFrequency1Code']:
                return OBExternalStatementInterestFrequency1Code
            __annotations__ = {
                "CreditDebitIndicator": CreditDebitIndicator,
                "Type": Type,
                "Amount": Amount,
                "Description": Description,
                "Rate": Rate,
                "RateType": RateType,
                "Frequency": Frequency,
            }
    
    Type: 'OBExternalStatementInterestType1Code'
    Amount: 'OBActiveOrHistoricCurrencyAndAmount7'
    CreditDebitIndicator: 'OBCreditDebitCode0'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditDebitIndicator"]) -> 'OBCreditDebitCode0': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> 'OBExternalStatementInterestType1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Amount"]) -> 'OBActiveOrHistoricCurrencyAndAmount7': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> 'Description2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Rate"]) -> MetaOapg.properties.Rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RateType"]) -> 'OBExternalStatementInterestRateType1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Frequency"]) -> 'OBExternalStatementInterestFrequency1Code': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["CreditDebitIndicator", "Type", "Amount", "Description", "Rate", "RateType", "Frequency", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditDebitIndicator"]) -> 'OBCreditDebitCode0': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> 'OBExternalStatementInterestType1Code': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Amount"]) -> 'OBActiveOrHistoricCurrencyAndAmount7': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> typing.Union['Description2', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Rate"]) -> typing.Union[MetaOapg.properties.Rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RateType"]) -> typing.Union['OBExternalStatementInterestRateType1Code', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Frequency"]) -> typing.Union['OBExternalStatementInterestFrequency1Code', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["CreditDebitIndicator", "Type", "Amount", "Description", "Rate", "RateType", "Frequency", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Type: 'OBExternalStatementInterestType1Code',
        Amount: 'OBActiveOrHistoricCurrencyAndAmount7',
        CreditDebitIndicator: 'OBCreditDebitCode0',
        Description: typing.Union['Description2', schemas.Unset] = schemas.unset,
        Rate: typing.Union[MetaOapg.properties.Rate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        RateType: typing.Union['OBExternalStatementInterestRateType1Code', schemas.Unset] = schemas.unset,
        Frequency: typing.Union['OBExternalStatementInterestFrequency1Code', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBStatement2StatementInterestItem':
        return super().__new__(
            cls,
            *args,
            Type=Type,
            Amount=Amount,
            CreditDebitIndicator=CreditDebitIndicator,
            Description=Description,
            Rate=Rate,
            RateType=RateType,
            Frequency=Frequency,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.description2 import Description2
from hsbc_account_information_ce_python_sdk.model.ob_active_or_historic_currency_and_amount7 import OBActiveOrHistoricCurrencyAndAmount7
from hsbc_account_information_ce_python_sdk.model.ob_credit_debit_code0 import OBCreditDebitCode0
from hsbc_account_information_ce_python_sdk.model.ob_external_statement_interest_frequency1_code import OBExternalStatementInterestFrequency1Code
from hsbc_account_information_ce_python_sdk.model.ob_external_statement_interest_rate_type1_code import OBExternalStatementInterestRateType1Code
from hsbc_account_information_ce_python_sdk.model.ob_external_statement_interest_type1_code import OBExternalStatementInterestType1Code
