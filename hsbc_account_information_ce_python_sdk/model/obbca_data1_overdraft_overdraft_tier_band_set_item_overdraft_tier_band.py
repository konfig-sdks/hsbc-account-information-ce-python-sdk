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


class OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBand(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Provides overdraft details for a specific tier or band
    """


    class MetaOapg:
        min_items = 1
        
        @staticmethod
        def items() -> typing.Type['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem']:
            return OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem'], typing.List['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBand':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem':
        return super().__getitem__(i)

from hsbc_account_information_ce_python_sdk.model.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem
