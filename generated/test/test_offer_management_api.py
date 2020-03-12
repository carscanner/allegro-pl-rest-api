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
from allegro_api.api.offer_management_api import OfferManagementApi  # noqa: E501
from allegro_api.rest import ApiException


class TestOfferManagementApi(unittest.TestCase):
    """OfferManagementApi unit test stubs"""

    def setUp(self):
        self.api = allegro_api.api.offer_management_api.OfferManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_publication_status_using_put(self):
        """Test case for change_publication_status_using_put

        Batch offer publish / unpublish  # noqa: E501
        """
        pass

    def test_create_change_price_command_using_put(self):
        """Test case for create_change_price_command_using_put

        Modify the Buy Now price in an offer  # noqa: E501
        """
        pass

    def test_create_offer_using_post(self):
        """Test case for create_offer_using_post

        Create a draft offer  # noqa: E501
        """
        pass

    def test_delete_offer_using_delete(self):
        """Test case for delete_offer_using_delete

        Delete a draft offer  # noqa: E501
        """
        pass

    def test_get_publication_report_using_get(self):
        """Test case for get_publication_report_using_get

        Publish command summary  # noqa: E501
        """
        pass

    def test_get_publication_tasks_using_get(self):
        """Test case for get_publication_tasks_using_get

        Publish command detailed report  # noqa: E501
        """
        pass

    def test_update_offer_using_put(self):
        """Test case for update_offer_using_put

        Complete a draft offer or edit an offer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
