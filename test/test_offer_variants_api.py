# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    OpenAPI spec version: latest
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.offer_variants_api import OfferVariantsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestOfferVariantsApi(unittest.TestCase):
    """OfferVariantsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.offer_variants_api.OfferVariantsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_or_update_variant_set(self):
        """Test case for create_or_update_variant_set

        [BETA] Create or update variant set  # noqa: E501
        """
        pass

    def test_delete_variant_set(self):
        """Test case for delete_variant_set

        [BETA] Delete a variant set  # noqa: E501
        """
        pass

    def test_get_variant_set(self):
        """Test case for get_variant_set

        [BETA] Get a variant set  # noqa: E501
        """
        pass

    def test_get_variant_sets(self):
        """Test case for get_variant_sets

        [BETA] Get the user's variant sets  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
