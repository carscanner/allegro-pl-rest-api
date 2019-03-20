# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    OpenAPI spec version: latest
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient


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

        Use this resource to get seller implied warranties listing. More information about this resource you can find <a href=\"../../news/2017-04-05-news_warunki_oferty/\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_seller_listing_using_get(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str seller_id: Filter by user id. You are allowed to get your implied warranties only. (required)
        :param int limit: Limit
        :param int offset: Offset
        :return: ImpliedWarrantiesListImpliedWarrantyBasic
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_public_seller_listing_using_get_with_http_info(seller_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_public_seller_listing_using_get_with_http_info(seller_id, **kwargs)  # noqa: E501
            return data

    def get_public_seller_listing_using_get_with_http_info(self, seller_id, **kwargs):  # noqa: E501
        """Get the user's implied warranties  # noqa: E501

        Use this resource to get seller implied warranties listing. More information about this resource you can find <a href=\"../../news/2017-04-05-news_warunki_oferty/\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_seller_listing_using_get_with_http_info(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str seller_id: Filter by user id. You are allowed to get your implied warranties only. (required)
        :param int limit: Limit
        :param int offset: Offset
        :return: ImpliedWarrantiesListImpliedWarrantyBasic
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
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_public_seller_listing_using_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'seller_id' is set
        if ('seller_id' not in local_var_params or
                local_var_params['seller_id'] is None):
            raise ValueError("Missing the required parameter `seller_id` when calling `get_public_seller_listing_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'seller_id' in local_var_params:
            query_params.append(('seller.id', local_var_params['seller_id']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
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

        Use this resource to get seller return policies listing. More information about this resource you can find <a href=\"../../news/2017-04-05-news_warunki_oferty/\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_seller_listing_using_get1(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str seller_id: Filter by user id. You are allowed to get your return policies only. (required)
        :param int limit: Limit
        :param int offset: Offset
        :return: ReturnPoliciesListReturnPolicyBasic
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_public_seller_listing_using_get1_with_http_info(seller_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_public_seller_listing_using_get1_with_http_info(seller_id, **kwargs)  # noqa: E501
            return data

    def get_public_seller_listing_using_get1_with_http_info(self, seller_id, **kwargs):  # noqa: E501
        """Get the user's return policies  # noqa: E501

        Use this resource to get seller return policies listing. More information about this resource you can find <a href=\"../../news/2017-04-05-news_warunki_oferty/\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_seller_listing_using_get1_with_http_info(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str seller_id: Filter by user id. You are allowed to get your return policies only. (required)
        :param int limit: Limit
        :param int offset: Offset
        :return: ReturnPoliciesListReturnPolicyBasic
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
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_public_seller_listing_using_get1" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'seller_id' is set
        if ('seller_id' not in local_var_params or
                local_var_params['seller_id'] is None):
            raise ValueError("Missing the required parameter `seller_id` when calling `get_public_seller_listing_using_get1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'seller_id' in local_var_params:
            query_params.append(('seller.id', local_var_params['seller_id']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
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

        Use this resource to get seller warranties listing. More information about this resource you can find <a href=\"../../news/2017-04-05-news_warunki_oferty/\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_seller_listing_using_get2(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str seller_id: Filter by user id. You are allowed to get your warranties only. (required)
        :param int limit: Limit
        :param int offset: Offset
        :return: WarrantiesListWarrantyBasic
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_public_seller_listing_using_get2_with_http_info(seller_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_public_seller_listing_using_get2_with_http_info(seller_id, **kwargs)  # noqa: E501
            return data

    def get_public_seller_listing_using_get2_with_http_info(self, seller_id, **kwargs):  # noqa: E501
        """Get the user's warranties  # noqa: E501

        Use this resource to get seller warranties listing. More information about this resource you can find <a href=\"../../news/2017-04-05-news_warunki_oferty/\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_seller_listing_using_get2_with_http_info(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str seller_id: Filter by user id. You are allowed to get your warranties only. (required)
        :param int limit: Limit
        :param int offset: Offset
        :return: WarrantiesListWarrantyBasic
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
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_public_seller_listing_using_get2" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'seller_id' is set
        if ('seller_id' not in local_var_params or
                local_var_params['seller_id'] is None):
            raise ValueError("Missing the required parameter `seller_id` when calling `get_public_seller_listing_using_get2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'seller_id' in local_var_params:
            query_params.append(('seller.id', local_var_params['seller_id']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
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
