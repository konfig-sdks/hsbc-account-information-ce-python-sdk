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


class OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeType(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Fee/charge type which is being capped
    """


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def ARRANGED_OVERDRAFT(cls):
                return cls("ArrangedOverdraft")
            
            @schemas.classproperty
            def EMERGENCY_BORROWING(cls):
                return cls("EmergencyBorrowing")
            
            @schemas.classproperty
            def BORROWING_ITEM(cls):
                return cls("BorrowingItem")
            
            @schemas.classproperty
            def OVERDRAFT_RENEWAL(cls):
                return cls("OverdraftRenewal")
            
            @schemas.classproperty
            def ANNUAL_REVIEW(cls):
                return cls("AnnualReview")
            
            @schemas.classproperty
            def OVERDRAFT_SETUP(cls):
                return cls("OverdraftSetup")
            
            @schemas.classproperty
            def SURCHARGE(cls):
                return cls("Surcharge")
            
            @schemas.classproperty
            def TEMP_OVERDRAFT(cls):
                return cls("TempOverdraft")
            
            @schemas.classproperty
            def UNAUTHORISED_BORROWING(cls):
                return cls("UnauthorisedBorrowing")
            
            @schemas.classproperty
            def UNAUTHORISED_PAID_TRANS(cls):
                return cls("UnauthorisedPaidTrans")
            
            @schemas.classproperty
            def OTHER(cls):
                return cls("Other")
            
            @schemas.classproperty
            def UNAUTHORISED_UNPAID_TRANS(cls):
                return cls("UnauthorisedUnpaidTrans")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeType':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
