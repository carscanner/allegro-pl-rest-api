# allegro_api.CompatibilityListApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_categories_that_support_compatibility_list**](CompatibilityListApi.md#get_categories_that_support_compatibility_list) | **GET** /sale/compatibility-list/supported-categories | Get list of categories where compatibility list is supported
[**get_compatible_products**](CompatibilityListApi.md#get_compatible_products) | **GET** /sale/compatible-products | Get list of compatible products
[**get_compatible_products_groups**](CompatibilityListApi.md#get_compatible_products_groups) | **GET** /sale/compatible-products/groups | Get list of compatible product groups


# **get_categories_that_support_compatibility_list**
> CompatibilityListSupportedCategoriesDto get_categories_that_support_compatibility_list()

Get list of categories where compatibility list is supported

Compatibility list is available in particular categories, this resource allows to get the list of these categories with additional details.

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
    api_instance = allegro_api.CompatibilityListApi(api_client)
    
    try:
        # Get list of categories where compatibility list is supported
        api_response = api_instance.get_categories_that_support_compatibility_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CompatibilityListApi->get_categories_that_support_compatibility_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CompatibilityListSupportedCategoriesDto**](CompatibilityListSupportedCategoriesDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration of supported categories. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compatible_products**
> CompatibleProductsListDto get_compatible_products(type, if_modified_since=if_modified_since, group_id=group_id, tecdoc_k_typ_nr=tecdoc_k_typ_nr, tecdoc_n_typ_nr=tecdoc_n_typ_nr, phrase=phrase, limit=limit, offset=offset)

Get list of compatible products

Resource allows to fetch compatible products of given type.

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
    api_instance = allegro_api.CompatibilityListApi(api_client)
    type = 'CAR' # str | Type of compatible products. You can find available types in the response for the GET <a href=\"/documentation/#tag/Compatibility-List/paths/~1sale~1compatibility-list~1supported-categories/get\">supported-categories</a> resource. You can use value provided in `itemsType`, for categories where `inputType=ID`.
if_modified_since = 'Mon, 01 Dec 2018 10:00:00 GMT' # str | Date of last data modification. If data has been modified after specified date, full set of data is returned. If header is not specified, full set of data is returned. Date has to be provided in HTTP-date format. Header is ignored if `phrase` parameter is used. (optional)
group_id = 'group_id_example' # str | Group identifier from `/sale/compatible-products/groups` resource. Parameter is required when parameter `tecdoc.kTypNr` or `tecdoc.nTypNr` or `phrase` is not specified. (optional)
tecdoc_k_typ_nr = 'tecdoc_k_typ_nr_example' # str | Identifier of passenger vehicle (kTypNr) from TecDoc database. When used, `group.id` parameter is ignored. (optional)
tecdoc_n_typ_nr = 'tecdoc_n_typ_nr_example' # str | Identifier of commercial vehicle (nTypNr) from TecDoc database. When used, `group.id` parameter is ignored. (optional)
phrase = 'phrase_example' # str | Query for compatible products. When used, parameters: `group.id`, `limit`, `offset` and header `If-Modified-Since` are ignored. (optional)
limit = 200 # int | The limit of returned items. If `phrase` parameter is present, parameter is ignored and maximum value is set to `200`. (optional) (default to 200)
offset = 0 # int | The offset of returned items. If `phrase` parameter is present, parameter is ignored. (optional) (default to 0)

    try:
        # Get list of compatible products
        api_response = api_instance.get_compatible_products(type, if_modified_since=if_modified_since, group_id=group_id, tecdoc_k_typ_nr=tecdoc_k_typ_nr, tecdoc_n_typ_nr=tecdoc_n_typ_nr, phrase=phrase, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CompatibilityListApi->get_compatible_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of compatible products. You can find available types in the response for the GET &lt;a href&#x3D;\&quot;/documentation/#tag/Compatibility-List/paths/~1sale~1compatibility-list~1supported-categories/get\&quot;&gt;supported-categories&lt;/a&gt; resource. You can use value provided in &#x60;itemsType&#x60;, for categories where &#x60;inputType&#x3D;ID&#x60;. | 
 **if_modified_since** | **str**| Date of last data modification. If data has been modified after specified date, full set of data is returned. If header is not specified, full set of data is returned. Date has to be provided in HTTP-date format. Header is ignored if &#x60;phrase&#x60; parameter is used. | [optional] 
 **group_id** | **str**| Group identifier from &#x60;/sale/compatible-products/groups&#x60; resource. Parameter is required when parameter &#x60;tecdoc.kTypNr&#x60; or &#x60;tecdoc.nTypNr&#x60; or &#x60;phrase&#x60; is not specified. | [optional] 
 **tecdoc_k_typ_nr** | **str**| Identifier of passenger vehicle (kTypNr) from TecDoc database. When used, &#x60;group.id&#x60; parameter is ignored. | [optional] 
 **tecdoc_n_typ_nr** | **str**| Identifier of commercial vehicle (nTypNr) from TecDoc database. When used, &#x60;group.id&#x60; parameter is ignored. | [optional] 
 **phrase** | **str**| Query for compatible products. When used, parameters: &#x60;group.id&#x60;, &#x60;limit&#x60;, &#x60;offset&#x60; and header &#x60;If-Modified-Since&#x60; are ignored. | [optional] 
 **limit** | **int**| The limit of returned items. If &#x60;phrase&#x60; parameter is present, parameter is ignored and maximum value is set to &#x60;200&#x60;. | [optional] [default to 200]
 **offset** | **int**| The offset of returned items. If &#x60;phrase&#x60; parameter is present, parameter is ignored. | [optional] [default to 0]

### Return type

[**CompatibleProductsListDto**](CompatibleProductsListDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compatible products returned successfully. |  -  |
**304** | Data has not been modified after the date provided in If-Modified-Since header. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compatible_products_groups**
> CompatibleProductsGroupsDto get_compatible_products_groups(type, if_modified_since=if_modified_since, limit=limit, offset=offset)

Get list of compatible product groups

Compatible products are organized in groups, this resource allows to browse these groups.

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
    api_instance = allegro_api.CompatibilityListApi(api_client)
    type = 'CAR' # str | Type of compatible products. You can find available types in the response for the GET <a href=\"/documentation/#tag/Compatibility-List/paths/~1sale~1compatibility-list~1supported-categories/get\">supported-categories</a> resource. You can use value provided in `itemsType`, for categories where `inputType=ID`.
if_modified_since = 'Mon, 01 Dec 2018 10:00:00 GMT' # str | Date of last data modification. If data has been modified after specified date, full set of data is returned. If header is not specified, full set of data is returned. Date has to be provided in HTTP-date format. (optional)
limit = 200 # int | The limit of returned items. (optional) (default to 200)
offset = 0 # int | The offset of returned items. (optional) (default to 0)

    try:
        # Get list of compatible product groups
        api_response = api_instance.get_compatible_products_groups(type, if_modified_since=if_modified_since, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CompatibilityListApi->get_compatible_products_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of compatible products. You can find available types in the response for the GET &lt;a href&#x3D;\&quot;/documentation/#tag/Compatibility-List/paths/~1sale~1compatibility-list~1supported-categories/get\&quot;&gt;supported-categories&lt;/a&gt; resource. You can use value provided in &#x60;itemsType&#x60;, for categories where &#x60;inputType&#x3D;ID&#x60;. | 
 **if_modified_since** | **str**| Date of last data modification. If data has been modified after specified date, full set of data is returned. If header is not specified, full set of data is returned. Date has to be provided in HTTP-date format. | [optional] 
 **limit** | **int**| The limit of returned items. | [optional] [default to 200]
 **offset** | **int**| The offset of returned items. | [optional] [default to 0]

### Return type

[**CompatibleProductsGroupsDto**](CompatibleProductsGroupsDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Groups of compatible products returned successfully. |  -  |
**304** | Data has not been modified after the date provided in If-Modified-Since header. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

