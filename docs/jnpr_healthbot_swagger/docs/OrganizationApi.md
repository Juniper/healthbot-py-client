# swagger_client.OrganizationApi

All URIs are relative to *http://api-server/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_healthbot_organization_site_edge_edge_by_id**](OrganizationApi.md#create_healthbot_organization_site_edge_edge_by_id) | **POST** /config/organization/{organization_name}/site/{site_name}/edge/{edge_name}/ | Create edge by ID
[**create_healthbot_organization_site_site_by_id**](OrganizationApi.md#create_healthbot_organization_site_site_by_id) | **POST** /config/organization/{organization_name}/site/{site_name}/ | Create site by ID
[**delete_healthbot_organization_site_edge_edge_by_id**](OrganizationApi.md#delete_healthbot_organization_site_edge_edge_by_id) | **DELETE** /config/organization/{organization_name}/site/{site_name}/edge/{edge_name}/ | Delete edge by ID
[**delete_healthbot_organization_site_site_by_id**](OrganizationApi.md#delete_healthbot_organization_site_site_by_id) | **DELETE** /config/organization/{organization_name}/site/{site_name}/ | Delete site by ID
[**retrieve_healthbot_organization_site_edge_edge_by_id**](OrganizationApi.md#retrieve_healthbot_organization_site_edge_edge_by_id) | **GET** /config/organization/{organization_name}/site/{site_name}/edge/{edge_name}/ | Retrieve edge by ID
[**retrieve_healthbot_organization_site_site_by_id**](OrganizationApi.md#retrieve_healthbot_organization_site_site_by_id) | **GET** /config/organization/{organization_name}/site/{site_name}/ | Retrieve site by ID
[**update_healthbot_organization_site_edge_edge_by_id**](OrganizationApi.md#update_healthbot_organization_site_edge_edge_by_id) | **PUT** /config/organization/{organization_name}/site/{site_name}/edge/{edge_name}/ | Update edge by ID
[**update_healthbot_organization_site_site_by_id**](OrganizationApi.md#update_healthbot_organization_site_site_by_id) | **PUT** /config/organization/{organization_name}/site/{site_name}/ | Update site by ID


# **create_healthbot_organization_site_edge_edge_by_id**
> create_healthbot_organization_site_edge_edge_by_id(organization_name, site_name, edge_name, edge, x_iam_token=x_iam_token)

Create edge by ID

Create operation of resource: edge

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
organization_name = 'organization_name_example' # str | ID of organization-name
site_name = 'site_name_example' # str | ID of site-name
edge_name = 'edge_name_example' # str | ID of edge-name
edge = swagger_client.EdgeSchema() # EdgeSchema | edgebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create edge by ID
    api_instance.create_healthbot_organization_site_edge_edge_by_id(organization_name, site_name, edge_name, edge, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling OrganizationApi->create_healthbot_organization_site_edge_edge_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**| ID of organization-name | 
 **site_name** | **str**| ID of site-name | 
 **edge_name** | **str**| ID of edge-name | 
 **edge** | [**EdgeSchema**](EdgeSchema.md)| edgebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_organization_site_site_by_id**
> create_healthbot_organization_site_site_by_id(organization_name, site_name, site, x_iam_token=x_iam_token)

Create site by ID

Create operation of resource: site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
organization_name = 'organization_name_example' # str | ID of organization-name
site_name = 'site_name_example' # str | ID of site-name
site = swagger_client.SiteSchema() # SiteSchema | sitebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create site by ID
    api_instance.create_healthbot_organization_site_site_by_id(organization_name, site_name, site, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling OrganizationApi->create_healthbot_organization_site_site_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**| ID of organization-name | 
 **site_name** | **str**| ID of site-name | 
 **site** | [**SiteSchema**](SiteSchema.md)| sitebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_organization_site_edge_edge_by_id**
> delete_healthbot_organization_site_edge_edge_by_id(organization_name, site_name, edge_name, x_iam_token=x_iam_token)

Delete edge by ID

Delete operation of resource: edge

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
organization_name = 'organization_name_example' # str | ID of organization-name
site_name = 'site_name_example' # str | ID of site-name
edge_name = 'edge_name_example' # str | ID of edge-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete edge by ID
    api_instance.delete_healthbot_organization_site_edge_edge_by_id(organization_name, site_name, edge_name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling OrganizationApi->delete_healthbot_organization_site_edge_edge_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**| ID of organization-name | 
 **site_name** | **str**| ID of site-name | 
 **edge_name** | **str**| ID of edge-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_organization_site_site_by_id**
> delete_healthbot_organization_site_site_by_id(organization_name, site_name, x_iam_token=x_iam_token)

Delete site by ID

Delete operation of resource: site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
organization_name = 'organization_name_example' # str | ID of organization-name
site_name = 'site_name_example' # str | ID of site-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete site by ID
    api_instance.delete_healthbot_organization_site_site_by_id(organization_name, site_name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling OrganizationApi->delete_healthbot_organization_site_site_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**| ID of organization-name | 
 **site_name** | **str**| ID of site-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_organization_site_edge_edge_by_id**
> EdgeSchema retrieve_healthbot_organization_site_edge_edge_by_id(organization_name, site_name, edge_name, x_iam_token=x_iam_token, working=working)

Retrieve edge by ID

Retrieve operation of resource: edge

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
organization_name = 'organization_name_example' # str | ID of organization-name
site_name = 'site_name_example' # str | ID of site-name
edge_name = 'edge_name_example' # str | ID of edge-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve edge by ID
    api_response = api_instance.retrieve_healthbot_organization_site_edge_edge_by_id(organization_name, site_name, edge_name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->retrieve_healthbot_organization_site_edge_edge_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**| ID of organization-name | 
 **site_name** | **str**| ID of site-name | 
 **edge_name** | **str**| ID of edge-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**EdgeSchema**](EdgeSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_organization_site_site_by_id**
> SiteSchema retrieve_healthbot_organization_site_site_by_id(organization_name, site_name, x_iam_token=x_iam_token, working=working)

Retrieve site by ID

Retrieve operation of resource: site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
organization_name = 'organization_name_example' # str | ID of organization-name
site_name = 'site_name_example' # str | ID of site-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve site by ID
    api_response = api_instance.retrieve_healthbot_organization_site_site_by_id(organization_name, site_name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->retrieve_healthbot_organization_site_site_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**| ID of organization-name | 
 **site_name** | **str**| ID of site-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**SiteSchema**](SiteSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_organization_site_edge_edge_by_id**
> update_healthbot_organization_site_edge_edge_by_id(organization_name, site_name, edge_name, edge, x_iam_token=x_iam_token)

Update edge by ID

Update operation of resource: edge

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
organization_name = 'organization_name_example' # str | ID of organization-name
site_name = 'site_name_example' # str | ID of site-name
edge_name = 'edge_name_example' # str | ID of edge-name
edge = swagger_client.EdgeSchema() # EdgeSchema | edgebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update edge by ID
    api_instance.update_healthbot_organization_site_edge_edge_by_id(organization_name, site_name, edge_name, edge, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling OrganizationApi->update_healthbot_organization_site_edge_edge_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**| ID of organization-name | 
 **site_name** | **str**| ID of site-name | 
 **edge_name** | **str**| ID of edge-name | 
 **edge** | [**EdgeSchema**](EdgeSchema.md)| edgebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_organization_site_site_by_id**
> update_healthbot_organization_site_site_by_id(organization_name, site_name, site, x_iam_token=x_iam_token)

Update site by ID

Update operation of resource: site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
organization_name = 'organization_name_example' # str | ID of organization-name
site_name = 'site_name_example' # str | ID of site-name
site = swagger_client.SiteSchema() # SiteSchema | sitebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update site by ID
    api_instance.update_healthbot_organization_site_site_by_id(organization_name, site_name, site, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling OrganizationApi->update_healthbot_organization_site_site_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**| ID of organization-name | 
 **site_name** | **str**| ID of site-name | 
 **site** | [**SiteSchema**](SiteSchema.md)| sitebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

