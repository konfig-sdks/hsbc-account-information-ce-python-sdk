# coding: utf-8

"""
    Account Information API

    In this document, you'll find the steps your organization needs to take to use our API services. Included in this guide are details of request and response messages used to support your organization’s integration. The intended audience for this document are **Technical Architects**, **Development Engineers**, **Test Engineers**, and **Operation & Maintenance Engineers** involved in development and support of your organization’s integration. Setting up our API Services is best completed with the assistance of your organization’s IT team, or someone with experience and knowledge of application programming interfaces. This should include experience with **JSON payloads**, **security** and **public key infrastructure (PKI)**. This Document describes the following request and response structure of HSBCnet - Account Information API. For detail implementation guidelines, please refer to the respective section from [develop.hsbc.com](https://develop.hsbc.com/ob-api-documentation/account-information-uk-personal-v319) 

    The version of the OpenAPI document: 3.1.11
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from hsbc_account_information_ce_python_sdk.pydantic.ob_read_consent_response1_data_permissions import OBReadConsentResponse1DataPermissions

class OBReadConsentResponse1Data(BaseModel):
    # Unique identification as assigned to identify the account access consent resource.
    consent_id: str = Field(alias='ConsentId')

    # Date and time at which the resource was created.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    creation_date_time: datetime = Field(alias='CreationDateTime')

    # Specifies the status of consent resource in code form.
    status: Literal["Authorised", "AwaitingAuthorisation", "Rejected", "Revoked"] = Field(alias='Status')

    # Date and time at which the resource status was updated.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    status_update_date_time: datetime = Field(alias='StatusUpdateDateTime')

    permissions: OBReadConsentResponse1DataPermissions = Field(alias='Permissions')

    # Specified date and time the permissions will expire. If this is not populated, the permissions will be open ended.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    expiration_date_time: typing.Optional[datetime] = Field(None, alias='ExpirationDateTime')

    # Specified start date and time for the transaction query period. If this is not populated, the start date will be open ended, and data will be returned from the earliest available transaction.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    transaction_from_date_time: typing.Optional[datetime] = Field(None, alias='TransactionFromDateTime')

    # Specified end date and time for the transaction query period. If this is not populated, the end date will be open ended, and data will be returned to the latest available transaction.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    transaction_to_date_time: typing.Optional[datetime] = Field(None, alias='TransactionToDateTime')
    class Config:
        arbitrary_types_allowed = True