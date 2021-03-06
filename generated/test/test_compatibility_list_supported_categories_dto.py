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
from allegro_api.models.compatibility_list_supported_categories_dto import CompatibilityListSupportedCategoriesDto  # noqa: E501
from allegro_api.rest import ApiException

class TestCompatibilityListSupportedCategoriesDto(unittest.TestCase):
    """CompatibilityListSupportedCategoriesDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CompatibilityListSupportedCategoriesDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.compatibility_list_supported_categories_dto.CompatibilityListSupportedCategoriesDto()  # noqa: E501
        if include_optional :
            return CompatibilityListSupportedCategoriesDto(
                supported_categories = [{"categoryId":"620","name":"Części samochodowe","itemsType":"CAR","inputType":"ID","validationRules":{"maxRows":2000}},{"categoryId":"257358","name":"Pióra wycieraczek","itemsType":"CAR","inputType":"ID","validationRules":{"maxRows":2000}},{"categoryId":"158","name":"Części motocyklowe","itemsType":"MOTORCYCLE","inputType":"ID","validationRules":{"maxRows":2000}},{"categoryId":"9108","name":"Tusze","itemsType":"PRINTER","inputType":"TEXT","validationRules":{"maxRows":200,"maxCharactersPerLine":100}}]
            )
        else :
            return CompatibilityListSupportedCategoriesDto(
        )

    def testCompatibilityListSupportedCategoriesDto(self):
        """Test CompatibilityListSupportedCategoriesDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
