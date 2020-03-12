# allegro_api.BlacklistManagementApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**do_add_to_black_list**](BlacklistManagementApi.md#do_add_to_black_list) | **POST** /sale/blacklisted-users | Add a users to the blacklist
[**do_get_black_list_users**](BlacklistManagementApi.md#do_get_black_list_users) | **GET** /sale/blacklisted-users | Get list of blacklisted users
[**do_remove_from_black_list**](BlacklistManagementApi.md#do_remove_from_black_list) | **DELETE** /sale/blacklisted-users/{excludedUserId} | Remove users from the blacklist


# **do_add_to_black_list**
> BlackListResponse do_add_to_black_list(blacklist_request)

Add a users to the blacklist

Use this resource to add new users to the blacklist on given account. At least one of id or login is required.

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
    api_instance = allegro_api.BlacklistManagementApi(api_client)
    blacklist_request = allegro_api.BlacklistRequest() # BlacklistRequest | request

    try:
        # Add a users to the blacklist
        api_response = api_instance.do_add_to_black_list(blacklist_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlacklistManagementApi->do_add_to_black_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blacklist_request** | [**BlacklistRequest**](BlacklistRequest.md)| request | 

### Return type

[**BlackListResponse**](BlackListResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Users successfully added to the blacklist. |  -  |
**401** | Unauthorized |  -  |
**409** | User already added to the blacklist. |  -  |
**400** | Request is invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_get_black_list_users**
> BlackListPagedResponse do_get_black_list_users(offset=offset, limit=limit)

Get list of blacklisted users

Use this resource to get a list of blacklisted users created on given account.

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
    api_instance = allegro_api.BlacklistManagementApi(api_client)
    offset = 0 # int | Index of first returned user from all results. (optional) (default to 0)
limit = 25 # int | Maximum number of users in response. (optional) (default to 25)

    try:
        # Get list of blacklisted users
        api_response = api_instance.do_get_black_list_users(offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlacklistManagementApi->do_get_black_list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Index of first returned user from all results. | [optional] [default to 0]
 **limit** | **int**| Maximum number of users in response. | [optional] [default to 25]

### Return type

[**BlackListPagedResponse**](BlackListPagedResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of blacklisted users returned successfully |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_remove_from_black_list**
> do_remove_from_black_list(excluded_user_id)

Remove users from the blacklist

Use this resource to remove users from the blacklist on given account.

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
    api_instance = allegro_api.BlacklistManagementApi(api_client)
    excluded_user_id = 56 # int | Remove users from the blacklist.

    try:
        # Remove users from the blacklist
        api_instance.do_remove_from_black_list(excluded_user_id)
    except ApiException as e:
        print("Exception when calling BlacklistManagementApi->do_remove_from_black_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **excluded_user_id** | **int**| Remove users from the blacklist. | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | User removed form the blacklist successfully. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

