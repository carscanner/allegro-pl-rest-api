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
from allegro_api.api.user_information_api import UserInformationApi  # noqa: E501
from allegro_api.rest import ApiException


class TestUserInformationApi(unittest.TestCase):
    """UserInformationApi unit test stubs"""

    def setUp(self):
        self.api = allegro_api.api.user_information_api.UserInformationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_user_ratings_using_get(self):
        """Test case for get_user_ratings_using_get

        Get the user's ratings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()