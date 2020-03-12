# allegro_api.OfferRatingApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offer_rating_get**](OfferRatingApi.md#offer_rating_get) | **GET** /sale/offers/{offerId}/rating | Get offer rating


# **offer_rating_get**
> OfferRating offer_rating_get(offer_id)

Get offer rating

Use this resource to get offer rating.

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
    api_instance = allegro_api.OfferRatingApi(api_client)
    offer_id = 'offer_id_example' # str | Offer identifier.

    try:
        # Get offer rating
        api_response = api_instance.offer_rating_get(offer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfferRatingApi->offer_rating_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Offer identifier. | 

### Return type

[**OfferRating**](OfferRating.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**403** | Offer access denied. |  -  |
**404** | Offer not found. |  -  |
**401** | Unauthorized action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

