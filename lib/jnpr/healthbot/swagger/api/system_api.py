# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from jnpr.healthbot.swagger.api_client import ApiClient


class SystemApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def query_tsdb(self, db, device_group, device, **kwargs):  # noqa: E501
        """TSDB query  # noqa: E501

        Query TSDB  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_tsdb(db, device_group, device, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str db: Name of the database. Multiple databases should be separated by ','. '*' can be used to specify all databases. (required)
        :param str device_group: Name of the deviceGroup(s). Multiple device groups should be separated by ','. This can be used in combination with device, but is not mandatory. If device is given, then query will be executed only for that particular devices in the given device group, else all devices in group will be considered. Given devices will be applicable for all give device-groups. (required)
        :param str device: Name of the device. Multiple device should be separated by ','. This should be used along with deviceGroup. Without deviceGroup, this config will not be considered (required)
        :param str measurement: Name of the measurement. Optional if topic/rule/trigger is used
        :param str topic: Name of Healthbot topic. Optional if measurement is used
        :param str rule: Name of Healthbot rule. Required if topic is used. Optional if measurement is used
        :param str trigger: Name of Healthbot trigger. Optional if measurement is used or rule table is being queried
        :param str fields: Fields that needs to be retrieved. Use * for to query all fields. Eg: fields=field1, field2
        :param str order: Sort points in descending order based on time. By default points will be sorted in ascending order. Eg: order=desc
        :param str group_by: Group results based on specified tags. Use * to group by all tags. Eg: groupBy=key1, key2
        :param str limit: Limit number of points in the result. If groupBy is used limit is applied per group. Eg: limit=10
        :param str where: Where clause filters data based on fields, tags, and/or timestamps. Eg: where=\"interface-name\" = 'ge-0/0/1' and \"in-pkts\" > 0
        :return: TsdbResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_tsdb_with_http_info(db, device_group, device, **kwargs)  # noqa: E501
        else:
            (data) = self.query_tsdb_with_http_info(db, device_group, device, **kwargs)  # noqa: E501
            return data

    def query_tsdb_with_http_info(self, db, device_group, device, **kwargs):  # noqa: E501
        """TSDB query  # noqa: E501

        Query TSDB  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_tsdb_with_http_info(db, device_group, device, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str db: Name of the database. Multiple databases should be separated by ','. '*' can be used to specify all databases. (required)
        :param str device_group: Name of the deviceGroup(s). Multiple device groups should be separated by ','. This can be used in combination with device, but is not mandatory. If device is given, then query will be executed only for that particular devices in the given device group, else all devices in group will be considered. Given devices will be applicable for all give device-groups. (required)
        :param str device: Name of the device. Multiple device should be separated by ','. This should be used along with deviceGroup. Without deviceGroup, this config will not be considered (required)
        :param str measurement: Name of the measurement. Optional if topic/rule/trigger is used
        :param str topic: Name of Healthbot topic. Optional if measurement is used
        :param str rule: Name of Healthbot rule. Required if topic is used. Optional if measurement is used
        :param str trigger: Name of Healthbot trigger. Optional if measurement is used or rule table is being queried
        :param str fields: Fields that needs to be retrieved. Use * for to query all fields. Eg: fields=field1, field2
        :param str order: Sort points in descending order based on time. By default points will be sorted in ascending order. Eg: order=desc
        :param str group_by: Group results based on specified tags. Use * to group by all tags. Eg: groupBy=key1, key2
        :param str limit: Limit number of points in the result. If groupBy is used limit is applied per group. Eg: limit=10
        :param str where: Where clause filters data based on fields, tags, and/or timestamps. Eg: where=\"interface-name\" = 'ge-0/0/1' and \"in-pkts\" > 0
        :return: TsdbResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['db', 'device_group', 'device', 'measurement', 'topic', 'rule', 'trigger', 'fields', 'order', 'group_by', 'limit', 'where']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_tsdb" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'db' is set
        if ('db' not in params or
                params['db'] is None):
            raise ValueError("Missing the required parameter `db` when calling `query_tsdb`")  # noqa: E501
        # verify the required parameter 'device_group' is set
        if ('device_group' not in params or
                params['device_group'] is None):
            raise ValueError("Missing the required parameter `device_group` when calling `query_tsdb`")  # noqa: E501
        # verify the required parameter 'device' is set
        if ('device' not in params or
                params['device'] is None):
            raise ValueError("Missing the required parameter `device` when calling `query_tsdb`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'db' in params:
            query_params.append(('db', params['db']))  # noqa: E501
        if 'device_group' in params:
            query_params.append(('deviceGroup', params['device_group']))  # noqa: E501
        if 'device' in params:
            query_params.append(('device', params['device']))  # noqa: E501
        if 'measurement' in params:
            query_params.append(('measurement', params['measurement']))  # noqa: E501
        if 'topic' in params:
            query_params.append(('topic', params['topic']))  # noqa: E501
        if 'rule' in params:
            query_params.append(('rule', params['rule']))  # noqa: E501
        if 'trigger' in params:
            query_params.append(('trigger', params['trigger']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'group_by' in params:
            query_params.append(('groupBy', params['group_by']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'where' in params:
            query_params.append(('where', params['where']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tsdb/query', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TsdbResults',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query_tsdb_post(self, db, device_group, device, **kwargs):  # noqa: E501
        """TSDB query  # noqa: E501

        Query TSDB  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_tsdb_post(db, device_group, device, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str db: Name of the database. Multiple databases should be separated by ','. '*' can be used to specify all databases. (required)
        :param str device_group: Name of the deviceGroup(s). Multiple device groups should be separated by ','. This can be used in combination with device, but is not mandatory. If device is given, then query will be executed only for that particular devices in the given device group, else all devices in group will be considered. Given devices will be applicable for all give device-groups. (required)
        :param str device: Name of the device. Multiple device should be separated by ','. This should be used along with deviceGroup. Without deviceGroup, this config will not be considered (required)
        :param TsdbPostBody tsdb_query_body: Query TSDB body object
        :param str measurement: Name of the measurement. Optional if topic/rule/trigger is used
        :param str topic: Name of Healthbot topic. Optional if measurement is used
        :param str rule: Name of Healthbot rule. Required if topic is used. Optional if measurement is used
        :param str trigger: Name of Healthbot trigger. Optional if measurement is used or rule table is being queried
        :param str fields: Fields that needs to be retrieved. Use * for to query all fields. Eg: fields=field1, field2
        :param str order: Sort points in descending order based on time. By default points will be sorted in ascending order. Eg: order=desc
        :param str group_by: Group results based on specified tags. Use * to group by all tags. Eg: groupBy=key1, key2
        :param str limit: Limit number of points in the result. If groupBy is used limit is applied per group. Eg: limit=10
        :param str where: Where clause filters data based on fields, tags, and/or timestamps. Eg: where=\"interface-name\" = 'ge-0/0/1' and \"in-pkts\" > 0
        :return: TsdbResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_tsdb_post_with_http_info(db, device_group, device, **kwargs)  # noqa: E501
        else:
            (data) = self.query_tsdb_post_with_http_info(db, device_group, device, **kwargs)  # noqa: E501
            return data

    def query_tsdb_post_with_http_info(self, db, device_group, device, **kwargs):  # noqa: E501
        """TSDB query  # noqa: E501

        Query TSDB  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_tsdb_post_with_http_info(db, device_group, device, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str db: Name of the database. Multiple databases should be separated by ','. '*' can be used to specify all databases. (required)
        :param str device_group: Name of the deviceGroup(s). Multiple device groups should be separated by ','. This can be used in combination with device, but is not mandatory. If device is given, then query will be executed only for that particular devices in the given device group, else all devices in group will be considered. Given devices will be applicable for all give device-groups. (required)
        :param str device: Name of the device. Multiple device should be separated by ','. This should be used along with deviceGroup. Without deviceGroup, this config will not be considered (required)
        :param TsdbPostBody tsdb_query_body: Query TSDB body object
        :param str measurement: Name of the measurement. Optional if topic/rule/trigger is used
        :param str topic: Name of Healthbot topic. Optional if measurement is used
        :param str rule: Name of Healthbot rule. Required if topic is used. Optional if measurement is used
        :param str trigger: Name of Healthbot trigger. Optional if measurement is used or rule table is being queried
        :param str fields: Fields that needs to be retrieved. Use * for to query all fields. Eg: fields=field1, field2
        :param str order: Sort points in descending order based on time. By default points will be sorted in ascending order. Eg: order=desc
        :param str group_by: Group results based on specified tags. Use * to group by all tags. Eg: groupBy=key1, key2
        :param str limit: Limit number of points in the result. If groupBy is used limit is applied per group. Eg: limit=10
        :param str where: Where clause filters data based on fields, tags, and/or timestamps. Eg: where=\"interface-name\" = 'ge-0/0/1' and \"in-pkts\" > 0
        :return: TsdbResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['db', 'device_group', 'device', 'tsdb_query_body', 'measurement', 'topic', 'rule', 'trigger', 'fields', 'order', 'group_by', 'limit', 'where']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_tsdb_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'db' is set
        if ('db' not in params or
                params['db'] is None):
            raise ValueError("Missing the required parameter `db` when calling `query_tsdb_post`")  # noqa: E501
        # verify the required parameter 'device_group' is set
        if ('device_group' not in params or
                params['device_group'] is None):
            raise ValueError("Missing the required parameter `device_group` when calling `query_tsdb_post`")  # noqa: E501
        # verify the required parameter 'device' is set
        if ('device' not in params or
                params['device'] is None):
            raise ValueError("Missing the required parameter `device` when calling `query_tsdb_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'db' in params:
            query_params.append(('db', params['db']))  # noqa: E501
        if 'device_group' in params:
            query_params.append(('deviceGroup', params['device_group']))  # noqa: E501
        if 'device' in params:
            query_params.append(('device', params['device']))  # noqa: E501
        if 'measurement' in params:
            query_params.append(('measurement', params['measurement']))  # noqa: E501
        if 'topic' in params:
            query_params.append(('topic', params['topic']))  # noqa: E501
        if 'rule' in params:
            query_params.append(('rule', params['rule']))  # noqa: E501
        if 'trigger' in params:
            query_params.append(('trigger', params['trigger']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'group_by' in params:
            query_params.append(('groupBy', params['group_by']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'where' in params:
            query_params.append(('where', params['where']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tsdb_query_body' in params:
            body_params = params['tsdb_query_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tsdb/query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TsdbResults',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_available_nodes(self, **kwargs):  # noqa: E501
        """List of available nodes  # noqa: E501

        Get the list of available nodes in the installation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_available_nodes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_available_nodes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_available_nodes_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_available_nodes_with_http_info(self, **kwargs):  # noqa: E501
        """List of available nodes  # noqa: E501

        Get the list of available nodes in the installation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_available_nodes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_available_nodes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/nodes/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_sensor_device_group(self, device_group_name, **kwargs):  # noqa: E501
        """Get all All API's.  # noqa: E501

        GET sensors subscribed for a device-group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_sensor_device_group(device_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_group_name: Device Group (required)
        :param str authorization: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_sensor_device_group_with_http_info(device_group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_sensor_device_group_with_http_info(device_group_name, **kwargs)  # noqa: E501
            return data

    def retrieve_sensor_device_group_with_http_info(self, device_group_name, **kwargs):  # noqa: E501
        """Get all All API's.  # noqa: E501

        GET sensors subscribed for a device-group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_sensor_device_group_with_http_info(device_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_group_name: Device Group (required)
        :param str authorization: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_group_name', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_sensor_device_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_group_name' is set
        if ('device_group_name' not in params or
                params['device_group_name'] is None):
            raise ValueError("Missing the required parameter `device_group_name` when calling `retrieve_sensor_device_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_group_name' in params:
            path_params['device_group_name'] = params['device_group_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/config/sensor/device-group/{device_group_name}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_system_details(self, **kwargs):  # noqa: E501
        """Retrieve system details.  # noqa: E501

        Retrieve system details for HealthBot system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_system_details(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :param str service_name: service name takes in the name of the service for which details are required.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_system_details_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_system_details_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_system_details_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve system details.  # noqa: E501

        Retrieve system details for HealthBot system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_system_details_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :param str service_name: service name takes in the name of the service for which details are required.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'service_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_system_details" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'service_name' in params:
            query_params.append(('service_name', params['service_name']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/system-details/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_tsdb_counters(self, **kwargs):  # noqa: E501
        """TSDB counters  # noqa: E501

        Get TSDB counters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_tsdb_counters(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_tsdb_counters_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_tsdb_counters_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_tsdb_counters_with_http_info(self, **kwargs):  # noqa: E501
        """TSDB counters  # noqa: E501

        Get TSDB counters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_tsdb_counters_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_tsdb_counters" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tsdb-counters/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
