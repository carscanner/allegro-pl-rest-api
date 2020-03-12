# allegro_api.PaymentsApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_id_mapping**](PaymentsApi.md#get_payment_id_mapping) | **GET** /payments/payment-id-mappings | Mapping of payment identifiers
[**get_payments_operation_history**](PaymentsApi.md#get_payments_operation_history) | **GET** /payments/payment-operations | Payment operations history
[**get_refunded_payments**](PaymentsApi.md#get_refunded_payments) | **GET** /payments/refunds | Get a list of refunded payments
[**initiate_refund**](PaymentsApi.md#initiate_refund) | **POST** /payments/refunds | Initiate a refund of a payment


# **get_payment_id_mapping**
> PaymentIdMapping get_payment_id_mapping(payment_id=payment_id, transaction_id=transaction_id)

Mapping of payment identifiers

Use this endpoint to get payment identifiers compatible with RestAPI and WebAPI. Querying is allowed only by paymentId or transactionId. Identifiers are returned for payments created in last 3 months.

### Example

* OAuth Authentication (bearer-token-for-user):
```python
from __future__ import print_function
import time
import allegro_api
from allegro_api.rest import ApiException
from pprint import pprint
configuration = allegro_api.Configuration()
# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.allegro.pl
configuration.host = "https://api.allegro.pl"
# Enter a context with an instance of the API client
with allegro_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = allegro_api.PaymentsApi(api_client)
    payment_id = 'payment_id_example' # str | Payment identifier. (optional)
transaction_id = 'transaction_id_example' # str | Transaction identifier. (optional)

    try:
        # Mapping of payment identifiers
        api_response = api_instance.get_payment_id_mapping(payment_id=payment_id, transaction_id=transaction_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->get_payment_id_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)| Payment identifier. | [optional] 
 **transaction_id** | **str**| Transaction identifier. | [optional] 

### Return type

[**PaymentIdMapping**](PaymentIdMapping.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The payment identifiers for given query param returned successfully. |  -  |
**400** | Returned when none or every of query params was provided in search parameters. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_operation_history**
> PaymentOperations get_payments_operation_history(wallet_type=wallet_type, wallet_payment_operator=wallet_payment_operator, payment_id=payment_id, participant_login=participant_login, occurred_at_gte=occurred_at_gte, occurred_at_lte=occurred_at_lte, group=group, limit=limit, offset=offset)

Payment operations history

Use this endpoint to get the list of the seller's payment operations.

### Example

* OAuth Authentication (bearer-token-for-user):
```python
from __future__ import print_function
import time
import allegro_api
from allegro_api.rest import ApiException
from pprint import pprint
configuration = allegro_api.Configuration()
# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.allegro.pl
configuration.host = "https://api.allegro.pl"
# Enter a context with an instance of the API client
with allegro_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = allegro_api.PaymentsApi(api_client)
    wallet_type = 'AVAILABLE' # str | Type of the wallet: * AVAILABLE - operations available for payout. * WAITING - operations temporarily suspended for payout. (optional) (default to 'AVAILABLE')
wallet_payment_operator = 'wallet_payment_operator_example' # str | Payment operator: * PAYU - operations processed by PAYU operator. * P24 - operations processed by PRZELEWY24 operator. (optional)
payment_id = 'payment_id_example' # str | The payment ID. (optional)
participant_login = 'participant_login_example' # str | Login of the participant. In case of REFUND_INCREASE operation this is the login of the seller, in other cases, of the buyer. (optional)
occurred_at_gte = '2019-05-08T09:45:20.818Z' # datetime | The minimum date and time of operation occurrence in ISO 8601 format. (optional)
occurred_at_lte = '2019-05-08T09:45:20.818Z' # datetime | The maximum date and time of operation occurrence in ISO 8601 format. (optional)
group = ['group_example'] # list[str] | Group of operation types: * INCOME - CONTRIBUTION, SURCHARGE, CORRECTION, DEDUCTION_INCREASE. * OUTCOME - PAYOUT, PAYOUT_CANCEL, DEDUCTION_CHARGE. * REFUND - REFUND_CHARGE, REFUND_CANCEL, REFUND_INCREASE, CORRECTION. (optional)
limit = 50 # int | Number of returned operations. (optional) (default to 50)
offset = 0 # int | Index of the first returned payment operation from all search results. (optional) (default to 0)

    try:
        # Payment operations history
        api_response = api_instance.get_payments_operation_history(wallet_type=wallet_type, wallet_payment_operator=wallet_payment_operator, payment_id=payment_id, participant_login=participant_login, occurred_at_gte=occurred_at_gte, occurred_at_lte=occurred_at_lte, group=group, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->get_payments_operation_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_type** | **str**| Type of the wallet: * AVAILABLE - operations available for payout. * WAITING - operations temporarily suspended for payout. | [optional] [default to &#39;AVAILABLE&#39;]
 **wallet_payment_operator** | **str**| Payment operator: * PAYU - operations processed by PAYU operator. * P24 - operations processed by PRZELEWY24 operator. | [optional] 
 **payment_id** | [**str**](.md)| The payment ID. | [optional] 
 **participant_login** | **str**| Login of the participant. In case of REFUND_INCREASE operation this is the login of the seller, in other cases, of the buyer. | [optional] 
 **occurred_at_gte** | **datetime**| The minimum date and time of operation occurrence in ISO 8601 format. | [optional] 
 **occurred_at_lte** | **datetime**| The maximum date and time of operation occurrence in ISO 8601 format. | [optional] 
 **group** | [**list[str]**](str.md)| Group of operation types: * INCOME - CONTRIBUTION, SURCHARGE, CORRECTION, DEDUCTION_INCREASE. * OUTCOME - PAYOUT, PAYOUT_CANCEL, DEDUCTION_CHARGE. * REFUND - REFUND_CHARGE, REFUND_CANCEL, REFUND_INCREASE, CORRECTION. | [optional] 
 **limit** | **int**| Number of returned operations. | [optional] [default to 50]
 **offset** | **int**| Index of the first returned payment operation from all search results. | [optional] [default to 0]

### Return type

[**PaymentOperations**](PaymentOperations.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | The payment operations history for given search criteria returned successfully. |  -  |
**422** | Returned when any of the given search parameters have an invalid value or when the search result reached the limit of found operations - 10000. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refunded_payments**
> object get_refunded_payments(limit=limit, offset=offset, id=id, payment_id=payment_id, occurred_at_gte=occurred_at_gte, occurred_at_lte=occurred_at_lte, status=status)

Get a list of refunded payments

Get a list of refunded payments.

### Example

* OAuth Authentication (bearer-token-for-user):
```python
from __future__ import print_function
import time
import allegro_api
from allegro_api.rest import ApiException
from pprint import pprint
configuration = allegro_api.Configuration()
# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.allegro.pl
configuration.host = "https://api.allegro.pl"
# Enter a context with an instance of the API client
with allegro_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = allegro_api.PaymentsApi(api_client)
    limit = 50 # int | Number of returned operations. (optional) (default to 50)
offset = 0 # int | Index of the first returned payment operation from all search results. (optional) (default to 0)
id = 'id_example' # str | ID of the refund. (optional)
payment_id = 'payment_id_example' # str | ID of the payment. (optional)
occurred_at_gte = '2019-05-08T09:45:43.818Z' # datetime | Minimum date and time when the refund occurred provided in ISO 8601 format. (optional)
occurred_at_lte = '2019-05-08T09:45:32.818Z' # datetime | Maximum date and time when the refund occurred provided in ISO 8601 format. (optional)
status = ['status_example'] # list[str] | Current status of payment refund. (optional)

    try:
        # Get a list of refunded payments
        api_response = api_instance.get_refunded_payments(limit=limit, offset=offset, id=id, payment_id=payment_id, occurred_at_gte=occurred_at_gte, occurred_at_lte=occurred_at_lte, status=status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->get_refunded_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of returned operations. | [optional] [default to 50]
 **offset** | **int**| Index of the first returned payment operation from all search results. | [optional] [default to 0]
 **id** | [**str**](.md)| ID of the refund. | [optional] 
 **payment_id** | [**str**](.md)| ID of the payment. | [optional] 
 **occurred_at_gte** | **datetime**| Minimum date and time when the refund occurred provided in ISO 8601 format. | [optional] 
 **occurred_at_lte** | **datetime**| Maximum date and time when the refund occurred provided in ISO 8601 format. | [optional] 
 **status** | [**list[str]**](str.md)| Current status of payment refund. | [optional] 

### Return type

**object**

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of payments refunds returned successfully. |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity. Returned when any of the given search parameters have an invalid value. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_refund**
> RefundDetails initiate_refund(initialize_refund=initialize_refund)

Initiate a refund of a payment

Use this endpoint to initiate a refund of a payment.

### Example

* OAuth Authentication (bearer-token-for-user):
```python
from __future__ import print_function
import time
import allegro_api
from allegro_api.rest import ApiException
from pprint import pprint
configuration = allegro_api.Configuration()
# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.allegro.pl
configuration.host = "https://api.allegro.pl"
# Enter a context with an instance of the API client
with allegro_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = allegro_api.PaymentsApi(api_client)
    initialize_refund = allegro_api.InitializeRefund() # InitializeRefund |  (optional)

    try:
        # Initiate a refund of a payment
        api_response = api_instance.initiate_refund(initialize_refund=initialize_refund)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->initiate_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initialize_refund** | [**InitializeRefund**](InitializeRefund.md)|  | [optional] 

### Return type

[**RefundDetails**](RefundDetails.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Refund request created successfully. |  -  |
**400** | Syntactically incorrect request. |  -  |
**401** | Unauthorized. |  -  |
**422** | Unprocessable Entity. |  -  |
**404** | Payment not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

