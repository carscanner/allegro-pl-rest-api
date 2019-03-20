# openapi_client.AfterSaleServicesApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_seller_listing_using_get**](AfterSaleServicesApi.md#get_public_seller_listing_using_get) | **GET** /after-sales-service-conditions/implied-warranties | Get the user&#39;s implied warranties
[**get_public_seller_listing_using_get1**](AfterSaleServicesApi.md#get_public_seller_listing_using_get1) | **GET** /after-sales-service-conditions/return-policies | Get the user&#39;s return policies
[**get_public_seller_listing_using_get2**](AfterSaleServicesApi.md#get_public_seller_listing_using_get2) | **GET** /after-sales-service-conditions/warranties | Get the user&#39;s warranties


# **get_public_seller_listing_using_get**
> ImpliedWarrantiesListImpliedWarrantyBasic get_public_seller_listing_using_get(seller_id, limit=limit, offset=offset)

Get the user's implied warranties

Use this resource to get seller implied warranties listing. More information about this resource you can find <a href=\"../../news/2017-04-05-news_warunki_oferty/\" target=\"_blank\">here</a>.

### Example

* OAuth Authentication (bearer-token-for-user): 
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.AfterSaleServicesApi(openapi_client.ApiClient(configuration))
seller_id = 'seller_id_example' # str | Filter by user id. You are allowed to get your implied warranties only.
limit = 56 # int | Limit (optional)
offset = 0 # int | Offset (optional) (default to 0)

try:
    # Get the user's implied warranties
    api_response = api_instance.get_public_seller_listing_using_get(seller_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AfterSaleServicesApi->get_public_seller_listing_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| Filter by user id. You are allowed to get your implied warranties only. | 
 **limit** | **int**| Limit | [optional] 
 **offset** | **int**| Offset | [optional] [default to 0]

### Return type

[**ImpliedWarrantiesListImpliedWarrantyBasic**](ImpliedWarrantiesListImpliedWarrantyBasic.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_seller_listing_using_get1**
> ReturnPoliciesListReturnPolicyBasic get_public_seller_listing_using_get1(seller_id, limit=limit, offset=offset)

Get the user's return policies

Use this resource to get seller return policies listing. More information about this resource you can find <a href=\"../../news/2017-04-05-news_warunki_oferty/\" target=\"_blank\">here</a>.

### Example

* OAuth Authentication (bearer-token-for-user): 
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.AfterSaleServicesApi(openapi_client.ApiClient(configuration))
seller_id = 'seller_id_example' # str | Filter by user id. You are allowed to get your return policies only.
limit = 56 # int | Limit (optional)
offset = 0 # int | Offset (optional) (default to 0)

try:
    # Get the user's return policies
    api_response = api_instance.get_public_seller_listing_using_get1(seller_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AfterSaleServicesApi->get_public_seller_listing_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| Filter by user id. You are allowed to get your return policies only. | 
 **limit** | **int**| Limit | [optional] 
 **offset** | **int**| Offset | [optional] [default to 0]

### Return type

[**ReturnPoliciesListReturnPolicyBasic**](ReturnPoliciesListReturnPolicyBasic.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_seller_listing_using_get2**
> WarrantiesListWarrantyBasic get_public_seller_listing_using_get2(seller_id, limit=limit, offset=offset)

Get the user's warranties

Use this resource to get seller warranties listing. More information about this resource you can find <a href=\"../../news/2017-04-05-news_warunki_oferty/\" target=\"_blank\">here</a>.

### Example

* OAuth Authentication (bearer-token-for-user): 
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.AfterSaleServicesApi(openapi_client.ApiClient(configuration))
seller_id = 'seller_id_example' # str | Filter by user id. You are allowed to get your warranties only.
limit = 56 # int | Limit (optional)
offset = 0 # int | Offset (optional) (default to 0)

try:
    # Get the user's warranties
    api_response = api_instance.get_public_seller_listing_using_get2(seller_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AfterSaleServicesApi->get_public_seller_listing_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| Filter by user id. You are allowed to get your warranties only. | 
 **limit** | **int**| Limit | [optional] 
 **offset** | **int**| Offset | [optional] [default to 0]

### Return type

[**WarrantiesListWarrantyBasic**](WarrantiesListWarrantyBasic.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

