# allegro_api.DeliveryApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shipping_rates_set_using_post**](DeliveryApi.md#create_shipping_rates_set_using_post) | **POST** /sale/shipping-rates | Create a new shipping rates set
[**get_list_of_delivery_methods_using_get**](DeliveryApi.md#get_list_of_delivery_methods_using_get) | **GET** /sale/delivery-methods | Get the list of available delivery methods
[**get_list_of_shipping_ratest_using_get**](DeliveryApi.md#get_list_of_shipping_ratest_using_get) | **GET** /sale/shipping-rates | Get the user&#39;s shipping rates
[**get_shipping_rates_set_using_get**](DeliveryApi.md#get_shipping_rates_set_using_get) | **GET** /sale/shipping-rates/{id} | Get the details of a shipping rates set
[**modify_shipiing_rates_set_using_put**](DeliveryApi.md#modify_shipiing_rates_set_using_put) | **PUT** /sale/shipping-rates/{id} | Edit a user&#39;s shipping rates set


# **create_shipping_rates_set_using_post**
> ShippingRatesSet create_shipping_rates_set_using_post(shipping_rates_set)

Create a new shipping rates set

Use this resource to create a new seller's shipping rates set. More information about this resource you can find <a href=\"../news/2018-08-14-cenniki_dostawy/\" target=\"_blank\">here</a>.

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
api_instance = allegro_api.DeliveryApi(allegro_api.ApiClient(configuration))
shipping_rates_set = allegro_api.ShippingRatesSet() # ShippingRatesSet | Shipping rates set

try:
    # Create a new shipping rates set
    api_response = api_instance.create_shipping_rates_set_using_post(shipping_rates_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveryApi->create_shipping_rates_set_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_rates_set** | [**ShippingRatesSet**](ShippingRatesSet.md)| Shipping rates set | 

### Return type

[**ShippingRatesSet**](ShippingRatesSet.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_delivery_methods_using_get**
> InlineResponse2001 get_list_of_delivery_methods_using_get()

Get the list of available delivery methods

Use this resource to get a list of available delivery methods. More information about this resource you can find <a href=\"../news/2018-08-14-cenniki_dostawy/\" target=\"_blank\">here</a>.

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
api_instance = allegro_api.DeliveryApi(allegro_api.ApiClient(configuration))

try:
    # Get the list of available delivery methods
    api_response = api_instance.get_list_of_delivery_methods_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveryApi->get_list_of_delivery_methods_using_get: %s\n" % e)
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
api_instance = allegro_api.DeliveryApi(allegro_api.ApiClient(configuration))

try:
    # Get the list of available delivery methods
    api_response = api_instance.get_list_of_delivery_methods_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveryApi->get_list_of_delivery_methods_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[bearer-token-for-application](../README.md#bearer-token-for-application), [bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_shipping_ratest_using_get**
> InlineResponse200 get_list_of_shipping_ratest_using_get(seller_id)

Get the user's shipping rates

Use this resource to get a list of seller's shipping rates. More information about this resource you can find <a href=\"../news/2018-08-14-cenniki_dostawy/\" target=\"_blank\">here</a>.

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
api_instance = allegro_api.DeliveryApi(allegro_api.ApiClient(configuration))
seller_id = 'seller_id_example' # str | id of shipping rates owner

try:
    # Get the user's shipping rates
    api_response = api_instance.get_list_of_shipping_ratest_using_get(seller_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveryApi->get_list_of_shipping_ratest_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| id of shipping rates owner | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipping_rates_set_using_get**
> ShippingRatesSet get_shipping_rates_set_using_get(id)

Get the details of a shipping rates set

Use this resource to get details of the given shipping rates set. More information about this resource you can find <a href=\"../news/2018-08-14-cenniki_dostawy\" target=\"_blank\">here</a>.

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
api_instance = allegro_api.DeliveryApi(allegro_api.ApiClient(configuration))
id = 'id_example' # str | id of shipping rates set

try:
    # Get the details of a shipping rates set
    api_response = api_instance.get_shipping_rates_set_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveryApi->get_shipping_rates_set_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of shipping rates set | 

### Return type

[**ShippingRatesSet**](ShippingRatesSet.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_shipiing_rates_set_using_put**
> ShippingRatesSet modify_shipiing_rates_set_using_put(id, shipping_rates_set)

Edit a user's shipping rates set

Use this resource to edit a new seller's shipping rates set. More information about this resource you can find <a href=\"../news/2018-08-14-cenniki_dostawy/\" target=\"_blank\">here</a>.

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
api_instance = allegro_api.DeliveryApi(allegro_api.ApiClient(configuration))
id = 'id_example' # str | id of shipping rates set
shipping_rates_set = allegro_api.ShippingRatesSet() # ShippingRatesSet | Shipping rates set

try:
    # Edit a user's shipping rates set
    api_response = api_instance.modify_shipiing_rates_set_using_put(id, shipping_rates_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveryApi->modify_shipiing_rates_set_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of shipping rates set | 
 **shipping_rates_set** | [**ShippingRatesSet**](ShippingRatesSet.md)| Shipping rates set | 

### Return type

[**ShippingRatesSet**](ShippingRatesSet.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

