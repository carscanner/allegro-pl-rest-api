# allegro_api.ClassifiedsApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_classified_packages_using_put**](ClassifiedsApi.md#assign_classified_packages_using_put) | **PUT** /sale/offer-classifieds-packages/{offerId} | Assign packages to a classified
[**get_classified_package_configuration_using_get**](ClassifiedsApi.md#get_classified_package_configuration_using_get) | **GET** /sale/classifieds-packages/{packageId} | Get the configuration of a package
[**get_classified_package_configurations_for_category_using_get**](ClassifiedsApi.md#get_classified_package_configurations_for_category_using_get) | **GET** /sale/classifieds-packages | Get configurations of packages
[**get_classified_packages_using_get**](ClassifiedsApi.md#get_classified_packages_using_get) | **GET** /sale/offer-classifieds-packages/{offerId} | Get classified packages assigned to an offer


# **assign_classified_packages_using_put**
> assign_classified_packages_using_put(offer_id, classified_packages)

Assign packages to a classified

Use this resource to assign classified packages to an offer.

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
    api_instance = allegro_api.ClassifiedsApi(api_client)
    offer_id = 'offer_id_example' # str | The offer ID.
classified_packages = allegro_api.ClassifiedPackages() # ClassifiedPackages | Packages that should be assigned to the classified.

    try:
        # Assign packages to a classified
        api_instance.assign_classified_packages_using_put(offer_id, classified_packages)
    except ApiException as e:
        print("Exception when calling ClassifiedsApi->assign_classified_packages_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| The offer ID. | 
 **classified_packages** | [**ClassifiedPackages**](ClassifiedPackages.md)| Packages that should be assigned to the classified. | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Packages have been successfully assigned to the classified. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classified_package_configuration_using_get**
> ClassifiedPackageConfig get_classified_package_configuration_using_get(package_id)

Get the configuration of a package

Use this resource to retrieve the configuration of a classifieds package.

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
    api_instance = allegro_api.ClassifiedsApi(api_client)
    package_id = 'package_id_example' # str | The classifieds package ID.

    try:
        # Get the configuration of a package
        api_response = api_instance.get_classified_package_configuration_using_get(package_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClassifiedsApi->get_classified_package_configuration_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**| The classifieds package ID. | 

### Return type

[**ClassifiedPackageConfig**](ClassifiedPackageConfig.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The package&#39;s configuration returned successfully. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The classifieds package not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classified_package_configurations_for_category_using_get**
> ClassifiedPackageConfigs get_classified_package_configurations_for_category_using_get(category_id)

Get configurations of packages

Use this resource to retrieve configurations of classifieds packages for a category.

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
    api_instance = allegro_api.ClassifiedsApi(api_client)
    category_id = 'category_id_example' # str | The category ID.

    try:
        # Get configurations of packages
        api_response = api_instance.get_classified_package_configurations_for_category_using_get(category_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClassifiedsApi->get_classified_package_configurations_for_category_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The category ID. | 

### Return type

[**ClassifiedPackageConfigs**](ClassifiedPackageConfigs.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Package configurations for the category returned successfully. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classified_packages_using_get**
> ClassifiedResponse get_classified_packages_using_get(offer_id)

Get classified packages assigned to an offer

Use this resource to retrieve classified packages currently assigned to an offer.

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
    api_instance = allegro_api.ClassifiedsApi(api_client)
    offer_id = 'offer_id_example' # str | Offer ID.

    try:
        # Get classified packages assigned to an offer
        api_response = api_instance.get_classified_packages_using_get(offer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClassifiedsApi->get_classified_packages_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Offer ID. | 

### Return type

[**ClassifiedResponse**](ClassifiedResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Packages returned successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Classified not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

