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


class OBReadConsentResponse1Data(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "Status",
            "StatusUpdateDateTime",
            "CreationDateTime",
            "Permissions",
            "ConsentId",
        }
        
        class properties:
            
            
            class ConsentId(
                schemas.StrSchema
            ):
                pass
            CreationDateTime = schemas.DateTimeSchema
            
            
            class Status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AUTHORISED(cls):
                    return cls("Authorised")
                
                @schemas.classproperty
                def AWAITING_AUTHORISATION(cls):
                    return cls("AwaitingAuthorisation")
                
                @schemas.classproperty
                def REJECTED(cls):
                    return cls("Rejected")
                
                @schemas.classproperty
                def REVOKED(cls):
                    return cls("Revoked")
            StatusUpdateDateTime = schemas.DateTimeSchema
        
            @staticmethod
            def Permissions() -> typing.Type['OBReadConsentResponse1DataPermissions']:
                return OBReadConsentResponse1DataPermissions
            ExpirationDateTime = schemas.DateTimeSchema
            TransactionFromDateTime = schemas.DateTimeSchema
            TransactionToDateTime = schemas.DateTimeSchema
            __annotations__ = {
                "ConsentId": ConsentId,
                "CreationDateTime": CreationDateTime,
                "Status": Status,
                "StatusUpdateDateTime": StatusUpdateDateTime,
                "Permissions": Permissions,
                "ExpirationDateTime": ExpirationDateTime,
                "TransactionFromDateTime": TransactionFromDateTime,
                "TransactionToDateTime": TransactionToDateTime,
            }
    
    Status: MetaOapg.properties.Status
    StatusUpdateDateTime: MetaOapg.properties.StatusUpdateDateTime
    CreationDateTime: MetaOapg.properties.CreationDateTime
    Permissions: 'OBReadConsentResponse1DataPermissions'
    ConsentId: MetaOapg.properties.ConsentId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ConsentId"]) -> MetaOapg.properties.ConsentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreationDateTime"]) -> MetaOapg.properties.CreationDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Status"]) -> MetaOapg.properties.Status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatusUpdateDateTime"]) -> MetaOapg.properties.StatusUpdateDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Permissions"]) -> 'OBReadConsentResponse1DataPermissions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ExpirationDateTime"]) -> MetaOapg.properties.ExpirationDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TransactionFromDateTime"]) -> MetaOapg.properties.TransactionFromDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TransactionToDateTime"]) -> MetaOapg.properties.TransactionToDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ConsentId", "CreationDateTime", "Status", "StatusUpdateDateTime", "Permissions", "ExpirationDateTime", "TransactionFromDateTime", "TransactionToDateTime", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ConsentId"]) -> MetaOapg.properties.ConsentId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreationDateTime"]) -> MetaOapg.properties.CreationDateTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Status"]) -> MetaOapg.properties.Status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatusUpdateDateTime"]) -> MetaOapg.properties.StatusUpdateDateTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Permissions"]) -> 'OBReadConsentResponse1DataPermissions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ExpirationDateTime"]) -> typing.Union[MetaOapg.properties.ExpirationDateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TransactionFromDateTime"]) -> typing.Union[MetaOapg.properties.TransactionFromDateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TransactionToDateTime"]) -> typing.Union[MetaOapg.properties.TransactionToDateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ConsentId", "CreationDateTime", "Status", "StatusUpdateDateTime", "Permissions", "ExpirationDateTime", "TransactionFromDateTime", "TransactionToDateTime", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Status: typing.Union[MetaOapg.properties.Status, str, ],
        StatusUpdateDateTime: typing.Union[MetaOapg.properties.StatusUpdateDateTime, str, datetime, ],
        CreationDateTime: typing.Union[MetaOapg.properties.CreationDateTime, str, datetime, ],
        Permissions: 'OBReadConsentResponse1DataPermissions',
        ConsentId: typing.Union[MetaOapg.properties.ConsentId, str, ],
        ExpirationDateTime: typing.Union[MetaOapg.properties.ExpirationDateTime, str, datetime, schemas.Unset] = schemas.unset,
        TransactionFromDateTime: typing.Union[MetaOapg.properties.TransactionFromDateTime, str, datetime, schemas.Unset] = schemas.unset,
        TransactionToDateTime: typing.Union[MetaOapg.properties.TransactionToDateTime, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadConsentResponse1Data':
        return super().__new__(
            cls,
            *args,
            Status=Status,
            StatusUpdateDateTime=StatusUpdateDateTime,
            CreationDateTime=CreationDateTime,
            Permissions=Permissions,
            ConsentId=ConsentId,
            ExpirationDateTime=ExpirationDateTime,
            TransactionFromDateTime=TransactionFromDateTime,
            TransactionToDateTime=TransactionToDateTime,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.ob_read_consent_response1_data_permissions import OBReadConsentResponse1DataPermissions
