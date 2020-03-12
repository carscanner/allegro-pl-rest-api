# allegro_api.OfferTagsApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_tag_to_offer_post**](OfferTagsApi.md#assign_tag_to_offer_post) | **POST** /sale/offers/{offerId}/tags | Assign tags to an offer
[**create_tag_post1**](OfferTagsApi.md#create_tag_post1) | **POST** /sale/offer-tags | Create a tag
[**delete_tag_using_delete**](OfferTagsApi.md#delete_tag_using_delete) | **DELETE** /sale/offer-tags/{tagId} | Delete a tag
[**list_assigned_offer_tags_get**](OfferTagsApi.md#list_assigned_offer_tags_get) | **GET** /sale/offers/{offerId}/tags | Get tags assigned to an offer
[**list_seller_tags_get1**](OfferTagsApi.md#list_seller_tags_get1) | **GET** /sale/offer-tags | Get the user&#39;s tags
[**update_tag_put**](OfferTagsApi.md#update_tag_put) | **PUT** /sale/offer-tags/{tagId} | Modify a tag


# **assign_tag_to_offer_post**
> assign_tag_to_offer_post(offer_id, tag_ids_request)

Assign tags to an offer

Use this resource to assign a tag to offer. <a href=\"../../news/2018-09-24-tagi-zalaczniki/#PrzypiszTagiDoOferty\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.OfferTagsApi(api_client)
    offer_id = 'offer_id_example' # str | Offer identifier.
tag_ids_request = allegro_api.TagIdsRequest() # TagIdsRequest | request

    try:
        # Assign tags to an offer
        api_instance.assign_tag_to_offer_post(offer_id, tag_ids_request)
    except ApiException as e:
        print("Exception when calling OfferTagsApi->assign_tag_to_offer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Offer identifier. | 
 **tag_ids_request** | [**TagIdsRequest**](TagIdsRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully assigned tag to offer |  -  |
**400** | Bad request |  -  |
**403** | Forbidden - offer is created by someone else or user is not brandzone user or doesn&#39;t have tags subscription |  -  |
**422** | Validation failed - your request was correct, but the tag could not be assigned. |  -  |
**401** | Unauthorized action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tag_post1**
> TagId create_tag_post1(tag_request)

Create a tag

Use this resource to create a new tag. <a href=\"../../news/2018-09-24-tagi-zalaczniki/#DodajDoKonta\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.OfferTagsApi(api_client)
    tag_request = allegro_api.TagRequest() # TagRequest | request

    try:
        # Create a tag
        api_response = api_instance.create_tag_post1(tag_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfferTagsApi->create_tag_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_request** | [**TagRequest**](TagRequest.md)| request | 

### Return type

[**TagId**](TagId.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created the requested tag |  -  |
**400** | Bad request |  -  |
**422** | Validation failed - your request was correct, but the tag could not be created. |  -  |
**401** | Unauthorized action |  -  |
**403** | User is not brandzone user and doesn&#39;t have tags subscription |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag_using_delete**
> delete_tag_using_delete(tag_id)

Delete a tag

Use this resource to delete the tag. <a href=\"../../news/2018-09-24-tagi-zalaczniki/#UsunTagZKonta\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.OfferTagsApi(api_client)
    tag_id = 'tag_id_example' # str | Tag identifier.

    try:
        # Delete a tag
        api_instance.delete_tag_using_delete(tag_id)
    except ApiException as e:
        print("Exception when calling OfferTagsApi->delete_tag_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| Tag identifier. | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted tag |  -  |
**404** | Tag not found |  -  |
**401** | Unauthorized action |  -  |
**403** | User is not brandzone user and doesn&#39;t have tags subscription |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assigned_offer_tags_get**
> TagListResponse list_assigned_offer_tags_get(offer_id)

Get tags assigned to an offer

Use this resource to get a list of tags assigned to offer. <a href=\"../../news/2018-09-24-tagi-zalaczniki/#PobierzTagiZOferty\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.OfferTagsApi(api_client)
    offer_id = 'offer_id_example' # str | Offer identifier.

    try:
        # Get tags assigned to an offer
        api_response = api_instance.list_assigned_offer_tags_get(offer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfferTagsApi->list_assigned_offer_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Offer identifier. | 

### Return type

[**TagListResponse**](TagListResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned list of assigned tags |  -  |
**401** | Unauthorized action |  -  |
**403** | User is not brandzone user and doesn&#39;t have tags subscription |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_seller_tags_get1**
> TagListResponse list_seller_tags_get1(user_id, limit=limit, offset=offset)

Get the user's tags

Use this resource to get a list of tags defined by the specified user (Defaults: limit = 1000, offset = 0). <a href=\"../../news/2018-09-24-tagi-zalaczniki/#PobierzTagi\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.OfferTagsApi(api_client)
    user_id = 'user_id_example' # str | User identifier.
limit = 56 # int | The limit of elements in the response. (optional)
offset = 56 # int | The offset of elements in the response. (optional)

    try:
        # Get the user's tags
        api_response = api_instance.list_seller_tags_get1(user_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfferTagsApi->list_seller_tags_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User identifier. | 
 **limit** | **int**| The limit of elements in the response. | [optional] 
 **offset** | **int**| The offset of elements in the response. | [optional] 

### Return type

[**TagListResponse**](TagListResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the requested list of tags |  -  |
**401** | Unauthorized action |  -  |
**403** | User is not brandzone user and doesn&#39;t have tags subscription |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag_put**
> update_tag_put(tag_id, tag_request)

Modify a tag

Use this resource to update a tag. <a href=\"../../news/2018-09-24-tagi-zalaczniki/#ZmienNazwe\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.OfferTagsApi(api_client)
    tag_id = 'tag_id_example' # str | Tag identifier.
tag_request = allegro_api.TagRequest() # TagRequest | request

    try:
        # Modify a tag
        api_instance.update_tag_put(tag_id, tag_request)
    except ApiException as e:
        print("Exception when calling OfferTagsApi->update_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| Tag identifier. | 
 **tag_request** | [**TagRequest**](TagRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the requested tag |  -  |
**422** | Validation failed - your request was correct, but the tag could not be updated. |  -  |
**401** | Unauthorized action |  -  |
**403** | User is not brandzone user and doesn&#39;t have tags subscription |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

