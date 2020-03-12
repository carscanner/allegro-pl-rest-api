# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    The version of the OpenAPI document: 2020.03.12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from allegro_api.configuration import Configuration


class OfferListingDto(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'category': 'OfferCategory',
        'primary_image': 'OfferListingDtoImage',
        'selling_mode': 'SellingMode',
        'sale_info': 'OfferListingDtoV1SaleInfo',
        'stock': 'OfferListingDtoV1Stock',
        'stats': 'OfferListingDtoV1Stats',
        'publication': 'OfferListingDtoV1Publication',
        'after_sales_services': 'AfterSalesServices',
        'additional_services': 'OfferAdditionalServices',
        'external': 'ExternalId',
        'delivery': 'OfferListingDtoV1Delivery'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'category': 'category',
        'primary_image': 'primaryImage',
        'selling_mode': 'sellingMode',
        'sale_info': 'saleInfo',
        'stock': 'stock',
        'stats': 'stats',
        'publication': 'publication',
        'after_sales_services': 'afterSalesServices',
        'additional_services': 'additionalServices',
        'external': 'external',
        'delivery': 'delivery'
    }

    def __init__(self, id=None, name=None, category=None, primary_image=None, selling_mode=None, sale_info=None, stock=None, stats=None, publication=None, after_sales_services=None, additional_services=None, external=None, delivery=None, local_vars_configuration=None):  # noqa: E501
        """OfferListingDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._category = None
        self._primary_image = None
        self._selling_mode = None
        self._sale_info = None
        self._stock = None
        self._stats = None
        self._publication = None
        self._after_sales_services = None
        self._additional_services = None
        self._external = None
        self._delivery = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if category is not None:
            self.category = category
        if primary_image is not None:
            self.primary_image = primary_image
        if selling_mode is not None:
            self.selling_mode = selling_mode
        if sale_info is not None:
            self.sale_info = sale_info
        if stock is not None:
            self.stock = stock
        if stats is not None:
            self.stats = stats
        if publication is not None:
            self.publication = publication
        if after_sales_services is not None:
            self.after_sales_services = after_sales_services
        if additional_services is not None:
            self.additional_services = additional_services
        if external is not None:
            self.external = external
        if delivery is not None:
            self.delivery = delivery

    @property
    def id(self):
        """Gets the id of this OfferListingDto.  # noqa: E501

        The offer ID.  # noqa: E501

        :return: The id of this OfferListingDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OfferListingDto.

        The offer ID.  # noqa: E501

        :param id: The id of this OfferListingDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this OfferListingDto.  # noqa: E501

        The title of the offer.  # noqa: E501

        :return: The name of this OfferListingDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OfferListingDto.

        The title of the offer.  # noqa: E501

        :param name: The name of this OfferListingDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def category(self):
        """Gets the category of this OfferListingDto.  # noqa: E501


        :return: The category of this OfferListingDto.  # noqa: E501
        :rtype: OfferCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this OfferListingDto.


        :param category: The category of this OfferListingDto.  # noqa: E501
        :type: OfferCategory
        """

        self._category = category

    @property
    def primary_image(self):
        """Gets the primary_image of this OfferListingDto.  # noqa: E501


        :return: The primary_image of this OfferListingDto.  # noqa: E501
        :rtype: OfferListingDtoImage
        """
        return self._primary_image

    @primary_image.setter
    def primary_image(self, primary_image):
        """Sets the primary_image of this OfferListingDto.


        :param primary_image: The primary_image of this OfferListingDto.  # noqa: E501
        :type: OfferListingDtoImage
        """

        self._primary_image = primary_image

    @property
    def selling_mode(self):
        """Gets the selling_mode of this OfferListingDto.  # noqa: E501


        :return: The selling_mode of this OfferListingDto.  # noqa: E501
        :rtype: SellingMode
        """
        return self._selling_mode

    @selling_mode.setter
    def selling_mode(self, selling_mode):
        """Sets the selling_mode of this OfferListingDto.


        :param selling_mode: The selling_mode of this OfferListingDto.  # noqa: E501
        :type: SellingMode
        """

        self._selling_mode = selling_mode

    @property
    def sale_info(self):
        """Gets the sale_info of this OfferListingDto.  # noqa: E501


        :return: The sale_info of this OfferListingDto.  # noqa: E501
        :rtype: OfferListingDtoV1SaleInfo
        """
        return self._sale_info

    @sale_info.setter
    def sale_info(self, sale_info):
        """Sets the sale_info of this OfferListingDto.


        :param sale_info: The sale_info of this OfferListingDto.  # noqa: E501
        :type: OfferListingDtoV1SaleInfo
        """

        self._sale_info = sale_info

    @property
    def stock(self):
        """Gets the stock of this OfferListingDto.  # noqa: E501


        :return: The stock of this OfferListingDto.  # noqa: E501
        :rtype: OfferListingDtoV1Stock
        """
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Sets the stock of this OfferListingDto.


        :param stock: The stock of this OfferListingDto.  # noqa: E501
        :type: OfferListingDtoV1Stock
        """

        self._stock = stock

    @property
    def stats(self):
        """Gets the stats of this OfferListingDto.  # noqa: E501


        :return: The stats of this OfferListingDto.  # noqa: E501
        :rtype: OfferListingDtoV1Stats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this OfferListingDto.


        :param stats: The stats of this OfferListingDto.  # noqa: E501
        :type: OfferListingDtoV1Stats
        """

        self._stats = stats

    @property
    def publication(self):
        """Gets the publication of this OfferListingDto.  # noqa: E501


        :return: The publication of this OfferListingDto.  # noqa: E501
        :rtype: OfferListingDtoV1Publication
        """
        return self._publication

    @publication.setter
    def publication(self, publication):
        """Sets the publication of this OfferListingDto.


        :param publication: The publication of this OfferListingDto.  # noqa: E501
        :type: OfferListingDtoV1Publication
        """

        self._publication = publication

    @property
    def after_sales_services(self):
        """Gets the after_sales_services of this OfferListingDto.  # noqa: E501


        :return: The after_sales_services of this OfferListingDto.  # noqa: E501
        :rtype: AfterSalesServices
        """
        return self._after_sales_services

    @after_sales_services.setter
    def after_sales_services(self, after_sales_services):
        """Sets the after_sales_services of this OfferListingDto.


        :param after_sales_services: The after_sales_services of this OfferListingDto.  # noqa: E501
        :type: AfterSalesServices
        """

        self._after_sales_services = after_sales_services

    @property
    def additional_services(self):
        """Gets the additional_services of this OfferListingDto.  # noqa: E501


        :return: The additional_services of this OfferListingDto.  # noqa: E501
        :rtype: OfferAdditionalServices
        """
        return self._additional_services

    @additional_services.setter
    def additional_services(self, additional_services):
        """Sets the additional_services of this OfferListingDto.


        :param additional_services: The additional_services of this OfferListingDto.  # noqa: E501
        :type: OfferAdditionalServices
        """

        self._additional_services = additional_services

    @property
    def external(self):
        """Gets the external of this OfferListingDto.  # noqa: E501


        :return: The external of this OfferListingDto.  # noqa: E501
        :rtype: ExternalId
        """
        return self._external

    @external.setter
    def external(self, external):
        """Sets the external of this OfferListingDto.


        :param external: The external of this OfferListingDto.  # noqa: E501
        :type: ExternalId
        """

        self._external = external

    @property
    def delivery(self):
        """Gets the delivery of this OfferListingDto.  # noqa: E501


        :return: The delivery of this OfferListingDto.  # noqa: E501
        :rtype: OfferListingDtoV1Delivery
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this OfferListingDto.


        :param delivery: The delivery of this OfferListingDto.  # noqa: E501
        :type: OfferListingDtoV1Delivery
        """

        self._delivery = delivery

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OfferListingDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OfferListingDto):
            return True

        return self.to_dict() != other.to_dict()
