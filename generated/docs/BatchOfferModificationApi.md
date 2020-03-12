# allegro_api.BatchOfferModificationApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_general_report_using_get**](BatchOfferModificationApi.md#get_general_report_using_get) | **GET** /sale/offer-modification-commands/{commandId} | Modification command summary
[**get_price_modification_command_status_using_get**](BatchOfferModificationApi.md#get_price_modification_command_status_using_get) | **GET** /sale/offer-price-change-commands/{commandId} | Change price command summary
[**get_price_modification_command_tasks_statuses_using_get**](BatchOfferModificationApi.md#get_price_modification_command_tasks_statuses_using_get) | **GET** /sale/offer-price-change-commands/{commandId}/tasks | Change price command detailed report
[**get_quantity_modification_command_status_using_get**](BatchOfferModificationApi.md#get_quantity_modification_command_status_using_get) | **GET** /sale/offer-quantity-change-commands/{commandId} | Change quantity command summary
[**get_quantity_modification_command_tasks_statuses_using_get**](BatchOfferModificationApi.md#get_quantity_modification_command_tasks_statuses_using_get) | **GET** /sale/offer-quantity-change-commands/{commandId}/tasks | Change quantity command detailed report
[**get_tasks_using_get**](BatchOfferModificationApi.md#get_tasks_using_get) | **GET** /sale/offer-modification-commands/{commandId}/tasks | Modification command detailed report
[**modification_command_using_put**](BatchOfferModificationApi.md#modification_command_using_put) | **PUT** /sale/offer-modification-commands/{commandId} | Batch offer modification
[**price_modification_command_using_put**](BatchOfferModificationApi.md#price_modification_command_using_put) | **PUT** /sale/offer-price-change-commands/{commandId} | Batch offer price modification
[**quantity_modification_command_using_put**](BatchOfferModificationApi.md#quantity_modification_command_using_put) | **PUT** /sale/offer-quantity-change-commands/{commandId} | Batch offer quantity modification


# **get_general_report_using_get**
> GeneralReport get_general_report_using_get(command_id)

Modification command summary

Use this resource to find out how many offers were edited within one {commandId}. You will receive a summary with a number of successfully edited offers. <a href=\"../../news/2018-04-19-news_grupowa_edycja_ofert_update/#2\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.BatchOfferModificationApi(api_client)
    command_id = 'command_id_example' # str | Command identifier.

    try:
        # Modification command summary
        api_response = api_instance.get_general_report_using_get(command_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchOfferModificationApi->get_general_report_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| Command identifier. | 

### Return type

[**GeneralReport**](GeneralReport.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | report was generated and successfully returned |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Command not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_modification_command_status_using_get**
> GeneralReport get_price_modification_command_status_using_get(command_id)

Change price command summary

Returns status and summary of particular command execution.

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
    api_instance = allegro_api.BatchOfferModificationApi(api_client)
    command_id = 'command_id_example' # str | Command identifier.

    try:
        # Change price command summary
        api_response = api_instance.get_price_modification_command_status_using_get(command_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchOfferModificationApi->get_price_modification_command_status_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| Command identifier. | 

### Return type

[**GeneralReport**](GeneralReport.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | report was generated and successfully returned |  -  |
**401** | Unauthorized |  -  |
**404** | Command not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_modification_command_tasks_statuses_using_get**
> TaskReport get_price_modification_command_tasks_statuses_using_get(command_id, limit=limit, offset=offset)

Change price command detailed report

Defaults: limit = 100, offset = 0.

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
    api_instance = allegro_api.BatchOfferModificationApi(api_client)
    command_id = 'command_id_example' # str | Command identifier.
limit = 56 # int | The limit of elements in the response. (optional)
offset = 56 # int | The offset of elements in the response. (optional)

    try:
        # Change price command detailed report
        api_response = api_instance.get_price_modification_command_tasks_statuses_using_get(command_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchOfferModificationApi->get_price_modification_command_tasks_statuses_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| Command identifier. | 
 **limit** | **int**| The limit of elements in the response. | [optional] 
 **offset** | **int**| The offset of elements in the response. | [optional] 

### Return type

[**TaskReport**](TaskReport.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task status successfully returned |  -  |
**401** | Unauthorized |  -  |
**404** | Command not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quantity_modification_command_status_using_get**
> GeneralReport get_quantity_modification_command_status_using_get(command_id)

Change quantity command summary

Returns status and summary of the command.

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
    api_instance = allegro_api.BatchOfferModificationApi(api_client)
    command_id = 'command_id_example' # str | Command identifier.

    try:
        # Change quantity command summary
        api_response = api_instance.get_quantity_modification_command_status_using_get(command_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchOfferModificationApi->get_quantity_modification_command_status_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| Command identifier. | 

### Return type

[**GeneralReport**](GeneralReport.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | report was generated and successfully returned |  -  |
**401** | Unauthorized |  -  |
**404** | Command not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quantity_modification_command_tasks_statuses_using_get**
> TaskReport get_quantity_modification_command_tasks_statuses_using_get(command_id, limit=limit, offset=offset)

Change quantity command detailed report

Defaults: limit = 100, offset = 0.

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
    api_instance = allegro_api.BatchOfferModificationApi(api_client)
    command_id = 'command_id_example' # str | Command identifier.
limit = 56 # int | The limit of elements in the response. (optional)
offset = 56 # int | The offset of elements in the response. (optional)

    try:
        # Change quantity command detailed report
        api_response = api_instance.get_quantity_modification_command_tasks_statuses_using_get(command_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchOfferModificationApi->get_quantity_modification_command_tasks_statuses_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| Command identifier. | 
 **limit** | **int**| The limit of elements in the response. | [optional] 
 **offset** | **int**| The offset of elements in the response. | [optional] 

### Return type

[**TaskReport**](TaskReport.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task status successfully returned |  -  |
**401** | Unauthorized |  -  |
**404** | Command not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_using_get**
> TaskReport get_tasks_using_get(command_id, limit=limit, offset=offset)

Modification command detailed report

Use this resource to retrieve a detailed summary of changes introduced within one {commandId} (defaults: limit = 100, offset = 0). <a href=\"../../news/2018-04-19-news_grupowa_edycja_ofert_update/#2\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.BatchOfferModificationApi(api_client)
    command_id = 'command_id_example' # str | Command identifier.
limit = 56 # int | The limit of elements in the response. (optional)
offset = 56 # int | The offset of elements in the response. (optional)

    try:
        # Modification command detailed report
        api_response = api_instance.get_tasks_using_get(command_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchOfferModificationApi->get_tasks_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| Command identifier. | 
 **limit** | **int**| The limit of elements in the response. | [optional] 
 **offset** | **int**| The offset of elements in the response. | [optional] 

### Return type

[**TaskReport**](TaskReport.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task status successfully returned |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Command not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modification_command_using_put**
> GeneralReport modification_command_using_put(command_id, offer_change_command)

Batch offer modification

Use this resource to modify multiple offers at once. <a href=\"../../news/2018-04-19-news_grupowa_edycja_ofert_update/#1\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.BatchOfferModificationApi(api_client)
    command_id = 'command_id_example' # str | Command identifier.
offer_change_command = allegro_api.OfferChangeCommand() # OfferChangeCommand | offerChangeCommandDto

    try:
        # Batch offer modification
        api_response = api_instance.modification_command_using_put(command_id, offer_change_command)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchOfferModificationApi->modification_command_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| Command identifier. | 
 **offer_change_command** | [**OfferChangeCommand**](OfferChangeCommand.md)| offerChangeCommandDto | 

### Return type

[**GeneralReport**](GeneralReport.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Command was registered |  -  |
**400** | Semantically incorrect request or provided conditions not correct |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Command id was already used |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **price_modification_command_using_put**
> GeneralReport price_modification_command_using_put(command_id, offer_price_change_command)

Batch offer price modification

Change price of offers.

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
    api_instance = allegro_api.BatchOfferModificationApi(api_client)
    command_id = 'command_id_example' # str | Command identifier.
offer_price_change_command = allegro_api.OfferPriceChangeCommand() # OfferPriceChangeCommand | offerPriceChangeCommandDto

    try:
        # Batch offer price modification
        api_response = api_instance.price_modification_command_using_put(command_id, offer_price_change_command)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchOfferModificationApi->price_modification_command_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| Command identifier. | 
 **offer_price_change_command** | [**OfferPriceChangeCommand**](OfferPriceChangeCommand.md)| offerPriceChangeCommandDto | 

### Return type

[**GeneralReport**](GeneralReport.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Command was registered |  -  |
**400** | Semantically incorrect request or provided conditions not correct |  -  |
**401** | Unauthorized |  -  |
**409** | Command id was already used |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quantity_modification_command_using_put**
> GeneralReport quantity_modification_command_using_put(command_id, offer_quantity_change_command)

Batch offer quantity modification

Change quantity of multiple offers.

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
    api_instance = allegro_api.BatchOfferModificationApi(api_client)
    command_id = 'command_id_example' # str | Command identifier.
offer_quantity_change_command = allegro_api.OfferQuantityChangeCommand() # OfferQuantityChangeCommand | offerQuantityChangeCommandDto

    try:
        # Batch offer quantity modification
        api_response = api_instance.quantity_modification_command_using_put(command_id, offer_quantity_change_command)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchOfferModificationApi->quantity_modification_command_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| Command identifier. | 
 **offer_quantity_change_command** | [**OfferQuantityChangeCommand**](OfferQuantityChangeCommand.md)| offerQuantityChangeCommandDto | 

### Return type

[**GeneralReport**](GeneralReport.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Command was registered |  -  |
**400** | Semantically incorrect request or provided conditions not correct |  -  |
**401** | Unauthorized |  -  |
**409** | Command id was already used |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

