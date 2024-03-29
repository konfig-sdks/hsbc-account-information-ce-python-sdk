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


class OBReadProduct2DataProductItemOtherProductType(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Other product type details associated with the account.
    """


    class MetaOapg:
        required = {
            "Description",
            "Name",
        }
        
        class properties:
            
            
            class Name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 350
                    min_length = 1
            
            
            class Description(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 350
                    min_length = 1
        
            @staticmethod
            def ProductDetails() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeProductDetails']:
                return OBReadProduct2DataProductItemOtherProductTypeProductDetails
        
            @staticmethod
            def CreditInterest() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeCreditInterest']:
                return OBReadProduct2DataProductItemOtherProductTypeCreditInterest
        
            @staticmethod
            def Overdraft() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeOverdraft']:
                return OBReadProduct2DataProductItemOtherProductTypeOverdraft
        
            @staticmethod
            def LoanInterest() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeLoanInterest']:
                return OBReadProduct2DataProductItemOtherProductTypeLoanInterest
        
            @staticmethod
            def Repayment() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeRepayment']:
                return OBReadProduct2DataProductItemOtherProductTypeRepayment
        
            @staticmethod
            def OtherFeesCharges() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeOtherFeesCharges']:
                return OBReadProduct2DataProductItemOtherProductTypeOtherFeesCharges
        
            @staticmethod
            def SupplementaryData() -> typing.Type['OBSupplementaryData1']:
                return OBSupplementaryData1
            __annotations__ = {
                "Name": Name,
                "Description": Description,
                "ProductDetails": ProductDetails,
                "CreditInterest": CreditInterest,
                "Overdraft": Overdraft,
                "LoanInterest": LoanInterest,
                "Repayment": Repayment,
                "OtherFeesCharges": OtherFeesCharges,
                "SupplementaryData": SupplementaryData,
            }
    
    Description: MetaOapg.properties.Description
    Name: MetaOapg.properties.Name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProductDetails"]) -> 'OBReadProduct2DataProductItemOtherProductTypeProductDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditInterest"]) -> 'OBReadProduct2DataProductItemOtherProductTypeCreditInterest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Overdraft"]) -> 'OBReadProduct2DataProductItemOtherProductTypeOverdraft': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LoanInterest"]) -> 'OBReadProduct2DataProductItemOtherProductTypeLoanInterest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Repayment"]) -> 'OBReadProduct2DataProductItemOtherProductTypeRepayment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherFeesCharges"]) -> 'OBReadProduct2DataProductItemOtherProductTypeOtherFeesCharges': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SupplementaryData"]) -> 'OBSupplementaryData1': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Name", "Description", "ProductDetails", "CreditInterest", "Overdraft", "LoanInterest", "Repayment", "OtherFeesCharges", "SupplementaryData", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProductDetails"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeProductDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditInterest"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeCreditInterest', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Overdraft"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeOverdraft', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LoanInterest"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeLoanInterest', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Repayment"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepayment', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherFeesCharges"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeOtherFeesCharges', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SupplementaryData"]) -> typing.Union['OBSupplementaryData1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Name", "Description", "ProductDetails", "CreditInterest", "Overdraft", "LoanInterest", "Repayment", "OtherFeesCharges", "SupplementaryData", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Description: typing.Union[MetaOapg.properties.Description, str, ],
        Name: typing.Union[MetaOapg.properties.Name, str, ],
        ProductDetails: typing.Union['OBReadProduct2DataProductItemOtherProductTypeProductDetails', schemas.Unset] = schemas.unset,
        CreditInterest: typing.Union['OBReadProduct2DataProductItemOtherProductTypeCreditInterest', schemas.Unset] = schemas.unset,
        Overdraft: typing.Union['OBReadProduct2DataProductItemOtherProductTypeOverdraft', schemas.Unset] = schemas.unset,
        LoanInterest: typing.Union['OBReadProduct2DataProductItemOtherProductTypeLoanInterest', schemas.Unset] = schemas.unset,
        Repayment: typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepayment', schemas.Unset] = schemas.unset,
        OtherFeesCharges: typing.Union['OBReadProduct2DataProductItemOtherProductTypeOtherFeesCharges', schemas.Unset] = schemas.unset,
        SupplementaryData: typing.Union['OBSupplementaryData1', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadProduct2DataProductItemOtherProductType':
        return super().__new__(
            cls,
            *args,
            Description=Description,
            Name=Name,
            ProductDetails=ProductDetails,
            CreditInterest=CreditInterest,
            Overdraft=Overdraft,
            LoanInterest=LoanInterest,
            Repayment=Repayment,
            OtherFeesCharges=OtherFeesCharges,
            SupplementaryData=SupplementaryData,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.ob_read_product2_data_product_item_other_product_type_credit_interest import OBReadProduct2DataProductItemOtherProductTypeCreditInterest
from hsbc_account_information_ce_python_sdk.model.ob_read_product2_data_product_item_other_product_type_loan_interest import OBReadProduct2DataProductItemOtherProductTypeLoanInterest
from hsbc_account_information_ce_python_sdk.model.ob_read_product2_data_product_item_other_product_type_other_fees_charges import OBReadProduct2DataProductItemOtherProductTypeOtherFeesCharges
from hsbc_account_information_ce_python_sdk.model.ob_read_product2_data_product_item_other_product_type_overdraft import OBReadProduct2DataProductItemOtherProductTypeOverdraft
from hsbc_account_information_ce_python_sdk.model.ob_read_product2_data_product_item_other_product_type_product_details import OBReadProduct2DataProductItemOtherProductTypeProductDetails
from hsbc_account_information_ce_python_sdk.model.ob_read_product2_data_product_item_other_product_type_repayment import OBReadProduct2DataProductItemOtherProductTypeRepayment
from hsbc_account_information_ce_python_sdk.model.ob_supplementary_data1 import OBSupplementaryData1
