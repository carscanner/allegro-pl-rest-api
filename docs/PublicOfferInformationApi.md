# allegro_api.PublicOfferInformationApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_listing**](PublicOfferInformationApi.md#get_listing) | **GET** /offers/listing | Search offers


# **get_listing**
> ListingResponse get_listing(category_id=category_id, phrase=phrase, seller_id=seller_id, search_mode=search_mode, offset=offset, limit=limit, sort=sort, include=include, fallback=fallback)

Search offers

Use this resource to get a list of offers according to provided parameters. At least one of: phrase, seller.id or category.id is required. Additional available parameters vary depending on category.id. The parameters are defined in the filters entity. More information about this resource you can find <a href=\"../../news/2018-07-03-listing_ofert/\" target=\"_blank\">here</a>.

### Example

* OAuth Authentication (bearer-token-for-application): 
```python
from __future__ import print_function
import time
import allegro_api
from allegro_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-application
configuration = allegro_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = allegro_api.PublicOfferInformationApi(allegro_api.ApiClient(configuration))
category_id = 'category_id_example' # str | The category identifier to search. (optional)
phrase = 'phrase_example' # str | Search phrase. (optional)
seller_id = 'seller_id_example' # str | Identifier of the seller. May be provided more than once. Only items of provided sellers are returned. (optional)
search_mode = 'search_mode_example' # str | Search mode. Allowed values: *REGULAR* - searching for a phrase in the title of offers; *DESCRIPTIONS* - searching for a phrase in titles and offers descriptions; *CLOSED* -  searching for a phrase in titles of closed offers. Default *REGULAR*. (optional)
offset = 56 # int | Index of first returned offer from all search results. (optional)
limit = 56 # int | Maximum number of offers in response (acceptable values: from 0 to 100, default is 60). (optional)
sort = 'sort_example' # str | Search results sorting order. Allowed values (+ or no prefix means ascending order, - prefix means descending order): relevance, +price, -price, +withDeliveryPrice, -withDeliveryPrice, -popularity, +endTime, -startTime. The default sorting order is relevancy. (optional)
include = 'include_example' # str | Specify parts that should be included in the output. Allowed values are names of top level entities and *all* as an alias to all entities. By default, all top level entities are included. Use \"-\" prefix to exclude entity. Example: *include=-all&include=filters&include=sort* - returns only filters and sort entities. (optional)
fallback = True # bool | Defines behaviour of searching when no results with exact phrase match are found: *true* - related (not exact) results are returned; *false* - empty results are returned. The default is true. (optional)

try:
    # Search offers
    api_response = api_instance.get_listing(category_id=category_id, phrase=phrase, seller_id=seller_id, search_mode=search_mode, offset=offset, limit=limit, sort=sort, include=include, fallback=fallback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicOfferInformationApi->get_listing: %s\n" % e)
```


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
api_instance = allegro_api.PublicOfferInformationApi(allegro_api.ApiClient(configuration))
category_id = 'category_id_example' # str | The category identifier to search. (optional)
phrase = 'phrase_example' # str | Search phrase. (optional)
seller_id = 'seller_id_example' # str | Identifier of the seller. May be provided more than once. Only items of provided sellers are returned. (optional)
search_mode = 'search_mode_example' # str | Search mode. Allowed values: *REGULAR* - searching for a phrase in the title of offers; *DESCRIPTIONS* - searching for a phrase in titles and offers descriptions; *CLOSED* -  searching for a phrase in titles of closed offers. Default *REGULAR*. (optional)
offset = 56 # int | Index of first returned offer from all search results. (optional)
limit = 56 # int | Maximum number of offers in response (acceptable values: from 0 to 100, default is 60). (optional)
sort = 'sort_example' # str | Search results sorting order. Allowed values (+ or no prefix means ascending order, - prefix means descending order): relevance, +price, -price, +withDeliveryPrice, -withDeliveryPrice, -popularity, +endTime, -startTime. The default sorting order is relevancy. (optional)
include = 'include_example' # str | Specify parts that should be included in the output. Allowed values are names of top level entities and *all* as an alias to all entities. By default, all top level entities are included. Use \"-\" prefix to exclude entity. Example: *include=-all&include=filters&include=sort* - returns only filters and sort entities. (optional)
fallback = True # bool | Defines behaviour of searching when no results with exact phrase match are found: *true* - related (not exact) results are returned; *false* - empty results are returned. The default is true. (optional)

try:
    # Search offers
    api_response = api_instance.get_listing(category_id=category_id, phrase=phrase, seller_id=seller_id, search_mode=search_mode, offset=offset, limit=limit, sort=sort, include=include, fallback=fallback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicOfferInformationApi->get_listing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The category identifier to search. | [optional] 
 **phrase** | **str**| Search phrase. | [optional] 
 **seller_id** | **str**| Identifier of the seller. May be provided more than once. Only items of provided sellers are returned. | [optional] 
 **search_mode** | **str**| Search mode. Allowed values: *REGULAR* - searching for a phrase in the title of offers; *DESCRIPTIONS* - searching for a phrase in titles and offers descriptions; *CLOSED* -  searching for a phrase in titles of closed offers. Default *REGULAR*. | [optional] 
 **offset** | **int**| Index of first returned offer from all search results. | [optional] 
 **limit** | **int**| Maximum number of offers in response (acceptable values: from 0 to 100, default is 60). | [optional] 
 **sort** | **str**| Search results sorting order. Allowed values (+ or no prefix means ascending order, - prefix means descending order): relevance, +price, -price, +withDeliveryPrice, -withDeliveryPrice, -popularity, +endTime, -startTime. The default sorting order is relevancy. | [optional] 
 **include** | **str**| Specify parts that should be included in the output. Allowed values are names of top level entities and *all* as an alias to all entities. By default, all top level entities are included. Use \&quot;-\&quot; prefix to exclude entity. Example: *include&#x3D;-all&amp;include&#x3D;filters&amp;include&#x3D;sort* - returns only filters and sort entities. | [optional] 
 **fallback** | **bool**| Defines behaviour of searching when no results with exact phrase match are found: *true* - related (not exact) results are returned; *false* - empty results are returned. The default is true. | [optional] 

### Return type

[**ListingResponse**](ListingResponse.md)

### Authorization

[bearer-token-for-application](../README.md#bearer-token-for-application), [bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

