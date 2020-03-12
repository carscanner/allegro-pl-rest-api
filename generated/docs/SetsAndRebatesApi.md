# allegro_api.SetsAndRebatesApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_promotion_using_post1**](SetsAndRebatesApi.md#create_promotion_using_post1) | **POST** /sale/loyalty/promotions | Create a new promotion
[**deactivate_promotion_using_delete**](SetsAndRebatesApi.md#deactivate_promotion_using_delete) | **DELETE** /sale/loyalty/promotions/{promotionId} | Deactivate a promotion by id
[**get_promotion_using_get**](SetsAndRebatesApi.md#get_promotion_using_get) | **GET** /sale/loyalty/promotions/{promotionId} | Get a promotion data by id
[**list_seller_promotions_using_get1**](SetsAndRebatesApi.md#list_seller_promotions_using_get1) | **GET** /sale/loyalty/promotions | Get the user&#39;s list of promotions


# **create_promotion_using_post1**
> SellerRebateDto create_promotion_using_post1(seller_create_rebate_request_dto)

Create a new promotion

This endpoint creates a new promotion. You can define the following types of promotions: 1. Bundle In order to create a new bundle, you have to define a  promotion with a single benefit of type **ORDER_FIXED_DISCOUNT** and a single criterion of type **CONTAINS_OFFERS**. In the benefit specification you have to declare the discount amount that you want to be deducted from the sum of bundled offers prices. In the offer criterion you need to pass a list of offers that are to be grouped as a bundle. For each offer you have to define a fixed quantity (that many pieces of your offer will be part of the bundle) and you also have to set a promotionEntryPoint flag (offers with this flag set to true will have a section that allows the users to purchase your bundle).  2. Multipack In order to create a new multipack, you have to define a promotion with a single benefit of type **UNIT_PERCENTAGE_DISCOUNT** and a single criterion of type **CONTAINS_OFFERS**. The benefit specification should contain a configuration section with a percentage which indicates the specific discount for the discounted offer. This percentage should be an integer value greater than 15 for quantity 2, greater than 30 for quantity 3, greater than 40 for quantity 4, greater than 50 for quantity 5 and lower than or equal to 100. The specification should also contain a trigger section with a field forEachQuantity that defines the amount of items in the multipack which is necessary to trigger the benefit. Additionally, the discountedNumber field must be set to 1 by default as you can only discount one unit in a multipack. Finally, the offer criterion specifies the offer for which the multipack promotion will take effect. 3. Cross-offer multipack A cross-offer multipack is created in the same fashion as a standard multipack. The only difference is that you need to pass more than 1 offer in the offer criterion section. This group of offers is then considered as a pool from which users can pick and choose forEachQuantity offers and the cheapest of them gets a discount. Read more about <a href=\"../../news/2017-10-18-news_promocyjne_zestawy_ofert/\" target=\"_blank\">bundles</a>, <a href=\"../../news/2018-02-01-rabaty_ilosciowe/\" target=\"_blank\">multipack</a> and <a href=\"../../news/2018-10-08-rabaty_ilosciowe/\" target=\"_blank\">cross-offer multipack</a>.

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
    api_instance = allegro_api.SetsAndRebatesApi(api_client)
    seller_create_rebate_request_dto = {"benefits":[{"specification":{"type":"ORDER_FIXED_DISCOUNT","value":{"amount":"10.00","currency":"PLN"}}}],"offerCriteria":[{"type":"CONTAINS_OFFERS","offers":[{"id":"1122334455","quantity":2,"promotionEntryPoint":true},{"id":"2233445566","quantity":1,"promotionEntryPoint":false}]}]} # SellerCreateRebateRequestDto | 

    try:
        # Create a new promotion
        api_response = api_instance.create_promotion_using_post1(seller_create_rebate_request_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SetsAndRebatesApi->create_promotion_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_create_rebate_request_dto** | [**SellerCreateRebateRequestDto**](SellerCreateRebateRequestDto.md)|  | 

### Return type

[**SellerRebateDto**](SellerRebateDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created the requested promotion |  -  |
**400** | Bad request |  -  |
**422** | Validation failed - your request was correct, but the promotion could not be created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_promotion_using_delete**
> deactivate_promotion_using_delete(promotion_id)

Deactivate a promotion by id

Use this resource to deactivate the requested promotion. You need to use its unique id. Read more about <a href=\"../../news/2017-10-18-news_promocyjne_zestawy_ofert/#4\" target=\"_blank\">bundles</a> and <a href=\"../../news/2018-02-01-rabaty_ilosciowe/#4\" target=\"_blank\">multipack</a>.

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
    api_instance = allegro_api.SetsAndRebatesApi(api_client)
    promotion_id = 'promotion_id_example' # str | Promotion identifier.

    try:
        # Deactivate a promotion by id
        api_instance.deactivate_promotion_using_delete(promotion_id)
    except ApiException as e:
        print("Exception when calling SetsAndRebatesApi->deactivate_promotion_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_id** | **str**| Promotion identifier. | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deactivated the requested promotion |  -  |
**404** | Promotion not found |  -  |
**422** | Promotion cannot be reactivated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_promotion_using_get**
> SellerRebateDto get_promotion_using_get(promotion_id)

Get a promotion data by id

Use this resource to returns the requested promotion. You need to use its unique id. Read more about <a href=\"../../news/2017-10-18-news_promocyjne_zestawy_ofert/#3\" target=\"_blank\">bundles</a> and <a href=\"../../news/2018-02-01-rabaty_ilosciowe/#3\" target=\"_blank\">multipack</a>.

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
    api_instance = allegro_api.SetsAndRebatesApi(api_client)
    promotion_id = 'promotion_id_example' # str | Promotion identifier.

    try:
        # Get a promotion data by id
        api_response = api_instance.get_promotion_using_get(promotion_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SetsAndRebatesApi->get_promotion_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_id** | **str**| Promotion identifier. | 

### Return type

[**SellerRebateDto**](SellerRebateDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the requested promotion |  -  |
**404** | Promotion not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_seller_promotions_using_get1**
> SellerRebatesDto list_seller_promotions_using_get1(user_id, limit=limit, offset=offset, offer_id=offer_id, promotion_type=promotion_type)

Get the user's list of promotions

<p>Get a list of promotions defined by the authorized user.</p> <p>Restrictions:</p> <p>Sum of limit and offset must be equal to or lower than 50000. Limit must be equal to or lower than 5000.</p> <p>Example:</p> <p>offset = 49950 and limit = 50 will return promotions</p> <p>offset = 49950 and limit = 51 will return 422 http error</p> <p>offset = 0 and limit = 5000 will return promotions</p> <p>offset = 0 and limit = 5001 will return 422 http error</p> <p>Read more about <a href=\"../../news/2017-10-18-news_promocyjne_zestawy_ofert/#2\" target=\"_blank\">Bundles</a> and <a href=\"../../news/2018-02-01-rabaty_ilosciowe/#2\" target=\"_blank\">Multipack</a>.</p>

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
    api_instance = allegro_api.SetsAndRebatesApi(api_client)
    user_id = '11111111' # str | The id of the user who is the owner of the promotions.
limit = 50 # int | Limit of promotions per page. (optional) (default to 50)
offset = 0 # int | Distance between the beginning of the document and the point from which promotions are returned. (optional) (default to 0)
offer_id = '8226673525' # str | Filter by offer id. (optional)
promotion_type = 'promotion_type_example' # str | Filter by promotion type. (optional)

    try:
        # Get the user's list of promotions
        api_response = api_instance.list_seller_promotions_using_get1(user_id, limit=limit, offset=offset, offer_id=offer_id, promotion_type=promotion_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SetsAndRebatesApi->list_seller_promotions_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user who is the owner of the promotions. | 
 **limit** | **int**| Limit of promotions per page. | [optional] [default to 50]
 **offset** | **int**| Distance between the beginning of the document and the point from which promotions are returned. | [optional] [default to 0]
 **offer_id** | **str**| Filter by offer id. | [optional] 
 **promotion_type** | **str**| Filter by promotion type. | [optional] 

### Return type

[**SellerRebatesDto**](SellerRebatesDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the requested list of promotions |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized action |  -  |
**404** | User id not found |  -  |
**422** | Restrictions were not satisfied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

