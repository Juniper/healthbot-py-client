# swagger_client.LogsApi

All URIs are relative to *http://api-server/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_logs_for_device_group**](LogsApi.md#retrieve_logs_for_device_group) | **GET** /logs/device-group/{device_group_name}/ | Logs for the given device-group.
[**retrieve_logs_for_device_group_service**](LogsApi.md#retrieve_logs_for_device_group_service) | **GET** /logs/device-group/{device_group_name}/service/{service_name}/ | Get the logs for the given service running for the given device-group.
[**retrieve_logs_for_network_group**](LogsApi.md#retrieve_logs_for_network_group) | **GET** /logs/network-group/{network_group_name}/ | Logs for the given network group.
[**retrieve_logs_for_network_group_service**](LogsApi.md#retrieve_logs_for_network_group_service) | **GET** /logs/network-group/{network_group_name}/service/{service_name}/ | Get the logs for the given service running for the given network-group.


# **retrieve_logs_for_device_group**
> retrieve_logs_for_device_group(device_group_name, x_iam_token=x_iam_token, download=download, filename=filename)

Logs for the given device-group.

Get the logs for all the services for the given {device_group_name}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LogsApi()
device_group_name = 'device_group_name_example' # str | Device group name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
download = true # bool | Download the logs (optional) (default to true)
filename = 'filename_example' # str | Name of the log file (optional)

try:
    # Logs for the given device-group.
    api_instance.retrieve_logs_for_device_group(device_group_name, x_iam_token=x_iam_token, download=download, filename=filename)
except ApiException as e:
    print("Exception when calling LogsApi->retrieve_logs_for_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| Device group name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **download** | **bool**| Download the logs | [optional] [default to true]
 **filename** | **str**| Name of the log file | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/gzip, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_logs_for_device_group_service**
> retrieve_logs_for_device_group_service(device_group_name, service_name, x_iam_token=x_iam_token, download=download, filename=filename, number_of_lines=number_of_lines)

Get the logs for the given service running for the given device-group.

Get the logs for the service {service_name} for the given {device_group_name}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LogsApi()
device_group_name = 'device_group_name_example' # str | Device group name
service_name = 'service_name_example' # str | Device-group service name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
download = true # bool | Download the logs (optional) (default to true)
filename = 'filename_example' # str | Name of the log file (optional)
number_of_lines = 100000 # int | Number of lines to show from the end of the logs (optional) (default to 100000)

try:
    # Get the logs for the given service running for the given device-group.
    api_instance.retrieve_logs_for_device_group_service(device_group_name, service_name, x_iam_token=x_iam_token, download=download, filename=filename, number_of_lines=number_of_lines)
except ApiException as e:
    print("Exception when calling LogsApi->retrieve_logs_for_device_group_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| Device group name | 
 **service_name** | **str**| Device-group service name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **download** | **bool**| Download the logs | [optional] [default to true]
 **filename** | **str**| Name of the log file | [optional] 
 **number_of_lines** | **int**| Number of lines to show from the end of the logs | [optional] [default to 100000]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/gzip, application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_logs_for_network_group**
> retrieve_logs_for_network_group(network_group_name, x_iam_token=x_iam_token, download=download, filename=filename)

Logs for the given network group.

Get the logs for the service {service_name} for the given {network_group_name}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LogsApi()
network_group_name = 'network_group_name_example' # str | Network group name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
download = true # bool | Download the logs (optional) (default to true)
filename = 'filename_example' # str | Name of the log file (optional)

try:
    # Logs for the given network group.
    api_instance.retrieve_logs_for_network_group(network_group_name, x_iam_token=x_iam_token, download=download, filename=filename)
except ApiException as e:
    print("Exception when calling LogsApi->retrieve_logs_for_network_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_group_name** | **str**| Network group name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **download** | **bool**| Download the logs | [optional] [default to true]
 **filename** | **str**| Name of the log file | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/gzip, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_logs_for_network_group_service**
> retrieve_logs_for_network_group_service(network_group_name, service_name, x_iam_token=x_iam_token, download=download, filename=filename, number_of_lines=number_of_lines)

Get the logs for the given service running for the given network-group.

Get the logs for all the services for the given {network_group_name}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LogsApi()
network_group_name = 'network_group_name_example' # str | Network group name
service_name = 'service_name_example' # str | Network group service name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
download = true # bool | Download the logs (optional) (default to true)
filename = 'filename_example' # str | Name of the log file (optional)
number_of_lines = 100000 # int | Number of lines to show from the end of the logs (optional) (default to 100000)

try:
    # Get the logs for the given service running for the given network-group.
    api_instance.retrieve_logs_for_network_group_service(network_group_name, service_name, x_iam_token=x_iam_token, download=download, filename=filename, number_of_lines=number_of_lines)
except ApiException as e:
    print("Exception when calling LogsApi->retrieve_logs_for_network_group_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_group_name** | **str**| Network group name | 
 **service_name** | **str**| Network group service name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **download** | **bool**| Download the logs | [optional] [default to true]
 **filename** | **str**| Name of the log file | [optional] 
 **number_of_lines** | **int**| Number of lines to show from the end of the logs | [optional] [default to 100000]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/gzip, application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

