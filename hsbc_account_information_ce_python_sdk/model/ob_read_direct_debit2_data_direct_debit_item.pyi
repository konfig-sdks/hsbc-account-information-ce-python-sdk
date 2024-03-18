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


class OBReadDirectDebit2DataDirectDebitItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Account to or from which a cash entry is made.
    """


    class MetaOapg:
        required = {
            "AccountId",
            "MandateIdentification",
            "Name",
        }
        
        class properties:
        
            @staticmethod
            def AccountId() -> typing.Type['AccountId']:
                return AccountId
        
            @staticmethod
            def MandateIdentification() -> typing.Type['MandateIdentification']:
                return MandateIdentification
        
            @staticmethod
            def Name() -> typing.Type['Name2']:
                return Name2
        
            @staticmethod
            def DirectDebitId() -> typing.Type['DirectDebitId']:
                return DirectDebitId
        
            @staticmethod
            def DirectDebitStatusCode() -> typing.Type['OBExternalDirectDebitStatus1Code']:
                return OBExternalDirectDebitStatus1Code
            PreviousPaymentDateTime = schemas.DateTimeSchema
            
            
            class Frequency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ANNUAL(cls):
                    return cls("UK.OBIE.Annual")
                
                @schemas.classproperty
                def DAILY(cls):
                    return cls("UK.OBIE.Daily")
                
                @schemas.classproperty
                def FORTNIGHTLY(cls):
                    return cls("UK.OBIE.Fortnightly")
                
                @schemas.classproperty
                def HALF_YEARLY(cls):
                    return cls("UK.OBIE.HalfYearly")
                
                @schemas.classproperty
                def MONTHLY(cls):
                    return cls("UK.OBIE.Monthly")
                
                @schemas.classproperty
                def NOT_KNOWN(cls):
                    return cls("UK.OBIE.NotKnown")
                
                @schemas.classproperty
                def QUARTERLY(cls):
                    return cls("UK.OBIE.Quarterly")
                
                @schemas.classproperty
                def WEEKLY(cls):
                    return cls("UK.OBIE.Weekly")
        
            @staticmethod
            def PreviousPaymentAmount() -> typing.Type['OBActiveOrHistoricCurrencyAndAmount0']:
                return OBActiveOrHistoricCurrencyAndAmount0
            __annotations__ = {
                "AccountId": AccountId,
                "MandateIdentification": MandateIdentification,
                "Name": Name,
                "DirectDebitId": DirectDebitId,
                "DirectDebitStatusCode": DirectDebitStatusCode,
                "PreviousPaymentDateTime": PreviousPaymentDateTime,
                "Frequency": Frequency,
                "PreviousPaymentAmount": PreviousPaymentAmount,
            }
    
    AccountId: 'AccountId'
    MandateIdentification: 'MandateIdentification'
    Name: 'Name2'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MandateIdentification"]) -> 'MandateIdentification': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> 'Name2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DirectDebitId"]) -> 'DirectDebitId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DirectDebitStatusCode"]) -> 'OBExternalDirectDebitStatus1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PreviousPaymentDateTime"]) -> MetaOapg.properties.PreviousPaymentDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Frequency"]) -> MetaOapg.properties.Frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PreviousPaymentAmount"]) -> 'OBActiveOrHistoricCurrencyAndAmount0': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AccountId", "MandateIdentification", "Name", "DirectDebitId", "DirectDebitStatusCode", "PreviousPaymentDateTime", "Frequency", "PreviousPaymentAmount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MandateIdentification"]) -> 'MandateIdentification': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> 'Name2': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DirectDebitId"]) -> typing.Union['DirectDebitId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DirectDebitStatusCode"]) -> typing.Union['OBExternalDirectDebitStatus1Code', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PreviousPaymentDateTime"]) -> typing.Union[MetaOapg.properties.PreviousPaymentDateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Frequency"]) -> typing.Union[MetaOapg.properties.Frequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PreviousPaymentAmount"]) -> typing.Union['OBActiveOrHistoricCurrencyAndAmount0', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AccountId", "MandateIdentification", "Name", "DirectDebitId", "DirectDebitStatusCode", "PreviousPaymentDateTime", "Frequency", "PreviousPaymentAmount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        AccountId: 'AccountId',
        MandateIdentification: 'MandateIdentification',
        Name: 'Name2',
        DirectDebitId: typing.Union['DirectDebitId', schemas.Unset] = schemas.unset,
        DirectDebitStatusCode: typing.Union['OBExternalDirectDebitStatus1Code', schemas.Unset] = schemas.unset,
        PreviousPaymentDateTime: typing.Union[MetaOapg.properties.PreviousPaymentDateTime, str, datetime, schemas.Unset] = schemas.unset,
        Frequency: typing.Union[MetaOapg.properties.Frequency, str, schemas.Unset] = schemas.unset,
        PreviousPaymentAmount: typing.Union['OBActiveOrHistoricCurrencyAndAmount0', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadDirectDebit2DataDirectDebitItem':
        return super().__new__(
            cls,
            *args,
            AccountId=AccountId,
            MandateIdentification=MandateIdentification,
            Name=Name,
            DirectDebitId=DirectDebitId,
            DirectDebitStatusCode=DirectDebitStatusCode,
            PreviousPaymentDateTime=PreviousPaymentDateTime,
            Frequency=Frequency,
            PreviousPaymentAmount=PreviousPaymentAmount,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.account_id import AccountId
from hsbc_account_information_ce_python_sdk.model.direct_debit_id import DirectDebitId
from hsbc_account_information_ce_python_sdk.model.mandate_identification import MandateIdentification
from hsbc_account_information_ce_python_sdk.model.name2 import Name2
from hsbc_account_information_ce_python_sdk.model.ob_active_or_historic_currency_and_amount0 import OBActiveOrHistoricCurrencyAndAmount0
from hsbc_account_information_ce_python_sdk.model.ob_external_direct_debit_status1_code import OBExternalDirectDebitStatus1Code
