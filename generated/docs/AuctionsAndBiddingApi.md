# allegro_api.AuctionsAndBiddingApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bid**](AuctionsAndBiddingApi.md#get_bid) | **GET** /bidding/offers/{offerId}/bid | Get current user&#39;s bid information
[**place_bid**](AuctionsAndBiddingApi.md#place_bid) | **PUT** /bidding/offers/{offerId}/bid | Place a bid in an auction


# **get_bid**
> MyBidResponse get_bid(offer_id)

Get current user's bid information

Get current user's bid information.

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
    api_instance = allegro_api.AuctionsAndBiddingApi(api_client)
    offer_id = 'offer_id_example' # str | The offer ID.

    try:
        # Get current user's bid information
        api_response = api_instance.get_bid(offer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuctionsAndBiddingApi->get_bid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| The offer ID. | 

### Return type

[**MyBidResponse**](MyBidResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bid information succesfully found. |  -  |
**404** | Auction not found or user did not bid in the auction. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_bid**
> MyBidResponse place_bid(offer_id, bid_request=bid_request)

Place a bid in an auction

Place a bid in an auction.

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
    api_instance = allegro_api.AuctionsAndBiddingApi(api_client)
    offer_id = 'offer_id_example' # str | The offer ID.
bid_request = allegro_api.BidRequest() # BidRequest |  (optional)

    try:
        # Place a bid in an auction
        api_response = api_instance.place_bid(offer_id, bid_request=bid_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuctionsAndBiddingApi->place_bid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| The offer ID. | 
 **bid_request** | [**BidRequest**](BidRequest.md)|  | [optional] 

### Return type

[**MyBidResponse**](MyBidResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bid succesfully placed |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized |  -  |
**404** | Auction not found. |  -  |
**422** | If bidding was not allowed (see message for explanation). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

