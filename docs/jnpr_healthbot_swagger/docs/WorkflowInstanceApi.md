# swagger_client.WorkflowInstanceApi

All URIs are relative to *http://api-server/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_healthbot_workflow_instance_by_id**](WorkflowInstanceApi.md#create_healthbot_workflow_instance_by_id) | **POST** /workflow-instance/{workflow_name}/ | Create workflow by ID
[**delete_healthbot_workflow_instance_by_id**](WorkflowInstanceApi.md#delete_healthbot_workflow_instance_by_id) | **DELETE** /workflow-instance/{workflow_name}/ | Delete workflow instance by ID
[**delete_healthbot_workflow_instances**](WorkflowInstanceApi.md#delete_healthbot_workflow_instances) | **DELETE** /workflow-instances/ | Delete workflow by ID
[**retrieve_healthbot_workflow_instance_by_id**](WorkflowInstanceApi.md#retrieve_healthbot_workflow_instance_by_id) | **GET** /workflow-instance/{workflow_name}/ | Retrieve workflow by ID
[**retrieve_healthbot_workflow_instances**](WorkflowInstanceApi.md#retrieve_healthbot_workflow_instances) | **GET** /workflow-instances/ | Retrieve workflow instances
[**update_healthbot_workflow_instance_by_id**](WorkflowInstanceApi.md#update_healthbot_workflow_instance_by_id) | **PUT** /workflow-instance/{workflow_name}/ | Retrieve workflow by ID
[**update_healthbot_workflow_instances**](WorkflowInstanceApi.md#update_healthbot_workflow_instances) | **PUT** /workflow-instances/ | Update workflow instances


# **create_healthbot_workflow_instance_by_id**
> WorkflowInstanceSchema create_healthbot_workflow_instance_by_id(workflow_name, x_iam_token=x_iam_token, workflow=workflow)

Create workflow by ID

Create operation of resource: workflow instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowInstanceApi()
workflow_name = 'workflow_name_example' # str | ID of workflow-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
workflow = swagger_client.WorkflowInstanceSchema() # WorkflowInstanceSchema | workflowbody object (optional)

try:
    # Create workflow by ID
    api_response = api_instance.create_healthbot_workflow_instance_by_id(workflow_name, x_iam_token=x_iam_token, workflow=workflow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowInstanceApi->create_healthbot_workflow_instance_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_name** | **str**| ID of workflow-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **workflow** | [**WorkflowInstanceSchema**](WorkflowInstanceSchema.md)| workflowbody object | [optional] 

### Return type

[**WorkflowInstanceSchema**](WorkflowInstanceSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_workflow_instance_by_id**
> delete_healthbot_workflow_instance_by_id(workflow_name, x_iam_token=x_iam_token, workflow_instance_name=workflow_instance_name)

Delete workflow instance by ID

Delete operation of resource: workflow instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowInstanceApi()
workflow_name = 'workflow_name_example' # str | Name of the workflow
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
workflow_instance_name = 'workflow_instance_name_example' # str | ID of workflow instance (optional)

try:
    # Delete workflow instance by ID
    api_instance.delete_healthbot_workflow_instance_by_id(workflow_name, x_iam_token=x_iam_token, workflow_instance_name=workflow_instance_name)
except ApiException as e:
    print("Exception when calling WorkflowInstanceApi->delete_healthbot_workflow_instance_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_name** | **str**| Name of the workflow | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **workflow_instance_name** | **str**| ID of workflow instance | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_workflow_instances**
> delete_healthbot_workflow_instances(x_iam_token=x_iam_token)

Delete workflow by ID

Delete operation of resource: workflow instances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowInstanceApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete workflow by ID
    api_instance.delete_healthbot_workflow_instances(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling WorkflowInstanceApi->delete_healthbot_workflow_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_workflow_instance_by_id**
> WorkflowInstancesSchema retrieve_healthbot_workflow_instance_by_id(workflow_name, x_iam_token=x_iam_token, workflow_instance_name=workflow_instance_name, extensive=extensive)

Retrieve workflow by ID

Retrieve operation of resource: workflow instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowInstanceApi()
workflow_name = 'workflow_name_example' # str | Name of the workflow
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
workflow_instance_name = 'workflow_instance_name_example' # str | Name of the workflow instance (optional)
extensive = true # bool | Get extensive information including logs (optional)

try:
    # Retrieve workflow by ID
    api_response = api_instance.retrieve_healthbot_workflow_instance_by_id(workflow_name, x_iam_token=x_iam_token, workflow_instance_name=workflow_instance_name, extensive=extensive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowInstanceApi->retrieve_healthbot_workflow_instance_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_name** | **str**| Name of the workflow | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **workflow_instance_name** | **str**| Name of the workflow instance | [optional] 
 **extensive** | **bool**| Get extensive information including logs | [optional] 

### Return type

[**WorkflowInstancesSchema**](WorkflowInstancesSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_workflow_instances**
> WorkflowInstancesSchema retrieve_healthbot_workflow_instances(x_iam_token=x_iam_token)

Retrieve workflow instances

Retrieve operation of all workflow instances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowInstanceApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Retrieve workflow instances
    api_response = api_instance.retrieve_healthbot_workflow_instances(x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowInstanceApi->retrieve_healthbot_workflow_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**WorkflowInstancesSchema**](WorkflowInstancesSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_workflow_instance_by_id**
> WorkflowInstancesSchema update_healthbot_workflow_instance_by_id(workflow_name, operation, x_iam_token=x_iam_token, workflow_instance_name=workflow_instance_name)

Retrieve workflow by ID

Update operation of resource: workflow instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowInstanceApi()
workflow_name = 'workflow_name_example' # str | Name of the workflow
operation = 'operation_example' # str | Name of the update operation
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
workflow_instance_name = 'workflow_instance_name_example' # str | Name of the workflow instance (optional)

try:
    # Retrieve workflow by ID
    api_response = api_instance.update_healthbot_workflow_instance_by_id(workflow_name, operation, x_iam_token=x_iam_token, workflow_instance_name=workflow_instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowInstanceApi->update_healthbot_workflow_instance_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_name** | **str**| Name of the workflow | 
 **operation** | **str**| Name of the update operation | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **workflow_instance_name** | **str**| Name of the workflow instance | [optional] 

### Return type

[**WorkflowInstancesSchema**](WorkflowInstancesSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_workflow_instances**
> WorkflowInstancesSchema update_healthbot_workflow_instances(operation, x_iam_token=x_iam_token)

Update workflow instances

Update operation of all workflow instances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowInstanceApi()
operation = 'operation_example' # str | Name of the update operation
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update workflow instances
    api_response = api_instance.update_healthbot_workflow_instances(operation, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowInstanceApi->update_healthbot_workflow_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation** | **str**| Name of the update operation | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**WorkflowInstancesSchema**](WorkflowInstancesSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

