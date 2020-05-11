# swagger_client.SystemApi

All URIs are relative to *http://api-server/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_available_nodes**](SystemApi.md#retrieve_available_nodes) | **GET** /nodes/ | List of available nodes
[**retrieve_sensor_device_group**](SystemApi.md#retrieve_sensor_device_group) | **GET** /sensor/device-group/{device_group_name}/ | Get all All API&#39;s.
[**retrieve_system_details**](SystemApi.md#retrieve_system_details) | **GET** /system-details/ | Retrieve system details.
[**retrieve_tsdb_counters**](SystemApi.md#retrieve_tsdb_counters) | **GET** /tsdb-counters/ | TSDB counters


# **retrieve_available_nodes**
> retrieve_available_nodes(authorization=authorization)

List of available nodes

Get the list of available nodes in the installation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # List of available nodes
    api_instance.retrieve_available_nodes(authorization=authorization)
except ApiException as e:
    print("Exception when calling SystemApi->retrieve_available_nodes: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_sensor_device_group**
> retrieve_sensor_device_group(device_group_name, authorization=authorization)

Get all All API's.

GET sensors subscribed for a device-group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()
device_group_name = 'device_group_name_example' # str | Device Group
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Get all All API's.
    api_instance.retrieve_sensor_device_group(device_group_name, authorization=authorization)
except ApiException as e:
    print("Exception when calling SystemApi->retrieve_sensor_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| Device Group | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_system_details**
> retrieve_system_details(authorization=authorization, service_name=service_name)

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
authorization = 'authorization_example' # str | authentication header object (optional)
service_name = 'service_name_example' # str | service name takes in the name of the service for which details are required. (optional)

try:
    # Retrieve system details.
    api_instance.retrieve_system_details(authorization=authorization, service_name=service_name)
except ApiException as e:
    print("Exception when calling SystemApi->retrieve_system_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
 **service_name** | **str**| service name takes in the name of the service for which details are required. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_tsdb_counters**
> retrieve_tsdb_counters(authorization=authorization)

TSDB counters

Get TSDB counters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # TSDB counters
    api_instance.retrieve_tsdb_counters(authorization=authorization)
except ApiException as e:
    print("Exception when calling SystemApi->retrieve_tsdb_counters: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

