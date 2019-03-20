# allegro_api.ImagesAndAttachmentsApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_offer_attachment_using_post**](ImagesAndAttachmentsApi.md#create_offer_attachment_using_post) | **POST** /sale/offer-attachments | Create an offer attachment


# **create_offer_attachment_using_post**
> OfferAttachment create_offer_attachment_using_post(offer_attachment_request)

Create an offer attachment

Creates attachment and returns location header for file upload

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
api_instance = allegro_api.ImagesAndAttachmentsApi(allegro_api.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

