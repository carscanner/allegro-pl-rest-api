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

from allegro_api.api_client import ApiClient


class ImagesAndAttachmentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_offer_attachment_using_post(self, offer_attachment_request, **kwargs):  # noqa: E501
        """Create an offer attachment  # noqa: E501

        Creates attachment and returns location header for file upload  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_offer_attachment_using_post(offer_attachment_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OfferAttachmentRequest offer_attachment_request: offer attachment (required)
        :return: OfferAttachment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_offer_attachment_using_post_with_http_info(offer_attachment_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_offer_attachment_using_post_with_http_info(offer_attachment_request, **kwargs)  # noqa: E501
            return data

    def create_offer_attachment_using_post_with_http_info(self, offer_attachment_request, **kwargs):  # noqa: E501
        """Create an offer attachment  # noqa: E501

        Creates attachment and returns location header for file upload  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_offer_attachment_using_post_with_http_info(offer_attachment_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OfferAttachmentRequest offer_attachment_request: offer attachment (required)
        :return: OfferAttachment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['offer_attachment_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_offer_attachment_using_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'offer_attachment_request' is set
        if ('offer_attachment_request' not in local_var_params or
                local_var_params['offer_attachment_request'] is None):
            raise ValueError("Missing the required parameter `offer_attachment_request` when calling `create_offer_attachment_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'offer_attachment_request' in local_var_params:
            body_params = local_var_params['offer_attachment_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-token-for-user']  # noqa: E501

        return self.api_client.call_api(
            '/sale/offer-attachments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OfferAttachment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)