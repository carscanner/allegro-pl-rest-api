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
from allegro_api.models.blacklist_request import BlacklistRequest  # noqa: E501
from allegro_api.rest import ApiException

class TestBlacklistRequest(unittest.TestCase):
    """BlacklistRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BlacklistRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.blacklist_request.BlacklistRequest()  # noqa: E501
        if include_optional :
            return BlacklistRequest(
                user = allegro_api.models.blacklist_user.BlacklistUser(
                    id = 123456, 
                    login = 'bad_buyer', ), 
                note = 'Rude person'
            )
        else :
            return BlacklistRequest(
        )

    def testBlacklistRequest(self):
        """Test BlacklistRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
