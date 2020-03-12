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
from allegro_api.api.information_about_user_api import InformationAboutUserApi  # noqa: E501
from allegro_api.rest import ApiException


class TestInformationAboutUserApi(unittest.TestCase):
    """InformationAboutUserApi unit test stubs"""

    def setUp(self):
        self.api = allegro_api.api.information_about_user_api.InformationAboutUserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_additional_email_using_post(self):
        """Test case for add_additional_email_using_post

        Add a new additional email address to user's account  # noqa: E501
        """
        pass

    def test_answer_user_rating_using_put(self):
        """Test case for answer_user_rating_using_put

        Answer for user's rating  # noqa: E501
        """
        pass

    def test_delete_additional_email_using_delete(self):
        """Test case for delete_additional_email_using_delete

        Delete an additional email address  # noqa: E501
        """
        pass

    def test_get_additional_email_using_get(self):
        """Test case for get_additional_email_using_get

        Get information about a particular additional email  # noqa: E501
        """
        pass

    def test_get_list_of_additional_emails_using_get(self):
        """Test case for get_list_of_additional_emails_using_get

        Get user's additional emails  # noqa: E501
        """
        pass

    def test_get_user_ratings_using_get(self):
        """Test case for get_user_ratings_using_get

        Get the user's ratings  # noqa: E501
        """
        pass

    def test_me_get(self):
        """Test case for me_get

        Get basic information about user  # noqa: E501
        """
        pass

    def test_user_rating_removal_using_put(self):
        """Test case for user_rating_removal_using_put

        Request removal of user's rating  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
