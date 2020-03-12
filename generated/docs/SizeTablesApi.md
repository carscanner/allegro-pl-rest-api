# allegro_api.SizeTablesApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_table_using_get**](SizeTablesApi.md#get_table_using_get) | **GET** /sale/size-tables/{tableId} | Get a size table details
[**get_tables_using_get**](SizeTablesApi.md#get_tables_using_get) | **GET** /sale/size-tables | Get the user&#39;s size tables


# **get_table_using_get**
> PublicTableDto get_table_using_get(table_id)

Get a size table details

Use this resource to get selected size table. <a href=\"../../news/2018-04-19-news_tabele_rozmiarow/\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.SizeTablesApi(api_client)
    table_id = 'table_id_example' # str | Table identifier.

    try:
        # Get a size table details
        api_response = api_instance.get_table_using_get(table_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SizeTablesApi->get_table_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_id** | **str**| Table identifier. | 

### Return type

[**PublicTableDto**](PublicTableDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Size table returned successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tables_using_get**
> PublicTablesDto get_tables_using_get(user_id)

Get the user's size tables

Use this resource to get all size tables assigned to a seller account. <a href=\"../../news/2018-04-19-news_tabele_rozmiarow/\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.SizeTablesApi(api_client)
    user_id = 'user_id_example' # str | User identifier.

    try:
        # Get the user's size tables
        api_response = api_instance.get_tables_using_get(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SizeTablesApi->get_tables_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User identifier. | 

### Return type

[**PublicTablesDto**](PublicTablesDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Size tables returned successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

