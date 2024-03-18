<div align="left">

[![Visit Hsbc](./header.png)](https://hsbc.com)

# Hsbc<a id="hsbc"></a>

In this document, you'll find the steps your organization needs to take to use our API services. Included in this guide are details of request and response messages used to support your organization’s integration. The intended audience for this document are **Technical Architects**, **Development Engineers**, **Test Engineers**, and **Operation & Maintenance Engineers** involved in development and support of your organization’s integration. Setting up our API Services is best completed with the assistance of your organization’s IT team, or someone with experience and knowledge of application programming interfaces. This should include experience with **JSON payloads**, **security** and **public key infrastructure (PKI)**. This Document describes the following request and response structure of HSBCnet - Account Information API. For detail implementation guidelines, please refer to the respective section from [develop.hsbc.com](https://develop.hsbc.com/ob-api-documentation/account-information-uk-personal-v319)



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`hsbcaccountinformationce.account_access_consents.create_consent`](#hsbcaccountinformationceaccount_access_consentscreate_consent)
  * [`hsbcaccountinformationce.account_access_consents.delete_consent`](#hsbcaccountinformationceaccount_access_consentsdelete_consent)
  * [`hsbcaccountinformationce.account_access_consents.get_by_consent_id`](#hsbcaccountinformationceaccount_access_consentsget_by_consent_id)
  * [`hsbcaccountinformationce.accounts.get_all`](#hsbcaccountinformationceaccountsget_all)
  * [`hsbcaccountinformationce.accounts.get_balances_by_account_id`](#hsbcaccountinformationceaccountsget_balances_by_account_id)
  * [`hsbcaccountinformationce.balances.get_by_account_id`](#hsbcaccountinformationcebalancesget_by_account_id)
  * [`hsbcaccountinformationce.beneficiaries.get_by_account_id`](#hsbcaccountinformationcebeneficiariesget_by_account_id)
  * [`hsbcaccountinformationce.direct_debits.get_by_account_id`](#hsbcaccountinformationcedirect_debitsget_by_account_id)
  * [`hsbcaccountinformationce.parties.get_by_account_id`](#hsbcaccountinformationcepartiesget_by_account_id)
  * [`hsbcaccountinformationce.products.get_by_account_id`](#hsbcaccountinformationceproductsget_by_account_id)
  * [`hsbcaccountinformationce.scheduled_payments.get_by_account_id`](#hsbcaccountinformationcescheduled_paymentsget_by_account_id)
  * [`hsbcaccountinformationce.standing_orders.get_by_account_id`](#hsbcaccountinformationcestanding_ordersget_by_account_id)
  * [`hsbcaccountinformationce.transactions.get_by_account_id`](#hsbcaccountinformationcetransactionsget_by_account_id)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=HSBC&serviceName=AccountInformationCE&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from hsbc_account_information_ce_python_sdk import (
    HsbcAccountInformationCe,
    ApiException,
)

hsbcaccountinformationce = HsbcAccountInformationCe(
    access_token="YOUR_BEARER_TOKEN",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Create Account Access Consents
    create_consent_response = hsbcaccountinformationce.account_access_consents.create_consent(
        data={
            "permissions": ["ReadAccountsBasic"],
            "expiration_date_time": "2022-11-15 09:14:41",
            "transaction_from_date_time": "test value",
            "transaction_to_date_time": "2022-11-15 09:14:49",
        },
        risk={},
        x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
        x_fapi_customer_ip_address="12.201.45.125",
        x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
        x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    )
    print(create_consent_response)
except ApiException as e:
    print("Exception when calling AccountAccessConsentsApi.create_consent: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["code"])
        pprint(e.body["message"])
        pprint(e.body["errors"])
        pprint(e.body["id"])
    if e.status == 500:
        pprint(e.body["code"])
        pprint(e.body["message"])
        pprint(e.body["errors"])
        pprint(e.body["id"])
    if e.status == 403:
        pprint(e.body["code"])
        pprint(e.body["message"])
        pprint(e.body["errors"])
        pprint(e.body["id"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from hsbc_account_information_ce_python_sdk import (
    HsbcAccountInformationCe,
    ApiException,
)

hsbcaccountinformationce = HsbcAccountInformationCe(
    access_token="YOUR_BEARER_TOKEN",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main():
    try:
        # Create Account Access Consents
        create_consent_response = await hsbcaccountinformationce.account_access_consents.acreate_consent(
            data={
                "permissions": ["ReadAccountsBasic"],
                "expiration_date_time": "2022-11-15 09:14:41",
                "transaction_from_date_time": "test value",
                "transaction_to_date_time": "2022-11-15 09:14:49",
            },
            risk={},
            x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
            x_fapi_customer_ip_address="12.201.45.125",
            x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
            x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        )
        print(create_consent_response)
    except ApiException as e:
        print(
            "Exception when calling AccountAccessConsentsApi.create_consent: %s\n" % e
        )
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["code"])
            pprint(e.body["message"])
            pprint(e.body["errors"])
            pprint(e.body["id"])
        if e.status == 500:
            pprint(e.body["code"])
            pprint(e.body["message"])
            pprint(e.body["errors"])
            pprint(e.body["id"])
        if e.status == 403:
            pprint(e.body["code"])
            pprint(e.body["message"])
            pprint(e.body["errors"])
            pprint(e.body["id"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from hsbc_account_information_ce_python_sdk import (
    HsbcAccountInformationCe,
    ApiException,
)

hsbcaccountinformationce = HsbcAccountInformationCe(
    access_token="YOUR_BEARER_TOKEN",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Create Account Access Consents
    create_consent_response = hsbcaccountinformationce.account_access_consents.raw.create_consent(
        data={
            "permissions": ["ReadAccountsBasic"],
            "expiration_date_time": "2022-11-15 09:14:41",
            "transaction_from_date_time": "test value",
            "transaction_to_date_time": "2022-11-15 09:14:49",
        },
        risk={},
        x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
        x_fapi_customer_ip_address="12.201.45.125",
        x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
        x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    )
    pprint(create_consent_response.body)
    pprint(create_consent_response.body["data"])
    pprint(create_consent_response.body["risk"])
    pprint(create_consent_response.body["links"])
    pprint(create_consent_response.body["meta"])
    pprint(create_consent_response.headers)
    pprint(create_consent_response.status)
    pprint(create_consent_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountAccessConsentsApi.create_consent: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["code"])
        pprint(e.body["message"])
        pprint(e.body["errors"])
        pprint(e.body["id"])
    if e.status == 500:
        pprint(e.body["code"])
        pprint(e.body["message"])
        pprint(e.body["errors"])
        pprint(e.body["id"])
    if e.status == 403:
        pprint(e.body["code"])
        pprint(e.body["message"])
        pprint(e.body["errors"])
        pprint(e.body["id"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `hsbcaccountinformationce.account_access_consents.create_consent`<a id="hsbcaccountinformationceaccount_access_consentscreate_consent"></a>

This endpoint enables TPP to create account access consent. Supports all product types -Personal Current Account, Savings Account, Credit Cards, Foreign Currency Accounts, Global Money, Working Capital

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_consent_response = hsbcaccountinformationce.account_access_consents.create_consent(
    data={
        "permissions": ["ReadAccountsBasic"],
        "expiration_date_time": "2022-11-15 09:14:41",
        "transaction_from_date_time": "test value",
        "transaction_to_date_time": "2022-11-15 09:14:49",
    },
    risk={},
    x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
    x_fapi_customer_ip_address="12.201.45.125",
    x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
    x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: [`OBReadConsent1Data`](./hsbc_account_information_ce_python_sdk/type/ob_read_consent1_data.py)<a id="data-obreadconsent1datahsbc_account_information_ce_python_sdktypeob_read_consent1_datapy"></a>


##### risk: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="risk-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

The Risk section is sent by the initiating party to the ASPSP. It is used to specify additional details for risk scoring for Account Info.

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OBReadConsent1`](./hsbc_account_information_ce_python_sdk/type/ob_read_consent1.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OBReadConsentResponse1`](./hsbc_account_information_ce_python_sdk/pydantic/ob_read_consent_response1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account-access-consents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hsbcaccountinformationce.account_access_consents.delete_consent`<a id="hsbcaccountinformationceaccount_access_consentsdelete_consent"></a>

This endpoint enables TPP to delete account access consent

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hsbcaccountinformationce.account_access_consents.delete_consent(
    consent_id="7404e99b-1a4d-4b08-b441-c327661527f0",
    x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
    x_fapi_customer_ip_address="12.201.45.125",
    x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
    x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consent_id: `str`<a id="consent_id-str"></a>

ConsentId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account-access-consents/{ConsentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hsbcaccountinformationce.account_access_consents.get_by_consent_id`<a id="hsbcaccountinformationceaccount_access_consentsget_by_consent_id"></a>

This endpoint enables TPP to get account access consent by ConsentId. Supports all product types -Personal Current Account, Savings Account, Credit Cards, Foreign Currency Accounts, Global Money Working Capital

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_consent_id_response = hsbcaccountinformationce.account_access_consents.get_by_consent_id(
    consent_id="7404e99b-1a4d-4b08-b441-c327661527f0",
    x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
    x_fapi_customer_ip_address="12.201.45.125",
    x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
    x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consent_id: `str`<a id="consent_id-str"></a>

ConsentId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadConsentResponse1`](./hsbc_account_information_ce_python_sdk/pydantic/ob_read_consent_response1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account-access-consents/{ConsentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hsbcaccountinformationce.accounts.get_all`<a id="hsbcaccountinformationceaccountsget_all"></a>

This endpoint enables to get Accounts. Supports all product types -Personal Current Account, Savings Account, Credit Cards, Foreign Currency Accounts, Global Money, Working Capital

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = hsbcaccountinformationce.accounts.get_all(
    x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
    x_fapi_customer_ip_address="12.201.45.125",
    x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
    x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadAccount6`](./hsbc_account_information_ce_python_sdk/pydantic/ob_read_account6.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hsbcaccountinformationce.accounts.get_balances_by_account_id`<a id="hsbcaccountinformationceaccountsget_balances_by_account_id"></a>

This endpoint enables to get Balances by AccountId. Supports all product types -Personal Current Account, Savings Account, Credit Cards, Foreign Currency Accounts, Global Money, Working Capital

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_balances_by_account_id_response = hsbcaccountinformationce.accounts.get_balances_by_account_id(
    account_id="ThR-RpLMV5lZzDu8vrfEFg",
    x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
    x_fapi_customer_ip_address="12.201.45.125",
    x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
    x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadAccount6`](./hsbc_account_information_ce_python_sdk/pydantic/ob_read_account6.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hsbcaccountinformationce.balances.get_by_account_id`<a id="hsbcaccountinformationcebalancesget_by_account_id"></a>

This endpoint enables to get Balances by AccountId. Supports all product types -Personal Current Account, Savings Account, Credit Cards, Foreign Currency Accounts, Global Money, Working Capital

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_account_id_response = hsbcaccountinformationce.balances.get_by_account_id(
    account_id="ThR-RpLMV5lZzDu8vrfEFg",
    x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
    x_fapi_customer_ip_address="12.201.45.125",
    x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
    x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadBalance1`](./hsbc_account_information_ce_python_sdk/pydantic/ob_read_balance1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/balances` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hsbcaccountinformationce.beneficiaries.get_by_account_id`<a id="hsbcaccountinformationcebeneficiariesget_by_account_id"></a>

This endpoint enables to get Beneficiaries by AccountId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_account_id_response = hsbcaccountinformationce.beneficiaries.get_by_account_id(
    account_id="ThR-RpLMV5lZzDu8vrfEFg",
    x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
    x_fapi_customer_ip_address="12.201.45.125",
    x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
    x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadBeneficiary5`](./hsbc_account_information_ce_python_sdk/pydantic/ob_read_beneficiary5.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/beneficiaries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hsbcaccountinformationce.direct_debits.get_by_account_id`<a id="hsbcaccountinformationcedirect_debitsget_by_account_id"></a>

This endpoint enables to get Direct Debits by AccountId. Supported product type is Personal Current Account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_account_id_response = hsbcaccountinformationce.direct_debits.get_by_account_id(
    account_id="ThR-RpLMV5lZzDu8vrfEFg",
    x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
    x_fapi_customer_ip_address="12.201.45.125",
    x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
    x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadDirectDebit2`](./hsbc_account_information_ce_python_sdk/pydantic/ob_read_direct_debit2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/direct-debits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hsbcaccountinformationce.parties.get_by_account_id`<a id="hsbcaccountinformationcepartiesget_by_account_id"></a>

This endpoint enables to get Parties by AccountId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_account_id_response = hsbcaccountinformationce.parties.get_by_account_id(
    account_id="ThR-RpLMV5lZzDu8vrfEFg",
    x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
    x_fapi_customer_ip_address="12.201.45.125",
    x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
    x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadParty3`](./hsbc_account_information_ce_python_sdk/pydantic/ob_read_party3.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/parties` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hsbcaccountinformationce.products.get_by_account_id`<a id="hsbcaccountinformationceproductsget_by_account_id"></a>

This endpoint enables to get Products by AccountId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_account_id_response = hsbcaccountinformationce.products.get_by_account_id(
    account_id="ThR-RpLMV5lZzDu8vrfEFg",
    x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
    x_fapi_customer_ip_address="12.201.45.125",
    x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
    x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadProduct2`](./hsbc_account_information_ce_python_sdk/pydantic/ob_read_product2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/product` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hsbcaccountinformationce.scheduled_payments.get_by_account_id`<a id="hsbcaccountinformationcescheduled_paymentsget_by_account_id"></a>

This endpoint enables to get Scheduled Payments by AccountId. Supported product types -Personal Current Account, Savings Account, Foreign Currency Accounts, Global Money.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_account_id_response = hsbcaccountinformationce.scheduled_payments.get_by_account_id(
    account_id="ThR-RpLMV5lZzDu8vrfEFg",
    x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
    x_fapi_customer_ip_address="12.201.45.125",
    x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
    x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadScheduledPayment3`](./hsbc_account_information_ce_python_sdk/pydantic/ob_read_scheduled_payment3.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/scheduled-payments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hsbcaccountinformationce.standing_orders.get_by_account_id`<a id="hsbcaccountinformationcestanding_ordersget_by_account_id"></a>

This endpoint enables to get Standing Orders by AccountId. Supported product types -Personal Current Account, Foreign Currency Accounts.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_account_id_response = hsbcaccountinformationce.standing_orders.get_by_account_id(
    account_id="ThR-RpLMV5lZzDu8vrfEFg",
    x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
    x_fapi_customer_ip_address="12.201.45.125",
    x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
    x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadStandingOrder6`](./hsbc_account_information_ce_python_sdk/pydantic/ob_read_standing_order6.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/standing-orders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hsbcaccountinformationce.transactions.get_by_account_id`<a id="hsbcaccountinformationcetransactionsget_by_account_id"></a>

This endpoint enables to get account Transactions by AccountId. Supports all product types -Personal Current Account, Savings Account, Credit Cards, Foreign Currency Accounts, Global Money, Working Capital

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_account_id_response = hsbcaccountinformationce.transactions.get_by_account_id(
    account_id="ThR-RpLMV5lZzDu8vrfEFg",
    x_fapi_auth_date="Tue, 18 Apr 2023 14:42:25 UTC",
    x_fapi_customer_ip_address="12.201.45.125",
    x_fapi_interaction_id="20177a90-5e29-43ba-bea0-cc6c344a9d32",
    x_customer_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    from_booking_date_time="2023-01-04T13:21:07+00:00",
    to_booking_date_time="2023-02-04T13:21:07+00:00",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

##### from_booking_date_time: `datetime`<a id="from_booking_date_time-datetime"></a>

The UTC ISO 8601 Date Time to filter transactions FROM NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

##### to_booking_date_time: `datetime`<a id="to_booking_date_time-datetime"></a>

The UTC ISO 8601 Date Time to filter transactions TO NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadTransaction6`](./hsbc_account_information_ce_python_sdk/pydantic/ob_read_transaction6.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
