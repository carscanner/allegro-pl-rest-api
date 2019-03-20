# openapi_client.DisputesApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_message_to_dispute_using_post**](DisputesApi.md#add_message_to_dispute_using_post) | **POST** /sale/disputes/{disputeId}/messages | Add a message to a dispute
[**create_an_attachment_using_post**](DisputesApi.md#create_an_attachment_using_post) | **POST** /sale/dispute-attachments | Create an attachment declaration
[**get_attachment_using_get**](DisputesApi.md#get_attachment_using_get) | **GET** /sale/dispute-attachments/{attachmentId} | Get an attachment
[**get_dispute_using_get**](DisputesApi.md#get_dispute_using_get) | **GET** /sale/disputes/{disputeId} | Get a single dispute
[**get_list_of_disputes_using_get**](DisputesApi.md#get_list_of_disputes_using_get) | **GET** /sale/disputes | Get the user&#39;s disputes
[**get_messages_from_dispute_using_get**](DisputesApi.md#get_messages_from_dispute_using_get) | **GET** /sale/disputes/{disputeId}/messages | Get the messages within a dispute


# **add_message_to_dispute_using_post**
> DisputeMessage add_message_to_dispute_using_post(dispute_id, message_request)

Add a message to a dispute

Use this resource to post a message in certain dispute. At least one of fields: 'text', 'attachment' has to be present. More information about this resource you can find <a href=\"../../news/2018-09-18-dyskusje/#PostMessage\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.DisputesApi(openapi_client.ApiClient(configuration))
dispute_id = 'dispute_id_example' # str | Id of the dispute
message_request = openapi_client.MessageRequest() # MessageRequest | Message request

try:
    # Add a message to a dispute
    api_response = api_instance.add_message_to_dispute_using_post(dispute_id, message_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisputesApi->add_message_to_dispute_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispute_id** | [**str**](.md)| Id of the dispute | 
 **message_request** | [**MessageRequest**](MessageRequest.md)| Message request | 

### Return type

[**DisputeMessage**](DisputeMessage.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_an_attachment_using_post**
> DisputeAttachmentId create_an_attachment_using_post(attachment_declaration)

Create an attachment declaration

Use this resource to post an attachment declaration. More information about this resource you can find <a href=\"../../news/2018-09-18-dyskusje/#PostAttach\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.DisputesApi(openapi_client.ApiClient(configuration))
attachment_declaration = openapi_client.AttachmentDeclaration() # AttachmentDeclaration | A detailed declaration of a file to be uploaded

try:
    # Create an attachment declaration
    api_response = api_instance.create_an_attachment_using_post(attachment_declaration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisputesApi->create_an_attachment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_declaration** | [**AttachmentDeclaration**](AttachmentDeclaration.md)| A detailed declaration of a file to be uploaded | 

### Return type

[**DisputeAttachmentId**](DisputeAttachmentId.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_using_get**
> file get_attachment_using_get(attachment_id)

Get an attachment

Use this resource to get an attachment. More information about this resource you can find <a href=\"../../news/2018-09-18-dyskusje/#GetAttach\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.DisputesApi(openapi_client.ApiClient(configuration))
attachment_id = 'attachment_id_example' # str | Id of the attachment resource

try:
    # Get an attachment
    api_response = api_instance.get_attachment_using_get(attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisputesApi->get_attachment_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | [**str**](.md)| Id of the attachment resource | 

### Return type

**file**

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dispute_using_get**
> Dispute get_dispute_using_get(dispute_id)

Get a single dispute

Use this resource to get a single dispute. More information about this resource you can find <a href=\"../../news/2018-09-18-dyskusje/#GetOne\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.DisputesApi(openapi_client.ApiClient(configuration))
dispute_id = 'dispute_id_example' # str | Id of the dispute

try:
    # Get a single dispute
    api_response = api_instance.get_dispute_using_get(dispute_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisputesApi->get_dispute_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispute_id** | [**str**](.md)| Id of the dispute | 

### Return type

[**Dispute**](Dispute.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_disputes_using_get**
> DisputeListResponse get_list_of_disputes_using_get(checkout_form_id=checkout_form_id)

Get the user's disputes

Use this resource to get the list of your disputes. More information about this resource you can find <a href=\"../../news/2018-09-18-dyskusje/#GetAll\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.DisputesApi(openapi_client.ApiClient(configuration))
checkout_form_id = 29738e61-7f6a-11e8-ac45-09db60ede9d6 # str | CheckoutForm id (optional)

try:
    # Get the user's disputes
    api_response = api_instance.get_list_of_disputes_using_get(checkout_form_id=checkout_form_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisputesApi->get_list_of_disputes_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_form_id** | [**str**](.md)| CheckoutForm id | [optional] 

### Return type

[**DisputeListResponse**](DisputeListResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages_from_dispute_using_get**
> DisputeMessageList get_messages_from_dispute_using_get(dispute_id)

Get the messages within a dispute

Use this resource to get the list of messages within dispute. More information about this resource you can find <a href=\"../../news/2018-09-18-dyskusje/#GetMessage\" target=\"_blank\">here</a>.

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
api_instance = openapi_client.DisputesApi(openapi_client.ApiClient(configuration))
dispute_id = 'dispute_id_example' # str | Id of the dispute

try:
    # Get the messages within a dispute
    api_response = api_instance.get_messages_from_dispute_using_get(dispute_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisputesApi->get_messages_from_dispute_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispute_id** | [**str**](.md)| Id of the dispute | 

### Return type

[**DisputeMessageList**](DisputeMessageList.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

