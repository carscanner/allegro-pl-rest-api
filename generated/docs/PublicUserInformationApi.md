# allegro_api.PublicUserInformationApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_summary_using_get**](PublicUserInformationApi.md#get_user_summary_using_get) | **GET** /users/{userId}/ratings-summary | Get any user&#39;s ratings summary


# **get_user_summary_using_get**
> UserRatingSummaryResponse get_user_summary_using_get(user_id)

Get any user's ratings summary

Use this resource to receive feedback statistics. <a href=\"../../news/2017-10-09-news_informacje_o_ocenach/\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.PublicUserInformationApi(api_client)
    user_id = '41846511' # str | The ID of the user.

    try:
        # Get any user's ratings summary
        api_response = api_instance.get_user_summary_using_get(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicUserInformationApi->get_user_summary_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user. | 

### Return type

[**UserRatingSummaryResponse**](UserRatingSummaryResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Feedback statistics returned successfully. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | User with the given ID not found or user is not a seller. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

