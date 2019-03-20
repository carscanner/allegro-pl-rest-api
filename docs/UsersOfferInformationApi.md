# allegro_api.UsersOfferInformationApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_offer_using_get**](UsersOfferInformationApi.md#get_offer_using_get) | **GET** /sale/offers/{offerId} | Get all fields of the particular offer
[**search_offers_using_get**](UsersOfferInformationApi.md#search_offers_using_get) | **GET** /sale/offers | Get seller&#39;s offers


# **get_offer_using_get**
> Offer get_offer_using_get(offer_id)

Get all fields of the particular offer

Use this resource to retrieve all fields of the particular offer. More information about this resource you can find <a href=\"../../sale/#similar-offer\" target=\"_blank\">here</a>.

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
api_instance = allegro_api.UsersOfferInformationApi(allegro_api.ApiClient(configuration))
offer_id = 'offer_id_example' # str | offerId

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
 **offer_id** | **str**| offerId | 

### Return type

[**Offer**](Offer.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_offers_using_get**
> OffersSearchResultDtoV1 search_offers_using_get(seller_id, name=name, selling_mode_price_amount_gte=selling_mode_price_amount_gte, selling_mode_price_amount_lte=selling_mode_price_amount_lte, publication_status=publication_status, selling_mode_format=selling_mode_format, external_id=external_id, sort=sort, limit=limit, offset=offset)

Get seller's offers

Search seller's offers by given criteria. Accept header should be set to application/vnd.allegro.beta.v1+json

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
api_instance = allegro_api.UsersOfferInformationApi(allegro_api.ApiClient(configuration))
seller_id = 'seller_id_example' # str | Seller id
name = 'name_example' # str | Text to search in offer title (optional)
selling_mode_price_amount_gte = 3.4 # float | Minimal threshold of price (optional)
selling_mode_price_amount_lte = 3.4 # float | Maximal threshold of price (optional)
publication_status = 'ACTIVE,ACTIVATING,ENDED' # str | Publication statuses may contain more than one comma separated value (optional) (default to 'ACTIVE,ACTIVATING,ENDED')
selling_mode_format = 'selling_mode_format_example' # str | Selling mode may contain more than one comma separated value (optional)
external_id = 'external_id_example' # str | ID from external client system (optional)
sort = 'sort_example' # str | Sort direction (optional)
limit = 56 # int | Maximum number of seller's offers in response (acceptable values: from 1 to 1000, default is 20). (optional)
offset = 56 # int | Index of first returned seller's offers from all search results. (optional)

try:
    # Get seller's offers
    api_response = api_instance.search_offers_using_get(seller_id, name=name, selling_mode_price_amount_gte=selling_mode_price_amount_gte, selling_mode_price_amount_lte=selling_mode_price_amount_lte, publication_status=publication_status, selling_mode_format=selling_mode_format, external_id=external_id, sort=sort, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersOfferInformationApi->search_offers_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| Seller id | 
 **name** | **str**| Text to search in offer title | [optional] 
 **selling_mode_price_amount_gte** | **float**| Minimal threshold of price | [optional] 
 **selling_mode_price_amount_lte** | **float**| Maximal threshold of price | [optional] 
 **publication_status** | **str**| Publication statuses may contain more than one comma separated value | [optional] [default to &#39;ACTIVE,ACTIVATING,ENDED&#39;]
 **selling_mode_format** | **str**| Selling mode may contain more than one comma separated value | [optional] 
 **external_id** | **str**| ID from external client system | [optional] 
 **sort** | **str**| Sort direction | [optional] 
 **limit** | **int**| Maximum number of seller&#39;s offers in response (acceptable values: from 1 to 1000, default is 20). | [optional] 
 **offset** | **int**| Index of first returned seller&#39;s offers from all search results. | [optional] 

### Return type

[**OffersSearchResultDtoV1**](OffersSearchResultDtoV1.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

