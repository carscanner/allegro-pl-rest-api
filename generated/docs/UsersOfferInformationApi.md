# allegro_api.UsersOfferInformationApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_offer_events**](UsersOfferInformationApi.md#get_offer_events) | **GET** /sale/offer-events | Get events about the seller&#39;s offers
[**get_offer_using_get**](UsersOfferInformationApi.md#get_offer_using_get) | **GET** /sale/offers/{offerId} | Get all fields of the particular offer
[**search_offers_using_get**](UsersOfferInformationApi.md#search_offers_using_get) | **GET** /sale/offers | Get seller&#39;s offers


# **get_offer_events**
> SellerOfferEventsResponse get_offer_events(_from=_from, limit=limit, type=type)

Get events about the seller's offers

Use this endpoint to get events concerning changes in the authorized seller's offers. At present we support the following events:   - OFFER_ACTIVATED - offer is visible on site and available for purchase, occurs when offer status changes from ACTIVATING to ACTIVE.   - OFFER_CHANGED - occurs when offer's fields has been changed e.g. description or photos.   - OFFER_ENDED - offer is no longer available for purchase, occurs when offer status changes from ACTIVE to ENDED.   - OFFER_STOCK_CHANGED - stock in an offer was changed either via purchase or by seller.   - OFFER_PRICE_CHANGED - occurs when price in an offer was changed.   - OFFER_ARCHIVED - offer is no longer available on listing and has been archived.   - OFFER_BID_PLACED - bid was placed on the offer   - OFFER_BID_CANCELED - bid for offer was canceled  Returned events may occur by actions made via browser or API. The resource allows you to get events concerning active offers and offers scheduled for activation (status ACTIVE and ACTIVATING). Returned events do not concern offers in INACTIVE and ENDED status (the exception is OFFER_ARCHIVED event). Please note that one change may result in more than one event.

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
    api_instance = allegro_api.UsersOfferInformationApi(api_client)
    _from = 'MTEzMjQzODU3NA' # str | The ID of the last seen event. Events that occured after the given event will be returned. (optional)
limit = 100 # int | The number of events that will be returned in the response. (optional) (default to 100)
type = ['type_example'] # list[str] | The types of events that will be returned in the response. All types of events are returned by default. (optional)

    try:
        # Get events about the seller's offers
        api_response = api_instance.get_offer_events(_from=_from, limit=limit, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersOfferInformationApi->get_offer_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| The ID of the last seen event. Events that occured after the given event will be returned. | [optional] 
 **limit** | **int**| The number of events that will be returned in the response. | [optional] [default to 100]
 **type** | [**list[str]**](str.md)| The types of events that will be returned in the response. All types of events are returned by default. | [optional] 

### Return type

[**SellerOfferEventsResponse**](SellerOfferEventsResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of offer events returned successfully. |  -  |
**400** | Invalid parameters supplied in the request. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_using_get**
> Offer get_offer_using_get(offer_id)

Get all fields of the particular offer

Use this resource to retrieve all fields of the particular offer. <a href=\"../../sale/#similar-offer\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.UsersOfferInformationApi(api_client)
    offer_id = 'offer_id_example' # str | Offer identifier.

    try:
        # Get all fields of the particular offer
        api_response = api_instance.get_offer_using_get(offer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersOfferInformationApi->get_offer_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Offer identifier. | 

### Return type

[**Offer**](Offer.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Offer returned successfully |  -  |
**400** | Syntactically incorrect request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_offers_using_get**
> OffersSearchResultDto search_offers_using_get(offer_id=offer_id, name=name, selling_mode_price_amount_gte=selling_mode_price_amount_gte, selling_mode_price_amount_lte=selling_mode_price_amount_lte, publication_status=publication_status, selling_mode_format=selling_mode_format, external_id=external_id, delivery_shipping_rates_id=delivery_shipping_rates_id, delivery_shipping_rates_id_empty=delivery_shipping_rates_id_empty, sort=sort, limit=limit, offset=offset)

Get seller's offers

Use this resource to get the list of the seller's offers. You can use different query parameters to filter the list.

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
    api_instance = allegro_api.UsersOfferInformationApi(api_client)
    offer_id = 'offer_id_example' # str | Offer ID. (optional)
name = 'name_example' # str | The text to search in the offer title. (optional)
selling_mode_price_amount_gte = 9.99 # float | The lower threshold of price. (optional)
selling_mode_price_amount_lte = 125.99 # float | The upper threshold of price. (optional)
publication_status = ['publication_status_example'] # list[str] | The publication status of the offer. Passing more than one value will search for offers with any of the given statuses. By default all statuses are included. Example: `publication.status=INACTIVE&publication.status=ACTIVE` - returns offers with status `INACTIVE` or `ACTIVE`. (optional)
selling_mode_format = ['selling_mode_format_example'] # list[str] | The offer's selling format. Passing more than one value will search for offers with any of the given formats. By default all formats are included. Example: `sellingMode.format=BUY_NOW&sellingMode.format=ADVERTISEMENT` - returns offers with with format `BUY_NOW` or `ADVERTISEMENT`. (optional)
external_id = ['external_id_example'] # list[str] | The ID from the client's external system. Passing more than one value will search for offers with any of the given IDs. By default no ID is included. Example: `external.id=1233&external.id=1234` - returns offers with ID `1233` or `1234`. Single ID length shouldn't exceed 100 characters. (optional)
delivery_shipping_rates_id = 'delivery_shipping_rates_id_example' # str | The ID of shipping rates. Returns offers with given shipping rates ID. (optional)
delivery_shipping_rates_id_empty = True # bool | Allow to filter offers by existence of shipping rates ID. (optional)
sort = 'sort_example' # str | The results' sorting order. No prefix in the value means ascending order. `-` prefix means descending order. If you don't provide the sort parameter, the list is sorted by offer creation time, descending. (optional)
limit = 20 # int | The maximum number of offers returned in the response. (optional) (default to 20)
offset = 56 # int | Index of the first returned offer from all search results. (optional)

    try:
        # Get seller's offers
        api_response = api_instance.search_offers_using_get(offer_id=offer_id, name=name, selling_mode_price_amount_gte=selling_mode_price_amount_gte, selling_mode_price_amount_lte=selling_mode_price_amount_lte, publication_status=publication_status, selling_mode_format=selling_mode_format, external_id=external_id, delivery_shipping_rates_id=delivery_shipping_rates_id, delivery_shipping_rates_id_empty=delivery_shipping_rates_id_empty, sort=sort, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersOfferInformationApi->search_offers_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Offer ID. | [optional] 
 **name** | **str**| The text to search in the offer title. | [optional] 
 **selling_mode_price_amount_gte** | **float**| The lower threshold of price. | [optional] 
 **selling_mode_price_amount_lte** | **float**| The upper threshold of price. | [optional] 
 **publication_status** | [**list[str]**](str.md)| The publication status of the offer. Passing more than one value will search for offers with any of the given statuses. By default all statuses are included. Example: &#x60;publication.status&#x3D;INACTIVE&amp;publication.status&#x3D;ACTIVE&#x60; - returns offers with status &#x60;INACTIVE&#x60; or &#x60;ACTIVE&#x60;. | [optional] 
 **selling_mode_format** | [**list[str]**](str.md)| The offer&#39;s selling format. Passing more than one value will search for offers with any of the given formats. By default all formats are included. Example: &#x60;sellingMode.format&#x3D;BUY_NOW&amp;sellingMode.format&#x3D;ADVERTISEMENT&#x60; - returns offers with with format &#x60;BUY_NOW&#x60; or &#x60;ADVERTISEMENT&#x60;. | [optional] 
 **external_id** | [**list[str]**](str.md)| The ID from the client&#39;s external system. Passing more than one value will search for offers with any of the given IDs. By default no ID is included. Example: &#x60;external.id&#x3D;1233&amp;external.id&#x3D;1234&#x60; - returns offers with ID &#x60;1233&#x60; or &#x60;1234&#x60;. Single ID length shouldn&#39;t exceed 100 characters. | [optional] 
 **delivery_shipping_rates_id** | [**str**](.md)| The ID of shipping rates. Returns offers with given shipping rates ID. | [optional] 
 **delivery_shipping_rates_id_empty** | **bool**| Allow to filter offers by existence of shipping rates ID. | [optional] 
 **sort** | **str**| The results&#39; sorting order. No prefix in the value means ascending order. &#x60;-&#x60; prefix means descending order. If you don&#39;t provide the sort parameter, the list is sorted by offer creation time, descending. | [optional] 
 **limit** | **int**| The maximum number of offers returned in the response. | [optional] [default to 20]
 **offset** | **int**| Index of the first returned offer from all search results. | [optional] 

### Return type

[**OffersSearchResultDto**](OffersSearchResultDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of offers returned successfully. |  -  |
**400** | The request query parameters are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

