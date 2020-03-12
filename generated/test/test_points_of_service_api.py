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
from allegro_api.api.points_of_service_api import PointsOfServiceApi  # noqa: E501
from allegro_api.rest import ApiException


class TestPointsOfServiceApi(unittest.TestCase):
    """PointsOfServiceApi unit test stubs"""

    def setUp(self):
        self.api = allegro_api.api.points_of_service_api.PointsOfServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_pos_using_post(self):
        """Test case for create_pos_using_post

        Create a point of service  # noqa: E501
        """
        pass

    def test_delete_pos_using_delete(self):
        """Test case for delete_pos_using_delete

        Delete a point of service  # noqa: E501
        """
        pass

    def test_get_pos_data_using_get(self):
        """Test case for get_pos_data_using_get

        Get the details of a point of service  # noqa: E501
        """
        pass

    def test_get_pos_list_using_get(self):
        """Test case for get_pos_list_using_get

        Get the user's points of service  # noqa: E501
        """
        pass

    def test_modify_pos_using_put(self):
        """Test case for modify_pos_using_put

        Modify a point of service  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
