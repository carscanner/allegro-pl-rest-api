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
from allegro_api.models.description_section_item import DescriptionSectionItem  # noqa: E501
from allegro_api.rest import ApiException

class TestDescriptionSectionItem(unittest.TestCase):
    """DescriptionSectionItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DescriptionSectionItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.description_section_item.DescriptionSectionItem()  # noqa: E501
        if include_optional :
            return DescriptionSectionItem(
                type = '0'
            )
        else :
            return DescriptionSectionItem(
                type = '0',
        )

    def testDescriptionSectionItem(self):
        """Test DescriptionSectionItem"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()