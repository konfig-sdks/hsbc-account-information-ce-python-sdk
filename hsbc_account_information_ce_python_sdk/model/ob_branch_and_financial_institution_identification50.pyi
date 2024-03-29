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


class OBBranchAndFinancialInstitutionIdentification50(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Party that manages the account on behalf of the account owner, that is manages the registration and booking of entries on the account, calculates balances on the account and provides information about the account.
    """


    class MetaOapg:
        required = {
            "Identification",
            "SchemeName",
        }
        
        class properties:
        
            @staticmethod
            def SchemeName() -> typing.Type['OBExternalFinancialInstitutionIdentification4Code']:
                return OBExternalFinancialInstitutionIdentification4Code
        
            @staticmethod
            def Identification() -> typing.Type['Identification1']:
                return Identification1
            __annotations__ = {
                "SchemeName": SchemeName,
                "Identification": Identification,
            }
    
    Identification: 'Identification1'
    SchemeName: 'OBExternalFinancialInstitutionIdentification4Code'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SchemeName"]) -> 'OBExternalFinancialInstitutionIdentification4Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Identification"]) -> 'Identification1': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["SchemeName", "Identification", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SchemeName"]) -> 'OBExternalFinancialInstitutionIdentification4Code': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Identification"]) -> 'Identification1': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["SchemeName", "Identification", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Identification: 'Identification1',
        SchemeName: 'OBExternalFinancialInstitutionIdentification4Code',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBBranchAndFinancialInstitutionIdentification50':
        return super().__new__(
            cls,
            *args,
            Identification=Identification,
            SchemeName=SchemeName,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.identification1 import Identification1
from hsbc_account_information_ce_python_sdk.model.ob_external_financial_institution_identification4_code import OBExternalFinancialInstitutionIdentification4Code
