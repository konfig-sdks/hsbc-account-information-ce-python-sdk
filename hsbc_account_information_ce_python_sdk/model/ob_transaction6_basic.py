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


class OBTransaction6Basic(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Provides further details on an entry in the report.
    """


    class MetaOapg:
        required = {
            "Status",
            "BookingDateTime",
            "AccountId",
            "Amount",
            "CreditDebitIndicator",
        }
        
        class properties:
        
            @staticmethod
            def AccountId() -> typing.Type['AccountId']:
                return AccountId
        
            @staticmethod
            def CreditDebitIndicator() -> typing.Type['OBCreditDebitCode1']:
                return OBCreditDebitCode1
        
            @staticmethod
            def Status() -> typing.Type['OBEntryStatus1Code']:
                return OBEntryStatus1Code
            BookingDateTime = schemas.DateTimeSchema
        
            @staticmethod
            def Amount() -> typing.Type['OBActiveOrHistoricCurrencyAndAmount9']:
                return OBActiveOrHistoricCurrencyAndAmount9
        
            @staticmethod
            def TransactionId() -> typing.Type['TransactionId']:
                return TransactionId
        
            @staticmethod
            def TransactionReference() -> typing.Type['TransactionReference']:
                return TransactionReference
            
            
            class StatementReference(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StatementReference']:
                        return StatementReference
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['StatementReference'], typing.List['StatementReference']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'StatementReference':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StatementReference':
                    return super().__getitem__(i)
        
            @staticmethod
            def TransactionMutability() -> typing.Type['OBTransactionMutability1Code']:
                return OBTransactionMutability1Code
            ValueDateTime = schemas.DateTimeSchema
        
            @staticmethod
            def AddressLine() -> typing.Type['AddressLine']:
                return AddressLine
        
            @staticmethod
            def ChargeAmount() -> typing.Type['OBActiveOrHistoricCurrencyAndAmount10']:
                return OBActiveOrHistoricCurrencyAndAmount10
        
            @staticmethod
            def CurrencyExchange() -> typing.Type['OBCurrencyExchange5']:
                return OBCurrencyExchange5
        
            @staticmethod
            def BankTransactionCode() -> typing.Type['OBBankTransactionCodeStructure1']:
                return OBBankTransactionCodeStructure1
        
            @staticmethod
            def ProprietaryBankTransactionCode() -> typing.Type['ProprietaryBankTransactionCodeStructure1']:
                return ProprietaryBankTransactionCodeStructure1
        
            @staticmethod
            def CardInstrument() -> typing.Type['OBTransactionCardInstrument1']:
                return OBTransactionCardInstrument1
        
            @staticmethod
            def SupplementaryData() -> typing.Type['OBSupplementaryData1']:
                return OBSupplementaryData1
            __annotations__ = {
                "AccountId": AccountId,
                "CreditDebitIndicator": CreditDebitIndicator,
                "Status": Status,
                "BookingDateTime": BookingDateTime,
                "Amount": Amount,
                "TransactionId": TransactionId,
                "TransactionReference": TransactionReference,
                "StatementReference": StatementReference,
                "TransactionMutability": TransactionMutability,
                "ValueDateTime": ValueDateTime,
                "AddressLine": AddressLine,
                "ChargeAmount": ChargeAmount,
                "CurrencyExchange": CurrencyExchange,
                "BankTransactionCode": BankTransactionCode,
                "ProprietaryBankTransactionCode": ProprietaryBankTransactionCode,
                "CardInstrument": CardInstrument,
                "SupplementaryData": SupplementaryData,
            }
    
    Status: 'OBEntryStatus1Code'
    BookingDateTime: MetaOapg.properties.BookingDateTime
    AccountId: 'AccountId'
    Amount: 'OBActiveOrHistoricCurrencyAndAmount9'
    CreditDebitIndicator: 'OBCreditDebitCode1'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditDebitIndicator"]) -> 'OBCreditDebitCode1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Status"]) -> 'OBEntryStatus1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BookingDateTime"]) -> MetaOapg.properties.BookingDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Amount"]) -> 'OBActiveOrHistoricCurrencyAndAmount9': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TransactionId"]) -> 'TransactionId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TransactionReference"]) -> 'TransactionReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatementReference"]) -> MetaOapg.properties.StatementReference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TransactionMutability"]) -> 'OBTransactionMutability1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ValueDateTime"]) -> MetaOapg.properties.ValueDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AddressLine"]) -> 'AddressLine': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ChargeAmount"]) -> 'OBActiveOrHistoricCurrencyAndAmount10': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CurrencyExchange"]) -> 'OBCurrencyExchange5': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankTransactionCode"]) -> 'OBBankTransactionCodeStructure1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProprietaryBankTransactionCode"]) -> 'ProprietaryBankTransactionCodeStructure1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CardInstrument"]) -> 'OBTransactionCardInstrument1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SupplementaryData"]) -> 'OBSupplementaryData1': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AccountId", "CreditDebitIndicator", "Status", "BookingDateTime", "Amount", "TransactionId", "TransactionReference", "StatementReference", "TransactionMutability", "ValueDateTime", "AddressLine", "ChargeAmount", "CurrencyExchange", "BankTransactionCode", "ProprietaryBankTransactionCode", "CardInstrument", "SupplementaryData", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditDebitIndicator"]) -> 'OBCreditDebitCode1': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Status"]) -> 'OBEntryStatus1Code': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BookingDateTime"]) -> MetaOapg.properties.BookingDateTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Amount"]) -> 'OBActiveOrHistoricCurrencyAndAmount9': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TransactionId"]) -> typing.Union['TransactionId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TransactionReference"]) -> typing.Union['TransactionReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatementReference"]) -> typing.Union[MetaOapg.properties.StatementReference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TransactionMutability"]) -> typing.Union['OBTransactionMutability1Code', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ValueDateTime"]) -> typing.Union[MetaOapg.properties.ValueDateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AddressLine"]) -> typing.Union['AddressLine', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ChargeAmount"]) -> typing.Union['OBActiveOrHistoricCurrencyAndAmount10', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CurrencyExchange"]) -> typing.Union['OBCurrencyExchange5', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankTransactionCode"]) -> typing.Union['OBBankTransactionCodeStructure1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProprietaryBankTransactionCode"]) -> typing.Union['ProprietaryBankTransactionCodeStructure1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CardInstrument"]) -> typing.Union['OBTransactionCardInstrument1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SupplementaryData"]) -> typing.Union['OBSupplementaryData1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AccountId", "CreditDebitIndicator", "Status", "BookingDateTime", "Amount", "TransactionId", "TransactionReference", "StatementReference", "TransactionMutability", "ValueDateTime", "AddressLine", "ChargeAmount", "CurrencyExchange", "BankTransactionCode", "ProprietaryBankTransactionCode", "CardInstrument", "SupplementaryData", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Status: 'OBEntryStatus1Code',
        BookingDateTime: typing.Union[MetaOapg.properties.BookingDateTime, str, datetime, ],
        AccountId: 'AccountId',
        Amount: 'OBActiveOrHistoricCurrencyAndAmount9',
        CreditDebitIndicator: 'OBCreditDebitCode1',
        TransactionId: typing.Union['TransactionId', schemas.Unset] = schemas.unset,
        TransactionReference: typing.Union['TransactionReference', schemas.Unset] = schemas.unset,
        StatementReference: typing.Union[MetaOapg.properties.StatementReference, list, tuple, schemas.Unset] = schemas.unset,
        TransactionMutability: typing.Union['OBTransactionMutability1Code', schemas.Unset] = schemas.unset,
        ValueDateTime: typing.Union[MetaOapg.properties.ValueDateTime, str, datetime, schemas.Unset] = schemas.unset,
        AddressLine: typing.Union['AddressLine', schemas.Unset] = schemas.unset,
        ChargeAmount: typing.Union['OBActiveOrHistoricCurrencyAndAmount10', schemas.Unset] = schemas.unset,
        CurrencyExchange: typing.Union['OBCurrencyExchange5', schemas.Unset] = schemas.unset,
        BankTransactionCode: typing.Union['OBBankTransactionCodeStructure1', schemas.Unset] = schemas.unset,
        ProprietaryBankTransactionCode: typing.Union['ProprietaryBankTransactionCodeStructure1', schemas.Unset] = schemas.unset,
        CardInstrument: typing.Union['OBTransactionCardInstrument1', schemas.Unset] = schemas.unset,
        SupplementaryData: typing.Union['OBSupplementaryData1', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBTransaction6Basic':
        return super().__new__(
            cls,
            *args,
            Status=Status,
            BookingDateTime=BookingDateTime,
            AccountId=AccountId,
            Amount=Amount,
            CreditDebitIndicator=CreditDebitIndicator,
            TransactionId=TransactionId,
            TransactionReference=TransactionReference,
            StatementReference=StatementReference,
            TransactionMutability=TransactionMutability,
            ValueDateTime=ValueDateTime,
            AddressLine=AddressLine,
            ChargeAmount=ChargeAmount,
            CurrencyExchange=CurrencyExchange,
            BankTransactionCode=BankTransactionCode,
            ProprietaryBankTransactionCode=ProprietaryBankTransactionCode,
            CardInstrument=CardInstrument,
            SupplementaryData=SupplementaryData,
            _configuration=_configuration,
            **kwargs,
        )

from hsbc_account_information_ce_python_sdk.model.account_id import AccountId
from hsbc_account_information_ce_python_sdk.model.address_line import AddressLine
from hsbc_account_information_ce_python_sdk.model.ob_active_or_historic_currency_and_amount10 import OBActiveOrHistoricCurrencyAndAmount10
from hsbc_account_information_ce_python_sdk.model.ob_active_or_historic_currency_and_amount9 import OBActiveOrHistoricCurrencyAndAmount9
from hsbc_account_information_ce_python_sdk.model.ob_bank_transaction_code_structure1 import OBBankTransactionCodeStructure1
from hsbc_account_information_ce_python_sdk.model.ob_credit_debit_code1 import OBCreditDebitCode1
from hsbc_account_information_ce_python_sdk.model.ob_currency_exchange5 import OBCurrencyExchange5
from hsbc_account_information_ce_python_sdk.model.ob_entry_status1_code import OBEntryStatus1Code
from hsbc_account_information_ce_python_sdk.model.ob_supplementary_data1 import OBSupplementaryData1
from hsbc_account_information_ce_python_sdk.model.ob_transaction_card_instrument1 import OBTransactionCardInstrument1
from hsbc_account_information_ce_python_sdk.model.ob_transaction_mutability1_code import OBTransactionMutability1Code
from hsbc_account_information_ce_python_sdk.model.proprietary_bank_transaction_code_structure1 import ProprietaryBankTransactionCodeStructure1
from hsbc_account_information_ce_python_sdk.model.statement_reference import StatementReference
from hsbc_account_information_ce_python_sdk.model.transaction_id import TransactionId
from hsbc_account_information_ce_python_sdk.model.transaction_reference import TransactionReference
