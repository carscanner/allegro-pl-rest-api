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
from allegro_api.models.integer_category_product_parameter import IntegerCategoryProductParameter  # noqa: E501
from allegro_api.rest import ApiException

class TestIntegerCategoryProductParameter(unittest.TestCase):
    """IntegerCategoryProductParameter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IntegerCategoryProductParameter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.integer_category_product_parameter.IntegerCategoryProductParameter()  # noqa: E501
        if include_optional :
            return IntegerCategoryProductParameter(
                type = 'integer', 
                restrictions = allegro_api.models.integer_category_product_parameter_all_of_restrictions.IntegerCategoryProductParameter_allOf_restrictions(
                    min = 8, 
                    max = 128, 
                    range = True, )
            )
        else :
            return IntegerCategoryProductParameter(
        )

    def testIntegerCategoryProductParameter(self):
        """Test IntegerCategoryProductParameter"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
