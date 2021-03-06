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
from allegro_api.api.sets_and_rebates_api import SetsAndRebatesApi  # noqa: E501
from allegro_api.rest import ApiException


class TestSetsAndRebatesApi(unittest.TestCase):
    """SetsAndRebatesApi unit test stubs"""

    def setUp(self):
        self.api = allegro_api.api.sets_and_rebates_api.SetsAndRebatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_promotion_using_post1(self):
        """Test case for create_promotion_using_post1

        Create a new promotion  # noqa: E501
        """
        pass

    def test_deactivate_promotion_using_delete(self):
        """Test case for deactivate_promotion_using_delete

        Deactivate a promotion by id  # noqa: E501
        """
        pass

    def test_get_promotion_using_get(self):
        """Test case for get_promotion_using_get

        Get a promotion data by id  # noqa: E501
        """
        pass

    def test_list_seller_promotions_using_get1(self):
        """Test case for list_seller_promotions_using_get1

        Get the user's list of promotions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
