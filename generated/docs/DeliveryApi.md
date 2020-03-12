# allegro_api.DeliveryApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shipping_rates_set_using_post**](DeliveryApi.md#create_shipping_rates_set_using_post) | **POST** /sale/shipping-rates | Create a new shipping rates set
[**get_list_of_delivery_methods_using_get**](DeliveryApi.md#get_list_of_delivery_methods_using_get) | **GET** /sale/delivery-methods | Get the list of delivery methods
[**get_list_of_shipping_ratest_using_get**](DeliveryApi.md#get_list_of_shipping_ratest_using_get) | **GET** /sale/shipping-rates | Get the user&#39;s shipping rates
[**get_offer_shipping_rates_get**](DeliveryApi.md#get_offer_shipping_rates_get) | **GET** /sale/offers/{offerId}/shipping-rates | [BETA] Get shipping rates assigned to an offer
[**get_sale_delivery_settings**](DeliveryApi.md#get_sale_delivery_settings) | **GET** /sale/delivery-settings | Get the user&#39;s delivery settings
[**get_shipping_rates_set_using_get**](DeliveryApi.md#get_shipping_rates_set_using_get) | **GET** /sale/shipping-rates/{id} | Get the details of a shipping rates set
[**modify_shipping_rates_set_using_put**](DeliveryApi.md#modify_shipping_rates_set_using_put) | **PUT** /sale/shipping-rates/{id} | Edit a user&#39;s shipping rates set
[**put_sale_delivery_settings**](DeliveryApi.md#put_sale_delivery_settings) | **PUT** /sale/delivery-settings | Modify the user&#39;s delivery settings


# **create_shipping_rates_set_using_post**
> ShippingRatesSet create_shipping_rates_set_using_post(shipping_rates_set)

Create a new shipping rates set

Use this resource to create a new seller's shipping rates set. <a href=\"../../sale/#shipping-rates\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.DeliveryApi(api_client)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**401** | Authentication required |  -  |
**422** | The user has reached the limit of shipping rates sets. Information on the limit will be returned in the error message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_delivery_methods_using_get**
> InlineResponse2001 get_list_of_delivery_methods_using_get()

Get the list of delivery methods

Use this resource to get a list of all delivery methods currently available on the platform, as well as those that have already been discontinued. <a href=\"../../sale/#shipping-rates\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.DeliveryApi(api_client)
    
    try:
        # Get the list of delivery methods
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
    api_instance = allegro_api.DeliveryApi(api_client)
    
    try:
        # Get the list of delivery methods
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication required. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_shipping_ratest_using_get**
> InlineResponse200 get_list_of_shipping_ratest_using_get(seller_id)

Get the user's shipping rates

Use this resource to get a list of seller's shipping rates. <a href=\"../../sale/#shipping-rates\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.DeliveryApi(api_client)
    seller_id = 'seller_id_example' # str | Shipping rates owner identifier.

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
 **seller_id** | **str**| Shipping rates owner identifier. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication required |  -  |
**403** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_shipping_rates_get**
> OfferShippingRates get_offer_shipping_rates_get(offer_id)

[BETA] Get shipping rates assigned to an offer

Use this resource to get the delivery methods and costs defined in the offer when there is no seller's shipping rates set attached to offer.

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
    api_instance = allegro_api.DeliveryApi(api_client)
    offer_id = 'offer_id_example' # str | Offer identifier.

    try:
        # [BETA] Get shipping rates assigned to an offer
        api_response = api_instance.get_offer_shipping_rates_get(offer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeliveryApi->get_offer_shipping_rates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Offer identifier. | 

### Return type

[**OfferShippingRates**](OfferShippingRates.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned assigned shipping rates set |  -  |
**401** | Unauthorized action |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sale_delivery_settings**
> DeliverySettingsDto get_sale_delivery_settings()

Get the user's delivery settings

Use this resource to get the delivery settings declared by the seller.

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
    api_instance = allegro_api.DeliveryApi(api_client)
    
    try:
        # Get the user's delivery settings
        api_response = api_instance.get_sale_delivery_settings()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeliveryApi->get_sale_delivery_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeliverySettingsDto**](DeliverySettingsDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication required. |  -  |
**403** | Forbidden - not allowed to access user data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipping_rates_set_using_get**
> ShippingRatesSet get_shipping_rates_set_using_get(id)

Get the details of a shipping rates set

Use this resource to get details of the given shipping rates set. <a href=\"../../sale/#shipping-rates\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.DeliveryApi(api_client)
    id = 'id_example' # str | Shipping rates set identifier.

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
 **id** | **str**| Shipping rates set identifier. | 

### Return type

[**ShippingRatesSet**](ShippingRatesSet.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication required |  -  |
**403** | Unauthorized |  -  |
**404** | Shipping rates set with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_shipping_rates_set_using_put**
> ShippingRatesSet modify_shipping_rates_set_using_put(id, shipping_rates_set)

Edit a user's shipping rates set

Use this resource to edit a new seller's shipping rates set. <a href=\"../../sale/#shipping-rates\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.DeliveryApi(api_client)
    id = 'id_example' # str | Shipping rates set identifier.
shipping_rates_set = allegro_api.ShippingRatesSet() # ShippingRatesSet | Shipping rates set

    try:
        # Edit a user's shipping rates set
        api_response = api_instance.modify_shipping_rates_set_using_put(id, shipping_rates_set)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeliveryApi->modify_shipping_rates_set_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Shipping rates set identifier. | 
 **shipping_rates_set** | [**ShippingRatesSet**](ShippingRatesSet.md)| Shipping rates set | 

### Return type

[**ShippingRatesSet**](ShippingRatesSet.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication required |  -  |
**404** | Set with given id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sale_delivery_settings**
> DeliverySettingsDto put_sale_delivery_settings()

Modify the user's delivery settings

Use this resource to modify the delivery settings declared by the seller.

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
    api_instance = allegro_api.DeliveryApi(api_client)
    
    try:
        # Modify the user's delivery settings
        api_response = api_instance.put_sale_delivery_settings()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeliveryApi->put_sale_delivery_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeliverySettingsDto**](DeliverySettingsDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication required. |  -  |
**403** | Forbidden - not allowed to access user data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

