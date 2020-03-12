# allegro_api.BillingApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_billing_entries**](BillingApi.md#get_billing_entries) | **GET** /billing/billing-entries | Get a list of billing entries


# **get_billing_entries**
> object get_billing_entries(occurred_at_gte=occurred_at_gte, occurred_at_lte=occurred_at_lte, type_id=type_id, offer_id=offer_id, limit=limit, offset=offset)

Get a list of billing entries

The billing entries are sorted in a descending order (newest first) by date on which they occurred.

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
    api_instance = allegro_api.BillingApi(api_client)
    occurred_at_gte = '2019-05-08T09:45:32.818Z' # datetime | Date from which billing entries are filtered. If occurredAt.lte is also set, occurredAt.gte cannot be later. (optional)
occurred_at_lte = '2019-05-08T09:45:32.818Z' # datetime | Date to which billing entries are filtered. If occurredAt.gte is also set, occurredAt.lte cannot be earlier. (optional)
type_id = ['type_id_example'] # list[str] | List of billing types by which billing entries are filtered. (optional)
offer_id = 'offer_id_example' # str | Offer ID by which billing entries are filtered. (optional)
limit = 100 # int | Number of returned operations. (optional) (default to 100)
offset = 0 # int | Index of the first returned payment operation from all search results. (optional) (default to 0)

    try:
        # Get a list of billing entries
        api_response = api_instance.get_billing_entries(occurred_at_gte=occurred_at_gte, occurred_at_lte=occurred_at_lte, type_id=type_id, offer_id=offer_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->get_billing_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **occurred_at_gte** | **datetime**| Date from which billing entries are filtered. If occurredAt.lte is also set, occurredAt.gte cannot be later. | [optional] 
 **occurred_at_lte** | **datetime**| Date to which billing entries are filtered. If occurredAt.gte is also set, occurredAt.lte cannot be earlier. | [optional] 
 **type_id** | [**list[str]**](str.md)| List of billing types by which billing entries are filtered. | [optional] 
 **offer_id** | **str**| Offer ID by which billing entries are filtered. | [optional] 
 **limit** | **int**| Number of returned operations. | [optional] [default to 100]
 **offset** | **int**| Index of the first returned payment operation from all search results. | [optional] [default to 0]

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
**200** | List of billing entries returned successfully. |  -  |
**401** | Unauthorized |  -  |
**406** | Not Acceptable |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

