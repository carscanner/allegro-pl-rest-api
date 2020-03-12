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


class AfterSaleServicesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_public_seller_listing_using_get(self, seller_id, **kwargs):  # noqa: E501
        """Get the user's implied warranties  # noqa: E501

        Use this resource to get seller implied warranties listing. <a href=\"../../news/2017-04-05-news_warunki_oferty/\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_seller_listing_using_get(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str seller_id: Filter by user id. You are allowed to get your implied warranties only. (required)
        :param int limit: The limit of elements in the response.
        :param int offset: The offset of elements in the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ImpliedWarrantiesListImpliedWarrantyBasic
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_public_seller_listing_using_get_with_http_info(seller_id, **kwargs)  # noqa: E501

    def get_public_seller_listing_using_get_with_http_info(self, seller_id, **kwargs):  # noqa: E501
        """Get the user's implied warranties  # noqa: E501

        Use this resource to get seller implied warranties listing. <a href=\"../../news/2017-04-05-news_warunki_oferty/\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_seller_listing_using_get_with_http_info(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str seller_id: Filter by user id. You are allowed to get your implied warranties only. (required)
        :param int limit: The limit of elements in the response.
        :param int offset: The offset of elements in the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ImpliedWarrantiesListImpliedWarrantyBasic, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['seller_id', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_public_seller_listing_using_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'seller_id' is set
        if self.api_client.client_side_validation and ('seller_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['seller_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `seller_id` when calling `get_public_seller_listing_using_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 60:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_public_seller_listing_using_get`, must be a value less than or equal to `60`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_public_seller_listing_using_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] > 59:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_public_seller_listing_using_get`, must be a value less than or equal to `59`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_public_seller_listing_using_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'seller_id' in local_var_params and local_var_params['seller_id'] is not None:  # noqa: E501
            query_params.append(('seller.id', local_var_params['seller_id']))  # noqa: E501
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
            '/after-sales-service-conditions/implied-warranties', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ImpliedWarrantiesListImpliedWarrantyBasic',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_public_seller_listing_using_get1(self, seller_id, **kwargs):  # noqa: E501
        """Get the user's return policies  # noqa: E501

        Use this resource to get seller return policies listing. <a href=\"../../news/2017-04-05-news_warunki_oferty/\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_seller_listing_using_get1(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str seller_id: Filter by user id. You are allowed to get your return policies only. (required)
        :param int limit: The limit of elements in the response.
        :param int offset: The offset of elements in the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ReturnPoliciesListReturnPolicyBasic
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_public_seller_listing_using_get1_with_http_info(seller_id, **kwargs)  # noqa: E501

    def get_public_seller_listing_using_get1_with_http_info(self, seller_id, **kwargs):  # noqa: E501
        """Get the user's return policies  # noqa: E501

        Use this resource to get seller return policies listing. <a href=\"../../news/2017-04-05-news_warunki_oferty/\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_seller_listing_using_get1_with_http_info(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str seller_id: Filter by user id. You are allowed to get your return policies only. (required)
        :param int limit: The limit of elements in the response.
        :param int offset: The offset of elements in the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ReturnPoliciesListReturnPolicyBasic, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['seller_id', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_public_seller_listing_using_get1" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'seller_id' is set
        if self.api_client.client_side_validation and ('seller_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['seller_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `seller_id` when calling `get_public_seller_listing_using_get1`")  # noqa: E501

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 60:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_public_seller_listing_using_get1`, must be a value less than or equal to `60`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_public_seller_listing_using_get1`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] > 59:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_public_seller_listing_using_get1`, must be a value less than or equal to `59`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_public_seller_listing_using_get1`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'seller_id' in local_var_params and local_var_params['seller_id'] is not None:  # noqa: E501
            query_params.append(('seller.id', local_var_params['seller_id']))  # noqa: E501
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
            '/after-sales-service-conditions/return-policies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReturnPoliciesListReturnPolicyBasic',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_public_seller_listing_using_get2(self, seller_id, **kwargs):  # noqa: E501
        """Get the user's warranties  # noqa: E501

        Use this resource to get seller warranties listing. <a href=\"../../news/2017-04-05-news_warunki_oferty/\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_seller_listing_using_get2(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str seller_id: Filter by user id. You are allowed to get your warranties only. (required)
        :param int limit: The limit of elements in the response.
        :param int offset: The offset of elements in the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: WarrantiesListWarrantyBasic
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_public_seller_listing_using_get2_with_http_info(seller_id, **kwargs)  # noqa: E501

    def get_public_seller_listing_using_get2_with_http_info(self, seller_id, **kwargs):  # noqa: E501
        """Get the user's warranties  # noqa: E501

        Use this resource to get seller warranties listing. <a href=\"../../news/2017-04-05-news_warunki_oferty/\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_seller_listing_using_get2_with_http_info(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str seller_id: Filter by user id. You are allowed to get your warranties only. (required)
        :param int limit: The limit of elements in the response.
        :param int offset: The offset of elements in the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(WarrantiesListWarrantyBasic, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['seller_id', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_public_seller_listing_using_get2" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'seller_id' is set
        if self.api_client.client_side_validation and ('seller_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['seller_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `seller_id` when calling `get_public_seller_listing_using_get2`")  # noqa: E501

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 60:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_public_seller_listing_using_get2`, must be a value less than or equal to `60`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_public_seller_listing_using_get2`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] > 59:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_public_seller_listing_using_get2`, must be a value less than or equal to `59`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_public_seller_listing_using_get2`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'seller_id' in local_var_params and local_var_params['seller_id'] is not None:  # noqa: E501
            query_params.append(('seller.id', local_var_params['seller_id']))  # noqa: E501
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
            '/after-sales-service-conditions/warranties', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WarrantiesListWarrantyBasic',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)