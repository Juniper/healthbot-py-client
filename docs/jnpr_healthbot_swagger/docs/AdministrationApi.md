# swagger_client.AdministrationApi

All URIs are relative to *http://api-server/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthbot_alter_app_settings**](AdministrationApi.md#healthbot_alter_app_settings) | **POST** /config/app-settings/ | Change runtime app-settings


# **healthbot_alter_app_settings**
> healthbot_alter_app_settings(x_iam_token=x_iam_token, app_settings=app_settings)

Change runtime app-settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
app_settings = NULL # object | Maintenance endpoint to change app-settings. Not accessible externally. (optional)

try:
    # Change runtime app-settings
    api_instance.healthbot_alter_app_settings(x_iam_token=x_iam_token, app_settings=app_settings)
except ApiException as e:
    print("Exception when calling AdministrationApi->healthbot_alter_app_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **app_settings** | **object**| Maintenance endpoint to change app-settings. Not accessible externally. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

