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
from allegro_api.models.get_sale_products_response import GetSaleProductsResponse  # noqa: E501
from allegro_api.rest import ApiException

class TestGetSaleProductsResponse(unittest.TestCase):
    """GetSaleProductsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetSaleProductsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.get_sale_products_response.GetSaleProductsResponse()  # noqa: E501
        if include_optional :
            return GetSaleProductsResponse(
                products = [
                    allegro_api.models.sale_product_response_dto.SaleProductResponseDto(
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
                            ], )
                    ], 
                categories = [
                    allegro_api.models.sale_product_response_categories_dto.SaleProductResponseCategoriesDto(
                        subcategories = [
                            allegro_api.models.products_category_subcategories.ProductsCategorySubcategories(
                                id = '0', 
                                name = '0', 
                                count = 56, )
                            ], 
                        path = [
                            allegro_api.models.products_category_path.ProductsCategoryPath(
                                id = '0', 
                                name = '0', )
                            ], )
                    ], 
                filters = [
                    allegro_api.models.listing_response_filters.ListingResponseFilters(
                        id = 'campaign', 
                        type = 'MULTI', 
                        name = 'kampania', 
                        values = [
                            allegro_api.models.listing_response_filters_values.ListingResponseFiltersValues(
                                name = 'raty zero', 
                                value = 'INSTALLMENTS_ZERO', 
                                id_suffix = '.to', 
                                count = 123, 
                                selected = True, )
                            ], 
                        min_value = 0, 
                        max_value = 1000, 
                        unit = 'zł', )
                    ], 
                next_page = allegro_api.models.get_sale_products_response_next_page.GetSaleProductsResponse_nextPage(
                    id = '0', )
            )
        else :
            return GetSaleProductsResponse(
                products = [
                    allegro_api.models.sale_product_response_dto.SaleProductResponseDto(
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
                            ], )
                    ],
        )

    def testGetSaleProductsResponse(self):
        """Test GetSaleProductsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
