# coding: utf-8

"""
    Account Information API

    In this document, you'll find the steps your organization needs to take to use our API services. Included in this guide are details of request and response messages used to support your organization’s integration. The intended audience for this document are **Technical Architects**, **Development Engineers**, **Test Engineers**, and **Operation & Maintenance Engineers** involved in development and support of your organization’s integration. Setting up our API Services is best completed with the assistance of your organization’s IT team, or someone with experience and knowledge of application programming interfaces. This should include experience with **JSON payloads**, **security** and **public key infrastructure (PKI)**. This Document describes the following request and response structure of HSBCnet - Account Information API. For detail implementation guidelines, please refer to the respective section from [develop.hsbc.com](https://develop.hsbc.com/ob-api-documentation/account-information-uk-personal-v319) 

    The version of the OpenAPI document: 3.1.11
    Generated by: https://konfigthis.com
"""

from hsbc_account_information_ce_python_sdk.paths.account_access_consents.post import CreateConsent
from hsbc_account_information_ce_python_sdk.paths.account_access_consents_consent_id.delete import DeleteConsent
from hsbc_account_information_ce_python_sdk.paths.account_access_consents_consent_id.get import GetByConsentId
from hsbc_account_information_ce_python_sdk.apis.tags.account_access_consents_api_raw import AccountAccessConsentsApiRaw


class AccountAccessConsentsApi(
    CreateConsent,
    DeleteConsent,
    GetByConsentId,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AccountAccessConsentsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AccountAccessConsentsApiRaw(api_client)
