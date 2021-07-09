# swagger_client.WorkflowApi

All URIs are relative to *http://api-server/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_healthbot_workflow_workflow_by_id**](WorkflowApi.md#create_healthbot_workflow_workflow_by_id) | **POST** /config/workflow/{workflow_name}/ | Create workflow by ID
[**create_healthbot_workflows_workflow_by_id**](WorkflowApi.md#create_healthbot_workflows_workflow_by_id) | **POST** /config/workflows/ | Create workflow by ID
[**delete_healthbot_workflow_workflow_by_id**](WorkflowApi.md#delete_healthbot_workflow_workflow_by_id) | **DELETE** /config/workflow/{workflow_name}/ | Delete workflow by ID
[**delete_healthbot_workflows_workflow_by_id**](WorkflowApi.md#delete_healthbot_workflows_workflow_by_id) | **DELETE** /config/workflows/ | Delete workflow by ID
[**retrieve_healthbot_workflow_workflow**](WorkflowApi.md#retrieve_healthbot_workflow_workflow) | **GET** /config/workflow/ | Retrieve workflow
[**retrieve_healthbot_workflow_workflow_by_id**](WorkflowApi.md#retrieve_healthbot_workflow_workflow_by_id) | **GET** /config/workflow/{workflow_name}/ | Retrieve workflow by ID
[**retrieve_healthbot_workflows_workflow_by_id**](WorkflowApi.md#retrieve_healthbot_workflows_workflow_by_id) | **GET** /config/workflows/ | Retrieve workflow by ID
[**update_healthbot_workflow_workflow_by_id**](WorkflowApi.md#update_healthbot_workflow_workflow_by_id) | **PUT** /config/workflow/{workflow_name}/ | Update workflow by ID
[**update_healthbot_workflows_workflow_by_id**](WorkflowApi.md#update_healthbot_workflows_workflow_by_id) | **PUT** /config/workflows/ | Update workflow by ID


# **create_healthbot_workflow_workflow_by_id**
> create_healthbot_workflow_workflow_by_id(workflow_name, workflow, x_iam_token=x_iam_token)

Create workflow by ID

Create operation of resource: workflow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowApi()
workflow_name = 'workflow_name_example' # str | ID of workflow-name
workflow = swagger_client.WorkflowSchema() # WorkflowSchema | workflowbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create workflow by ID
    api_instance.create_healthbot_workflow_workflow_by_id(workflow_name, workflow, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling WorkflowApi->create_healthbot_workflow_workflow_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_name** | **str**| ID of workflow-name | 
 **workflow** | [**WorkflowSchema**](WorkflowSchema.md)| workflowbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_workflows_workflow_by_id**
> create_healthbot_workflows_workflow_by_id(workflows, x_iam_token=x_iam_token)

Create workflow by ID

Create/Update multiple workflows. The new content for the existing workflows updates the existing content and the new workflows are created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowApi()
workflows = swagger_client.WorkflowsSchema() # WorkflowsSchema | workflowbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create workflow by ID
    api_instance.create_healthbot_workflows_workflow_by_id(workflows, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling WorkflowApi->create_healthbot_workflows_workflow_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflows** | [**WorkflowsSchema**](WorkflowsSchema.md)| workflowbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_workflow_workflow_by_id**
> delete_healthbot_workflow_workflow_by_id(workflow_name, x_iam_token=x_iam_token)

Delete workflow by ID

Delete operation of resource: workflow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowApi()
workflow_name = 'workflow_name_example' # str | ID of workflow-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete workflow by ID
    api_instance.delete_healthbot_workflow_workflow_by_id(workflow_name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling WorkflowApi->delete_healthbot_workflow_workflow_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_name** | **str**| ID of workflow-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_workflows_workflow_by_id**
> delete_healthbot_workflows_workflow_by_id(x_iam_token=x_iam_token)

Delete workflow by ID

Delete operation of resource: workflow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete workflow by ID
    api_instance.delete_healthbot_workflows_workflow_by_id(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling WorkflowApi->delete_healthbot_workflows_workflow_by_id: %s\n" % e)
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

# **retrieve_healthbot_workflow_workflow**
> list[str] retrieve_healthbot_workflow_workflow(x_iam_token=x_iam_token, working=working)

Retrieve workflow

Retrieve operation of resource: workflow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve workflow
    api_response = api_instance.retrieve_healthbot_workflow_workflow(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowApi->retrieve_healthbot_workflow_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_workflow_workflow_by_id**
> WorkflowSchema retrieve_healthbot_workflow_workflow_by_id(workflow_name, x_iam_token=x_iam_token, working=working)

Retrieve workflow by ID

Retrieve operation of resource: workflow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowApi()
workflow_name = 'workflow_name_example' # str | ID of workflow-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve workflow by ID
    api_response = api_instance.retrieve_healthbot_workflow_workflow_by_id(workflow_name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowApi->retrieve_healthbot_workflow_workflow_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_name** | **str**| ID of workflow-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**WorkflowSchema**](WorkflowSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_workflows_workflow_by_id**
> WorkflowsSchema retrieve_healthbot_workflows_workflow_by_id(x_iam_token=x_iam_token, working=working)

Retrieve workflow by ID

Retrieve operation of resource: workflow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve workflow by ID
    api_response = api_instance.retrieve_healthbot_workflows_workflow_by_id(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowApi->retrieve_healthbot_workflows_workflow_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**WorkflowsSchema**](WorkflowsSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_workflow_workflow_by_id**
> update_healthbot_workflow_workflow_by_id(workflow_name, workflow, x_iam_token=x_iam_token)

Update workflow by ID

Update operation of resource: workflow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowApi()
workflow_name = 'workflow_name_example' # str | ID of workflow-name
workflow = swagger_client.WorkflowSchema() # WorkflowSchema | workflowbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update workflow by ID
    api_instance.update_healthbot_workflow_workflow_by_id(workflow_name, workflow, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling WorkflowApi->update_healthbot_workflow_workflow_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_name** | **str**| ID of workflow-name | 
 **workflow** | [**WorkflowSchema**](WorkflowSchema.md)| workflowbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_workflows_workflow_by_id**
> update_healthbot_workflows_workflow_by_id(workflows, x_iam_token=x_iam_token)

Update workflow by ID

Update operation of resource: workflow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowApi()
workflows = swagger_client.WorkflowsSchema() # WorkflowsSchema | workflowbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update workflow by ID
    api_instance.update_healthbot_workflows_workflow_by_id(workflows, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling WorkflowApi->update_healthbot_workflows_workflow_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflows** | [**WorkflowsSchema**](WorkflowsSchema.md)| workflowbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

