# allegro_api.PublicOfferInformationApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_listing**](PublicOfferInformationApi.md#get_listing) | **GET** /offers/listing | Search offers


# **get_listing**
> ListingResponse get_listing(category_id=category_id, phrase=phrase, seller_id=seller_id, search_mode=search_mode, offset=offset, limit=limit, sort=sort, include=include, fallback=fallback, dynamic_filters=dynamic_filters)

Search offers

Use this resource to get a list of offers based on the provided query parameters. At least one of: phrase, seller.id or category.id is required. Additional available parameters vary depending on category.id. The parameters are defined in the filters entity. <a href=\"../../news/2018-07-03-listing_ofert/\" target=\"_blank\">Read more</a>.

### Example

* OAuth Authentication (bearer-token-for-application):
```python
from __future__ import print_function
import time
import allegro_api
from allegro_api.rest import ApiException
from pprint import pprint
configuration = allegro_api.Configuration()
# Configure OAuth2 access token for authorization: bearer-token-for-application
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = allegro_api.Configuration()
# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.allegro.pl
configuration.host = "https://api.allegro.pl"
# Enter a context with an instance of the API client
with allegro_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = allegro_api.PublicOfferInformationApi(api_client)
    category_id = 'category_id_example' # str | The identifier of the category, where you want to search for offers. (optional)
phrase = 'phrase_example' # str | The search phrase. The phrase is searched in different fields of the offers depending on the value of the `searchMode` parameter. (optional)
seller_id = 'seller_id_example' # str | The identifier of a seller, to limit the results to offers from this seller. May be provided more than once. (optional)
search_mode = 'REGULAR' # str | Defines where the given phrase should be searched in. Allowed values:    - *REGULAR* - searching for a phrase in the title,   - *DESCRIPTIONS* - searching for a phrase in the title and the descriptions,   - *CLOSED* - searching for a phrase in the title of closed offers. (optional) (default to 'REGULAR')
offset = 56 # int | Index of the first returned offer from all search results. (optional)
limit = 60 # int | The maximum number of offers in a response. (optional) (default to 60)
sort = 'relevance' # str | Search results sorting order. `+` or no prefix in the value means ascending order. `-` prefix means descending order. (optional) (default to 'relevance')
include = 'include_example' # str | Specify parts of the response that should be included in the output. Allowed values are the names of top level entities and *all* as an alias to all entities. By default, all top level entities are included. Use `-` prefix to exclude an entity. Example: `include=-all&include=filters&include=sort` - returns only filters and sort entities. (optional)
fallback = True # bool | Defines the behaviour of the search engine when no results with exact phrase match are found:    - *true* - related (not exact) results are returned,   - *false* - empty results are returned. (optional) (default to True)
dynamic_filters = {'key': 'dynamic_filters_example'} # dict(str, str) | You can filter and customize your search results to find exactly what you need by applying filters ids and their dictionary values to query according to the flowing pattern: id=value. When the filter definition looks like:   ````     {      \"id\": \"parameter.11323\",      \"type\": \"MULTI\",      \"name\": \"Stan\",      \"values\": [{        \"value\": \"11323_1\",        \"name\": \"nowe\",        \"count\": 21,        \"selected\": false       },       {        \"value\": \"11323_2\",        \"name\": \"używane\",        \"count\": 157,        \"selected\": false       },       {        \"value\": \"11323_238066\",        \"name\": \"po zwrocie\",        \"count\": 1,        \"selected\": false       }      ]     }   ```` You can use 'Stan' filter to query results, i.e.:   * `parameter.11323=11323_1` for \"nowe\"   * `parameter.11323=11323_2` for \"używane\"   * `parameter.11323=11323_238066` for \"po zwrocie\". (optional)

    try:
        # Search offers
        api_response = api_instance.get_listing(category_id=category_id, phrase=phrase, seller_id=seller_id, search_mode=search_mode, offset=offset, limit=limit, sort=sort, include=include, fallback=fallback, dynamic_filters=dynamic_filters)
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
configuration = allegro_api.Configuration()
# Configure OAuth2 access token for authorization: bearer-token-for-application
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = allegro_api.Configuration()
# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.allegro.pl
configuration.host = "https://api.allegro.pl"
# Enter a context with an instance of the API client
with allegro_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = allegro_api.PublicOfferInformationApi(api_client)
    category_id = 'category_id_example' # str | The identifier of the category, where you want to search for offers. (optional)
phrase = 'phrase_example' # str | The search phrase. The phrase is searched in different fields of the offers depending on the value of the `searchMode` parameter. (optional)
seller_id = 'seller_id_example' # str | The identifier of a seller, to limit the results to offers from this seller. May be provided more than once. (optional)
search_mode = 'REGULAR' # str | Defines where the given phrase should be searched in. Allowed values:    - *REGULAR* - searching for a phrase in the title,   - *DESCRIPTIONS* - searching for a phrase in the title and the descriptions,   - *CLOSED* - searching for a phrase in the title of closed offers. (optional) (default to 'REGULAR')
offset = 56 # int | Index of the first returned offer from all search results. (optional)
limit = 60 # int | The maximum number of offers in a response. (optional) (default to 60)
sort = 'relevance' # str | Search results sorting order. `+` or no prefix in the value means ascending order. `-` prefix means descending order. (optional) (default to 'relevance')
include = 'include_example' # str | Specify parts of the response that should be included in the output. Allowed values are the names of top level entities and *all* as an alias to all entities. By default, all top level entities are included. Use `-` prefix to exclude an entity. Example: `include=-all&include=filters&include=sort` - returns only filters and sort entities. (optional)
fallback = True # bool | Defines the behaviour of the search engine when no results with exact phrase match are found:    - *true* - related (not exact) results are returned,   - *false* - empty results are returned. (optional) (default to True)
dynamic_filters = {'key': 'dynamic_filters_example'} # dict(str, str) | You can filter and customize your search results to find exactly what you need by applying filters ids and their dictionary values to query according to the flowing pattern: id=value. When the filter definition looks like:   ````     {      \"id\": \"parameter.11323\",      \"type\": \"MULTI\",      \"name\": \"Stan\",      \"values\": [{        \"value\": \"11323_1\",        \"name\": \"nowe\",        \"count\": 21,        \"selected\": false       },       {        \"value\": \"11323_2\",        \"name\": \"używane\",        \"count\": 157,        \"selected\": false       },       {        \"value\": \"11323_238066\",        \"name\": \"po zwrocie\",        \"count\": 1,        \"selected\": false       }      ]     }   ```` You can use 'Stan' filter to query results, i.e.:   * `parameter.11323=11323_1` for \"nowe\"   * `parameter.11323=11323_2` for \"używane\"   * `parameter.11323=11323_238066` for \"po zwrocie\". (optional)

    try:
        # Search offers
        api_response = api_instance.get_listing(category_id=category_id, phrase=phrase, seller_id=seller_id, search_mode=search_mode, offset=offset, limit=limit, sort=sort, include=include, fallback=fallback, dynamic_filters=dynamic_filters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicOfferInformationApi->get_listing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The identifier of the category, where you want to search for offers. | [optional] 
 **phrase** | **str**| The search phrase. The phrase is searched in different fields of the offers depending on the value of the &#x60;searchMode&#x60; parameter. | [optional] 
 **seller_id** | **str**| The identifier of a seller, to limit the results to offers from this seller. May be provided more than once. | [optional] 
 **search_mode** | **str**| Defines where the given phrase should be searched in. Allowed values:    - *REGULAR* - searching for a phrase in the title,   - *DESCRIPTIONS* - searching for a phrase in the title and the descriptions,   - *CLOSED* - searching for a phrase in the title of closed offers. | [optional] [default to &#39;REGULAR&#39;]
 **offset** | **int**| Index of the first returned offer from all search results. | [optional] 
 **limit** | **int**| The maximum number of offers in a response. | [optional] [default to 60]
 **sort** | **str**| Search results sorting order. &#x60;+&#x60; or no prefix in the value means ascending order. &#x60;-&#x60; prefix means descending order. | [optional] [default to &#39;relevance&#39;]
 **include** | **str**| Specify parts of the response that should be included in the output. Allowed values are the names of top level entities and *all* as an alias to all entities. By default, all top level entities are included. Use &#x60;-&#x60; prefix to exclude an entity. Example: &#x60;include&#x3D;-all&amp;include&#x3D;filters&amp;include&#x3D;sort&#x60; - returns only filters and sort entities. | [optional] 
 **fallback** | **bool**| Defines the behaviour of the search engine when no results with exact phrase match are found:    - *true* - related (not exact) results are returned,   - *false* - empty results are returned. | [optional] [default to True]
 **dynamic_filters** | [**dict(str, str)**](str.md)| You can filter and customize your search results to find exactly what you need by applying filters ids and their dictionary values to query according to the flowing pattern: id&#x3D;value. When the filter definition looks like:   &#x60;&#x60;&#x60;&#x60;     {      \&quot;id\&quot;: \&quot;parameter.11323\&quot;,      \&quot;type\&quot;: \&quot;MULTI\&quot;,      \&quot;name\&quot;: \&quot;Stan\&quot;,      \&quot;values\&quot;: [{        \&quot;value\&quot;: \&quot;11323_1\&quot;,        \&quot;name\&quot;: \&quot;nowe\&quot;,        \&quot;count\&quot;: 21,        \&quot;selected\&quot;: false       },       {        \&quot;value\&quot;: \&quot;11323_2\&quot;,        \&quot;name\&quot;: \&quot;używane\&quot;,        \&quot;count\&quot;: 157,        \&quot;selected\&quot;: false       },       {        \&quot;value\&quot;: \&quot;11323_238066\&quot;,        \&quot;name\&quot;: \&quot;po zwrocie\&quot;,        \&quot;count\&quot;: 1,        \&quot;selected\&quot;: false       }      ]     }   &#x60;&#x60;&#x60;&#x60; You can use &#39;Stan&#39; filter to query results, i.e.:   * &#x60;parameter.11323&#x3D;11323_1&#x60; for \&quot;nowe\&quot;   * &#x60;parameter.11323&#x3D;11323_2&#x60; for \&quot;używane\&quot;   * &#x60;parameter.11323&#x3D;11323_238066&#x60; for \&quot;po zwrocie\&quot;. | [optional] 

### Return type

[**ListingResponse**](ListingResponse.md)

### Authorization

[bearer-token-for-application](../README.md#bearer-token-for-application), [bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request successfully returns the search result. |  -  |
**400** | Bad request. Check if all necessary parameters are provided. |  -  |
**404** | Given category was not found. Check category.id parameter. |  -  |
**422** | One of parameters have invalid value or given parameters combination is forbidden. |  -  |
**500** | Internal service error. |  -  |
**502** | Error caused by upstream service failure. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

