# allegro_api.OfferVariantsApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_variant_set**](OfferVariantsApi.md#create_or_update_variant_set) | **PUT** /sale/offer-variants/{setId} | [BETA] Create or update variant set
[**delete_variant_set**](OfferVariantsApi.md#delete_variant_set) | **DELETE** /sale/offer-variants/{setId} | [BETA] Delete a variant set
[**get_variant_set**](OfferVariantsApi.md#get_variant_set) | **GET** /sale/offer-variants/{setId} | [BETA] Get a variant set
[**get_variant_sets**](OfferVariantsApi.md#get_variant_sets) | **GET** /sale/offer-variants | [BETA] Get the user&#39;s variant sets


# **create_or_update_variant_set**
> create_or_update_variant_set(set_id, variant_set)

[BETA] Create or update variant set

[BETA] Use this resource to create or update variant set.   A valid variant set must consist of three required elements:  - name:    - it can't be blank and must not be longer than 50 characters  - parameters:    - it should contain parameter identifiers used for offer grouping    - parameter identifiers from the offers and special `color/pattern` value (for grouping via image) are permitted    - it must contain at least one element (up to 2)  - offers:    - it must contain at least 2 offers (500 at most)    - `colorPattern` value must be set for every offer if `color/pattern` parameter is used    - `colorPattern` value can't be blank and must not be longer than 50 characters    - `colorPattern` can take arbitrary string value like `red`, `b323592c-522f-4ec1-b9ea-3764538e0ac4` (UUID), etc.    - offers having the same image should have identical `colorPattern` value    Let's assume we have 4 offers:    - offer with id 2 having an image of a red t-shirt and S as a value of parameter with id 21    - offer with id 3 having an image of a red t-shirt and M as a value of parameter with id 21    - offer with id 4 having an image of a blue t-shirt and S as a value of parameter with id 21    - offer with id 5 having an image of a blue t-shirt and M as a value of parameter with id 21    You can build a variant set by grouping offers using combination of available parameters - examples are available in <i>Request samples</i>.    More general information about variant sets can be found [here](https://allegro.pl/pomoc/faq/wielowariantowosc-jak-polaczyc-oferty-xGgaOByGgTb#dodatkowe-informacje),  more information about variant sets API can be found <a href=\"../../news/2018-07-09-wielowariantowosc/#03\" target=\"_blank\">here</a>.

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
    api_instance = allegro_api.OfferVariantsApi(api_client)
    set_id = 'set_id_example' # str | Variant set identifier.
variant_set = {"name":"t-shirt","offers":[{"id":"2"},{"id":"3"}],"parameters":[{"id":"21"}]} # VariantSet | 

    try:
        # [BETA] Create or update variant set
        api_instance.create_or_update_variant_set(set_id, variant_set)
    except ApiException as e:
        print("Exception when calling OfferVariantsApi->create_or_update_variant_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_id** | **str**| Variant set identifier. | 
 **variant_set** | [**VariantSet**](VariantSet.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.beta.v1+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Variant set created or updated successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_variant_set**
> delete_variant_set(set_id)

[BETA] Delete a variant set

[BETA] Use this resource to delete variant set by id. Offers included in variant set will not be stopped or modified by this operation. <a href=\"../../news/2018-07-09-wielowariantowosc/#05\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.OfferVariantsApi(api_client)
    set_id = 'set_id_example' # str | Variant set identifier.

    try:
        # [BETA] Delete a variant set
        api_instance.delete_variant_set(set_id)
    except ApiException as e:
        print("Exception when calling OfferVariantsApi->delete_variant_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_id** | **str**| Variant set identifier. | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Variant set deleted successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Variant set not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_set**
> VariantSet get_variant_set(set_id)

[BETA] Get a variant set

[BETA] Use this resource to get variant set by set id. <a href=\"../../news/2018-07-09-wielowariantowosc/#04\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.OfferVariantsApi(api_client)
    set_id = 'set_id_example' # str | Variant set identifier.

    try:
        # [BETA] Get a variant set
        api_response = api_instance.get_variant_set(set_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfferVariantsApi->get_variant_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_id** | **str**| Variant set identifier. | 

### Return type

[**VariantSet**](VariantSet.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Variant set returned successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_sets**
> VariantSets get_variant_sets(user_id, offset=offset, limit=limit, query=query)

[BETA] Get the user's variant sets

[BETA] Use this resource to get created variant sets. The returned variant sets are ordered by name. <a href=\"../../news/2018-07-09-wielowariantowosc/\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.OfferVariantsApi(api_client)
    user_id = 'user_id_example' # str | Filter by user id, you are allowed to get your variant sets only.
offset = 0 # int | Index of first returned variant set. (optional) (default to 0)
limit = 10 # int | Maximum number of returned variant sets. (optional) (default to 10)
query = 'query_example' # str | Filter variant sets by name or offer id. (optional)

    try:
        # [BETA] Get the user's variant sets
        api_response = api_instance.get_variant_sets(user_id, offset=offset, limit=limit, query=query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfferVariantsApi->get_variant_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Filter by user id, you are allowed to get your variant sets only. | 
 **offset** | **int**| Index of first returned variant set. | [optional] [default to 0]
 **limit** | **int**| Maximum number of returned variant sets. | [optional] [default to 10]
 **query** | **str**| Filter variant sets by name or offer id. | [optional] 

### Return type

[**VariantSets**](VariantSets.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Variant sets returned successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

