# openapi_client.AdditionalServicesApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_additional_services_group_using_post**](AdditionalServicesApi.md#create_additional_services_group_using_post) | **POST** /sale/offer-additional-services/groups | Create additional services group
[**get_additional_services_group_using_get**](AdditionalServicesApi.md#get_additional_services_group_using_get) | **GET** /sale/offer-additional-services/groups/{groupId} | Get the details of an additional services group
[**get_list_of_additional_services_definitions_using_get**](AdditionalServicesApi.md#get_list_of_additional_services_definitions_using_get) | **GET** /sale/offer-additional-services/definitions | Get the user&#39;s additional services definitions
[**get_list_of_additional_services_groups_using_get**](AdditionalServicesApi.md#get_list_of_additional_services_groups_using_get) | **GET** /sale/offer-additional-services/groups | Get the user&#39;s additional services groups
[**modify_additional_services_group_using_put**](AdditionalServicesApi.md#modify_additional_services_group_using_put) | **PUT** /sale/offer-additional-services/groups/{groupId} | Modify an additional services group


# **create_additional_services_group_using_post**
> AdditionalServicesGroupResponse create_additional_services_group_using_post(additional_services_group_request)

Create additional services group

Use this resource to create a group of additional services. More information about this resource you can find <a href=\"../../news/2017-10-25-news_uslugi_dodatkowe/#2\" target=\"_blank\">here</a>.

### Example

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
api_instance = openapi_client.AdditionalServicesApi(openapi_client.ApiClient(configuration))
additional_services_group_request = openapi_client.AdditionalServicesGroupRequest() # AdditionalServicesGroupRequest | Additional service group body

try:
    # Create additional services group
    api_response = api_instance.create_additional_services_group_using_post(additional_services_group_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdditionalServicesApi->create_additional_services_group_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **additional_services_group_request** | [**AdditionalServicesGroupRequest**](AdditionalServicesGroupRequest.md)| Additional service group body | 

### Return type

[**AdditionalServicesGroupResponse**](AdditionalServicesGroupResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_additional_services_group_using_get**
> AdditionalServicesGroupResponse get_additional_services_group_using_get(group_id)

Get the details of an additional services group

Use this resource to get additional services group for a given ID. More information about this resource you can find <a href=\"../../news/2017-10-25-news_uslugi_dodatkowe/#5\" target=\"_blank\">here</a>.

### Example

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
api_instance = openapi_client.AdditionalServicesApi(openapi_client.ApiClient(configuration))
group_id = 'group_id_example' # str | Additional Service Group ID

try:
    # Get the details of an additional services group
    api_response = api_instance.get_additional_services_group_using_get(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdditionalServicesApi->get_additional_services_group_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Additional Service Group ID | 

### Return type

[**AdditionalServicesGroupResponse**](AdditionalServicesGroupResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_additional_services_definitions_using_get**
> DefinitionsResponse get_list_of_additional_services_definitions_using_get(user_id, offset=offset, limit=limit)

Get the user's additional services definitions

Use this resource to get additional services definitions by user ID. More information about this resource you can find <a href=\"../../news/2017-10-25-news_uslugi_dodatkowe/#1\" target=\"_blank\">here</a>.

### Example

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
api_instance = openapi_client.AdditionalServicesApi(openapi_client.ApiClient(configuration))
user_id = 'user_id_example' # str | User ID
offset = 0 # int | offset (optional) (default to 0)
limit = 100 # int | limit (optional) (default to 100)

try:
    # Get the user's additional services definitions
    api_response = api_instance.get_list_of_additional_services_definitions_using_get(user_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdditionalServicesApi->get_list_of_additional_services_definitions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 
 **offset** | **int**| offset | [optional] [default to 0]
 **limit** | **int**| limit | [optional] [default to 100]

### Return type

[**DefinitionsResponse**](DefinitionsResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_additional_services_groups_using_get**
> AdditionalServicesGroups get_list_of_additional_services_groups_using_get(user_id, offset=offset, limit=limit)

Get the user's additional services groups

Use this resource to retrieve a list of groups with additional services available to a given user which you may assign to offers. More information about this resource you can find <a href=\"../../news/2017-10-25-news_uslugi_dodatkowe/#4\" target=\"_blank\">here</a>.

### Example

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
api_instance = openapi_client.AdditionalServicesApi(openapi_client.ApiClient(configuration))
user_id = 'user_id_example' # str | User ID
offset = 0 # int | offset (optional) (default to 0)
limit = 1000 # int | limit (optional) (default to 1000)

try:
    # Get the user's additional services groups
    api_response = api_instance.get_list_of_additional_services_groups_using_get(user_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdditionalServicesApi->get_list_of_additional_services_groups_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 
 **offset** | **int**| offset | [optional] [default to 0]
 **limit** | **int**| limit | [optional] [default to 1000]

### Return type

[**AdditionalServicesGroups**](AdditionalServicesGroups.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_additional_services_group_using_put**
> AdditionalServicesGroupResponse modify_additional_services_group_using_put(group_id, additional_services_group_request)

Modify an additional services group

Use this resource to modify existing additional service group. More information about this resource you can find <a href=\"../../news/2017-10-25-news_uslugi_dodatkowe/#3\" target=\"_blank\">here</a>.

### Example

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
api_instance = openapi_client.AdditionalServicesApi(openapi_client.ApiClient(configuration))
group_id = 'group_id_example' # str | additional service group ID
additional_services_group_request = openapi_client.AdditionalServicesGroupRequest() # AdditionalServicesGroupRequest | Additional service group body

try:
    # Modify an additional services group
    api_response = api_instance.modify_additional_services_group_using_put(group_id, additional_services_group_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdditionalServicesApi->modify_additional_services_group_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| additional service group ID | 
 **additional_services_group_request** | [**AdditionalServicesGroupRequest**](AdditionalServicesGroupRequest.md)| Additional service group body | 

### Return type

[**AdditionalServicesGroupResponse**](AdditionalServicesGroupResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

