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


class OfferTagsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def assign_tag_to_offer_post(self, offer_id, tag_ids_request, **kwargs):  # noqa: E501
        """Assign tags to an offer  # noqa: E501

        Use this resource to assign a tag to offer. <a href=\"../../news/2018-09-24-tagi-zalaczniki/#PrzypiszTagiDoOferty\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.assign_tag_to_offer_post(offer_id, tag_ids_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str offer_id: Offer identifier. (required)
        :param TagIdsRequest tag_ids_request: request (required)
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
        return self.assign_tag_to_offer_post_with_http_info(offer_id, tag_ids_request, **kwargs)  # noqa: E501

    def assign_tag_to_offer_post_with_http_info(self, offer_id, tag_ids_request, **kwargs):  # noqa: E501
        """Assign tags to an offer  # noqa: E501

        Use this resource to assign a tag to offer. <a href=\"../../news/2018-09-24-tagi-zalaczniki/#PrzypiszTagiDoOferty\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.assign_tag_to_offer_post_with_http_info(offer_id, tag_ids_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str offer_id: Offer identifier. (required)
        :param TagIdsRequest tag_ids_request: request (required)
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

        all_params = ['offer_id', 'tag_ids_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method assign_tag_to_offer_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'offer_id' is set
        if self.api_client.client_side_validation and ('offer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['offer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `offer_id` when calling `assign_tag_to_offer_post`")  # noqa: E501
        # verify the required parameter 'tag_ids_request' is set
        if self.api_client.client_side_validation and ('tag_ids_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['tag_ids_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `tag_ids_request` when calling `assign_tag_to_offer_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'offer_id' in local_var_params:
            path_params['offerId'] = local_var_params['offer_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tag_ids_request' in local_var_params:
            body_params = local_var_params['tag_ids_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-token-for-user']  # noqa: E501

        return self.api_client.call_api(
            '/sale/offers/{offerId}/tags', 'POST',
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

    def create_tag_post1(self, tag_request, **kwargs):  # noqa: E501
        """Create a tag  # noqa: E501

        Use this resource to create a new tag. <a href=\"../../news/2018-09-24-tagi-zalaczniki/#DodajDoKonta\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tag_post1(tag_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TagRequest tag_request: request (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TagId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_tag_post1_with_http_info(tag_request, **kwargs)  # noqa: E501

    def create_tag_post1_with_http_info(self, tag_request, **kwargs):  # noqa: E501
        """Create a tag  # noqa: E501

        Use this resource to create a new tag. <a href=\"../../news/2018-09-24-tagi-zalaczniki/#DodajDoKonta\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tag_post1_with_http_info(tag_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TagRequest tag_request: request (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TagId, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tag_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_tag_post1" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tag_request' is set
        if self.api_client.client_side_validation and ('tag_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['tag_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `tag_request` when calling `create_tag_post1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tag_request' in local_var_params:
            body_params = local_var_params['tag_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-token-for-user']  # noqa: E501

        return self.api_client.call_api(
            '/sale/offer-tags', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagId',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_tag_using_delete(self, tag_id, **kwargs):  # noqa: E501
        """Delete a tag  # noqa: E501

        Use this resource to delete the tag. <a href=\"../../news/2018-09-24-tagi-zalaczniki/#UsunTagZKonta\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tag_using_delete(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tag_id: Tag identifier. (required)
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
        return self.delete_tag_using_delete_with_http_info(tag_id, **kwargs)  # noqa: E501

    def delete_tag_using_delete_with_http_info(self, tag_id, **kwargs):  # noqa: E501
        """Delete a tag  # noqa: E501

        Use this resource to delete the tag. <a href=\"../../news/2018-09-24-tagi-zalaczniki/#UsunTagZKonta\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tag_using_delete_with_http_info(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tag_id: Tag identifier. (required)
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

        all_params = ['tag_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_tag_using_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tag_id' is set
        if self.api_client.client_side_validation and ('tag_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['tag_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `tag_id` when calling `delete_tag_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag_id' in local_var_params:
            path_params['tagId'] = local_var_params['tag_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*', 'application/vnd.allegro.public.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-token-for-user']  # noqa: E501

        return self.api_client.call_api(
            '/sale/offer-tags/{tagId}', 'DELETE',
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

    def list_assigned_offer_tags_get(self, offer_id, **kwargs):  # noqa: E501
        """Get tags assigned to an offer  # noqa: E501

        Use this resource to get a list of tags assigned to offer. <a href=\"../../news/2018-09-24-tagi-zalaczniki/#PobierzTagiZOferty\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_assigned_offer_tags_get(offer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str offer_id: Offer identifier. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TagListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_assigned_offer_tags_get_with_http_info(offer_id, **kwargs)  # noqa: E501

    def list_assigned_offer_tags_get_with_http_info(self, offer_id, **kwargs):  # noqa: E501
        """Get tags assigned to an offer  # noqa: E501

        Use this resource to get a list of tags assigned to offer. <a href=\"../../news/2018-09-24-tagi-zalaczniki/#PobierzTagiZOferty\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_assigned_offer_tags_get_with_http_info(offer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str offer_id: Offer identifier. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TagListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['offer_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_assigned_offer_tags_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'offer_id' is set
        if self.api_client.client_side_validation and ('offer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['offer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `offer_id` when calling `list_assigned_offer_tags_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'offer_id' in local_var_params:
            path_params['offerId'] = local_var_params['offer_id']  # noqa: E501

        query_params = []

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
            '/sale/offers/{offerId}/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_seller_tags_get1(self, user_id, **kwargs):  # noqa: E501
        """Get the user's tags  # noqa: E501

        Use this resource to get a list of tags defined by the specified user (Defaults: limit = 1000, offset = 0). <a href=\"../../news/2018-09-24-tagi-zalaczniki/#PobierzTagi\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_seller_tags_get1(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str user_id: User identifier. (required)
        :param int limit: The limit of elements in the response.
        :param int offset: The offset of elements in the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TagListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_seller_tags_get1_with_http_info(user_id, **kwargs)  # noqa: E501

    def list_seller_tags_get1_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Get the user's tags  # noqa: E501

        Use this resource to get a list of tags defined by the specified user (Defaults: limit = 1000, offset = 0). <a href=\"../../news/2018-09-24-tagi-zalaczniki/#PobierzTagi\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_seller_tags_get1_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str user_id: User identifier. (required)
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
        :return: tuple(TagListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['user_id', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_seller_tags_get1" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['user_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id` when calling `list_seller_tags_get1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in local_var_params and local_var_params['user_id'] is not None:  # noqa: E501
            query_params.append(('user.id', local_var_params['user_id']))  # noqa: E501
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
            '/sale/offer-tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_tag_put(self, tag_id, tag_request, **kwargs):  # noqa: E501
        """Modify a tag  # noqa: E501

        Use this resource to update a tag. <a href=\"../../news/2018-09-24-tagi-zalaczniki/#ZmienNazwe\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_tag_put(tag_id, tag_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tag_id: Tag identifier. (required)
        :param TagRequest tag_request: request (required)
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
        return self.update_tag_put_with_http_info(tag_id, tag_request, **kwargs)  # noqa: E501

    def update_tag_put_with_http_info(self, tag_id, tag_request, **kwargs):  # noqa: E501
        """Modify a tag  # noqa: E501

        Use this resource to update a tag. <a href=\"../../news/2018-09-24-tagi-zalaczniki/#ZmienNazwe\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_tag_put_with_http_info(tag_id, tag_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tag_id: Tag identifier. (required)
        :param TagRequest tag_request: request (required)
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

        all_params = ['tag_id', 'tag_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_tag_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tag_id' is set
        if self.api_client.client_side_validation and ('tag_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['tag_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `tag_id` when calling `update_tag_put`")  # noqa: E501
        # verify the required parameter 'tag_request' is set
        if self.api_client.client_side_validation and ('tag_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['tag_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `tag_request` when calling `update_tag_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag_id' in local_var_params:
            path_params['tagId'] = local_var_params['tag_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tag_request' in local_var_params:
            body_params = local_var_params['tag_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-token-for-user']  # noqa: E501

        return self.api_client.call_api(
            '/sale/offer-tags/{tagId}', 'PUT',
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
