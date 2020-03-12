# allegro_api.InformationAboutUserApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_additional_email_using_post**](InformationAboutUserApi.md#add_additional_email_using_post) | **POST** /account/additional-emails | Add a new additional email address to user&#39;s account
[**answer_user_rating_using_put**](InformationAboutUserApi.md#answer_user_rating_using_put) | **PUT** /sale/user-ratings/{ratingId}/answer | Answer for user&#39;s rating
[**delete_additional_email_using_delete**](InformationAboutUserApi.md#delete_additional_email_using_delete) | **DELETE** /account/additional-emails/{emailId} | Delete an additional email address
[**get_additional_email_using_get**](InformationAboutUserApi.md#get_additional_email_using_get) | **GET** /account/additional-emails/{emailId} | Get information about a particular additional email
[**get_list_of_additional_emails_using_get**](InformationAboutUserApi.md#get_list_of_additional_emails_using_get) | **GET** /account/additional-emails | Get user&#39;s additional emails
[**get_user_ratings_using_get**](InformationAboutUserApi.md#get_user_ratings_using_get) | **GET** /sale/user-ratings | Get the user&#39;s ratings
[**me_get**](InformationAboutUserApi.md#me_get) | **GET** /me | Get basic information about user
[**user_rating_removal_using_put**](InformationAboutUserApi.md#user_rating_removal_using_put) | **PUT** /sale/user-ratings/{ratingId}/removal | Request removal of user&#39;s rating


# **add_additional_email_using_post**
> AdditionalEmail add_additional_email_using_post(additional_email_request)

Add a new additional email address to user's account

Use this resource to add a new additional email address to account.

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
    api_instance = allegro_api.InformationAboutUserApi(api_client)
    additional_email_request = allegro_api.AdditionalEmailRequest() # AdditionalEmailRequest | request

    try:
        # Add a new additional email address to user's account
        api_response = api_instance.add_additional_email_using_post(additional_email_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InformationAboutUserApi->add_additional_email_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **additional_email_request** | [**AdditionalEmailRequest**](AdditionalEmailRequest.md)| request | 

### Return type

[**AdditionalEmail**](AdditionalEmail.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Additional email added successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**422** | Email address provided in the request is not valid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **answer_user_rating_using_put**
> Answer answer_user_rating_using_put(rating_id, user_rating_answer_request)

Answer for user's rating

Use this resource to answer for received rating.

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
    api_instance = allegro_api.InformationAboutUserApi(api_client)
    rating_id = '5df0a6d1ef437e00255572a1' # str | ID of the rating.
user_rating_answer_request = allegro_api.UserRatingAnswerRequest() # UserRatingAnswerRequest | User rating answer request.

    try:
        # Answer for user's rating
        api_response = api_instance.answer_user_rating_using_put(rating_id, user_rating_answer_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InformationAboutUserApi->answer_user_rating_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rating_id** | **str**| ID of the rating. | 
 **user_rating_answer_request** | [**UserRatingAnswerRequest**](UserRatingAnswerRequest.md)| User rating answer request. | 

### Return type

[**Answer**](Answer.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_additional_email_using_delete**
> delete_additional_email_using_delete(email_id)

Delete an additional email address

Use this resource to delete one of additional emails.

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
    api_instance = allegro_api.InformationAboutUserApi(api_client)
    email_id = 'email_id_example' # str | Id of the additional email to be deleted.

    try:
        # Delete an additional email address
        api_instance.delete_additional_email_using_delete(email_id)
    except ApiException as e:
        print("Exception when calling InformationAboutUserApi->delete_additional_email_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **str**| Id of the additional email to be deleted. | 

### Return type

void (empty response body)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted additional email |  -  |
**401** | Unauthorized |  -  |
**404** | Additional email not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_additional_email_using_get**
> AdditionalEmail get_additional_email_using_get(email_id)

Get information about a particular additional email

Use this resource to retrieve a single additional email.

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
    api_instance = allegro_api.InformationAboutUserApi(api_client)
    email_id = 'email_id_example' # str | Id of the additional email.

    try:
        # Get information about a particular additional email
        api_response = api_instance.get_additional_email_using_get(email_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InformationAboutUserApi->get_additional_email_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **str**| Id of the additional email. | 

### Return type

[**AdditionalEmail**](AdditionalEmail.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Additional email returned successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Additional email not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_additional_emails_using_get**
> AdditionalEmailsResponse get_list_of_additional_emails_using_get()

Get user's additional emails

Use this resource to get a list of all additional email addresses assigned to account.

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
    api_instance = allegro_api.InformationAboutUserApi(api_client)
    
    try:
        # Get user's additional emails
        api_response = api_instance.get_list_of_additional_emails_using_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InformationAboutUserApi->get_list_of_additional_emails_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdditionalEmailsResponse**](AdditionalEmailsResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of user&#39;s additional emails returned successfully |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_ratings_using_get**
> UserRatingListResponse get_user_ratings_using_get(user_id, recommended=recommended, offset=offset, limit=limit)

Get the user's ratings

Use this resource to receive your sales score. <a href=\"../../news/2017-10-09-news_informacje_o_ocenach/\" target=\"_blank\">Read more</a>.

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
    api_instance = allegro_api.InformationAboutUserApi(api_client)
    user_id = 'user_id_example' # str | Filter by user id, you are allowed to get your ratings only.
recommended = 'recommended_example' # str | Filter by recommended. (optional)
offset = 0 # int | The offset of elements in the response. (optional) (default to 0)
limit = 20 # int | The limit of elements in the response. (optional) (default to 20)

    try:
        # Get the user's ratings
        api_response = api_instance.get_user_ratings_using_get(user_id, recommended=recommended, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InformationAboutUserApi->get_user_ratings_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Filter by user id, you are allowed to get your ratings only. | 
 **recommended** | **str**| Filter by recommended. | [optional] 
 **offset** | **int**| The offset of elements in the response. | [optional] [default to 0]
 **limit** | **int**| The limit of elements in the response. | [optional] [default to 20]

### Return type

[**UserRatingListResponse**](UserRatingListResponse.md)

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

# **me_get**
> MeResponse me_get()

Get basic information about user

Use this resource when you need basic information about authenticated user.

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
    api_instance = allegro_api.InformationAboutUserApi(api_client)
    
    try:
        # Get basic information about user
        api_response = api_instance.me_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InformationAboutUserApi->me_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MeResponse**](MeResponse.md)

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
**403** | Forbidden - when token is without user context |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_rating_removal_using_put**
> Removal user_rating_removal_using_put(rating_id, user_rating_removal_request)

Request removal of user's rating

Use this resource to request removal of received rating.

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
    api_instance = allegro_api.InformationAboutUserApi(api_client)
    rating_id = '5df0a6d1ef437e00255572a1' # str | ID of the rating.
user_rating_removal_request = allegro_api.UserRatingRemovalRequest() # UserRatingRemovalRequest | User rating removal request.

    try:
        # Request removal of user's rating
        api_response = api_instance.user_rating_removal_using_put(rating_id, user_rating_removal_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InformationAboutUserApi->user_rating_removal_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rating_id** | **str**| ID of the rating. | 
 **user_rating_removal_request** | [**UserRatingRemovalRequest**](UserRatingRemovalRequest.md)| User rating removal request. | 

### Return type

[**Removal**](Removal.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

