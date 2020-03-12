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
from allegro_api.models.propose_sale_product_request import ProposeSaleProductRequest  # noqa: E501
from allegro_api.rest import ApiException

class TestProposeSaleProductRequest(unittest.TestCase):
    """ProposeSaleProductRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProposeSaleProductRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.propose_sale_product_request.ProposeSaleProductRequest()  # noqa: E501
        if include_optional :
            return ProposeSaleProductRequest(
                name = 'iPhone 5s', 
                category = allegro_api.models.category.Category(
                    id = '0', ), 
                eans = ["0019062113399","0000007905193"], 
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
                    ], 
                description = allegro_api.models.standardized_description.StandardizedDescription(
                    sections = [
                        allegro_api.models.description_section.DescriptionSection(
                            items = [
                                allegro_api.models.description_section_item.DescriptionSectionItem(
                                    type = '0', )
                                ], )
                        ], )
            )
        else :
            return ProposeSaleProductRequest(
                name = 'iPhone 5s',
                category = allegro_api.models.category.Category(
                    id = '0', ),
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
                    ],
        )

    def testProposeSaleProductRequest(self):
        """Test ProposeSaleProductRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
