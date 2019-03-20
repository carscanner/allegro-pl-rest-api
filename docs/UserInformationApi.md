# allegro_api.UserInformationApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_ratings_using_get**](UserInformationApi.md#get_user_ratings_using_get) | **GET** /sale/user-ratings | Get the user&#39;s ratings


# **get_user_ratings_using_get**
> UserRatingListResponse get_user_ratings_using_get(user_id, recommended=recommended, offset=offset, limit=limit)

Get the user's ratings

Use this resource to receive your sales score. More information about this resource you can find <a href=\"../../news/2017-10-09-news_informacje_o_ocenach/\" target=\"_blank\">here</a>.

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
api_instance = allegro_api.UserInformationApi(allegro_api.ApiClient(configuration))
user_id = 'user_id_example' # str | Filter by user id, you are allowed to get your ratings only
recommended = 'recommended_example' # str | Filter by recommended (optional)
offset = 0 # int | Offset (optional) (default to 0)
limit = 20 # int | Limit (optional) (default to 20)

try:
    # Get the user's ratings
    api_response = api_instance.get_user_ratings_using_get(user_id, recommended=recommended, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInformationApi->get_user_ratings_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Filter by user id, you are allowed to get your ratings only | 
 **recommended** | **str**| Filter by recommended | [optional] 
 **offset** | **int**| Offset | [optional] [default to 0]
 **limit** | **int**| Limit | [optional] [default to 20]

### Return type

[**UserRatingListResponse**](UserRatingListResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

