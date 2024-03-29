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


class OBBeneficiary5(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    TO DO
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def AccountId() -> typing.Type['AccountId']:
                return AccountId
        
            @staticmethod
            def BeneficiaryId() -> typing.Type['BeneficiaryId']:
                return BeneficiaryId
        
            @staticmethod
            def BeneficiaryType() -> typing.Type['OBBeneficiaryType1Code']:
                return OBBeneficiaryType1Code
        
            @staticmethod
            def Reference() -> typing.Type['Reference']:
                return Reference
        
            @staticmethod
            def SupplementaryData() -> typing.Type['OBSupplementaryData1']:
                return OBSupplementaryData1
        
            @staticmethod
            def CreditorAgent() -> typing.Type['OBBranchAndFinancialInstitutionIdentification60']:
                return OBBranchAndFinancialInstitutionIdentification60
        
            @staticmethod
            def CreditorAccount() -> typing.Type['OBCashAccount50']:
                return OBCashAccount50
            __annotations__ = {
                "AccountId": AccountId,
                "BeneficiaryId": BeneficiaryId,
                "BeneficiaryType": BeneficiaryType,
                "Reference": Reference,
                "SupplementaryData": SupplementaryData,
                "CreditorAgent": CreditorAgent,
                "CreditorAccount": CreditorAccount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BeneficiaryId"]) -> 'BeneficiaryId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BeneficiaryType"]) -> 'OBBeneficiaryType1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Reference"]) -> 'Reference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SupplementaryData"]) -> 'OBSupplementaryData1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditorAgent"]) -> 'OBBranchAndFinancialInstitutionIdentification60': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditorAccount"]) -> 'OBCashAccount50': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AccountId", "BeneficiaryId", "BeneficiaryType", "Reference", "SupplementaryData", "CreditorAgent", "CreditorAccount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountId"]) -> typing.Union['AccountId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BeneficiaryId"]) -> typing.Union['BeneficiaryId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BeneficiaryType"]) -> typing.Union['OBBeneficiaryType1Code', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Reference"]) -> typing.Union['Reference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SupplementaryData"]) -> typing.Union['OBSupplementaryData1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditorAgent"]) -> typing.Union['OBBranchAndFinancialInstitutionIdentification60', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditorAccount"]) -> typing.Union['OBCashAccount50', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AccountId", "BeneficiaryId", "BeneficiaryType", "Reference", "SupplementaryData", "CreditorAgent", "CreditorAccount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        AccountId: typing.Union['AccountId', schemas.Unset] = schemas.unset,
        BeneficiaryId: typing.Union['BeneficiaryId', schemas.Unset] = schemas.unset,
        BeneficiaryType: typing.Union['OBBeneficiaryType1Code', schemas.Unset] = schemas.unset,
        Reference: typing.Union['Reference', schemas.Unset] = schemas.unset,
        SupplementaryData: typing.Union['OBSupplementaryData1', schemas.Unset] = schemas.unset,
        CreditorAgent: typing.Union['OBBranchAndFinancialInstitutionIdentification60', schemas.Unset] = schemas.unset,
        CreditorAccount: typing.Union['OBCashAccount50', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBBeneficiary5':
        return super().__new__(
            cls,
            *args,
            AccountId=AccountId,
            BeneficiaryId=BeneficiaryId,
            BeneficiaryType=BeneficiaryType,
            Reference=Reference,
            SupplementaryData=SupplementaryData,
            CreditorAgent=CreditorAgent,
            CreditorAccount=CreditorAccount,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.account_id import AccountId
from hsbc_account_information_ce_python_sdk.model.beneficiary_id import BeneficiaryId
from hsbc_account_information_ce_python_sdk.model.ob_beneficiary_type1_code import OBBeneficiaryType1Code
from hsbc_account_information_ce_python_sdk.model.ob_branch_and_financial_institution_identification60 import OBBranchAndFinancialInstitutionIdentification60
from hsbc_account_information_ce_python_sdk.model.ob_cash_account50 import OBCashAccount50
from hsbc_account_information_ce_python_sdk.model.ob_supplementary_data1 import OBSupplementaryData1
from hsbc_account_information_ce_python_sdk.model.reference import Reference
