# allegro_api.ImagesAndAttachmentsApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_offer_attachment_using_post**](ImagesAndAttachmentsApi.md#create_offer_attachment_using_post) | **POST** /sale/offer-attachments | Create an offer attachment
[**upload_offer_attachment_using_put**](ImagesAndAttachmentsApi.md#upload_offer_attachment_using_put) | **PUT** /sale/offer-attachments/{attachmentId} | Upload an offer attachment
[**upload_offer_image_using_post**](ImagesAndAttachmentsApi.md#upload_offer_image_using_post) | **POST** /sale/images | Upload an offer image


# **create_offer_attachment_using_post**
> OfferAttachment create_offer_attachment_using_post(offer_attachment_request)

Create an offer attachment

You can attach PDF files to your offers. We will present them under the offer description in the Additional information section. You can attach up to 7 files to one offer – one per each type from the list:   * \\- Guide (MANUAL)   * \\- Special offer terms (SPECIAL_OFFER_RULES)   * \\- Competition terms (COMPETITION_RULES)   * \\- Book excerpt (BOOK_EXCERPT)   * \\- Manual (USER_MANUAL)   * \\- Installation manual (INSTALLATION_INSTRUCTIONS)   * \\- Game manual (GAME_INSTRUCTIONS)  Uploading attachments flow:   1. Create an attachment object to receive an upload URL (*POST /sale/offer-attachments*),   2. Use the upload URL to submit the PDF file (*PUT /sale/offer-attachments/{attachmentId}*),   3. Add attachments to the offer (*PUT /sale/offers/{offerId}*).

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
    api_instance = allegro_api.ImagesAndAttachmentsApi(api_client)
    offer_attachment_request = allegro_api.OfferAttachmentRequest() # OfferAttachmentRequest | offer attachment

    try:
        # Create an offer attachment
        api_response = api_instance.create_offer_attachment_using_post(offer_attachment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImagesAndAttachmentsApi->create_offer_attachment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_attachment_request** | [**OfferAttachmentRequest**](OfferAttachmentRequest.md)| offer attachment | 

### Return type

[**OfferAttachment**](OfferAttachment.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Attachment created successfully |  -  |
**400** | Syntactically incorrect request |  -  |
**401** | Invalid or missing bearer token |  -  |
**415** | Unsupported media type |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_offer_attachment_using_put**
> upload_offer_attachment_using_put(attachment_id, body=body)

Upload an offer attachment

Upload an offer attachment. This operation should be used after creating an offer attachment with *POST /sale/offer-attachments* **Important!** You can find the URL address to upload the file to our server in the *Location* response header of *POST /sale/offer-attachments*. The URL is unique and one-time. As its format may change in time, you should always use the address from the header. Do not compose the address on your own.

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
    api_instance = allegro_api.ImagesAndAttachmentsApi(api_client)
    attachment_id = 'attachment_id_example' # str | The ID of the attachment.
body = '/path/to/file' # file |  (optional)

    try:
        # Upload an offer attachment
        api_instance.upload_offer_attachment_using_put(attachment_id, body=body)
    except ApiException as e:
        print("Exception when calling ImagesAndAttachmentsApi->upload_offer_attachment_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | [**str**](.md)| The ID of the attachment. | 
 **body** | **file**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/pdf
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File uploaded correctly |  -  |
**400** | Syntactically incorrect request |  -  |
**401** | Invalid or missing bearer token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_offer_image_using_post**
> OfferImageUploadResponse upload_offer_image_using_post(offer_image_link_upload_request)

Upload an offer image

Upload image to our servers. You can choose from two upload options:   * \\- provide a link and we will download an image for you   * \\- send an image as binary data  **Important!** Remember to use dedicated domain for upload, i.e.   * \\- https://upload.allegro.pl for Production   * \\- https://upload.allegro.pl.allegrosandbox.pl for Sandbox  More information about rules for photos in an offer's gallery and description you will find <a href=\"https://allegro.pl/dla-sprzedajacych/nowe-zasady-dla-zdjec-w-galerii-i-w-opisie-YLlAAa2oXf7\" target=\"_blank\">here</a>.

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
    api_instance = allegro_api.ImagesAndAttachmentsApi(api_client)
    offer_image_link_upload_request = allegro_api.OfferImageLinkUploadRequest() # OfferImageLinkUploadRequest | 

    try:
        # Upload an offer image
        api_response = api_instance.upload_offer_image_using_post(offer_image_link_upload_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImagesAndAttachmentsApi->upload_offer_image_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_image_link_upload_request** | [**OfferImageLinkUploadRequest**](OfferImageLinkUploadRequest.md)|  | 

### Return type

[**OfferImageUploadResponse**](OfferImageUploadResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json, image/jpeg, image/png
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Image uploaded correctly |  -  |
**400** | Syntactically incorrect request |  -  |
**401** | Invalid or missing bearer token |  -  |
**413** | Image is too big |  -  |
**415** | Unsupported media type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

