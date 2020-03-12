# allegro_api.BadgeCampaignsApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**badge_applications_get_all**](BadgeCampaignsApi.md#badge_applications_get_all) | **GET** /sale/badge-applications | [BETA] Get a list of badge applications
[**badge_applications_get_one**](BadgeCampaignsApi.md#badge_applications_get_one) | **GET** /sale/badge-applications/{applicationId} | [BETA] Get a badge application details
[**badge_campaigns_get_all**](BadgeCampaignsApi.md#badge_campaigns_get_all) | **GET** /sale/badge-campaigns | [BETA] Get a list of available badge campaigns
[**get_badges**](BadgeCampaignsApi.md#get_badges) | **GET** /sale/badges | [BETA] Get a list of badges
[**post_badges**](BadgeCampaignsApi.md#post_badges) | **POST** /sale/badges | [BETA] Apply for badge in selected offer


# **badge_applications_get_all**
> BadgeApplications badge_applications_get_all(campaign_id=campaign_id, offer_id=offer_id, offset=offset, limit=limit)

[BETA] Get a list of badge applications

Use this resource to get a list of badge applications. <a href=\"/badge/#4\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.BadgeCampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Campaign ID. (optional)
offer_id = 'offer_id_example' # str | Offer ID. (optional)
offset = 56 # int | Offset. (optional)
limit = 50 # int | The maximum number of applications returned in the response. (optional) (default to 50)

    try:
        # [BETA] Get a list of badge applications
        api_response = api_instance.badge_applications_get_all(campaign_id=campaign_id, offer_id=offer_id, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BadgeCampaignsApi->badge_applications_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Campaign ID. | [optional] 
 **offer_id** | **str**| Offer ID. | [optional] 
 **offset** | **int**| Offset. | [optional] 
 **limit** | **int**| The maximum number of applications returned in the response. | [optional] [default to 50]

### Return type

[**BadgeApplications**](BadgeApplications.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned badge applications list. |  -  |
**400** | Invalid values supplied in the query parameters. |  -  |
**401** | Unauthorized. |  -  |
**403** | Account is not a Company account type. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **badge_applications_get_one**
> BadgeApplication badge_applications_get_one(application_id)

[BETA] Get a badge application details

Use this resource to get a badge application details. <a href=\"/badge/#3\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.BadgeCampaignsApi(api_client)
    application_id = 'application_id_example' # str | Badge application ID.

    try:
        # [BETA] Get a badge application details
        api_response = api_instance.badge_applications_get_one(application_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BadgeCampaignsApi->badge_applications_get_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Badge application ID. | 

### Return type

[**BadgeApplication**](BadgeApplication.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned badge application. |  -  |
**401** | Unauthorized. |  -  |
**403** | Account is not a Company account type. |  -  |
**404** | Badge application not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **badge_campaigns_get_all**
> GetBadgeCampaignsList badge_campaigns_get_all()

[BETA] Get a list of available badge campaigns

Badge campaigns are another way to promote your offers. You can apply for a badge, which - depending on a type - will be displayed on your offer page of on the list of offers. First - use this resource to get a list of all available badge campaigns at the moment, then use *POST /sale/badges* to apply for badge. <a href=\"/badge/#1\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.BadgeCampaignsApi(api_client)
    
    try:
        # [BETA] Get a list of available badge campaigns
        api_response = api_instance.badge_campaigns_get_all()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BadgeCampaignsApi->badge_campaigns_get_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBadgeCampaignsList**](GetBadgeCampaignsList.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available badge campaigns. |  -  |
**401** | Unauthorized. |  -  |
**403** | Account is not a Company account type. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_badges**
> BadgesList get_badges(offer_id=offer_id, offset=offset, limit=limit)

[BETA] Get a list of badges

Use this resource to get a list of badges in authorized seller's offers. <a href=\"/badge/#5\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.BadgeCampaignsApi(api_client)
    offer_id = 'offer_id_example' # str | Offer ID. (optional)
offset = 56 # int | Offset. (optional)
limit = 50 # int | The maximum number of badges returned in the response. (optional) (default to 50)

    try:
        # [BETA] Get a list of badges
        api_response = api_instance.get_badges(offer_id=offer_id, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BadgeCampaignsApi->get_badges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Offer ID. | [optional] 
 **offset** | **int**| Offset. | [optional] 
 **limit** | **int**| The maximum number of badges returned in the response. | [optional] [default to 50]

### Return type

[**BadgesList**](BadgesList.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.beta.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned list of badges. |  -  |
**400** | Invalid values supplied in the query parameters. |  -  |
**401** | Unauthorized. |  -  |
**403** | Account is not a Company account type. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_badges**
> BadgeApplication post_badges(badge_application_request=badge_application_request)

[BETA] Apply for badge in selected offer

This resource allows you to apply for a badge. Most badges involve additional fee charged. Your badge application will be verified and you will be notified about the verification status via e-mail. You can use *Location* provided in header of the response to track your application status. Application will be removed after 30 days when status of the application was changed form PROCESSED or DECLINED. Fees will be charged in accordance with Annex No. 1 to the   <a href=\"https://allegro.pl/regulaminy/regulamin-strefy-okazji-9dGVAPB69In\"     target=\"_blank\">Daily deals zone terms and conditions</a>.  By using this resource you agree to the   <a href=\"https://allegro.pl/regulaminy/regulamin-strefy-okazji-9dGVAPB69In\"     target=\"_blank\">Daily deals zone terms and conditions</a> or   <a href=\"https://allegro.pl/regulaminy/regulamin-programu-bonusowego-prowizja-nawet-0-5-0KPkAE7wkcv\"     target=\"_blank\">Commission discount terms and conditions</a>. <a href=\"/badge/#2\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.BadgeCampaignsApi(api_client)
    badge_application_request = {"campaign":{"id":"BARGAIN"},"offer":{"id":"12345678"},"prices":{"market":{"amount":"19.99","currency":"PLN"},"bargain":{"amount":"9.99","currency":"PLN"}}} # BadgeApplicationRequest |  (optional)

    try:
        # [BETA] Apply for badge in selected offer
        api_response = api_instance.post_badges(badge_application_request=badge_application_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BadgeCampaignsApi->post_badges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **badge_application_request** | [**BadgeApplicationRequest**](BadgeApplicationRequest.md)|  | [optional] 

### Return type

[**BadgeApplication**](BadgeApplication.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.beta.v1+json
 - **Accept**: application/vnd.allegro.beta.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successfully applied for a badge. |  -  |
**400** | Syntactically incorrect request. |  -  |
**401** | Unauthorized |  -  |
**403** | Account is not a Company account type. |  -  |
**422** | Validation error. Invalid parameters provided in the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

