# allegro_api.CategoriesAndParametersApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_categories_using_get**](CategoriesAndParametersApi.md#get_categories_using_get) | **GET** /sale/categories | Get IDs of Allegro categories
[**get_category_using_get1**](CategoriesAndParametersApi.md#get_category_using_get1) | **GET** /sale/categories/{categoryId} | Get a category by ID
[**get_flat_parameters_using_get2**](CategoriesAndParametersApi.md#get_flat_parameters_using_get2) | **GET** /sale/categories/{categoryId}/parameters | Get parameters supported by a category


# **get_categories_using_get**
> CategoriesDto get_categories_using_get(parent_id=parent_id)

Get IDs of Allegro categories

Use this resource to traverse the Allegro categories tree. It returns the list of the given category's children or a list of the main Allegro categories. <a href=\"../../sale/#categories\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.CategoriesAndParametersApi(api_client)
    parent_id = '954b95b6-43cf-4104-8354-dea4d9b10ddf' # str | The ID of the category which children should be returned. If omitted, the list of main Allegro categories will be returned. (optional) (default to '954b95b6-43cf-4104-8354-dea4d9b10ddf')

    try:
        # Get IDs of Allegro categories
        api_response = api_instance.get_categories_using_get(parent_id=parent_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesAndParametersApi->get_categories_using_get: %s\n" % e)
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
    api_instance = allegro_api.CategoriesAndParametersApi(api_client)
    parent_id = '954b95b6-43cf-4104-8354-dea4d9b10ddf' # str | The ID of the category which children should be returned. If omitted, the list of main Allegro categories will be returned. (optional) (default to '954b95b6-43cf-4104-8354-dea4d9b10ddf')

    try:
        # Get IDs of Allegro categories
        api_response = api_instance.get_categories_using_get(parent_id=parent_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesAndParametersApi->get_categories_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **str**| The ID of the category which children should be returned. If omitted, the list of main Allegro categories will be returned. | [optional] [default to &#39;954b95b6-43cf-4104-8354-dea4d9b10ddf&#39;]

### Return type

[**CategoriesDto**](CategoriesDto.md)

### Authorization

[bearer-token-for-application](../README.md#bearer-token-for-application), [bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of categories returned successfully. |  -  |
**404** | The category with the given ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_using_get1**
> CategoryDto get_category_using_get1(category_id)

Get a category by ID

Use this resource to get the details of a specific category. <a href=\"../../news/2018-07-09-wielowariantowosc/#01\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.CategoriesAndParametersApi(api_client)
    category_id = '6061' # str | The category ID.

    try:
        # Get a category by ID
        api_response = api_instance.get_category_using_get1(category_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesAndParametersApi->get_category_using_get1: %s\n" % e)
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
    api_instance = allegro_api.CategoriesAndParametersApi(api_client)
    category_id = '6061' # str | The category ID.

    try:
        # Get a category by ID
        api_response = api_instance.get_category_using_get1(category_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesAndParametersApi->get_category_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The category ID. | 

### Return type

[**CategoryDto**](CategoryDto.md)

### Authorization

[bearer-token-for-application](../README.md#bearer-token-for-application), [bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of a category returned successfully. |  -  |
**404** | The category with the given ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flat_parameters_using_get2**
> CategoryParameterList get_flat_parameters_using_get2(category_id)

Get parameters supported by a category

Use this resource to get the list of parameters that are supported by the given category. <a href=\"../../sale/#parameters\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.CategoriesAndParametersApi(api_client)
    category_id = '709' # str | The category ID.

    try:
        # Get parameters supported by a category
        api_response = api_instance.get_flat_parameters_using_get2(category_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesAndParametersApi->get_flat_parameters_using_get2: %s\n" % e)
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
    api_instance = allegro_api.CategoriesAndParametersApi(api_client)
    category_id = '709' # str | The category ID.

    try:
        # Get parameters supported by a category
        api_response = api_instance.get_flat_parameters_using_get2(category_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesAndParametersApi->get_flat_parameters_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The category ID. | 

### Return type

[**CategoryParameterList**](CategoryParameterList.md)

### Authorization

[bearer-token-for-application](../README.md#bearer-token-for-application), [bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of parameters for the category returned successfully. |  -  |
**404** | The category with the given ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

