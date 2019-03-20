# openapi_client.PricingApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offer_quotes_public_using_get**](PricingApi.md#offer_quotes_public_using_get) | **GET** /pricing/offer-quotes | Get the user&#39;s current offer quotes
[**preview_fees_public_api_using_post**](PricingApi.md#preview_fees_public_api_using_post) | **POST** /pricing/fee-preview | Preview offer fees


# **offer_quotes_public_using_get**
> OfferQuotesDto offer_quotes_public_using_get(offer_id, name=name)

Get the user's current offer quotes

This endpoint returns current offer quotes (listing and promo fees) cycles for authenticated user and list of offers. More information about this resource you can find <a href=\"../../news/2018-02-14-zasob_do_sprawdzania_daty_oplaty/\" target=\"_blank\">here</a>. <br/>2018-07-18 - resource update <a href=\"../../news/2018-07-18-aktualizacja_zasob_do_sprawdzania_daty_oplaty/\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.PricingApi(openapi_client.ApiClient(configuration))
offer_id = ['offer_id_example'] # list[str] | List of offer ids, maximum 20 values
name = 'name_example' # str |  (optional)

try:
    # Get the user's current offer quotes
    api_response = api_instance.offer_quotes_public_using_get(offer_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PricingApi->offer_quotes_public_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | [**list[str]**](str.md)| List of offer ids, maximum 20 values | 
 **name** | **str**|  | [optional] 

### Return type

[**OfferQuotesDto**](OfferQuotesDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_fees_public_api_using_post**
> WrapsListingAndCommissionsFees preview_fees_public_api_using_post(wrapper_type_for_preview_conditions)

Preview offer fees

This endpoint calculates fees for a provided offer conditions. The quotation is estimated and based on the current configuration of the Allegro price list and the data entered in this API. The stated price does not include package discounts. The rules of charging and amount of charges are described in the Allegro regulations in Appendix 4. The final amount of the fee for the offer will be available after approval under the tab: My Account> Accounts> History. More information about this resource you can find <a href=\"../../news/2017-10-30-kalkulator_ogloszenia/\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.PricingApi(openapi_client.ApiClient(configuration))
wrapper_type_for_preview_conditions = openapi_client.WrapperTypeForPreviewConditions() # WrapperTypeForPreviewConditions | command

try:
    # Preview offer fees
    api_response = api_instance.preview_fees_public_api_using_post(wrapper_type_for_preview_conditions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PricingApi->preview_fees_public_api_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wrapper_type_for_preview_conditions** | [**WrapperTypeForPreviewConditions**](WrapperTypeForPreviewConditions.md)| command | 

### Return type

[**WrapsListingAndCommissionsFees**](WrapsListingAndCommissionsFees.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

