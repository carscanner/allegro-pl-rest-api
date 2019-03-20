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

Use this resource to assign a tag to offer. More information about this resource you can find <a href=\"../../news/2018-09-24-tagi-zalaczniki/#PrzypiszTagiDoOferty\" target=\"_blank\">here</a>. 

### Example

* OAuth Authentication (bearer-token-for-user): 
```python
from __future__ import print_function
import time
import allegro_api
from allegro_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration = allegro_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = allegro_api.OfferTagsApi(allegro_api.ApiClient(configuration))
offer_id = 'offer_id_example' # str | offerId
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
 **offer_id** | **str**| offerId | 
 **tag_ids_request** | [**TagIdsRequest**](TagIdsRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tag_post1**
> TagId create_tag_post1(tag_request)

Create a tag

Use this resource to create a new tag. More information about this resource you can find <a href=\"../../news/2018-09-24-tagi-zalaczniki/#DodajDoKonta\" target=\"_blank\">here</a>. 

### Example

* OAuth Authentication (bearer-token-for-user): 
```python
from __future__ import print_function
import time
import allegro_api
from allegro_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration = allegro_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = allegro_api.OfferTagsApi(allegro_api.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag_using_delete**
> delete_tag_using_delete(tag_id)

Delete a tag

Use this resource to delete the tag. More information about this resource you can find <a href=\"../../news/2018-09-24-tagi-zalaczniki/#UsunTagZKonta\" target=\"_blank\">here</a>.

### Example

* OAuth Authentication (bearer-token-for-user): 
```python
from __future__ import print_function
import time
import allegro_api
from allegro_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration = allegro_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = allegro_api.OfferTagsApi(allegro_api.ApiClient(configuration))
tag_id = 'tag_id_example' # str | tagId

try:
    # Delete a tag
    api_instance.delete_tag_using_delete(tag_id)
except ApiException as e:
    print("Exception when calling OfferTagsApi->delete_tag_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| tagId | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assigned_offer_tags_get**
> TagListResponse list_assigned_offer_tags_get(offer_id)

Get tags assigned to an offer

Use this resource to get a list of tags assigned to offer. More information about this resource you can find <a href=\"../../news/2018-09-24-tagi-zalaczniki/#PobierzTagiZOferty\" target=\"_blank\">here</a>.

### Example

* OAuth Authentication (bearer-token-for-user): 
```python
from __future__ import print_function
import time
import allegro_api
from allegro_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration = allegro_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = allegro_api.OfferTagsApi(allegro_api.ApiClient(configuration))
offer_id = 'offer_id_example' # str | offerId

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
 **offer_id** | **str**| offerId | 

### Return type

[**TagListResponse**](TagListResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_seller_tags_get1**
> TagListResponse list_seller_tags_get1(user_id, limit=limit, offset=offset)

Get the user's tags

Use this resource to get a list of tags defined by the specified user (Defaults: limit = 1000, offset = 0). More information about this resource you can find <a href=\"../../news/2018-09-24-tagi-zalaczniki/#PobierzTagi\" target=\"_blank\">here</a>.

### Example

* OAuth Authentication (bearer-token-for-user): 
```python
from __future__ import print_function
import time
import allegro_api
from allegro_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration = allegro_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = allegro_api.OfferTagsApi(allegro_api.ApiClient(configuration))
user_id = 'user_id_example' # str | user.id
limit = 56 # int | limit (optional)
offset = 56 # int | offset (optional)

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
 **user_id** | **str**| user.id | 
 **limit** | **int**| limit | [optional] 
 **offset** | **int**| offset | [optional] 

### Return type

[**TagListResponse**](TagListResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag_put**
> update_tag_put(tag_id, tag_request)

Modify a tag

Use this resource to update a tag. More information about this resource you can find <a href=\"../../news/2018-09-24-tagi-zalaczniki/#ZmienNazwe\" target=\"_blank\">here</a>.

### Example

* OAuth Authentication (bearer-token-for-user): 
```python
from __future__ import print_function
import time
import allegro_api
from allegro_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration = allegro_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = allegro_api.OfferTagsApi(allegro_api.ApiClient(configuration))
tag_id = 'tag_id_example' # str | tagId
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
 **tag_id** | **str**| tagId | 
 **tag_request** | [**TagRequest**](TagRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

