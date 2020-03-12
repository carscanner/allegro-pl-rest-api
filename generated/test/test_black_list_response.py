# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    The version of the OpenAPI document: 2020.03.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import allegro_api
from allegro_api.models.black_list_response import BlackListResponse  # noqa: E501
from allegro_api.rest import ApiException

class TestBlackListResponse(unittest.TestCase):
    """BlackListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BlackListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.black_list_response.BlackListResponse()  # noqa: E501
        if include_optional :
            return BlackListResponse(
                user = allegro_api.models.blacklist_user.BlacklistUser(
                    id = 123456, 
                    login = 'bad_buyer', ), 
                note = 'Rude person', 
                created_at = '2019-05-08T09:45:43.818Z'
            )
        else :
            return BlackListResponse(
        )

    def testBlackListResponse(self):
        """Test BlackListResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
