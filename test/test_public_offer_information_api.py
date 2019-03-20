# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    OpenAPI spec version: latest
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import allegro_api
from allegro_api.api.public_offer_information_api import PublicOfferInformationApi  # noqa: E501
from allegro_api.rest import ApiException


class TestPublicOfferInformationApi(unittest.TestCase):
    """PublicOfferInformationApi unit test stubs"""

    def setUp(self):
        self.api = allegro_api.api.public_offer_information_api.PublicOfferInformationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_listing(self):
        """Test case for get_listing

        Search offers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
