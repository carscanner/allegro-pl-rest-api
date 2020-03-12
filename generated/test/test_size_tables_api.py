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
from allegro_api.api.size_tables_api import SizeTablesApi  # noqa: E501
from allegro_api.rest import ApiException


class TestSizeTablesApi(unittest.TestCase):
    """SizeTablesApi unit test stubs"""

    def setUp(self):
        self.api = allegro_api.api.size_tables_api.SizeTablesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_table_using_get(self):
        """Test case for get_table_using_get

        Get a size table details  # noqa: E501
        """
        pass

    def test_get_tables_using_get(self):
        """Test case for get_tables_using_get

        Get the user's size tables  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
