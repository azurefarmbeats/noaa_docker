# coding: utf-8

"""
    Azure FarmBeats API

    <p> <p>Azure FarmBeats helps you build digital agricultural solutions in Azure. By providing a standardized schema to query agricultural data from various sources, Azure FarmBeats provides you: <ul >  <li style=\"margin: 7px;\">Ability to acquire, aggregate, process and store agricultural data.</li>  <li style=\"margin: 7px;\">Capability to fuse data between data sources and generate insights.</li>  <li style=\"margin: 7px;\">Schematized access and query capabilities on ingested data.</li> </ul> </p> <h><b>REST Operation Groups</b></h> <p><b>Farm:</b></p> <p>Farm corresponds to a physical location of interest within the system. Each Farm has a Farm name and a unique farm id.</p> <p><b>Device:</b></p> <p>Device corresponds to a physical device present in the farm. Each device has a unique device id. Device is typically provisioned to a farm with a farm id.</p> <p><b>DeviceModel:</b></p> <p>DeviceModel corresponds to the meta-data of the device such as the Manufacturer, Type of the device either Gateway or Node.</p> <p><b>Sensor:</b></p> <p>Sensor corresponds to a physical sensor that records values. A sensor is typically connected to a device with a device id.</p> </p> <p><b>SensorModel:</b></p> <p>SensorModel corresponds to the meta-data of the sensor such as the Manufacturer, Type of the sensor either Analog or Digital, Sensor Measure such as Ambient Temperature, Pressure etc.</p> <p><b>Telemetry:</b></p> <p>Telemetry provides the ability to read telemetry messages for a particular sensor & time range.</p> <p><b>Job:</b></p> <p>Job corresponds to any workflow of activities which are executed in the system to get a desired output. Each job is associated with a job id and job type.</p> <p><b>JobType:</b></p> <p>JobType corresponds to different job types supported by the system. This includes system defined & user-defined job types.</p> <p><b>ExtendedType:</b></p> <p>ExtendedType corresponds to the list of system & user-defined types in the system. This helps setup a new Sensor or Scene or Scenefile type in the system.</p> <p><b>Partner:</b></p> <p>Partner corresponds to the sensor/weather/imagery integration partner.</p> <p><b>Scene:</b></p> <p>Scene corresponds to any generated output in the context of a Farm. Each Scene has a scene id, scene source, scene type and farm id associated with it. Each scene id  can have multiple scene files associated with it.</p> <p><b>SceneFile:</b></p> <p>SceneFile corresponds to all files which are generated for single scene. A single scene id can have multiple SceneFile ids associated with it.</p> <p><b>Rule:</b></p> <p>Rule corresponds to a condition for farm-related data to trigger an alert. Each rule will be in the context of a farm's data.</p> <p><b>Alert:</b></p> <p>Alert corresponds to a notification which gets generated when a rule condition is met. Each alert will be in the context of a rule.</p> <p><b>RoleDefinition:</b></p> <p>RoleDefinition defines allowed and disallowed actions for a role.</p> <p><b>RoleAssignment:</b></p> <p>RoleAssignment corresponds to the assignment of a role to a user or a service principal.</p> </p>   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from datahub_lib.swagger_client.api_client import ApiClient
from datahub_lib.swagger_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class FarmApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def farm_create(self, **kwargs):  # noqa: E501
        """Creates new farm with given request body.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farm_create(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param FarmRequest input: Farm request object.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: FarmResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.farm_create_with_http_info(**kwargs)  # noqa: E501

    def farm_create_with_http_info(self, **kwargs):  # noqa: E501
        """Creates new farm with given request body.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farm_create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param FarmRequest input: Farm request object.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(FarmResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['input']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method farm_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input' in local_var_params:
            body_params = local_var_params['input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/Farm', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FarmResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def farm_delete(self, id, **kwargs):  # noqa: E501
        """Deletes the farm with given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farm_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Id of the farm object. (required)
        :param bool force: Gets or sets a value indicating whether force delete is allowed.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.farm_delete_with_http_info(id, **kwargs)  # noqa: E501

    def farm_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Deletes the farm with given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farm_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Id of the farm object. (required)
        :param bool force: Gets or sets a value indicating whether force delete is allowed.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'force']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method farm_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `farm_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'force' in local_var_params and local_var_params['force'] is not None:  # noqa: E501
            query_params.append(('force', local_var_params['force']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/Farm/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def farm_get(self, id, **kwargs):  # noqa: E501
        """Returns farm for the given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farm_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Id of the farm object. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: FarmResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.farm_get_with_http_info(id, **kwargs)  # noqa: E501

    def farm_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns farm for the given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farm_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Id of the farm object. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(FarmResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method farm_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `farm_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/Farm/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FarmResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def farm_get_all(self, **kwargs):  # noqa: E501
        """Returns list of farms.  # noqa: E501

        based on specified filters and date range. Requires ReadAll privileges.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farm_get_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] names: Gets or sets list of names of farms.
        :param list[str] ids: Gets or sets ids of the resource.
        :param str partner_id: Gets or sets id of the partner.
        :param datetime min_created_at: Gets or sets minimum creation date of resource (inclusive).
        :param datetime max_created_at: Gets or sets maximum creation date of resource (inclusive).
        :param datetime min_last_modified_at: Gets or sets minimum last modified date of resource (inclusive).
        :param datetime max_last_modified_at: Gets or sets maximum last modified date of resource (inclusive).
        :param str property_filter: Gets or sets property filter query.eg. \"x.y.z eq 'somestringvalue' and p.q gt 5 and a eq false\".  Only AND operation is supported.  Supported Operators: EQ,NE,LE,LT,GT,GE,CONTAINS,NCONTAINS.
        :param int max_items: Gets or sets maximum number of items needed (inclusive).  Maximum items = 5000.
        :param str x_ms_continuation: Gets or sets continuation token.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: FarmResponseListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.farm_get_all_with_http_info(**kwargs)  # noqa: E501

    def farm_get_all_with_http_info(self, **kwargs):  # noqa: E501
        """Returns list of farms.  # noqa: E501

        based on specified filters and date range. Requires ReadAll privileges.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farm_get_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] names: Gets or sets list of names of farms.
        :param list[str] ids: Gets or sets ids of the resource.
        :param str partner_id: Gets or sets id of the partner.
        :param datetime min_created_at: Gets or sets minimum creation date of resource (inclusive).
        :param datetime max_created_at: Gets or sets maximum creation date of resource (inclusive).
        :param datetime min_last_modified_at: Gets or sets minimum last modified date of resource (inclusive).
        :param datetime max_last_modified_at: Gets or sets maximum last modified date of resource (inclusive).
        :param str property_filter: Gets or sets property filter query.eg. \"x.y.z eq 'somestringvalue' and p.q gt 5 and a eq false\".  Only AND operation is supported.  Supported Operators: EQ,NE,LE,LT,GT,GE,CONTAINS,NCONTAINS.
        :param int max_items: Gets or sets maximum number of items needed (inclusive).  Maximum items = 5000.
        :param str x_ms_continuation: Gets or sets continuation token.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(FarmResponseListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['names', 'ids', 'partner_id', 'min_created_at', 'max_created_at', 'min_last_modified_at', 'max_last_modified_at', 'property_filter', 'max_items', 'x_ms_continuation']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method farm_get_all" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'max_items' in local_var_params and local_var_params['max_items'] > 5000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `max_items` when calling `farm_get_all`, must be a value less than or equal to `5000`")  # noqa: E501
        if self.api_client.client_side_validation and 'max_items' in local_var_params and local_var_params['max_items'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `max_items` when calling `farm_get_all`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'names' in local_var_params and local_var_params['names'] is not None:  # noqa: E501
            query_params.append(('names', local_var_params['names']))  # noqa: E501
            collection_formats['names'] = 'multi'  # noqa: E501
        if 'ids' in local_var_params and local_var_params['ids'] is not None:  # noqa: E501
            query_params.append(('ids', local_var_params['ids']))  # noqa: E501
            collection_formats['ids'] = 'multi'  # noqa: E501
        if 'partner_id' in local_var_params and local_var_params['partner_id'] is not None:  # noqa: E501
            query_params.append(('PartnerId', local_var_params['partner_id']))  # noqa: E501
        if 'min_created_at' in local_var_params and local_var_params['min_created_at'] is not None:  # noqa: E501
            query_params.append(('minCreatedAt', local_var_params['min_created_at']))  # noqa: E501
        if 'max_created_at' in local_var_params and local_var_params['max_created_at'] is not None:  # noqa: E501
            query_params.append(('maxCreatedAt', local_var_params['max_created_at']))  # noqa: E501
        if 'min_last_modified_at' in local_var_params and local_var_params['min_last_modified_at'] is not None:  # noqa: E501
            query_params.append(('minLastModifiedAt', local_var_params['min_last_modified_at']))  # noqa: E501
        if 'max_last_modified_at' in local_var_params and local_var_params['max_last_modified_at'] is not None:  # noqa: E501
            query_params.append(('maxLastModifiedAt', local_var_params['max_last_modified_at']))  # noqa: E501
        if 'property_filter' in local_var_params and local_var_params['property_filter'] is not None:  # noqa: E501
            query_params.append(('propertyFilter', local_var_params['property_filter']))  # noqa: E501
        if 'max_items' in local_var_params and local_var_params['max_items'] is not None:  # noqa: E501
            query_params.append(('maxItems', local_var_params['max_items']))  # noqa: E501

        header_params = {}
        if 'x_ms_continuation' in local_var_params:
            header_params['x-ms-continuation'] = local_var_params['x_ms_continuation']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/Farm', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FarmResponseListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def farm_update(self, id, **kwargs):  # noqa: E501
        """Updates the farm with given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farm_update(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Id of the farm. (required)
        :param FarmRequest input: Farm request object.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.farm_update_with_http_info(id, **kwargs)  # noqa: E501

    def farm_update_with_http_info(self, id, **kwargs):  # noqa: E501
        """Updates the farm with given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farm_update_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Id of the farm. (required)
        :param FarmRequest input: Farm request object.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'input']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method farm_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `farm_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input' in local_var_params:
            body_params = local_var_params['input']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/Farm/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
