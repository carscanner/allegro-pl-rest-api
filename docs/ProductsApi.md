# allegro_api.ProductsApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sale_product**](ProductsApi.md#get_sale_product) | **GET** /sale/products/{productId} | Get all data of the particular product
[**get_sale_products**](ProductsApi.md#get_sale_products) | **GET** /sale/products | Get search products results


# **get_sale_product**
> SaleProductResponseDto get_sale_product(product_id)

Get all data of the particular product

Use this resource to retrieve all data of the particular product.

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
api_instance = allegro_api.ProductsApi(allegro_api.ApiClient(configuration))
product_id = 'product_id_example' # str | Product identifier

try:
    # Get all data of the particular product
    api_response = api_instance.get_sale_product(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_sale_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product identifier | 

### Return type

[**SaleProductResponseDto**](SaleProductResponseDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sale_products**
> GetSaleProductsResponse get_sale_products(ean=ean)

Get search products results

Use this resource to get a list of products according to provided parameters. At least ean parameter is required.

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
api_instance = allegro_api.ProductsApi(allegro_api.ApiClient(configuration))
ean = 'ean_example' # str | The EAN values can include EAN, ISBN, and UPC identifier types. (optional)

try:
    # Get search products results
    api_response = api_instance.get_sale_products(ean=ean)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_sale_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **str**| The EAN values can include EAN, ISBN, and UPC identifier types. | [optional] 

### Return type

[**GetSaleProductsResponse**](GetSaleProductsResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

