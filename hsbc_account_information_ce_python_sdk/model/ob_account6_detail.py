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


class OBAccount6Detail(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Unambiguous identification of the account to which credit and debit entries are made.
    """


    class MetaOapg:
        required = {
            "Account",
            "AccountId",
            "Currency",
            "AccountType",
            "AccountSubType",
        }
        
        class properties:
        
            @staticmethod
            def AccountId() -> typing.Type['AccountId']:
                return AccountId
        
            @staticmethod
            def Currency() -> typing.Type['ActiveOrHistoricCurrencyCode0']:
                return ActiveOrHistoricCurrencyCode0
        
            @staticmethod
            def AccountType() -> typing.Type['OBExternalAccountType1Code']:
                return OBExternalAccountType1Code
        
            @staticmethod
            def AccountSubType() -> typing.Type['OBExternalAccountSubType1Code']:
                return OBExternalAccountSubType1Code
        
            @staticmethod
            def Account() -> typing.Type['OBAccount6DetailAccount']:
                return OBAccount6DetailAccount
        
            @staticmethod
            def Status() -> typing.Type['OBAccountStatus1Code']:
                return OBAccountStatus1Code
            StatusUpdateDateTime = schemas.DateTimeSchema
        
            @staticmethod
            def Description() -> typing.Type['Description0']:
                return Description0
        
            @staticmethod
            def Nickname() -> typing.Type['Nickname']:
                return Nickname
            OpeningDate = schemas.DateTimeSchema
            MaturityDate = schemas.DateTimeSchema
        
            @staticmethod
            def SwitchStatus() -> typing.Type['OBExternalSwitchStatusCode']:
                return OBExternalSwitchStatusCode
        
            @staticmethod
            def Servicer() -> typing.Type['OBBranchAndFinancialInstitutionIdentification50']:
                return OBBranchAndFinancialInstitutionIdentification50
            __annotations__ = {
                "AccountId": AccountId,
                "Currency": Currency,
                "AccountType": AccountType,
                "AccountSubType": AccountSubType,
                "Account": Account,
                "Status": Status,
                "StatusUpdateDateTime": StatusUpdateDateTime,
                "Description": Description,
                "Nickname": Nickname,
                "OpeningDate": OpeningDate,
                "MaturityDate": MaturityDate,
                "SwitchStatus": SwitchStatus,
                "Servicer": Servicer,
            }
    
    Account: 'OBAccount6DetailAccount'
    AccountId: 'AccountId'
    Currency: 'ActiveOrHistoricCurrencyCode0'
    AccountType: 'OBExternalAccountType1Code'
    AccountSubType: 'OBExternalAccountSubType1Code'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Currency"]) -> 'ActiveOrHistoricCurrencyCode0': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountType"]) -> 'OBExternalAccountType1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountSubType"]) -> 'OBExternalAccountSubType1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Account"]) -> 'OBAccount6DetailAccount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Status"]) -> 'OBAccountStatus1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatusUpdateDateTime"]) -> MetaOapg.properties.StatusUpdateDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> 'Description0': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Nickname"]) -> 'Nickname': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OpeningDate"]) -> MetaOapg.properties.OpeningDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MaturityDate"]) -> MetaOapg.properties.MaturityDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SwitchStatus"]) -> 'OBExternalSwitchStatusCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Servicer"]) -> 'OBBranchAndFinancialInstitutionIdentification50': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AccountId", "Currency", "AccountType", "AccountSubType", "Account", "Status", "StatusUpdateDateTime", "Description", "Nickname", "OpeningDate", "MaturityDate", "SwitchStatus", "Servicer", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Currency"]) -> 'ActiveOrHistoricCurrencyCode0': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountType"]) -> 'OBExternalAccountType1Code': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountSubType"]) -> 'OBExternalAccountSubType1Code': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Account"]) -> 'OBAccount6DetailAccount': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Status"]) -> typing.Union['OBAccountStatus1Code', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatusUpdateDateTime"]) -> typing.Union[MetaOapg.properties.StatusUpdateDateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> typing.Union['Description0', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Nickname"]) -> typing.Union['Nickname', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OpeningDate"]) -> typing.Union[MetaOapg.properties.OpeningDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MaturityDate"]) -> typing.Union[MetaOapg.properties.MaturityDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SwitchStatus"]) -> typing.Union['OBExternalSwitchStatusCode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Servicer"]) -> typing.Union['OBBranchAndFinancialInstitutionIdentification50', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AccountId", "Currency", "AccountType", "AccountSubType", "Account", "Status", "StatusUpdateDateTime", "Description", "Nickname", "OpeningDate", "MaturityDate", "SwitchStatus", "Servicer", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Account: 'OBAccount6DetailAccount',
        AccountId: 'AccountId',
        Currency: 'ActiveOrHistoricCurrencyCode0',
        AccountType: 'OBExternalAccountType1Code',
        AccountSubType: 'OBExternalAccountSubType1Code',
        Status: typing.Union['OBAccountStatus1Code', schemas.Unset] = schemas.unset,
        StatusUpdateDateTime: typing.Union[MetaOapg.properties.StatusUpdateDateTime, str, datetime, schemas.Unset] = schemas.unset,
        Description: typing.Union['Description0', schemas.Unset] = schemas.unset,
        Nickname: typing.Union['Nickname', schemas.Unset] = schemas.unset,
        OpeningDate: typing.Union[MetaOapg.properties.OpeningDate, str, datetime, schemas.Unset] = schemas.unset,
        MaturityDate: typing.Union[MetaOapg.properties.MaturityDate, str, datetime, schemas.Unset] = schemas.unset,
        SwitchStatus: typing.Union['OBExternalSwitchStatusCode', schemas.Unset] = schemas.unset,
        Servicer: typing.Union['OBBranchAndFinancialInstitutionIdentification50', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBAccount6Detail':
        return super().__new__(
            cls,
            *args,
            Account=Account,
            AccountId=AccountId,
            Currency=Currency,
            AccountType=AccountType,
            AccountSubType=AccountSubType,
            Status=Status,
            StatusUpdateDateTime=StatusUpdateDateTime,
            Description=Description,
            Nickname=Nickname,
            OpeningDate=OpeningDate,
            MaturityDate=MaturityDate,
            SwitchStatus=SwitchStatus,
            Servicer=Servicer,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.account_id import AccountId
from hsbc_account_information_ce_python_sdk.model.active_or_historic_currency_code0 import ActiveOrHistoricCurrencyCode0
from hsbc_account_information_ce_python_sdk.model.description0 import Description0
from hsbc_account_information_ce_python_sdk.model.nickname import Nickname
from hsbc_account_information_ce_python_sdk.model.ob_account6_detail_account import OBAccount6DetailAccount
from hsbc_account_information_ce_python_sdk.model.ob_account_status1_code import OBAccountStatus1Code
from hsbc_account_information_ce_python_sdk.model.ob_branch_and_financial_institution_identification50 import OBBranchAndFinancialInstitutionIdentification50
from hsbc_account_information_ce_python_sdk.model.ob_external_account_sub_type1_code import OBExternalAccountSubType1Code
from hsbc_account_information_ce_python_sdk.model.ob_external_account_type1_code import OBExternalAccountType1Code
from hsbc_account_information_ce_python_sdk.model.ob_external_switch_status_code import OBExternalSwitchStatusCode
