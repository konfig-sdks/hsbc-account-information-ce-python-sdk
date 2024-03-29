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


class OBExternalStatementAmountType1Code(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Amount type, in a coded form.
    """
    
    @schemas.classproperty
    def ARREARS_CLOSING_BALANCE(cls):
        return cls("UK.OBIE.ArrearsClosingBalance")
    
    @schemas.classproperty
    def AVAILABLE_BALANCE(cls):
        return cls("UK.OBIE.AvailableBalance")
    
    @schemas.classproperty
    def AVERAGE_BALANCE_WHEN_IN_CREDIT(cls):
        return cls("UK.OBIE.AverageBalanceWhenInCredit")
    
    @schemas.classproperty
    def AVERAGE_BALANCE_WHEN_IN_DEBIT(cls):
        return cls("UK.OBIE.AverageBalanceWhenInDebit")
    
    @schemas.classproperty
    def AVERAGE_DAILY_BALANCE(cls):
        return cls("UK.OBIE.AverageDailyBalance")
    
    @schemas.classproperty
    def BALANCE_TRANSFER_CLOSING_BALANCE(cls):
        return cls("UK.OBIE.BalanceTransferClosingBalance")
    
    @schemas.classproperty
    def CASH_CLOSING_BALANCE(cls):
        return cls("UK.OBIE.CashClosingBalance")
    
    @schemas.classproperty
    def CLOSING_BALANCE(cls):
        return cls("UK.OBIE.ClosingBalance")
    
    @schemas.classproperty
    def CREDIT_LIMIT(cls):
        return cls("UK.OBIE.CreditLimit")
    
    @schemas.classproperty
    def CURRENT_PAYMENT(cls):
        return cls("UK.OBIE.CurrentPayment")
    
    @schemas.classproperty
    def DIRECT_DEBIT_PAYMENT_DUE(cls):
        return cls("UK.OBIE.DirectDebitPaymentDue")
    
    @schemas.classproperty
    def FSCSINSURANCE(cls):
        return cls("UK.OBIE.FSCSInsurance")
    
    @schemas.classproperty
    def MINIMUM_PAYMENT_DUE(cls):
        return cls("UK.OBIE.MinimumPaymentDue")
    
    @schemas.classproperty
    def PENDING_TRANSACTIONS_BALANCE(cls):
        return cls("UK.OBIE.PendingTransactionsBalance")
    
    @schemas.classproperty
    def PREVIOUS_CLOSING_BALANCE(cls):
        return cls("UK.OBIE.PreviousClosingBalance")
    
    @schemas.classproperty
    def PREVIOUS_PAYMENT(cls):
        return cls("UK.OBIE.PreviousPayment")
    
    @schemas.classproperty
    def PURCHASE_CLOSING_BALANCE(cls):
        return cls("UK.OBIE.PurchaseClosingBalance")
    
    @schemas.classproperty
    def STARTING_BALANCE(cls):
        return cls("UK.OBIE.StartingBalance")
    
    @schemas.classproperty
    def TOTAL_ADJUSTMENTS(cls):
        return cls("UK.OBIE.TotalAdjustments")
    
    @schemas.classproperty
    def TOTAL_CASH_ADVANCES(cls):
        return cls("UK.OBIE.TotalCashAdvances")
    
    @schemas.classproperty
    def TOTAL_CHARGES(cls):
        return cls("UK.OBIE.TotalCharges")
    
    @schemas.classproperty
    def TOTAL_CREDITS(cls):
        return cls("UK.OBIE.TotalCredits")
    
    @schemas.classproperty
    def TOTAL_DEBITS(cls):
        return cls("UK.OBIE.TotalDebits")
    
    @schemas.classproperty
    def TOTAL_PURCHASES(cls):
        return cls("UK.OBIE.TotalPurchases")
