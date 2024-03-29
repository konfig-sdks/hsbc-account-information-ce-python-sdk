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


class OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemOtherLoanProviderInterestRateType(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Other loan interest rate types which are not available in the standard code list
    """


    class MetaOapg:
        required = {
            "Description",
            "Name",
        }
        
        class properties:
        
            @staticmethod
            def Name() -> typing.Type['Name4']:
                return Name4
        
            @staticmethod
            def Description() -> typing.Type['Description3']:
                return Description3
        
            @staticmethod
            def Code() -> typing.Type['OBCodeMnemonic']:
                return OBCodeMnemonic
            __annotations__ = {
                "Name": Name,
                "Description": Description,
                "Code": Code,
            }
    
    Description: 'Description3'
    Name: 'Name4'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> 'Name4': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> 'Description3': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Code"]) -> 'OBCodeMnemonic': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Name", "Description", "Code", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> 'Name4': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> 'Description3': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Code"]) -> typing.Union['OBCodeMnemonic', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Name", "Description", "Code", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Description: 'Description3',
        Name: 'Name4',
        Code: typing.Union['OBCodeMnemonic', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemOtherLoanProviderInterestRateType':
        return super().__new__(
            cls,
            *args,
            Description=Description,
            Name=Name,
            Code=Code,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.description3 import Description3
from hsbc_account_information_ce_python_sdk.model.name4 import Name4
from hsbc_account_information_ce_python_sdk.model.ob_code_mnemonic import OBCodeMnemonic
