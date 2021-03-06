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
from allegro_api.models.compatible_products_groups_dto import CompatibleProductsGroupsDto  # noqa: E501
from allegro_api.rest import ApiException

class TestCompatibleProductsGroupsDto(unittest.TestCase):
    """CompatibleProductsGroupsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CompatibleProductsGroupsDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.compatible_products_groups_dto.CompatibleProductsGroupsDto()  # noqa: E501
        if include_optional :
            return CompatibleProductsGroupsDto(
                groups = [{"id":"b0dfe6de8fb2f2b1309ad94c6cc4e09d","text":"ABARTH"},{"id":"4144e097d2fa7a491cec2a7a4322f2bc","text":"AC"},{"id":"de3e2253f276cd1c757f58860d77b9bb","text":"ACURA"}], 
                count = 3, 
                total_count = 256
            )
        else :
            return CompatibleProductsGroupsDto(
        )

    def testCompatibleProductsGroupsDto(self):
        """Test CompatibleProductsGroupsDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
