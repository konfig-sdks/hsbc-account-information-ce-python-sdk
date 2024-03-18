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


class OBReadBalance1DataBalanceItemAmount(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Amount of money of the cash balance.
    """


    class MetaOapg:
        required = {
            "Amount",
            "Currency",
        }
        
        class properties:
        
            @staticmethod
            def Amount() -> typing.Type['OBActiveCurrencyAndAmountSimpleType']:
                return OBActiveCurrencyAndAmountSimpleType
        
            @staticmethod
            def Currency() -> typing.Type['ActiveOrHistoricCurrencyCode1']:
                return ActiveOrHistoricCurrencyCode1
            __annotations__ = {
                "Amount": Amount,
                "Currency": Currency,
            }
    
    Amount: 'OBActiveCurrencyAndAmountSimpleType'
    Currency: 'ActiveOrHistoricCurrencyCode1'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Amount"]) -> 'OBActiveCurrencyAndAmountSimpleType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Currency"]) -> 'ActiveOrHistoricCurrencyCode1': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Amount", "Currency", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Amount"]) -> 'OBActiveCurrencyAndAmountSimpleType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Currency"]) -> 'ActiveOrHistoricCurrencyCode1': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Amount", "Currency", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Amount: 'OBActiveCurrencyAndAmountSimpleType',
        Currency: 'ActiveOrHistoricCurrencyCode1',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadBalance1DataBalanceItemAmount':
        return super().__new__(
            cls,
            *args,
            Amount=Amount,
            Currency=Currency,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.active_or_historic_currency_code1 import ActiveOrHistoricCurrencyCode1
from hsbc_account_information_ce_python_sdk.model.ob_active_currency_and_amount_simple_type import OBActiveCurrencyAndAmountSimpleType