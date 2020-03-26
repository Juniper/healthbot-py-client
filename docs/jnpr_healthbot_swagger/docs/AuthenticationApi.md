# swagger_client.AuthenticationApi

All URIs are relative to *http://api-server/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**refresh_token**](AuthenticationApi.md#refresh_token) | **POST** /token/ | Re-issue tokens from existing token
[**user_login**](AuthenticationApi.md#user_login) | **POST** /login/ | User login
[**user_logout**](AuthenticationApi.md#user_logout) | **POST** /logout/ | User logout


# **refresh_token**
> InlineResponse2006 refresh_token(token)

Re-issue tokens from existing token

Re-issue tokens from existing token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
token = swagger_client.Token() # Token | Token object

try:
    # Re-issue tokens from existing token
    api_response = api_instance.refresh_token(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | [**Token**](Token.md)| Token object | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_login**
> InlineResponse2006 user_login(credential)

User login

User login and recive tokens

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
credential = swagger_client.Credential() # Credential | topics body object

try:
    # User login
    api_response = api_instance.user_login(credential)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->user_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential** | [**Credential**](Credential.md)| topics body object | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_logout**
> user_logout(refresh_token)

User logout

User logout

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
refresh_token = swagger_client.RefreshToken() # RefreshToken | request body object

try:
    # User logout
    api_instance.user_logout(refresh_token)
except ApiException as e:
    print("Exception when calling AuthenticationApi->user_logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token** | [**RefreshToken**](RefreshToken.md)| request body object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

