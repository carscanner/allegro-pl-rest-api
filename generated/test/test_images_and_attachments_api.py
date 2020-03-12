# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    The version of the OpenAPI document: 2020.03.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import allegro_api
from allegro_api.api.images_and_attachments_api import ImagesAndAttachmentsApi  # noqa: E501
from allegro_api.rest import ApiException


class TestImagesAndAttachmentsApi(unittest.TestCase):
    """ImagesAndAttachmentsApi unit test stubs"""

    def setUp(self):
        self.api = allegro_api.api.images_and_attachments_api.ImagesAndAttachmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_offer_attachment_using_post(self):
        """Test case for create_offer_attachment_using_post

        Create an offer attachment  # noqa: E501
        """
        pass

    def test_upload_offer_attachment_using_put(self):
        """Test case for upload_offer_attachment_using_put

        Upload an offer attachment  # noqa: E501
        """
        pass

    def test_upload_offer_image_using_post(self):
        """Test case for upload_offer_image_using_post

        Upload an offer image  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()