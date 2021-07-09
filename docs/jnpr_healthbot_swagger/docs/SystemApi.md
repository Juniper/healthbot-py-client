# swagger_client.SystemApi

All URIs are relative to *http://api-server/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_resource_dependencies**](SystemApi.md#generate_resource_dependencies) | **GET** /config/rca/generate-resource-dependencies | Resource dependencies
[**query_tsdb**](SystemApi.md#query_tsdb) | **GET** /tsdb/query | TSDB query
[**query_tsdb_post**](SystemApi.md#query_tsdb_post) | **POST** /tsdb/query | TSDB query
[**retrieve_available_nodes**](SystemApi.md#retrieve_available_nodes) | **GET** /nodes/ | List of available nodes
[**retrieve_sensor_device_group**](SystemApi.md#retrieve_sensor_device_group) | **GET** /config/sensor/device-group/{device_group_name}/ | Get all All API&#39;s.
[**retrieve_system_details**](SystemApi.md#retrieve_system_details) | **GET** /system-details/ | Retrieve system details.
[**retrieve_tsdb_counters**](SystemApi.md#retrieve_tsdb_counters) | **GET** /tsdb-counters/ | TSDB counters


# **generate_resource_dependencies**
> generate_resource_dependencies(x_iam_token=x_iam_token)

Resource dependencies

Get resource dependency events. Internal API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Resource dependencies
    api_instance.generate_resource_dependencies(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling SystemApi->generate_resource_dependencies: %s\n" % e)
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

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_tsdb**
> TsdbResults query_tsdb(db, device_group, device, measurement=measurement, topic=topic, rule=rule, trigger=trigger, fields=fields, order=order, group_by=group_by, limit=limit, where=where, q=q)

TSDB query

Query TSDB

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()
db = 'db_example' # str | Name of the database. Multiple databases should be separated by ','. '*' can be used to specify all databases.
device_group = 'device_group_example' # str | Name of the deviceGroup(s). Multiple device groups should be separated by ','. This can be used in combination with device, but is not mandatory. If device is given, then query will be executed only for that particular devices in the given device group, else all devices in group will be considered. Given devices will be applicable for all give device-groups.
device = 'device_example' # str | Name of the device. Multiple device should be separated by ','. This should be used along with deviceGroup. Without deviceGroup, this config will not be considered
measurement = 'measurement_example' # str | Name of the measurement. Optional if topic/rule/trigger is used (optional)
topic = 'topic_example' # str | Name of Healthbot topic. Optional if measurement is used (optional)
rule = 'rule_example' # str | Name of Healthbot rule. Required if topic is used. Optional if measurement is used (optional)
trigger = 'trigger_example' # str | Name of Healthbot trigger. Optional if measurement is used or rule table is being queried (optional)
fields = 'fields_example' # str | Fields that needs to be retrieved. Use * for to query all fields. Eg: fields=field1, field2 (optional)
order = 'order_example' # str | Sort points in descending order based on time. By default points will be sorted in ascending order. Eg: order=desc (optional)
group_by = 'group_by_example' # str | Group results based on specified tags. Use * to group by all tags. Eg: groupBy=key1, key2 (optional)
limit = 'limit_example' # str | Limit number of points in the result. If groupBy is used limit is applied per group. Eg: limit=10 (optional)
where = 'where_example' # str | Where clause filters data based on fields, tags, and/or timestamps. Eg: where=\"interface-name\" = 'ge-0/0/1' and \"in-pkts\" > 0 (optional)
q = 'q_example' # str | Influx query string. Use this when custom query format does not support a query (optional)

try:
    # TSDB query
    api_response = api_instance.query_tsdb(db, device_group, device, measurement=measurement, topic=topic, rule=rule, trigger=trigger, fields=fields, order=order, group_by=group_by, limit=limit, where=where, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->query_tsdb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Name of the database. Multiple databases should be separated by &#39;,&#39;. &#39;*&#39; can be used to specify all databases. | 
 **device_group** | **str**| Name of the deviceGroup(s). Multiple device groups should be separated by &#39;,&#39;. This can be used in combination with device, but is not mandatory. If device is given, then query will be executed only for that particular devices in the given device group, else all devices in group will be considered. Given devices will be applicable for all give device-groups. | 
 **device** | **str**| Name of the device. Multiple device should be separated by &#39;,&#39;. This should be used along with deviceGroup. Without deviceGroup, this config will not be considered | 
 **measurement** | **str**| Name of the measurement. Optional if topic/rule/trigger is used | [optional] 
 **topic** | **str**| Name of Healthbot topic. Optional if measurement is used | [optional] 
 **rule** | **str**| Name of Healthbot rule. Required if topic is used. Optional if measurement is used | [optional] 
 **trigger** | **str**| Name of Healthbot trigger. Optional if measurement is used or rule table is being queried | [optional] 
 **fields** | **str**| Fields that needs to be retrieved. Use * for to query all fields. Eg: fields&#x3D;field1, field2 | [optional] 
 **order** | **str**| Sort points in descending order based on time. By default points will be sorted in ascending order. Eg: order&#x3D;desc | [optional] 
 **group_by** | **str**| Group results based on specified tags. Use * to group by all tags. Eg: groupBy&#x3D;key1, key2 | [optional] 
 **limit** | **str**| Limit number of points in the result. If groupBy is used limit is applied per group. Eg: limit&#x3D;10 | [optional] 
 **where** | **str**| Where clause filters data based on fields, tags, and/or timestamps. Eg: where&#x3D;\&quot;interface-name\&quot; &#x3D; &#39;ge-0/0/1&#39; and \&quot;in-pkts\&quot; &gt; 0 | [optional] 
 **q** | **str**| Influx query string. Use this when custom query format does not support a query | [optional] 

### Return type

[**TsdbResults**](TsdbResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_tsdb_post**
> TsdbResults query_tsdb_post(db, device_group, device, tsdb_query_body=tsdb_query_body, measurement=measurement, topic=topic, rule=rule, trigger=trigger, fields=fields, order=order, group_by=group_by, limit=limit, where=where, q=q)

TSDB query

Query TSDB

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()
db = 'db_example' # str | Name of the database. Multiple databases should be separated by ','. '*' can be used to specify all databases.
device_group = 'device_group_example' # str | Name of the deviceGroup(s). Multiple device groups should be separated by ','. This can be used in combination with device, but is not mandatory. If device is given, then query will be executed only for that particular devices in the given device group, else all devices in group will be considered. Given devices will be applicable for all give device-groups.
device = 'device_example' # str | Name of the device. Multiple device should be separated by ','. This should be used along with deviceGroup. Without deviceGroup, this config will not be considered
tsdb_query_body = swagger_client.TsdbPostBody() # TsdbPostBody | Query TSDB body object (optional)
measurement = 'measurement_example' # str | Name of the measurement. Optional if topic/rule/trigger is used (optional)
topic = 'topic_example' # str | Name of Healthbot topic. Optional if measurement is used (optional)
rule = 'rule_example' # str | Name of Healthbot rule. Required if topic is used. Optional if measurement is used (optional)
trigger = 'trigger_example' # str | Name of Healthbot trigger. Optional if measurement is used or rule table is being queried (optional)
fields = 'fields_example' # str | Fields that needs to be retrieved. Use * for to query all fields. Eg: fields=field1, field2 (optional)
order = 'order_example' # str | Sort points in descending order based on time. By default points will be sorted in ascending order. Eg: order=desc (optional)
group_by = 'group_by_example' # str | Group results based on specified tags. Use * to group by all tags. Eg: groupBy=key1, key2 (optional)
limit = 'limit_example' # str | Limit number of points in the result. If groupBy is used limit is applied per group. Eg: limit=10 (optional)
where = 'where_example' # str | Where clause filters data based on fields, tags, and/or timestamps. Eg: where=\"interface-name\" = 'ge-0/0/1' and \"in-pkts\" > 0 (optional)
q = 'q_example' # str | Influx query string. Use this when custom query format does not support a query (optional)

try:
    # TSDB query
    api_response = api_instance.query_tsdb_post(db, device_group, device, tsdb_query_body=tsdb_query_body, measurement=measurement, topic=topic, rule=rule, trigger=trigger, fields=fields, order=order, group_by=group_by, limit=limit, where=where, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->query_tsdb_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Name of the database. Multiple databases should be separated by &#39;,&#39;. &#39;*&#39; can be used to specify all databases. | 
 **device_group** | **str**| Name of the deviceGroup(s). Multiple device groups should be separated by &#39;,&#39;. This can be used in combination with device, but is not mandatory. If device is given, then query will be executed only for that particular devices in the given device group, else all devices in group will be considered. Given devices will be applicable for all give device-groups. | 
 **device** | **str**| Name of the device. Multiple device should be separated by &#39;,&#39;. This should be used along with deviceGroup. Without deviceGroup, this config will not be considered | 
 **tsdb_query_body** | [**TsdbPostBody**](TsdbPostBody.md)| Query TSDB body object | [optional] 
 **measurement** | **str**| Name of the measurement. Optional if topic/rule/trigger is used | [optional] 
 **topic** | **str**| Name of Healthbot topic. Optional if measurement is used | [optional] 
 **rule** | **str**| Name of Healthbot rule. Required if topic is used. Optional if measurement is used | [optional] 
 **trigger** | **str**| Name of Healthbot trigger. Optional if measurement is used or rule table is being queried | [optional] 
 **fields** | **str**| Fields that needs to be retrieved. Use * for to query all fields. Eg: fields&#x3D;field1, field2 | [optional] 
 **order** | **str**| Sort points in descending order based on time. By default points will be sorted in ascending order. Eg: order&#x3D;desc | [optional] 
 **group_by** | **str**| Group results based on specified tags. Use * to group by all tags. Eg: groupBy&#x3D;key1, key2 | [optional] 
 **limit** | **str**| Limit number of points in the result. If groupBy is used limit is applied per group. Eg: limit&#x3D;10 | [optional] 
 **where** | **str**| Where clause filters data based on fields, tags, and/or timestamps. Eg: where&#x3D;\&quot;interface-name\&quot; &#x3D; &#39;ge-0/0/1&#39; and \&quot;in-pkts\&quot; &gt; 0 | [optional] 
 **q** | **str**| Influx query string. Use this when custom query format does not support a query | [optional] 

### Return type

[**TsdbResults**](TsdbResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_available_nodes**
> retrieve_available_nodes(x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # List of available nodes
    api_instance.retrieve_available_nodes(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling SystemApi->retrieve_available_nodes: %s\n" % e)
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

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_sensor_device_group**
> retrieve_sensor_device_group(device_group_name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Get all All API's.
    api_instance.retrieve_sensor_device_group(device_group_name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling SystemApi->retrieve_sensor_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| Device Group | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_system_details**
> retrieve_system_details(x_iam_token=x_iam_token, service_name=service_name)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
service_name = 'service_name_example' # str | service name takes in the name of the service for which details are required. (optional)

try:
    # Retrieve system details.
    api_instance.retrieve_system_details(x_iam_token=x_iam_token, service_name=service_name)
except ApiException as e:
    print("Exception when calling SystemApi->retrieve_system_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> retrieve_tsdb_counters(x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # TSDB counters
    api_instance.retrieve_tsdb_counters(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling SystemApi->retrieve_tsdb_counters: %s\n" % e)
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

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

