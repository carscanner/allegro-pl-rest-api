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
from allegro_api.api.listing_badges_api import ListingBadgesApi  # noqa: E501
from allegro_api.rest import ApiException


class TestListingBadgesApi(unittest.TestCase):
    """ListingBadgesApi unit test stubs"""

    def setUp(self):
        self.api = allegro_api.api.listing_badges_api.ListingBadgesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_promotion_to_campaign_using_post(self):
        """Test case for add_promotion_to_campaign_using_post

        Create an application for a promotion campaign  # noqa: E501
        """
        pass

    def test_delete_campaign_from_promotion_using_delete(self):
        """Test case for delete_campaign_from_promotion_using_delete

        Delete a campaign in a promotion  # noqa: E501
        """
        pass

    def test_delete_promotion_campaign_application_using_delete(self):
        """Test case for delete_promotion_campaign_application_using_delete

        Delete an application for promotion campaign  # noqa: E501
        """
        pass

    def test_get_promotion_campaign_application_using_get(self):
        """Test case for get_promotion_campaign_application_using_get

        Get an application for promotion campaign  # noqa: E501
        """
        pass

    def test_get_promotion_campaigns_using_get(self):
        """Test case for get_promotion_campaigns_using_get

        Get the user's promotion campaigns  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
