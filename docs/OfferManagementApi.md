# openapi_client.OfferManagementApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_publication_status_using_put**](OfferManagementApi.md#change_publication_status_using_put) | **PUT** /sale/offer-publication-commands/{commandId} | Batch offer publish / unpublish
[**create_change_price_command_using_put**](OfferManagementApi.md#create_change_price_command_using_put) | **PUT** /offers/{offerId}/change-price-commands/{commandId} | Modify the Buy Now price in an offer
[**create_offer_using_post**](OfferManagementApi.md#create_offer_using_post) | **POST** /sale/offers | Create a draft offer
[**delete_offer_using_delete**](OfferManagementApi.md#delete_offer_using_delete) | **DELETE** /sale/offers/{offerId} | Delete a draft offer
[**get_publication_report_using_get**](OfferManagementApi.md#get_publication_report_using_get) | **GET** /sale/offer-publication-commands/{commandId} | Publish command summary
[**get_publication_tasks_using_get**](OfferManagementApi.md#get_publication_tasks_using_get) | **GET** /sale/offer-publication-commands/{commandId}/tasks | Publish command detailed report
[**update_offer_using_put**](OfferManagementApi.md#update_offer_using_put) | **PUT** /sale/offers/{offerId} | Complete a draft offer or edit an offer


# **change_publication_status_using_put**
> GeneralReport change_publication_status_using_put(command_id, publication_change_command_dto)

Batch offer publish / unpublish

Use this resource to modify multiple offers publication at once. More information about this resource you can find <a href=\"../../sale/#step-8-offer-publication-commands\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.OfferManagementApi(openapi_client.ApiClient(configuration))
command_id = 'command_id_example' # str | commandId
publication_change_command_dto = openapi_client.PublicationChangeCommandDto() # PublicationChangeCommandDto | publicationChangeCommandDto

try:
    # Batch offer publish / unpublish
    api_response = api_instance.change_publication_status_using_put(command_id, publication_change_command_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferManagementApi->change_publication_status_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| commandId | 
 **publication_change_command_dto** | [**PublicationChangeCommandDto**](PublicationChangeCommandDto.md)| publicationChangeCommandDto | 

### Return type

[**GeneralReport**](GeneralReport.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_change_price_command_using_put**
> ChangePrice create_change_price_command_using_put(offer_id, command_id, change_price_without_output)

Modify the Buy Now price in an offer

Use this resource to change the Buy Now price in a single offer. More information about this resource you can find <a href=\"../../news/2016-08-01-zmiana-ceny/\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.OfferManagementApi(openapi_client.ApiClient(configuration))
offer_id = 'offer_id_example' # str | Offer identifier
command_id = 'command_id_example' # str | Universally Unique  Identifier (UUID) you generate to enforce idempotency. UUID specification: http://www.ietf.org/rfc/rfc4122.txt
change_price_without_output = openapi_client.ChangePriceWithoutOutput() # ChangePriceWithoutOutput | Command input data. Note that the amount field must be transferred as a string to avoid rounding errors. A currency must be provided as a 3-letter code as defined in ISO 4217. (https://en.wikipedia.org/wiki/ISO_4217#Active_codes)

try:
    # Modify the Buy Now price in an offer
    api_response = api_instance.create_change_price_command_using_put(offer_id, command_id, change_price_without_output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferManagementApi->create_change_price_command_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Offer identifier | 
 **command_id** | **str**| Universally Unique  Identifier (UUID) you generate to enforce idempotency. UUID specification: http://www.ietf.org/rfc/rfc4122.txt | 
 **change_price_without_output** | [**ChangePriceWithoutOutput**](ChangePriceWithoutOutput.md)| Command input data. Note that the amount field must be transferred as a string to avoid rounding errors. A currency must be provided as a 3-letter code as defined in ISO 4217. (https://en.wikipedia.org/wiki/ISO_4217#Active_codes) | 

### Return type

[**ChangePrice**](ChangePrice.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_offer_using_post**
> Offer create_offer_using_post(offer)

Create a draft offer

Use this resource to create a draft offer. More information about this resource you can find <a href=\"../../sale/#step-6-draft\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.OfferManagementApi(openapi_client.ApiClient(configuration))
offer = openapi_client.Offer() # Offer | offer

try:
    # Create a draft offer
    api_response = api_instance.create_offer_using_post(offer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferManagementApi->create_offer_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer** | [**Offer**](Offer.md)| offer | 

### Return type

[**Offer**](Offer.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_offer_using_delete**
> delete_offer_using_delete(offer_id)

Delete a draft offer

Use this resource to delete a draft offer. More information about this resource you can find <a href=\"../../news/2018-10-09_draft_delete/\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.OfferManagementApi(openapi_client.ApiClient(configuration))
offer_id = 'offer_id_example' # str | offerId

try:
    # Delete a draft offer
    api_instance.delete_offer_using_delete(offer_id)
except ApiException as e:
    print("Exception when calling OfferManagementApi->delete_offer_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| offerId | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_publication_report_using_get**
> GeneralReport get_publication_report_using_get(command_id)

Publish command summary

Use this resource to retrieve information about the offer listing statuses. You will receive a summary with a number of correctly listed offers and errors. More information about this resource you can find <a href=\"../../sale/#step-8-offer-publication-commands\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.OfferManagementApi(openapi_client.ApiClient(configuration))
command_id = 'command_id_example' # str | commandId

try:
    # Publish command summary
    api_response = api_instance.get_publication_report_using_get(command_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferManagementApi->get_publication_report_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| commandId | 

### Return type

[**GeneralReport**](GeneralReport.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_publication_tasks_using_get**
> TaskReport get_publication_tasks_using_get(command_id, limit=limit, offset=offset)

Publish command detailed report

Use this resource to retrieve information about the offer statuses on the site (Defaults: limit = 100, offset = 0). More information about this resource you can find <a href=\"../../sale/#step-8-offer-publication-commands\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.OfferManagementApi(openapi_client.ApiClient(configuration))
command_id = 'command_id_example' # str | commandId
limit = 56 # int | limit (optional)
offset = 56 # int | offset (optional)

try:
    # Publish command detailed report
    api_response = api_instance.get_publication_tasks_using_get(command_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferManagementApi->get_publication_tasks_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| commandId | 
 **limit** | **int**| limit | [optional] 
 **offset** | **int**| offset | [optional] 

### Return type

[**TaskReport**](TaskReport.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_offer_using_put**
> Offer update_offer_using_put(offer_id, offer)

Complete a draft offer or edit an offer

Use this resource to complete a draft offer or edit ongoing offers. More information about this resource you can find <a href=\"../../sale/#step-7-complete\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.OfferManagementApi(openapi_client.ApiClient(configuration))
offer_id = 'offer_id_example' # str | offerId
offer = openapi_client.Offer() # Offer | offer

try:
    # Complete a draft offer or edit an offer
    api_response = api_instance.update_offer_using_put(offer_id, offer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferManagementApi->update_offer_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| offerId | 
 **offer** | [**Offer**](Offer.md)| offer | 

### Return type

[**Offer**](Offer.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

