# swagger_client.InstanceScheduleStateApi

All URIs are relative to *http://api-server/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_instances_schedule_state**](InstanceScheduleStateApi.md#retrieve_instances_schedule_state) | **GET** /instances-schedule-state/{group_type}/{group_name}/ | Get scheduled state of playbook instances with schedule.
[**update_instances_schedule_state**](InstanceScheduleStateApi.md#update_instances_schedule_state) | **PUT** /instances-schedule-state/{group_type}/{group_name}/ | Update scheduled state of playbook instances with schedule.


# **retrieve_instances_schedule_state**
> InstancesScheduleStateSchema retrieve_instances_schedule_state(group_name, group_type)

Get scheduled state of playbook instances with schedule.

Retrieve the scheduled state of instances with an active scheduler attached to it and present under the group with name passed in the path parameter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstanceScheduleStateApi()
group_name = 'group_name_example' # str | Group name
group_type = 'group_type_example' # str | Group type

try:
    # Get scheduled state of playbook instances with schedule.
    api_response = api_instance.retrieve_instances_schedule_state(group_name, group_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceScheduleStateApi->retrieve_instances_schedule_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Group name | 
 **group_type** | **str**| Group type | 

### Return type

[**InstancesScheduleStateSchema**](InstancesScheduleStateSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instances_schedule_state**
> update_instances_schedule_state(group_name, group_type, instances_schedule_state)

Update scheduled state of playbook instances with schedule.

Update the scheduled state of instances with active scheduler attached to it and present under the group with name passed in the path parameter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstanceScheduleStateApi()
group_name = 'group_name_example' # str | Group name
group_type = 'group_type_example' # str | Group type
instances_schedule_state = swagger_client.InstancesScheduleStateSchema() # InstancesScheduleStateSchema | List of instances and their scheduled state

try:
    # Update scheduled state of playbook instances with schedule.
    api_instance.update_instances_schedule_state(group_name, group_type, instances_schedule_state)
except ApiException as e:
    print("Exception when calling InstanceScheduleStateApi->update_instances_schedule_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Group name | 
 **group_type** | **str**| Group type | 
 **instances_schedule_state** | [**InstancesScheduleStateSchema**](InstancesScheduleStateSchema.md)| List of instances and their scheduled state | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

