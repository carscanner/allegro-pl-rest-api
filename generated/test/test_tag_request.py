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
from allegro_api.models.tag_request import TagRequest  # noqa: E501
from allegro_api.rest import ApiException

class TestTagRequest(unittest.TestCase):
    """TagRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TagRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.tag_request.TagRequest()  # noqa: E501
        if include_optional :
            return TagRequest(
                name = '0', 
                hidden = True
            )
        else :
            return TagRequest(
                name = '0',
        )

    def testTagRequest(self):
        """Test TagRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()