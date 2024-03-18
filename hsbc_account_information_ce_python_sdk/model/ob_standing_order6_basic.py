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


class OBStandingOrder6Basic(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "AccountId",
            "Frequency",
        }
        
        class properties:
        
            @staticmethod
            def AccountId() -> typing.Type['AccountId']:
                return AccountId
        
            @staticmethod
            def Frequency() -> typing.Type['Frequency1']:
                return Frequency1
        
            @staticmethod
            def StandingOrderId() -> typing.Type['StandingOrderId']:
                return StandingOrderId
        
            @staticmethod
            def Reference() -> typing.Type['Reference']:
                return Reference
            FirstPaymentDateTime = schemas.DateTimeSchema
            NextPaymentDateTime = schemas.DateTimeSchema
            LastPaymentDateTime = schemas.DateTimeSchema
            FinalPaymentDateTime = schemas.DateTimeSchema
        
            @staticmethod
            def NumberOfPayments() -> typing.Type['NumberOfPayments']:
                return NumberOfPayments
        
            @staticmethod
            def StandingOrderStatusCode() -> typing.Type['OBExternalStandingOrderStatus1Code']:
                return OBExternalStandingOrderStatus1Code
        
            @staticmethod
            def FirstPaymentAmount() -> typing.Type['OBActiveOrHistoricCurrencyAndAmount2']:
                return OBActiveOrHistoricCurrencyAndAmount2
        
            @staticmethod
            def NextPaymentAmount() -> typing.Type['OBActiveOrHistoricCurrencyAndAmount3']:
                return OBActiveOrHistoricCurrencyAndAmount3
        
            @staticmethod
            def LastPaymentAmount() -> typing.Type['OBActiveOrHistoricCurrencyAndAmount11']:
                return OBActiveOrHistoricCurrencyAndAmount11
        
            @staticmethod
            def FinalPaymentAmount() -> typing.Type['OBActiveOrHistoricCurrencyAndAmount4']:
                return OBActiveOrHistoricCurrencyAndAmount4
        
            @staticmethod
            def SupplementaryData() -> typing.Type['OBSupplementaryData1']:
                return OBSupplementaryData1
            __annotations__ = {
                "AccountId": AccountId,
                "Frequency": Frequency,
                "StandingOrderId": StandingOrderId,
                "Reference": Reference,
                "FirstPaymentDateTime": FirstPaymentDateTime,
                "NextPaymentDateTime": NextPaymentDateTime,
                "LastPaymentDateTime": LastPaymentDateTime,
                "FinalPaymentDateTime": FinalPaymentDateTime,
                "NumberOfPayments": NumberOfPayments,
                "StandingOrderStatusCode": StandingOrderStatusCode,
                "FirstPaymentAmount": FirstPaymentAmount,
                "NextPaymentAmount": NextPaymentAmount,
                "LastPaymentAmount": LastPaymentAmount,
                "FinalPaymentAmount": FinalPaymentAmount,
                "SupplementaryData": SupplementaryData,
            }
    
    AccountId: 'AccountId'
    Frequency: 'Frequency1'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Frequency"]) -> 'Frequency1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StandingOrderId"]) -> 'StandingOrderId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Reference"]) -> 'Reference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FirstPaymentDateTime"]) -> MetaOapg.properties.FirstPaymentDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NextPaymentDateTime"]) -> MetaOapg.properties.NextPaymentDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastPaymentDateTime"]) -> MetaOapg.properties.LastPaymentDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FinalPaymentDateTime"]) -> MetaOapg.properties.FinalPaymentDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NumberOfPayments"]) -> 'NumberOfPayments': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StandingOrderStatusCode"]) -> 'OBExternalStandingOrderStatus1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FirstPaymentAmount"]) -> 'OBActiveOrHistoricCurrencyAndAmount2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NextPaymentAmount"]) -> 'OBActiveOrHistoricCurrencyAndAmount3': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastPaymentAmount"]) -> 'OBActiveOrHistoricCurrencyAndAmount11': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FinalPaymentAmount"]) -> 'OBActiveOrHistoricCurrencyAndAmount4': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SupplementaryData"]) -> 'OBSupplementaryData1': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AccountId", "Frequency", "StandingOrderId", "Reference", "FirstPaymentDateTime", "NextPaymentDateTime", "LastPaymentDateTime", "FinalPaymentDateTime", "NumberOfPayments", "StandingOrderStatusCode", "FirstPaymentAmount", "NextPaymentAmount", "LastPaymentAmount", "FinalPaymentAmount", "SupplementaryData", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Frequency"]) -> 'Frequency1': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StandingOrderId"]) -> typing.Union['StandingOrderId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Reference"]) -> typing.Union['Reference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FirstPaymentDateTime"]) -> typing.Union[MetaOapg.properties.FirstPaymentDateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NextPaymentDateTime"]) -> typing.Union[MetaOapg.properties.NextPaymentDateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastPaymentDateTime"]) -> typing.Union[MetaOapg.properties.LastPaymentDateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FinalPaymentDateTime"]) -> typing.Union[MetaOapg.properties.FinalPaymentDateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NumberOfPayments"]) -> typing.Union['NumberOfPayments', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StandingOrderStatusCode"]) -> typing.Union['OBExternalStandingOrderStatus1Code', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FirstPaymentAmount"]) -> typing.Union['OBActiveOrHistoricCurrencyAndAmount2', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NextPaymentAmount"]) -> typing.Union['OBActiveOrHistoricCurrencyAndAmount3', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastPaymentAmount"]) -> typing.Union['OBActiveOrHistoricCurrencyAndAmount11', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FinalPaymentAmount"]) -> typing.Union['OBActiveOrHistoricCurrencyAndAmount4', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SupplementaryData"]) -> typing.Union['OBSupplementaryData1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AccountId", "Frequency", "StandingOrderId", "Reference", "FirstPaymentDateTime", "NextPaymentDateTime", "LastPaymentDateTime", "FinalPaymentDateTime", "NumberOfPayments", "StandingOrderStatusCode", "FirstPaymentAmount", "NextPaymentAmount", "LastPaymentAmount", "FinalPaymentAmount", "SupplementaryData", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        AccountId: 'AccountId',
        Frequency: 'Frequency1',
        StandingOrderId: typing.Union['StandingOrderId', schemas.Unset] = schemas.unset,
        Reference: typing.Union['Reference', schemas.Unset] = schemas.unset,
        FirstPaymentDateTime: typing.Union[MetaOapg.properties.FirstPaymentDateTime, str, datetime, schemas.Unset] = schemas.unset,
        NextPaymentDateTime: typing.Union[MetaOapg.properties.NextPaymentDateTime, str, datetime, schemas.Unset] = schemas.unset,
        LastPaymentDateTime: typing.Union[MetaOapg.properties.LastPaymentDateTime, str, datetime, schemas.Unset] = schemas.unset,
        FinalPaymentDateTime: typing.Union[MetaOapg.properties.FinalPaymentDateTime, str, datetime, schemas.Unset] = schemas.unset,
        NumberOfPayments: typing.Union['NumberOfPayments', schemas.Unset] = schemas.unset,
        StandingOrderStatusCode: typing.Union['OBExternalStandingOrderStatus1Code', schemas.Unset] = schemas.unset,
        FirstPaymentAmount: typing.Union['OBActiveOrHistoricCurrencyAndAmount2', schemas.Unset] = schemas.unset,
        NextPaymentAmount: typing.Union['OBActiveOrHistoricCurrencyAndAmount3', schemas.Unset] = schemas.unset,
        LastPaymentAmount: typing.Union['OBActiveOrHistoricCurrencyAndAmount11', schemas.Unset] = schemas.unset,
        FinalPaymentAmount: typing.Union['OBActiveOrHistoricCurrencyAndAmount4', schemas.Unset] = schemas.unset,
        SupplementaryData: typing.Union['OBSupplementaryData1', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBStandingOrder6Basic':
        return super().__new__(
            cls,
            *args,
            AccountId=AccountId,
            Frequency=Frequency,
            StandingOrderId=StandingOrderId,
            Reference=Reference,
            FirstPaymentDateTime=FirstPaymentDateTime,
            NextPaymentDateTime=NextPaymentDateTime,
            LastPaymentDateTime=LastPaymentDateTime,
            FinalPaymentDateTime=FinalPaymentDateTime,
            NumberOfPayments=NumberOfPayments,
            StandingOrderStatusCode=StandingOrderStatusCode,
            FirstPaymentAmount=FirstPaymentAmount,
            NextPaymentAmount=NextPaymentAmount,
            LastPaymentAmount=LastPaymentAmount,
            FinalPaymentAmount=FinalPaymentAmount,
            SupplementaryData=SupplementaryData,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.account_id import AccountId
from hsbc_account_information_ce_python_sdk.model.frequency1 import Frequency1
from hsbc_account_information_ce_python_sdk.model.number_of_payments import NumberOfPayments
from hsbc_account_information_ce_python_sdk.model.ob_active_or_historic_currency_and_amount11 import OBActiveOrHistoricCurrencyAndAmount11
from hsbc_account_information_ce_python_sdk.model.ob_active_or_historic_currency_and_amount2 import OBActiveOrHistoricCurrencyAndAmount2
from hsbc_account_information_ce_python_sdk.model.ob_active_or_historic_currency_and_amount3 import OBActiveOrHistoricCurrencyAndAmount3
from hsbc_account_information_ce_python_sdk.model.ob_active_or_historic_currency_and_amount4 import OBActiveOrHistoricCurrencyAndAmount4
from hsbc_account_information_ce_python_sdk.model.ob_external_standing_order_status1_code import OBExternalStandingOrderStatus1Code
from hsbc_account_information_ce_python_sdk.model.ob_supplementary_data1 import OBSupplementaryData1
from hsbc_account_information_ce_python_sdk.model.reference import Reference
from hsbc_account_information_ce_python_sdk.model.standing_order_id import StandingOrderId
