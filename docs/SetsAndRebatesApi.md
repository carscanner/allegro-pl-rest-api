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

This endpoint creates a new promotion. You can define the following types of promotions:  1. Bundle  In order to create a new bundle, you have to define a  promotion with a single benefit of type **ORDER_FIXED_DISCOUNT** and a single criterion of type **CONTAINS_OFFERS**. In the benefit specification you have to declare the discount amount that you want to be deducted from the sum of bundled offers prices. In the offer criterion you need to pass a list of offers that are to be grouped as a bundle. For each offer you have to define a fixed quantity (that many pieces of your offer will be part of the bundle) and you also have to set a promotionEntryPoint flag (offers with this flag set to true will have a section that allows the users to purchase your bundle).  2. Multipack  In order to create a new multipack, you have to define a promotion with a single benefit of type **UNIT_PERCENTAGE_DISCOUNT** and a single criterion of type **CONTAINS_OFFERS**. The benefit specification should contain a configuration section with a percentage which indicates the specific discount for the discounted offer. This percentage should be an integer value greater than 15 for quantity 2, greater than 30 for quantity 3, greater than 40 for quantity 4, greater than 50 for quantity 5 and lower than or equal to 100. The specification should also contain a trigger section with a field forEachQuantity that defines the amount of items in the multipack which is necessary to trigger the benefit. Additionally, the discountedNumber field must be set to 1 by default as you can only discount one unit in a multipack. Finally, the offer criterion specifies the offer for which the multipack promotion will take effect.  3. Cross-offer multipack  A cross-offer multipack is created in the same fashion as a standard multipack. The only difference is that you need to pass more than 1 offer in the offer criterion section. This group of offers is then considered as a pool from which users can pick and choose forEachQuantity offers and the cheapest of them gets a discount.  More information about this resource you can find <a href=\"../../news/2017-10-18-news_promocyjne_zestawy_ofert/\" target=\"_blank\">here (Bundles)</a>, <a href=\"../../news/2018-02-01-rabaty_ilosciowe/\" target=\"_blank\">here (Multipack)</a> and <a href=\"../../news/2018-10-08-rabaty_ilosciowe/\" target=\"_blank\">here (Cross-offer multipack)</a>.  **Example request bodies:** 1) Bundle ``` {   \"benefits\": [     {       \"specification\": {         \"type\": \"ORDER_FIXED_DISCOUNT\",         \"value\": {           \"amount\": \"10\",           \"currency\": \"PLN\"         }       }     }   ],   \"offerCriteria\": [     {       \"type\": \"CONTAINS_OFFERS\",       \"offers\": [         {           \"id\": \"1122334455\",           \"quantity\": 2,           \"promotionEntryPoint\": true         },         {           \"id\": \"2233445566\",           \"quantity\": 1,           \"promotionEntryPoint\": false         }       ]     }   ] } ``` 2) Multipack ``` {   \"benefits\": [     {       \"specification\": {         \"type\": \"UNIT_PERCENTAGE_DISCOUNT\",         \"configuration\": {           \"percentage\": \"100\"         },         \"trigger\": {           \"forEachQuantity\": \"3\",           \"discountedNumber\": \"1\"         }       }     }   ],   \"offerCriteria\": [     {       \"type\": \"CONTAINS_OFFERS\",       \"offers\": [         {           \"id\": \"1122334455\"         }       ]     }   ] } ``` 3) Cross-offer multipack ``` {   \"benefits\": [     {       \"specification\": {         \"type\": \"UNIT_PERCENTAGE_DISCOUNT\",         \"configuration\": {           \"percentage\": \"100\"         },         \"trigger\": {           \"forEachQuantity\": \"3\",           \"discountedNumber\": \"1\"         }       }     }   ],   \"offerCriteria\": [     {       \"type\": \"CONTAINS_OFFERS\",       \"offers\": [         {           \"id\": \"1122334455\"         },         {           \"id\": \"2233445566\"         },       ]     }   ] } ``` 

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
api_instance = allegro_api.SetsAndRebatesApi(allegro_api.ApiClient(configuration))
seller_create_rebate_request_dto = allegro_api.SellerCreateRebateRequestDto() # SellerCreateRebateRequestDto | request

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
 **seller_create_rebate_request_dto** | [**SellerCreateRebateRequestDto**](SellerCreateRebateRequestDto.md)| request | 

### Return type

[**SellerRebateDto**](SellerRebateDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_promotion_using_delete**
> deactivate_promotion_using_delete(promotion_id)

Deactivate a promotion by id

Use this resource to deactivate the requested promotion. You need to use its unique id. More information about this resource you can find <a href=\"../../news/2017-10-18-news_promocyjne_zestawy_ofert/#4\" target=\"_blank\">here (Bundles)</a> and <a href=\"../../news/2018-02-01-rabaty_ilosciowe/#4\" target=\"_blank\">here (Multipack)</a>.

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
api_instance = allegro_api.SetsAndRebatesApi(allegro_api.ApiClient(configuration))
promotion_id = 'promotion_id_example' # str | promotionId

try:
    # Deactivate a promotion by id
    api_instance.deactivate_promotion_using_delete(promotion_id)
except ApiException as e:
    print("Exception when calling SetsAndRebatesApi->deactivate_promotion_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_id** | **str**| promotionId | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_promotion_using_get**
> SellerRebateDto get_promotion_using_get(promotion_id)

Get a promotion data by id

Use this resource to returns the requested promotion. You need to use its unique id. More information about this resource you can find <a href=\"../../news/2017-10-18-news_promocyjne_zestawy_ofert/#3\" target=\"_blank\">here (Bundles)</a> and <a href=\"../../news/2018-02-01-rabaty_ilosciowe/#3\" target=\"_blank\">here (Multipack)</a>.

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
api_instance = allegro_api.SetsAndRebatesApi(allegro_api.ApiClient(configuration))
promotion_id = 'promotion_id_example' # str | promotionId

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
 **promotion_id** | **str**| promotionId | 

### Return type

[**SellerRebateDto**](SellerRebateDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_seller_promotions_using_get1**
> SellerRebatesDto list_seller_promotions_using_get1(user_id, limit=limit, offset=offset)

Get the user's list of promotions

Get a list of promotions defined by the specified user. You can list only your own promotions. More information about this resource you can find <a href=\"../../news/2017-10-18-news_promocyjne_zestawy_ofert/#2\" target=\"_blank\">here (Bundles)</a> and <a href=\"../../news/2018-02-01-rabaty_ilosciowe/#2\" target=\"_blank\">here (Multipack)</a>.

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
api_instance = allegro_api.SetsAndRebatesApi(allegro_api.ApiClient(configuration))
user_id = 'user_id_example' # str | user.id
limit = 50 # int | limit (optional) (default to 50)
offset = 0 # int | offset (optional) (default to 0)

try:
    # Get the user's list of promotions
    api_response = api_instance.list_seller_promotions_using_get1(user_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetsAndRebatesApi->list_seller_promotions_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| user.id | 
 **limit** | **int**| limit | [optional] [default to 50]
 **offset** | **int**| offset | [optional] [default to 0]

### Return type

[**SellerRebatesDto**](SellerRebatesDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

