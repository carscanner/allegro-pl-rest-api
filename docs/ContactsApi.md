# allegro_api.ContactsApi

All URIs are relative to *https://api.allegro.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact_using_post**](ContactsApi.md#create_contact_using_post) | **POST** /sale/offer-contacts | Create a new contact
[**get_contact_using_get**](ContactsApi.md#get_contact_using_get) | **GET** /sale/offer-contacts/{id} | Get contact details
[**get_list_of_contacts_using_get**](ContactsApi.md#get_list_of_contacts_using_get) | **GET** /sale/offer-contacts | Get the user&#39;s contacts
[**modify_contact_using_put**](ContactsApi.md#modify_contact_using_put) | **PUT** /sale/offer-contacts/{id} | Modify contact details


# **create_contact_using_post**
> ContactResponse create_contact_using_post(contact_request)

Create a new contact

Use this resource to create a new contact. More information about this resource you can find <a href=\"../../news/2018-01-17-news_zarzadzanie_kontaktami/#1\" target=\"_blank\">here</a>.

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
api_instance = allegro_api.ContactsApi(allegro_api.ApiClient(configuration))
contact_request = allegro_api.ContactRequest() # ContactRequest | New contact

try:
    # Create a new contact
    api_response = api_instance.create_contact_using_post(contact_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->create_contact_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_request** | [**ContactRequest**](ContactRequest.md)| New contact | 

### Return type

[**ContactResponse**](ContactResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_using_get**
> ContactResponse get_contact_using_get(id)

Get contact details

Use this resource to get contact details. More information about this resource you can find <a href=\"../../news/2018-01-17-news_zarzadzanie_kontaktami/#3\" target=\"_blank\">here</a>.

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
api_instance = allegro_api.ContactsApi(allegro_api.ApiClient(configuration))
id = 'id_example' # str | Contact id

try:
    # Get contact details
    api_response = api_instance.get_contact_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_contact_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Contact id | 

### Return type

[**ContactResponse**](ContactResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_contacts_using_get**
> ContactResponseList get_list_of_contacts_using_get(seller_id)

Get the user's contacts

Use this resource to get details of many contacts. More information about this resource you can find <a href=\"../../news/2018-01-17-news_zarzadzanie_kontaktami/#4\" target=\"_blank\">here</a>.

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
api_instance = allegro_api.ContactsApi(allegro_api.ApiClient(configuration))
seller_id = 'seller_id_example' # str | id of contacts owner

try:
    # Get the user's contacts
    api_response = api_instance.get_list_of_contacts_using_get(seller_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_list_of_contacts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| id of contacts owner | 

### Return type

[**ContactResponseList**](ContactResponseList.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_contact_using_put**
> ContactResponse modify_contact_using_put(id, contact_request)

Modify contact details

Use this resource to modify contact details. More information about this resource you can find <a href=\"../../news/2018-01-17-news_zarzadzanie_kontaktami/#2\" target=\"_blank\">here</a>.

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
api_instance = allegro_api.ContactsApi(allegro_api.ApiClient(configuration))
id = 'id_example' # str | Contact id
contact_request = allegro_api.ContactRequest() # ContactRequest | Contact

try:
    # Modify contact details
    api_response = api_instance.modify_contact_using_put(id, contact_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->modify_contact_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Contact id | 
 **contact_request** | [**ContactRequest**](ContactRequest.md)| Contact | 

### Return type

[**ContactResponse**](ContactResponse.md)

### Authorization

[bearer-token-for-user](../README.md#bearer-token-for-user)

### HTTP request headers

 - **Content-Type**: application/vnd.allegro.public.v1+json
 - **Accept**: application/vnd.allegro.public.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

