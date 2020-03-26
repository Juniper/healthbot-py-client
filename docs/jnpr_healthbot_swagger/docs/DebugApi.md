# swagger_client.DebugApi

All URIs are relative to *http://api-server/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthbot_debug_generate_configuration**](DebugApi.md#healthbot_debug_generate_configuration) | **POST** /debug/configuration/ | Request Healthbot MGD service to generate the debug related configuration for healthbot debugger to consume.
[**retrieve_debug_for_scenario**](DebugApi.md#retrieve_debug_for_scenario) | **POST** /debug/scenario/{scenario_name}/ | Run debugging for the given scenario name


# **healthbot_debug_generate_configuration**
> healthbot_debug_generate_configuration(authorization=authorization)

Request Healthbot MGD service to generate the debug related configuration for healthbot debugger to consume.

Request Healthbot MGD service to generate the debug related configuration for healthbot debugger to consume.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DebugApi()
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Request Healthbot MGD service to generate the debug related configuration for healthbot debugger to consume.
    api_instance.healthbot_debug_generate_configuration(authorization=authorization)
except ApiException as e:
    print("Exception when calling DebugApi->healthbot_debug_generate_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_debug_for_scenario**
> retrieve_debug_for_scenario(scenario_name, authorization=authorization, debug_arguments=debug_arguments)

Run debugging for the given scenario name

Run debugging for the given scenario name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DebugApi()
scenario_name = 'scenario_name_example' # str | Scenario name
authorization = 'authorization_example' # str | authentication header object (optional)
debug_arguments = swagger_client.DebugArgumentsSchema() # DebugArgumentsSchema | Debug arguments object (optional)

try:
    # Run debugging for the given scenario name
    api_instance.retrieve_debug_for_scenario(scenario_name, authorization=authorization, debug_arguments=debug_arguments)
except ApiException as e:
    print("Exception when calling DebugApi->retrieve_debug_for_scenario: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_name** | **str**| Scenario name | 
 **authorization** | **str**| authentication header object | [optional] 
 **debug_arguments** | [**DebugArgumentsSchema**](DebugArgumentsSchema.md)| Debug arguments object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

