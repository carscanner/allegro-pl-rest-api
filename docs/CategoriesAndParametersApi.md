# openapi_client.CategoriesAndParametersApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_categories_using_get**](CategoriesAndParametersApi.md#get_categories_using_get) | **GET** /sale/categories | Get IDs of main Allegro categories
[**get_category_using_get1**](CategoriesAndParametersApi.md#get_category_using_get1) | **GET** /sale/categories/{categoryId} | Get category by ID
[**get_flat_parameters_using_get2**](CategoriesAndParametersApi.md#get_flat_parameters_using_get2) | **GET** /sale/categories/{categoryId}/parameters | Get parameters by category ID


# **get_categories_using_get**
> CategoriesDto get_categories_using_get(parent_id=parent_id)

Get IDs of main Allegro categories

Use this resource to get IDs of main Allegro categories. More information about this resource you can find <a href=\"../../sale/#categories\" target=\"_blank\">here</a>.

### Example

* OAuth Authentication (bearer-token-for-application): 
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-application
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.CategoriesAndParametersApi(openapi_client.ApiClient(configuration))
parent_id = '954b95b6-43cf-4104-8354-dea4d9b10ddf' # str | parent.id (optional) (default to '954b95b6-43cf-4104-8354-dea4d9b10ddf')

try:
    # Get IDs of main Allegro categories
    api_response = api_instance.get_categories_using_get(parent_id=parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesAndParametersApi->get_categories_using_get: %s\n" % e)
```


* OAuth Authentication (bearer-token-for-user): 
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.CategoriesAndParametersApi(openapi_client.ApiClient(configuration))
parent_id = '954b95b6-43cf-4104-8354-dea4d9b10ddf' # str | parent.id (optional) (default to '954b95b6-43cf-4104-8354-dea4d9b10ddf')

try:
    # Get IDs of main Allegro categories
    api_response = api_instance.get_categories_using_get(parent_id=parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesAndParametersApi->get_categories_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **str**| parent.id | [optional] [default to &#39;954b95b6-43cf-4104-8354-dea4d9b10ddf&#39;]

### Return type

[**CategoriesDto**](CategoriesDto.md)

### Authorization

[bearer-token-for-application](../README.md#bearer-token-for-application), [bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_using_get1**
> CategoryDto get_category_using_get1(category_id)

Get category by ID

Use this resource to get the lowest tier category (remember – an offer can be listed in the lowest tier category if the category is marked “leaf”: true). More information about this resource you can find <a href=\"../../news/2018-07-09-wielowariantowosc/#01\" target=\"_blank\">here</a>.

### Example

* OAuth Authentication (bearer-token-for-application): 
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-application
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.CategoriesAndParametersApi(openapi_client.ApiClient(configuration))
category_id = 'category_id_example' # str | categoryId

try:
    # Get category by ID
    api_response = api_instance.get_category_using_get1(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesAndParametersApi->get_category_using_get1: %s\n" % e)
```


* OAuth Authentication (bearer-token-for-user): 
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.CategoriesAndParametersApi(openapi_client.ApiClient(configuration))
category_id = 'category_id_example' # str | categoryId

try:
    # Get category by ID
    api_response = api_instance.get_category_using_get1(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesAndParametersApi->get_category_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| categoryId | 

### Return type

[**CategoryDto**](CategoryDto.md)

### Authorization

[bearer-token-for-application](../README.md#bearer-token-for-application), [bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flat_parameters_using_get2**
> CategoryParameterList get_flat_parameters_using_get2(category_id)

Get parameters by category ID

Use this resource to get the lists of parameters that are supported by the category you indicated. Every time a list of parameters supported by the input category is returned. More information about this resource you can find <a href=\"../../sale/#parameters\" target=\"_blank\">here</a>.

### Example

* OAuth Authentication (bearer-token-for-application): 
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-application
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.CategoriesAndParametersApi(openapi_client.ApiClient(configuration))
category_id = 'category_id_example' # str | categoryId

try:
    # Get parameters by category ID
    api_response = api_instance.get_flat_parameters_using_get2(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesAndParametersApi->get_flat_parameters_using_get2: %s\n" % e)
```


* OAuth Authentication (bearer-token-for-user): 
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.CategoriesAndParametersApi(openapi_client.ApiClient(configuration))
category_id = 'category_id_example' # str | categoryId

try:
    # Get parameters by category ID
    api_response = api_instance.get_flat_parameters_using_get2(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesAndParametersApi->get_flat_parameters_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| categoryId | 

### Return type

[**CategoryParameterList**](CategoryParameterList.md)

### Authorization

[bearer-token-for-application](../README.md#bearer-token-for-application), [bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

