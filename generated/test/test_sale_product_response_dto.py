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
from allegro_api.models.sale_product_response_dto import SaleProductResponseDto  # noqa: E501
from allegro_api.rest import ApiException

class TestSaleProductResponseDto(unittest.TestCase):
    """SaleProductResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SaleProductResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.sale_product_response_dto.SaleProductResponseDto()  # noqa: E501
        if include_optional :
            return SaleProductResponseDto(
                id = '0', 
                name = '0', 
                category = allegro_api.models.category.Category(
                    id = '0', ), 
                eans = [
                    '0'
                    ], 
                images = [
                    allegro_api.models.image_url.ImageUrl(
                        url = '0', )
                    ], 
                parameters = [
                    allegro_api.models.product_parameter.ProductParameter(
                        id = '0', 
                        range_value = allegro_api.models.parameter_range_value.ParameterRangeValue(
                            from = '0', 
                            to = '0', ), 
                        values = [
                            '0'
                            ], 
                        values_ids = [
                            '0'
                            ], 
                        values_labels = [
                            '0'
                            ], 
                        unit = '0', 
                        options = [
                            allegro_api.models.product_parameter_options.ProductParameter_options(
                                identifies_product = True, )
                            ], )
                    ]
            )
        else :
            return SaleProductResponseDto(
                id = '0',
                name = '0',
                category = allegro_api.models.category.Category(
                    id = '0', ),
        )

    def testSaleProductResponseDto(self):
        """Test SaleProductResponseDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
