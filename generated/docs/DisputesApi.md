# allegro_api.DisputesApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_message_to_dispute_using_post**](DisputesApi.md#add_message_to_dispute_using_post) | **POST** /sale/disputes/{disputeId}/messages | Add a message to a dispute
[**create_an_attachment_using_post**](DisputesApi.md#create_an_attachment_using_post) | **POST** /sale/dispute-attachments | Create an attachment declaration
[**get_attachment_using_get**](DisputesApi.md#get_attachment_using_get) | **GET** /sale/dispute-attachments/{attachmentId} | Get an attachment
[**get_dispute_using_get**](DisputesApi.md#get_dispute_using_get) | **GET** /sale/disputes/{disputeId} | Get a single dispute
[**get_list_of_disputes_using_get**](DisputesApi.md#get_list_of_disputes_using_get) | **GET** /sale/disputes | Get the user&#39;s disputes
[**get_messages_from_dispute_using_get**](DisputesApi.md#get_messages_from_dispute_using_get) | **GET** /sale/disputes/{disputeId}/messages | Get the messages within a dispute
[**upload_dispute_attachment_using_put**](DisputesApi.md#upload_dispute_attachment_using_put) | **PUT** /sale/dispute-attachments/{attachmentId} | Upload a dispute message attachment


# **add_message_to_dispute_using_post**
> DisputeMessage add_message_to_dispute_using_post(dispute_id, message_request)

Add a message to a dispute

Use this resource to post a message in certain dispute. At least one of fields: 'text', 'attachment' has to be present. <a href=\"../../news/2018-09-18-dyskusje/#PostMessage\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.DisputesApi(api_client)
    dispute_id = 'dispute_id_example' # str | Dispute identifier.
message_request = allegro_api.MessageRequest() # MessageRequest | Message request

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
 **dispute_id** | [**str**](.md)| Dispute identifier. | 
 **message_request** | [**MessageRequest**](MessageRequest.md)| Message request | 

### Return type

[**DisputeMessage**](DisputeMessage.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_an_attachment_using_post**
> DisputeAttachmentId create_an_attachment_using_post(attachment_declaration)

Create an attachment declaration

Use this resource to post an attachment declaration. <a href=\"../../news/2018-09-18-dyskusje/#PostAttach\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.DisputesApi(api_client)
    attachment_declaration = allegro_api.AttachmentDeclaration() # AttachmentDeclaration | A detailed declaration of a file to be uploaded

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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  * Location - Use this URL to perform PUT request with binary data file coherent with the attachment declaration. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_using_get**
> file get_attachment_using_get(attachment_id)

Get an attachment

Use this resource to get an attachment. <a href=\"../../news/2018-09-18-dyskusje/#GetAttach\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.DisputesApi(api_client)
    attachment_id = 'attachment_id_example' # str | Attachment identifier.

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
 **attachment_id** | [**str**](.md)| Attachment identifier. | 

### Return type

**file**

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dispute_using_get**
> Dispute get_dispute_using_get(dispute_id)

Get a single dispute

Use this resource to get a single dispute. <a href=\"../../news/2018-09-18-dyskusje/#GetOne\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.DisputesApi(api_client)
    dispute_id = 'dispute_id_example' # str | Dispute identifier.

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
 **dispute_id** | [**str**](.md)| Dispute identifier. | 

### Return type

[**Dispute**](Dispute.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_disputes_using_get**
> DisputeListResponse get_list_of_disputes_using_get(checkout_form_id=checkout_form_id, limit=limit, offset=offset)

Get the user's disputes

Use this resource to get the list of your disputes. <a href=\"../../news/2018-09-18-dyskusje/#GetAll\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.DisputesApi(api_client)
    checkout_form_id = '29738e61-7f6a-11e8-ac45-09db60ede9d6' # str | Checkout form identifier. (optional)
limit = 10 # int | The maximum number of disputes in a response. (optional) (default to 10)
offset = 0 # int | Index of first returned dispute. (optional) (default to 0)

    try:
        # Get the user's disputes
        api_response = api_instance.get_list_of_disputes_using_get(checkout_form_id=checkout_form_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DisputesApi->get_list_of_disputes_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_form_id** | [**str**](.md)| Checkout form identifier. | [optional] 
 **limit** | **int**| The maximum number of disputes in a response. | [optional] [default to 10]
 **offset** | **int**| Index of first returned dispute. | [optional] [default to 0]

### Return type

[**DisputeListResponse**](DisputeListResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages_from_dispute_using_get**
> DisputeMessageList get_messages_from_dispute_using_get(dispute_id, limit=limit, offset=offset)

Get the messages within a dispute

Use this resource to get the list of messages within dispute. <a href=\"../../news/2018-09-18-dyskusje/#GetMessage\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.DisputesApi(api_client)
    dispute_id = 'dispute_id_example' # str | Dispute identifier.
limit = 10 # int | The maximum number of messages within dispute returned in a response. (optional) (default to 10)
offset = 0 # int | Index of first returned message within dispute. (optional) (default to 0)

    try:
        # Get the messages within a dispute
        api_response = api_instance.get_messages_from_dispute_using_get(dispute_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DisputesApi->get_messages_from_dispute_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispute_id** | [**str**](.md)| Dispute identifier. | 
 **limit** | **int**| The maximum number of messages within dispute returned in a response. | [optional] [default to 10]
 **offset** | **int**| Index of first returned message within dispute. | [optional] [default to 0]

### Return type

[**DisputeMessageList**](DisputeMessageList.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_dispute_attachment_using_put**
> upload_dispute_attachment_using_put(attachment_id, body)

Upload a dispute message attachment

Upload a dispute message attachment. This operation should be used after creating an attachment declaration with *POST /sale/dispute-attachments* **Important!** You can find the URL address to upload the file to our server in the *Location* response header of *POST /sale/dispute-attachments*. The URL is unique and one-time. As its format may change in time, you should always use the address from the header. Do not compose the address on your own.

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
    api_instance = allegro_api.DisputesApi(api_client)
    attachment_id = 'attachment_id_example' # str | Attachment identifier.
body = '/path/to/file' # file | 

    try:
        # Upload a dispute message attachment
        api_instance.upload_dispute_attachment_using_put(attachment_id, body)
    except ApiException as e:
        print("Exception when calling DisputesApi->upload_dispute_attachment_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | [**str**](.md)| Attachment identifier. | 
 **body** | **file**|  | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: image/png, image/gif, image/bmp, image/tiff, image/jpeg, application/pdf
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | File uploaded correctly |  -  |
**400** | Syntactically incorrect request |  -  |
**401** | Invalid or missing bearer token |  -  |
**413** | File is too big |  -  |
**415** | Unsupported media type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

