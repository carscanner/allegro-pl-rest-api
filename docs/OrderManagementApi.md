# openapi_client.OrderManagementApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order_shipments_using_post**](OrderManagementApi.md#create_order_shipments_using_post) | **POST** /order/checkout-forms/{id}/shipments | [BETA] Add a parcel tracking number
[**find_mapping**](OrderManagementApi.md#find_mapping) | **GET** /order/line-item-id-mappings | [BETA] Get mapping for line item id
[**get_list_of_orders_using_get**](OrderManagementApi.md#get_list_of_orders_using_get) | **GET** /order/checkout-forms | [BETA] Get the user&#39;s orders
[**get_order_events_statistics_using_get**](OrderManagementApi.md#get_order_events_statistics_using_get) | **GET** /order/event-stats | [BETA] Get order events statistics
[**get_order_events_using_get**](OrderManagementApi.md#get_order_events_using_get) | **GET** /order/events | [BETA] Get order events
[**get_order_shipments_using_get**](OrderManagementApi.md#get_order_shipments_using_get) | **GET** /order/checkout-forms/{id}/shipments | [BETA] Get a list of parcel tracking numbers
[**get_orders_details_using_get**](OrderManagementApi.md#get_orders_details_using_get) | **GET** /order/checkout-forms/{id} | [BETA] Get an order&#39;s details


# **create_order_shipments_using_post**
> CheckoutFormAddWaybillCreated create_order_shipments_using_post(id, checkout_form_add_waybill_request)

[BETA] Add a parcel tracking number

Add a parcel tracking number (shipment) to given order line items.

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
api_instance = openapi_client.OrderManagementApi(openapi_client.ApiClient(configuration))
id = 'id_example' # str | Order identifier
checkout_form_add_waybill_request = openapi_client.CheckoutFormAddWaybillRequest() # CheckoutFormAddWaybillRequest | request

try:
    # [BETA] Add a parcel tracking number
    api_response = api_instance.create_order_shipments_using_post(id, checkout_form_add_waybill_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderManagementApi->create_order_shipments_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Order identifier | 
 **checkout_form_add_waybill_request** | [**CheckoutFormAddWaybillRequest**](CheckoutFormAddWaybillRequest.md)| request | 

### Return type

[**CheckoutFormAddWaybillCreated**](CheckoutFormAddWaybillCreated.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.beta.v1+json
 - **Accept**: application/vnd.allegro.beta.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_mapping**
> LineItemIdMappings find_mapping(line_item_id=line_item_id, deal_id=deal_id)

[BETA] Get mapping for line item id

[BETA] Allows mapping identifiers from dealId to lineItemId and vice-versa. One of defined query parameters has to be provided.

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
api_instance = openapi_client.OrderManagementApi(openapi_client.ApiClient(configuration))
line_item_id = 'line_item_id_example' # str | line item id (optional)
deal_id = 'deal_id_example' # str | dealId (optional)

try:
    # [BETA] Get mapping for line item id
    api_response = api_instance.find_mapping(line_item_id=line_item_id, deal_id=deal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderManagementApi->find_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | [**str**](.md)| line item id | [optional] 
 **deal_id** | **str**| dealId | [optional] 

### Return type

[**LineItemIdMappings**](LineItemIdMappings.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_orders_using_get**
> CheckoutForms get_list_of_orders_using_get(offset=offset, limit=limit, status=status, line_items_bought_at_lte=line_items_bought_at_lte, line_items_bought_at_gte=line_items_bought_at_gte)

[BETA] Get the user's orders

[BETA] Use this resource to get an order list. More information about this resource you can find <a href=\"/orders/#03\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.OrderManagementApi(openapi_client.ApiClient(configuration))
offset = 56 # int | Index of first returned checkout-form from all search results. (optional)
limit = 56 # int | Maximum number of checkout-forms in response (acceptable values: from 0 to 100, default is 100). (optional)
status = 'status_example' # str | Specify status value that checkout-forms must have to be included in the output. Allowed values are:   * `BOUGHT`: purchase without checkout form filled in   * `FILLED_IN`: checkout form filled in but payment is not completed yet so data could still change   * `READY_FOR_PROCESSING`: payment completed. Purchase is ready for processing.   * `ALL`: return all checkout-forms  (optional)
line_items_bought_at_lte = '2013-10-20T19:20:30+01:00' # datetime | The upper bound of date time range from which checkout forms will be taken. (optional)
line_items_bought_at_gte = '2013-10-20T19:20:30+01:00' # datetime | The lower bound of date time range from which checkout forms will be taken. (optional)

try:
    # [BETA] Get the user's orders
    api_response = api_instance.get_list_of_orders_using_get(offset=offset, limit=limit, status=status, line_items_bought_at_lte=line_items_bought_at_lte, line_items_bought_at_gte=line_items_bought_at_gte)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderManagementApi->get_list_of_orders_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Index of first returned checkout-form from all search results. | [optional] 
 **limit** | **int**| Maximum number of checkout-forms in response (acceptable values: from 0 to 100, default is 100). | [optional] 
 **status** | **str**| Specify status value that checkout-forms must have to be included in the output. Allowed values are:   * &#x60;BOUGHT&#x60;: purchase without checkout form filled in   * &#x60;FILLED_IN&#x60;: checkout form filled in but payment is not completed yet so data could still change   * &#x60;READY_FOR_PROCESSING&#x60;: payment completed. Purchase is ready for processing.   * &#x60;ALL&#x60;: return all checkout-forms  | [optional] 
 **line_items_bought_at_lte** | **datetime**| The upper bound of date time range from which checkout forms will be taken. | [optional] 
 **line_items_bought_at_gte** | **datetime**| The lower bound of date time range from which checkout forms will be taken. | [optional] 

### Return type

[**CheckoutForms**](CheckoutForms.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_events_statistics_using_get**
> OrderEventStats get_order_events_statistics_using_get()

[BETA] Get order events statistics

[BETA] Use this resource to returns object that contains event id and occurrence date of the latest event. It gives you current starting point for reading events. More information about this resource you can find <a href=\"/orders/#02\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.OrderManagementApi(openapi_client.ApiClient(configuration))

try:
    # [BETA] Get order events statistics
    api_response = api_instance.get_order_events_statistics_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderManagementApi->get_order_events_statistics_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrderEventStats**](OrderEventStats.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_events_using_get**
> OrderEventsList get_order_events_using_get(_from=_from, type=type, limit=limit)

[BETA] Get order events

[BETA] Use this resource to return events that allow you to monitor actions which clients perform, i.e. making a purchase, filling in the checkout form (FOD), finishing payment process, making a surcharge. More information about this resource you can find <a href=\"/orders/#02\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.OrderManagementApi(openapi_client.ApiClient(configuration))
_from = '_from_example' # str | You can use the event ID to retrieve subsequent chunks of events (optional)
type = ['type_example'] # list[str] | Specify array of event types for filtering. Allowed values are:   * `BOUGHT`: purchase without checkout form filled in   * `FILLED_IN`: checkout form filled in but payment is not completed yet so data could still change   * `READY_FOR_PROCESSING`: payment completed. Purchase is ready for processing. (optional)
limit = 100 # int | Limit in the range of 1-1000 (optional) (default to 100)

try:
    # [BETA] Get order events
    api_response = api_instance.get_order_events_using_get(_from=_from, type=type, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderManagementApi->get_order_events_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| You can use the event ID to retrieve subsequent chunks of events | [optional] 
 **type** | [**list[str]**](str.md)| Specify array of event types for filtering. Allowed values are:   * &#x60;BOUGHT&#x60;: purchase without checkout form filled in   * &#x60;FILLED_IN&#x60;: checkout form filled in but payment is not completed yet so data could still change   * &#x60;READY_FOR_PROCESSING&#x60;: payment completed. Purchase is ready for processing. | [optional] 
 **limit** | **int**| Limit in the range of 1-1000 | [optional] [default to 100]

### Return type

[**OrderEventsList**](OrderEventsList.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_shipments_using_get**
> CheckoutFormOrderWaybillResponse get_order_shipments_using_get(id)

[BETA] Get a list of parcel tracking numbers

Get a list of parcel tracking numbers currently assigned to the order. Orders can be retrieved using REST API resource GET /order/checkout-forms. Please note that the shipment list may contain parcel tracking numbers added through other channels such as Moje Allegro or by the carrier that delivers the parcel.

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
api_instance = openapi_client.OrderManagementApi(openapi_client.ApiClient(configuration))
id = 'id_example' # str | Order identifier

try:
    # [BETA] Get a list of parcel tracking numbers
    api_response = api_instance.get_order_shipments_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderManagementApi->get_order_shipments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Order identifier | 

### Return type

[**CheckoutFormOrderWaybillResponse**](CheckoutFormOrderWaybillResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_details_using_get**
> CheckoutForm get_orders_details_using_get(id)

[BETA] Get an order's details

[BETA] Use this resource to get an order details. More information about this resource you can find <a href=\"/orders/#04\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.OrderManagementApi(openapi_client.ApiClient(configuration))
id = 29738e61-7f6a-11e8-ac45-09db60ede9d6 # str | Checkout Form id

try:
    # [BETA] Get an order's details
    api_response = api_instance.get_orders_details_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderManagementApi->get_orders_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Checkout Form id | 

### Return type

[**CheckoutForm**](CheckoutForm.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

