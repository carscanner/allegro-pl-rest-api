# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    The version of the OpenAPI document: 2020.03.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from allegro_api.api_client import ApiClient
from allegro_api.exceptions import (
    ApiTypeError,
    ApiValueError
)


class BillingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_billing_entries(self, **kwargs):  # noqa: E501
        """Get a list of billing entries  # noqa: E501

        The billing entries are sorted in a descending order (newest first) by date on which they occurred.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_billing_entries(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param datetime occurred_at_gte: Date from which billing entries are filtered. If occurredAt.lte is also set, occurredAt.gte cannot be later.
        :param datetime occurred_at_lte: Date to which billing entries are filtered. If occurredAt.gte is also set, occurredAt.lte cannot be earlier.
        :param list[str] type_id: List of billing types by which billing entries are filtered.
        :param str offer_id: Offer ID by which billing entries are filtered.
        :param int limit: Number of returned operations.
        :param int offset: Index of the first returned payment operation from all search results.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_billing_entries_with_http_info(**kwargs)  # noqa: E501

    def get_billing_entries_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of billing entries  # noqa: E501

        The billing entries are sorted in a descending order (newest first) by date on which they occurred.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_billing_entries_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param datetime occurred_at_gte: Date from which billing entries are filtered. If occurredAt.lte is also set, occurredAt.gte cannot be later.
        :param datetime occurred_at_lte: Date to which billing entries are filtered. If occurredAt.gte is also set, occurredAt.lte cannot be earlier.
        :param list[str] type_id: List of billing types by which billing entries are filtered.
        :param str offer_id: Offer ID by which billing entries are filtered.
        :param int limit: Number of returned operations.
        :param int offset: Index of the first returned payment operation from all search results.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['occurred_at_gte', 'occurred_at_lte', 'type_id', 'offer_id', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_billing_entries" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_billing_entries`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_billing_entries`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_billing_entries`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_billing_entries`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'occurred_at_gte' in local_var_params and local_var_params['occurred_at_gte'] is not None:  # noqa: E501
            query_params.append(('occurredAt.gte', local_var_params['occurred_at_gte']))  # noqa: E501
        if 'occurred_at_lte' in local_var_params and local_var_params['occurred_at_lte'] is not None:  # noqa: E501
            query_params.append(('occurredAt.lte', local_var_params['occurred_at_lte']))  # noqa: E501
        if 'type_id' in local_var_params and local_var_params['type_id'] is not None:  # noqa: E501
            query_params.append(('type.id', local_var_params['type_id']))  # noqa: E501
            collection_formats['type.id'] = 'multi'  # noqa: E501
        if 'offer_id' in local_var_params and local_var_params['offer_id'] is not None:  # noqa: E501
            query_params.append(('offer.id', local_var_params['offer_id']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-token-for-user']  # noqa: E501

        return self.api_client.call_api(
            '/billing/billing-entries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
