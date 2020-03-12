# allegro_api.OrderManagementApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order_shipments_using_post**](OrderManagementApi.md#create_order_shipments_using_post) | **POST** /order/checkout-forms/{id}/shipments | Add a parcel tracking number
[**find_mapping**](OrderManagementApi.md#find_mapping) | **GET** /order/line-item-id-mappings | Get mapping for line item id
[**get_list_of_orders_using_get**](OrderManagementApi.md#get_list_of_orders_using_get) | **GET** /order/checkout-forms | Get the user&#39;s orders
[**get_order_events_statistics_using_get**](OrderManagementApi.md#get_order_events_statistics_using_get) | **GET** /order/event-stats | Get order events statistics
[**get_order_events_using_get**](OrderManagementApi.md#get_order_events_using_get) | **GET** /order/events | Get order events
[**get_order_shipments_using_get**](OrderManagementApi.md#get_order_shipments_using_get) | **GET** /order/checkout-forms/{id}/shipments | Get a list of parcel tracking numbers
[**get_orders_details_using_get**](OrderManagementApi.md#get_orders_details_using_get) | **GET** /order/checkout-forms/{id} | Get an order&#39;s details
[**set_order_fulfillment_using_put**](OrderManagementApi.md#set_order_fulfillment_using_put) | **PUT** /order/checkout-forms/{id}/fulfillment | Set seller order status


# **create_order_shipments_using_post**
> CheckoutFormAddWaybillCreated create_order_shipments_using_post(id, checkout_form_add_waybill_request)

Add a parcel tracking number

Add a parcel tracking number (shipment) to given order line items.

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
    api_instance = allegro_api.OrderManagementApi(api_client)
    id = 'id_example' # str | Order identifier.
checkout_form_add_waybill_request = allegro_api.CheckoutFormAddWaybillRequest() # CheckoutFormAddWaybillRequest | request

    try:
        # Add a parcel tracking number
        api_response = api_instance.create_order_shipments_using_post(id, checkout_form_add_waybill_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->create_order_shipments_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Order identifier. | 
 **checkout_form_add_waybill_request** | [**CheckoutFormAddWaybillRequest**](CheckoutFormAddWaybillRequest.md)| request | 

### Return type

[**CheckoutFormAddWaybillCreated**](CheckoutFormAddWaybillCreated.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request is OK and the parcel tracking number will be assigned to the order |  -  |
**400** | Missing required field or invalid value in the request (e.g. unknown carrier id, carrier name too long) |  -  |
**401** | Authentication failed, e.g. token is expired |  -  |
**404** | Order not found or doesn’t belong to the seller |  -  |
**422** | Some of the provided data is invalid, e.g. line item doesn’t belong to the order |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_mapping**
> LineItemIdMappings find_mapping(line_item_id=line_item_id, deal_id=deal_id)

Get mapping for line item id

Allows mapping identifiers from dealId to lineItemId and vice-versa. One of defined query parameters has to be provided.

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
    api_instance = allegro_api.OrderManagementApi(api_client)
    line_item_id = 'line_item_id_example' # str | Line item identifier. (optional)
deal_id = 'deal_id_example' # str | Deal identifier. (optional)

    try:
        # Get mapping for line item id
        api_response = api_instance.find_mapping(line_item_id=line_item_id, deal_id=deal_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->find_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_item_id** | [**str**](.md)| Line item identifier. | [optional] 
 **deal_id** | **str**| Deal identifier. | [optional] 

### Return type

[**LineItemIdMappings**](LineItemIdMappings.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Missing required parameter. Provide lineItemId or dealId. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_orders_using_get**
> CheckoutForms get_list_of_orders_using_get(offset=offset, limit=limit, status=status, fulfillment_status=fulfillment_status, fulfillment_shipment_summary_line_items_sent=fulfillment_shipment_summary_line_items_sent, line_items_bought_at_lte=line_items_bought_at_lte, line_items_bought_at_gte=line_items_bought_at_gte, payment_id=payment_id, surcharges_id=surcharges_id, delivery_method_id=delivery_method_id, buyer_login=buyer_login, updated_at_lte=updated_at_lte, updated_at_gte=updated_at_gte, sort=sort)

Get the user's orders

Use this resource to get an order list. <a href=\"/orders/#03\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.OrderManagementApi(api_client)
    offset = 0 # int | Index of first returned checkout-form from all search results. (optional) (default to 0)
limit = 100 # int | Maximum number of checkout-forms in response. (optional) (default to 100)
status = 'status_example' # str | Specify status value that checkout-forms must have to be included in the output. Allowed values are:   * `BOUGHT`: purchase without checkout form filled in.   * `FILLED_IN`: checkout form filled in but payment is not completed yet so data could still change.   * `READY_FOR_PROCESSING`: payment completed. Purchase is ready for processing. (optional)
fulfillment_status = 'fulfillment_status_example' # str | Specify seller status value that checkout-forms must have to be included in the output. Allowed values are:   * `NEW`   * `PROCESSING`   * `READY_FOR_SHIPMENT`   * `SENT`   * `CANCELLED`. (optional)
fulfillment_shipment_summary_line_items_sent = 'fulfillment_shipment_summary_line_items_sent_example' # str | Specify filter for line items sending status. Allowed values are:   * `NONE`: none of line items have tracking number specified   * `SOME`: some of line items have tracking number specified   * `ALL`: all of line items have tracking number specified. (optional)
line_items_bought_at_lte = '2013-10-20T19:20:30+01:00' # datetime | Latest line item bought date. The upper bound of date time range from which checkout forms will be taken. (optional)
line_items_bought_at_gte = '2013-10-20T19:20:30+01:00' # datetime | Latest line item bought date. The lower bound of date time range from which checkout forms will be taken. (optional)
payment_id = 'payment_id_example' # str | Find checkout-forms having specified payment id. (optional)
surcharges_id = 'surcharges_id_example' # str | Find checkout-forms having specified surcharge id. (optional)
delivery_method_id = 'delivery_method_id_example' # str | Find checkout-forms having specified delivery method id. (optional)
buyer_login = 'buyer_login_example' # str | Find checkout-forms having specified buyer login. (optional)
updated_at_lte = '2013-10-20T19:20:30+01:00' # datetime | Checkout form last modification date. The upper bound of date time range from which checkout forms will be taken. (optional)
updated_at_gte = '2013-10-20T19:20:30+01:00' # datetime | Checkout form last modification date. The lower bound of date time range from which checkout forms will be taken. (optional)
sort = 'sort_example' # str | The results' sorting order. No prefix in the value means ascending order. `-` prefix means descending order. If you don't provide the sort parameter, the list is sorted by line item boughtAt date, descending. (optional)

    try:
        # Get the user's orders
        api_response = api_instance.get_list_of_orders_using_get(offset=offset, limit=limit, status=status, fulfillment_status=fulfillment_status, fulfillment_shipment_summary_line_items_sent=fulfillment_shipment_summary_line_items_sent, line_items_bought_at_lte=line_items_bought_at_lte, line_items_bought_at_gte=line_items_bought_at_gte, payment_id=payment_id, surcharges_id=surcharges_id, delivery_method_id=delivery_method_id, buyer_login=buyer_login, updated_at_lte=updated_at_lte, updated_at_gte=updated_at_gte, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->get_list_of_orders_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Index of first returned checkout-form from all search results. | [optional] [default to 0]
 **limit** | **int**| Maximum number of checkout-forms in response. | [optional] [default to 100]
 **status** | **str**| Specify status value that checkout-forms must have to be included in the output. Allowed values are:   * &#x60;BOUGHT&#x60;: purchase without checkout form filled in.   * &#x60;FILLED_IN&#x60;: checkout form filled in but payment is not completed yet so data could still change.   * &#x60;READY_FOR_PROCESSING&#x60;: payment completed. Purchase is ready for processing. | [optional] 
 **fulfillment_status** | **str**| Specify seller status value that checkout-forms must have to be included in the output. Allowed values are:   * &#x60;NEW&#x60;   * &#x60;PROCESSING&#x60;   * &#x60;READY_FOR_SHIPMENT&#x60;   * &#x60;SENT&#x60;   * &#x60;CANCELLED&#x60;. | [optional] 
 **fulfillment_shipment_summary_line_items_sent** | **str**| Specify filter for line items sending status. Allowed values are:   * &#x60;NONE&#x60;: none of line items have tracking number specified   * &#x60;SOME&#x60;: some of line items have tracking number specified   * &#x60;ALL&#x60;: all of line items have tracking number specified. | [optional] 
 **line_items_bought_at_lte** | **datetime**| Latest line item bought date. The upper bound of date time range from which checkout forms will be taken. | [optional] 
 **line_items_bought_at_gte** | **datetime**| Latest line item bought date. The lower bound of date time range from which checkout forms will be taken. | [optional] 
 **payment_id** | **str**| Find checkout-forms having specified payment id. | [optional] 
 **surcharges_id** | **str**| Find checkout-forms having specified surcharge id. | [optional] 
 **delivery_method_id** | **str**| Find checkout-forms having specified delivery method id. | [optional] 
 **buyer_login** | **str**| Find checkout-forms having specified buyer login. | [optional] 
 **updated_at_lte** | **datetime**| Checkout form last modification date. The upper bound of date time range from which checkout forms will be taken. | [optional] 
 **updated_at_gte** | **datetime**| Checkout form last modification date. The lower bound of date time range from which checkout forms will be taken. | [optional] 
 **sort** | **str**| The results&#39; sorting order. No prefix in the value means ascending order. &#x60;-&#x60; prefix means descending order. If you don&#39;t provide the sort parameter, the list is sorted by line item boughtAt date, descending. | [optional] 

### Return type

[**CheckoutForms**](CheckoutForms.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request - Returned when request parameters contains illegal values.  |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity - Returned when limit or offset value is outside an acceptable range  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_events_statistics_using_get**
> OrderEventStats get_order_events_statistics_using_get()

Get order events statistics

Use this resource to returns object that contains event id and occurrence date of the latest event. It gives you current starting point for reading events. <a href=\"/orders/#02\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.OrderManagementApi(api_client)
    
    try:
        # Get order events statistics
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
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_events_using_get**
> OrderEventsList get_order_events_using_get(_from=_from, type=type, limit=limit)

Get order events

Use this resource to return events that allow you to monitor actions which clients perform, i.e. making a purchase, filling in the checkout form (FOD), finishing payment process, making a surcharge. <a href=\"/orders/#02\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.OrderManagementApi(api_client)
    _from = '_from_example' # str | You can use the event ID to retrieve subsequent chunks of events. (optional)
type = ['type_example'] # list[str] | Specify array of event types for filtering. Allowed values are:   * `BOUGHT`: purchase without checkout form filled in   * `FILLED_IN`: checkout form filled in but payment is not completed yet so data could still change   * `READY_FOR_PROCESSING`: payment completed. Purchase is ready for processing   * `FULFILLMENT_STATUS_CHANGED`: fulfillment status changed. (optional)
limit = 100 # int | The maximum number of events returned in the response. (optional) (default to 100)

    try:
        # Get order events
        api_response = api_instance.get_order_events_using_get(_from=_from, type=type, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->get_order_events_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| You can use the event ID to retrieve subsequent chunks of events. | [optional] 
 **type** | [**list[str]**](str.md)| Specify array of event types for filtering. Allowed values are:   * &#x60;BOUGHT&#x60;: purchase without checkout form filled in   * &#x60;FILLED_IN&#x60;: checkout form filled in but payment is not completed yet so data could still change   * &#x60;READY_FOR_PROCESSING&#x60;: payment completed. Purchase is ready for processing   * &#x60;FULFILLMENT_STATUS_CHANGED&#x60;: fulfillment status changed. | [optional] 
 **limit** | **int**| The maximum number of events returned in the response. | [optional] [default to 100]

### Return type

[**OrderEventsList**](OrderEventsList.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_shipments_using_get**
> CheckoutFormOrderWaybillResponse get_order_shipments_using_get(id)

Get a list of parcel tracking numbers

Get a list of parcel tracking numbers currently assigned to the order. Orders can be retrieved using REST API resource GET /order/checkout-forms. Please note that the shipment list may contain parcel tracking numbers added through other channels such as Moje Allegro or by the carrier that delivers the parcel.

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
    api_instance = allegro_api.OrderManagementApi(api_client)
    id = 'id_example' # str | Order identifier.

    try:
        # Get a list of parcel tracking numbers
        api_response = api_instance.get_order_shipments_using_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->get_order_shipments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Order identifier. | 

### Return type

[**CheckoutFormOrderWaybillResponse**](CheckoutFormOrderWaybillResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of parcel tracking numbers (shipments) |  -  |
**401** | Authentication failed, e.g. token is expired |  -  |
**404** | Order not found or doesn’t belong to the seller |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_details_using_get**
> CheckoutForm get_orders_details_using_get(id)

Get an order's details

Use this resource to get an order details. <a href=\"/orders/#04\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.OrderManagementApi(api_client)
    id = '29738e61-7f6a-11e8-ac45-09db60ede9d6' # str | Checkout form identifier.

    try:
        # Get an order's details
        api_response = api_instance.get_orders_details_using_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->get_orders_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Checkout form identifier. | 

### Return type

[**CheckoutForm**](CheckoutForm.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_order_fulfillment_using_put**
> set_order_fulfillment_using_put(id, checkout_form_fulfillment)

Set seller order status

Use to set seller order status.

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
    api_instance = allegro_api.OrderManagementApi(api_client)
    id = 'id_example' # str | Order identifier.
checkout_form_fulfillment = allegro_api.CheckoutFormFulfillment() # CheckoutFormFulfillment | request

    try:
        # Set seller order status
        api_instance.set_order_fulfillment_using_put(id, checkout_form_fulfillment)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->set_order_fulfillment_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Order identifier. | 
 **checkout_form_fulfillment** | [**CheckoutFormFulfillment**](CheckoutFormFulfillment.md)| request | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Fulfillment set successfully |  -  |
**401** | Authentication failed, e.g. token is expired |  -  |
**404** | Order not found or doesn’t belong to the seller |  -  |
**422** | Some of the provided data is invalid, e.g. unrecognized status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

