# swagger_client.SystemApi

All URIs are relative to *http://api-server/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_system_details**](SystemApi.md#retrieve_system_details) | **GET** /system-details/ | Retrieve system details.


# **retrieve_system_details**
> retrieve_system_details()

Retrieve system details.

Retrieve system details for HealthBot system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try:
    # Retrieve system details.
    api_instance.retrieve_system_details()
except ApiException as e:
    print("Exception when calling SystemApi->retrieve_system_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

