# swagger_client.AdministrationApi

All URIs are relative to *http://api-server/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_groups**](AdministrationApi.md#create_groups) | **POST** /group/ | Create groups
[**create_users**](AdministrationApi.md#create_users) | **POST** /user/ | Create an user.
[**delete_group**](AdministrationApi.md#delete_group) | **DELETE** /group/{groupid}/ | Delete groups
[**delete_user**](AdministrationApi.md#delete_user) | **DELETE** /user/{userid}/ | Delete list of users.
[**flush_groups**](AdministrationApi.md#flush_groups) | **PUT** /group/ | Flush the groups
[**flush_users**](AdministrationApi.md#flush_users) | **PUT** /user/ | Flush user base with new set of records.
[**get_group_details**](AdministrationApi.md#get_group_details) | **GET** /group/{groupid}/ | Get lits of all the groups
[**get_user_details**](AdministrationApi.md#get_user_details) | **GET** /user/{userid}/ | Get lits of all the users
[**retrieve_groups**](AdministrationApi.md#retrieve_groups) | **GET** /group/ | Get lits of all the groups
[**retrieve_roles**](AdministrationApi.md#retrieve_roles) | **GET** /role/ | Get list of all the roles
[**retrieve_users**](AdministrationApi.md#retrieve_users) | **GET** /user/ | Get lits of all the users
[**update_group**](AdministrationApi.md#update_group) | **POST** /group/{groupid}/ | Get lits of all the roles
[**update_user_profile**](AdministrationApi.md#update_user_profile) | **POST** /user/{userid}/ | Update user profile informations.


# **create_groups**
> create_groups(authorization, groups)

Create groups

Create group in the system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
authorization = 'authorization_example' # str | authentication header object
groups = [swagger_client.Groups()] # list[Groups] | group details

try:
    # Create groups
    api_instance.create_groups(authorization, groups)
except ApiException as e:
    print("Exception when calling AdministrationApi->create_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | 
 **groups** | [**list[Groups]**](Groups.md)| group details | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_users**
> list[str] create_users(authorization, users)

Create an user.

Create users in the system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
authorization = 'authorization_example' # str | authentication header object
users = [swagger_client.UserSchema()] # list[UserSchema] | List of users

try:
    # Create an user.
    api_response = api_instance.create_users(authorization, users)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->create_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | 
 **users** | [**list[UserSchema]**](UserSchema.md)| List of users | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(authorization, groupid)

Delete groups

Delete the groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
authorization = 'authorization_example' # str | authentication header object
groupid = 'groupid_example' # str | Id of group

try:
    # Delete groups
    api_instance.delete_group(authorization, groupid)
except ApiException as e:
    print("Exception when calling AdministrationApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | 
 **groupid** | **str**| Id of group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(authorization, userid)

Delete list of users.

Delete list of users from system, for administrative purpose

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
authorization = 'authorization_example' # str | authentication header object
userid = 'userid_example' # str | Id of user

try:
    # Delete list of users.
    api_instance.delete_user(authorization, userid)
except ApiException as e:
    print("Exception when calling AdministrationApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | 
 **userid** | **str**| Id of user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flush_groups**
> flush_groups(authorization, groups)

Flush the groups

Flush the existing groups and create new set of groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
authorization = 'authorization_example' # str | authentication header object
groups = [swagger_client.Groups()] # list[Groups] | Group data

try:
    # Flush the groups
    api_instance.flush_groups(authorization, groups)
except ApiException as e:
    print("Exception when calling AdministrationApi->flush_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | 
 **groups** | [**list[Groups]**](Groups.md)| Group data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flush_users**
> list[InlineResponse2003] flush_users(authorization, users)

Flush user base with new set of records.

Flush the user base with new records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
authorization = 'authorization_example' # str | authentication header object
users = [swagger_client.UserSchema()] # list[UserSchema] | User details

try:
    # Flush user base with new set of records.
    api_response = api_instance.flush_users(authorization, users)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->flush_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | 
 **users** | [**list[UserSchema]**](UserSchema.md)| User details | 

### Return type

[**list[InlineResponse2003]**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_details**
> InlineResponse2008 get_group_details(authorization, groupid)

Get lits of all the groups

Get list of registered groups, for administrative purpose

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
authorization = 'authorization_example' # str | authentication header object
groupid = 'groupid_example' # str | Id of group

try:
    # Get lits of all the groups
    api_response = api_instance.get_group_details(authorization, groupid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_group_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | 
 **groupid** | **str**| Id of group | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_details**
> InlineResponse2004 get_user_details(authorization, userid)

Get lits of all the users

Get details of registered users, for administrative purpose

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
authorization = 'authorization_example' # str | authentication header object
userid = 'userid_example' # str | Id of user

try:
    # Get lits of all the users
    api_response = api_instance.get_user_details(authorization, userid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_user_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | 
 **userid** | **str**| Id of user | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_groups**
> list[InlineResponse2008] retrieve_groups(authorization)

Get lits of all the groups

Get list of registered groups, for administrative purpose

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
authorization = 'authorization_example' # str | authentication header object

try:
    # Get lits of all the groups
    api_response = api_instance.retrieve_groups(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->retrieve_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | 

### Return type

[**list[InlineResponse2008]**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_roles**
> RoleSchema retrieve_roles(authorization)

Get list of all the roles

Get list of registered roles, for administrative purpose

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
authorization = 'authorization_example' # str | authentication header object

try:
    # Get list of all the roles
    api_response = api_instance.retrieve_roles(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->retrieve_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | 

### Return type

[**RoleSchema**](RoleSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_users**
> list[InlineResponse2002] retrieve_users(authorization)

Get lits of all the users

Get list of registered users, for administrative purpose

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
authorization = 'authorization_example' # str | authentication header object

try:
    # Get lits of all the users
    api_response = api_instance.retrieve_users(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->retrieve_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | 

### Return type

[**list[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> InlineResponse2009 update_group(authorization, groupid, group)

Get lits of all the roles

Update group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
authorization = 'authorization_example' # str | authentication header object
groupid = 'groupid_example' # str | Id of group
group = swagger_client.Group() # Group | group details

try:
    # Get lits of all the roles
    api_response = api_instance.update_group(authorization, groupid, group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | 
 **groupid** | **str**| Id of group | 
 **group** | [**Group**](Group.md)| group details | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_profile**
> update_user_profile(authorization, userid, user)

Update user profile informations.

Update a user profile in the system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
authorization = 'authorization_example' # str | authentication header object
userid = 'userid_example' # str | Id of user
user = swagger_client.User() # User | user details

try:
    # Update user profile informations.
    api_instance.update_user_profile(authorization, userid, user)
except ApiException as e:
    print("Exception when calling AdministrationApi->update_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | 
 **userid** | **str**| Id of user | 
 **user** | [**User**](User.md)| user details | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

