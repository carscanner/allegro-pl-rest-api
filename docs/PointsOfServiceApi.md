# allegro_api.PointsOfServiceApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pos_using_post**](PointsOfServiceApi.md#create_pos_using_post) | **POST** /points-of-service | Create a point of service
[**delete_pos_using_delete**](PointsOfServiceApi.md#delete_pos_using_delete) | **DELETE** /points-of-service/{id} | Delete a point of service
[**get_pos_data_using_get**](PointsOfServiceApi.md#get_pos_data_using_get) | **GET** /points-of-service/{id} | Get the details of a point of service
[**get_pos_list_using_get**](PointsOfServiceApi.md#get_pos_list_using_get) | **GET** /points-of-service | Get the user&#39;s points of service
[**modify_pos_using_put**](PointsOfServiceApi.md#modify_pos_using_put) | **PUT** /points-of-service/{id} | Modify a point of service


# **create_pos_using_post**
> Pos create_pos_using_post(pos)

Create a point of service

Use this resource to create a point of service. More information about this resource you can find <a href=\"../../news/2017-08-11-punkty_odbioru/#1\" target=\"_blank\">here</a>.

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
api_instance = allegro_api.PointsOfServiceApi(allegro_api.ApiClient(configuration))
pos = allegro_api.Pos() # Pos | Point of service

try:
    # Create a point of service
    api_response = api_instance.create_pos_using_post(pos)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointsOfServiceApi->create_pos_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pos** | [**Pos**](Pos.md)| Point of service | 

### Return type

[**Pos**](Pos.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pos_using_delete**
> delete_pos_using_delete(id)

Delete a point of service

Use this resource to delete a point of service. More information about this resource you can find <a href=\"../../news/2017-08-11-punkty_odbioru/#5\" target=\"_blank\">here.

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
api_instance = allegro_api.PointsOfServiceApi(allegro_api.ApiClient(configuration))
id = 'id_example' # str | Point of service ID

try:
    # Delete a point of service
    api_instance.delete_pos_using_delete(id)
except ApiException as e:
    print("Exception when calling PointsOfServiceApi->delete_pos_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Point of service ID | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pos_data_using_get**
> Pos get_pos_data_using_get(id)

Get the details of a point of service

Use this resource to get a details of a point of service for a given ID. More information about this resource you can find <a href=\"../../news/2017-08-11-punkty_odbioru/#4\" target=\"_blank\">here.

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
api_instance = allegro_api.PointsOfServiceApi(allegro_api.ApiClient(configuration))
id = 'id_example' # str | Point of service ID

try:
    # Get the details of a point of service
    api_response = api_instance.get_pos_data_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointsOfServiceApi->get_pos_data_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Point of service ID | 

### Return type

[**Pos**](Pos.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pos_list_using_get**
> SearchResult get_pos_list_using_get(seller_id)

Get the user's points of service

Use this resource to get a list of points of service by seller ID. More information about this resource you can find <a href=\"../../news/2017-08-11-punkty_odbioru/#3\" target=\"_blank\">here</a>.

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
api_instance = allegro_api.PointsOfServiceApi(allegro_api.ApiClient(configuration))
seller_id = 'seller_id_example' # str | User ID

try:
    # Get the user's points of service
    api_response = api_instance.get_pos_list_using_get(seller_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointsOfServiceApi->get_pos_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| User ID | 

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_pos_using_put**
> Pos modify_pos_using_put(id, pos)

Modify a point of service

Use this resource to modify a point of service. More information about this resource you can find <a href=\"../../news/2017-08-11-punkty_odbioru/#2\" target=\"_blank\">here.

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
api_instance = allegro_api.PointsOfServiceApi(allegro_api.ApiClient(configuration))
id = 'id_example' # str | Point of service ID. Must match values with 'id' property from the body.
pos = allegro_api.Pos() # Pos | Point of service

try:
    # Modify a point of service
    api_response = api_instance.modify_pos_using_put(id, pos)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointsOfServiceApi->modify_pos_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Point of service ID. Must match values with &#39;id&#39; property from the body. | 
 **pos** | [**Pos**](Pos.md)| Point of service | 

### Return type

[**Pos**](Pos.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

