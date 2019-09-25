# swagger_client.DocumentationApi

All URIs are relative to *http://api-server/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_defined_api**](DocumentationApi.md#retrieve_defined_api) | **GET** / | Get all All API&#39;s.


# **retrieve_defined_api**
> retrieve_defined_api()

Get all All API's.

GET static api documentation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DocumentationApi()

try:
    # Get all All API's.
    api_instance.retrieve_defined_api()
except ApiException as e:
    print("Exception when calling DocumentationApi->retrieve_defined_api: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

