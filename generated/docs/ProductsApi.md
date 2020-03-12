# allegro_api.ProductsApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_flat_product_parameters_using_get**](ProductsApi.md#get_flat_product_parameters_using_get) | **GET** /sale/categories/{categoryId}/product-parameters | Get product parameters available in given category
[**get_sale_product**](ProductsApi.md#get_sale_product) | **GET** /sale/products/{productId} | Get all data of the particular product
[**get_sale_products**](ProductsApi.md#get_sale_products) | **GET** /sale/products | Get search products results
[**propose_sale_product**](ProductsApi.md#propose_sale_product) | **POST** /sale/product-proposals | Propose a product


# **get_flat_product_parameters_using_get**
> CategoryProductParameterList get_flat_product_parameters_using_get(category_id)

Get product parameters available in given category

Use this resource to get the list of product parameters available in given category. You can use these parameters to create a new product. <a href=\"../../productization\" target=\"_blank\">Read more</a>.

### Example

* OAuth Authentication (bearer-token-for-application):
```python
from __future__ import print_function
import time
import allegro_api
from allegro_api.rest import ApiException
from pprint import pprint
configuration = allegro_api.Configuration()
# Configure OAuth2 access token for authorization: bearer-token-for-application
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = allegro_api.Configuration()
# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.allegro.pl
configuration.host = "https://api.allegro.pl"
# Enter a context with an instance of the API client
with allegro_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = allegro_api.ProductsApi(api_client)
    category_id = '709' # str | The category ID.

    try:
        # Get product parameters available in given category
        api_response = api_instance.get_flat_product_parameters_using_get(category_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_flat_product_parameters_using_get: %s\n" % e)
```

* OAuth Authentication (bearer-token-for-user):
```python
from __future__ import print_function
import time
import allegro_api
from allegro_api.rest import ApiException
from pprint import pprint
configuration = allegro_api.Configuration()
# Configure OAuth2 access token for authorization: bearer-token-for-application
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = allegro_api.Configuration()
# Configure OAuth2 access token for authorization: bearer-token-for-user
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.allegro.pl
configuration.host = "https://api.allegro.pl"
# Enter a context with an instance of the API client
with allegro_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = allegro_api.ProductsApi(api_client)
    category_id = '709' # str | The category ID.

    try:
        # Get product parameters available in given category
        api_response = api_instance.get_flat_product_parameters_using_get(category_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_flat_product_parameters_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The category ID. | 

### Return type

[**CategoryProductParameterList**](CategoryProductParameterList.md)

### Authorization

[bearer-token-for-application](../README.md#bearer-token-for-application), [bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of product parameters for the category returned successfully. |  -  |
**404** | The category with the given ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sale_product**
> SaleProductDto get_sale_product(product_id)

Get all data of the particular product

Use this resource to retrieve all data of the particular product. <a href=\"../../productization/#details\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.ProductsApi(api_client)
    product_id = 'product_id_example' # str | The product identifier.

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
 **product_id** | **str**| The product identifier. | 

### Return type

[**SaleProductDto**](SaleProductDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product returned successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sale_products**
> GetSaleProductsResponse get_sale_products(ean=ean, phrase=phrase, category_id=category_id, dynamic_filters=dynamic_filters, page_id=page_id)

Get search products results

Use this resource to get a list of products according to provided parameters. At least ean or phrase parameter is required. <a href=\"../../productization/#search\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.ProductsApi(api_client)
    ean = 'ean_example' # str | The EAN values can include EAN, ISBN, and UPC identifier types. (optional)
phrase = 'phrase_example' # str | Search phrase. (optional)
category_id = 'category_id_example' # str | The category identifier to filter results. (optional)
dynamic_filters = {'key': 'dynamic_filters_example'} # dict(str, str) | You can filter and customize your search results to find exactly what you need by applying filters ids and their dictionary values to query according to the flowing pattern: id=value. When the filter definition looks like:   ````   {     \"id\": \"127448\",     \"name\": \"Kolor\",     \"type\": \"SINGLE\",     \"values\": [       {         \"name\": \"biały\",         \"value\": \"2\"       },       {         \"name\": \"czarny\",         \"value\": \"1\" }     ]   }   ```` You can use 'Kolor' filter to query results, i.e.:   * `127448=2` for \"biały\"   * `127448=1` for \"czarny\". (optional)
page_id = 'page_id_example' # str | A \"cursor\" to the next set of results. (optional)

    try:
        # Get search products results
        api_response = api_instance.get_sale_products(ean=ean, phrase=phrase, category_id=category_id, dynamic_filters=dynamic_filters, page_id=page_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_sale_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **str**| The EAN values can include EAN, ISBN, and UPC identifier types. | [optional] 
 **phrase** | **str**| Search phrase. | [optional] 
 **category_id** | **str**| The category identifier to filter results. | [optional] 
 **dynamic_filters** | [**dict(str, str)**](str.md)| You can filter and customize your search results to find exactly what you need by applying filters ids and their dictionary values to query according to the flowing pattern: id&#x3D;value. When the filter definition looks like:   &#x60;&#x60;&#x60;&#x60;   {     \&quot;id\&quot;: \&quot;127448\&quot;,     \&quot;name\&quot;: \&quot;Kolor\&quot;,     \&quot;type\&quot;: \&quot;SINGLE\&quot;,     \&quot;values\&quot;: [       {         \&quot;name\&quot;: \&quot;biały\&quot;,         \&quot;value\&quot;: \&quot;2\&quot;       },       {         \&quot;name\&quot;: \&quot;czarny\&quot;,         \&quot;value\&quot;: \&quot;1\&quot; }     ]   }   &#x60;&#x60;&#x60;&#x60; You can use &#39;Kolor&#39; filter to query results, i.e.:   * &#x60;127448&#x3D;2&#x60; for \&quot;biały\&quot;   * &#x60;127448&#x3D;1&#x60; for \&quot;czarny\&quot;. | [optional] 
 **page_id** | **str**| A \&quot;cursor\&quot; to the next set of results. | [optional] 

### Return type

[**GetSaleProductsResponse**](GetSaleProductsResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**401** | Unauthorized |  -  |
**422** | One of parameters have invalid value. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **propose_sale_product**
> SaleProductDto propose_sale_product(propose_sale_product_request)

Propose a product

Use this resource to propose a product.

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
    api_instance = allegro_api.ProductsApi(api_client)
    propose_sale_product_request = allegro_api.ProposeSaleProductRequest() # ProposeSaleProductRequest | 

    try:
        # Propose a product
        api_response = api_instance.propose_sale_product(propose_sale_product_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->propose_sale_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **propose_sale_product_request** | [**ProposeSaleProductRequest**](ProposeSaleProductRequest.md)|  | 

### Return type

[**SaleProductDto**](SaleProductDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Product proposed successfully. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - not allowed to access. |  -  |
**409** | Product already exists. Url of the existing product is provided in the HTTP Location header field of the response. |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

