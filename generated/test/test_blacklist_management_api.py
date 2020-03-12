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
from allegro_api.api.blacklist_management_api import BlacklistManagementApi  # noqa: E501
from allegro_api.rest import ApiException


class TestBlacklistManagementApi(unittest.TestCase):
    """BlacklistManagementApi unit test stubs"""

    def setUp(self):
        self.api = allegro_api.api.blacklist_management_api.BlacklistManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_do_add_to_black_list(self):
        """Test case for do_add_to_black_list

        Add a users to the blacklist  # noqa: E501
        """
        pass

    def test_do_get_black_list_users(self):
        """Test case for do_get_black_list_users

        Get list of blacklisted users  # noqa: E501
        """
        pass

    def test_do_remove_from_black_list(self):
        """Test case for do_remove_from_black_list

        Remove users from the blacklist  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()