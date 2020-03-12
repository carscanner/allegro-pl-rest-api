# allegro_api.PromotionCampaignsApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_promotion_to_campaign_using_post**](PromotionCampaignsApi.md#add_promotion_to_campaign_using_post) | **POST** /sale/loyalty/promotion-campaigns | Create an application for a promotion campaign
[**delete_campaign_from_promotion_using_delete**](PromotionCampaignsApi.md#delete_campaign_from_promotion_using_delete) | **DELETE** /sale/loyalty/promotion-campaigns | Delete a campaign in a promotion
[**delete_promotion_campaign_application_using_delete**](PromotionCampaignsApi.md#delete_promotion_campaign_application_using_delete) | **DELETE** /sale/loyalty/promotion-campaign-applications/{applicationId} | Delete an application for promotion campaign
[**get_promotion_campaign_application_using_get**](PromotionCampaignsApi.md#get_promotion_campaign_application_using_get) | **GET** /sale/loyalty/promotion-campaign-applications/{applicationId} | Get an application for promotion campaign
[**get_promotion_campaigns_using_get**](PromotionCampaignsApi.md#get_promotion_campaigns_using_get) | **GET** /sale/loyalty/promotion-campaigns | Get the user&#39;s promotion campaigns


# **add_promotion_to_campaign_using_post**
> PromotionCampaignResponseDto add_promotion_to_campaign_using_post(promotion_campaign_request_dto)

Create an application for a promotion campaign

For an additional fee, you can place a discount mark on a list of offers.         You have to define promotion id and campaign section giving LISTING_BADGE as the id.         Your promotion campaign application will be verified and you will be notified about the verification status via e-mail.         Fees will be charged in accordance with Annex No. 1 to the Daily deals zone regulations.         <a href=\"../../offer_bundles/#11\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.PromotionCampaignsApi(api_client)
    promotion_campaign_request_dto = allegro_api.PromotionCampaignRequestDto() # PromotionCampaignRequestDto | request

    try:
        # Create an application for a promotion campaign
        api_response = api_instance.add_promotion_to_campaign_using_post(promotion_campaign_request_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PromotionCampaignsApi->add_promotion_to_campaign_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_campaign_request_dto** | [**PromotionCampaignRequestDto**](PromotionCampaignRequestDto.md)| request | 

### Return type

[**PromotionCampaignResponseDto**](PromotionCampaignResponseDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Promotion campaign application created successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed - your request was correct, but the promotion campaign application could not be created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign_from_promotion_using_delete**
> delete_campaign_from_promotion_using_delete(promotion_id, campaign_id)

Delete a campaign in a promotion

Use this resource to delete campaign from promotion by promotion id and campaign id. <a href=\"../../offer_bundles/#16\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.PromotionCampaignsApi(api_client)
    promotion_id = 'promotion_id_example' # str | The promotion unique id.
campaign_id = 'campaign_id_example' # str | The campaign unique id.

    try:
        # Delete a campaign in a promotion
        api_instance.delete_campaign_from_promotion_using_delete(promotion_id, campaign_id)
    except ApiException as e:
        print("Exception when calling PromotionCampaignsApi->delete_campaign_from_promotion_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_id** | **str**| The promotion unique id. | 
 **campaign_id** | **str**| The campaign unique id. | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Campaign deletion requested successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Promotion not found |  -  |
**422** | Campaign cannot be deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_promotion_campaign_application_using_delete**
> delete_promotion_campaign_application_using_delete(application_id)

Delete an application for promotion campaign

Use this resource to delete promotion campaign application by application id. You need to use its unique id. <a href=\"../../offer_bundles/#15\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.PromotionCampaignsApi(api_client)
    application_id = 'application_id_example' # str | The application unique id.

    try:
        # Delete an application for promotion campaign
        api_instance.delete_promotion_campaign_application_using_delete(application_id)
    except ApiException as e:
        print("Exception when calling PromotionCampaignsApi->delete_promotion_campaign_application_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The application unique id. | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Promotion campaign application deletion requested successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Promotion campaign application not found |  -  |
**422** | Promotion campaign application cannot be deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_promotion_campaign_application_using_get**
> object get_promotion_campaign_application_using_get(application_id)

Get an application for promotion campaign

Use this resource to retrieve promotion campaign application. You need to use its unique id. <a href=\"../../offer_bundles/#12\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.PromotionCampaignsApi(api_client)
    application_id = 'application_id_example' # str | The application unique id.

    try:
        # Get an application for promotion campaign
        api_response = api_instance.get_promotion_campaign_application_using_get(application_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PromotionCampaignsApi->get_promotion_campaign_application_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The application unique id. | 

### Return type

**object**

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned promotion campaign application |  -  |
**303** | Promotion campaign application verified and accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Promotion campaign application not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_promotion_campaigns_using_get**
> PromotionCampaignsResponseDto get_promotion_campaigns_using_get(promotion_id=promotion_id, limit=limit, offset=offset)

Get the user's promotion campaigns

Use this resource to retrieve promotion campaigns. You can find promotion campaign by promotion id. <a href=\"../../offer_bundles/#13\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.PromotionCampaignsApi(api_client)
    promotion_id = 'promotion_id_example' # str | The promotion unique id. (optional)
limit = 50 # int | The limit of elements in the response. (optional) (default to 50)
offset = 0 # int | The offset of elements in the response. (optional) (default to 0)

    try:
        # Get the user's promotion campaigns
        api_response = api_instance.get_promotion_campaigns_using_get(promotion_id=promotion_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PromotionCampaignsApi->get_promotion_campaigns_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_id** | **str**| The promotion unique id. | [optional] 
 **limit** | **int**| The limit of elements in the response. | [optional] [default to 50]
 **offset** | **int**| The offset of elements in the response. | [optional] [default to 0]

### Return type

[**PromotionCampaignsResponseDto**](PromotionCampaignsResponseDto.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Active or suspended promotion campaigns returned successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Promotion campaign not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

