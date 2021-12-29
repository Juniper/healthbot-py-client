# swagger_client.WorkflowStatisticsApi

All URIs are relative to *http://api-server/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_healthbot_workflow_statistics**](WorkflowStatisticsApi.md#retrieve_healthbot_workflow_statistics) | **GET** /workflow-statistics/ | Retrieve workflow statistics


# **retrieve_healthbot_workflow_statistics**
> WorkflowStatisticsSchema retrieve_healthbot_workflow_statistics(x_iam_token=x_iam_token)

Retrieve workflow statistics

Retrieve operation of all workflow instances statistics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowStatisticsApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Retrieve workflow statistics
    api_response = api_instance.retrieve_healthbot_workflow_statistics(x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowStatisticsApi->retrieve_healthbot_workflow_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**WorkflowStatisticsSchema**](WorkflowStatisticsSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

