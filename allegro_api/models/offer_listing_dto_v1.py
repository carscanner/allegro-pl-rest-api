# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    OpenAPI spec version: latest
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class OfferListingDtoV1(object):
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
        'category': 'OfferListingDtoV1Category',
        'primary_image': 'OfferListingDtoV1Image',
        'selling_mode': 'OfferListingDtoV1SellingMode',
        'sale_info': 'OfferListingDtoV1SaleInfo',
        'stock': 'OfferListingDtoV1Stock',
        'stats': 'OfferListingDtoV1Stats',
        'publication': 'OfferListingDtoV1Publication',
        'after_sales_services': 'AfterSalesServices',
        'additional_services': 'JustId',
        'external': 'JustId'
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
        'external': 'external'
    }

    def __init__(self, id=None, name=None, category=None, primary_image=None, selling_mode=None, sale_info=None, stock=None, stats=None, publication=None, after_sales_services=None, additional_services=None, external=None):  # noqa: E501
        """OfferListingDtoV1 - a model defined in OpenAPI"""  # noqa: E501

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

    @property
    def id(self):
        """Gets the id of this OfferListingDtoV1.  # noqa: E501


        :return: The id of this OfferListingDtoV1.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OfferListingDtoV1.


        :param id: The id of this OfferListingDtoV1.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this OfferListingDtoV1.  # noqa: E501


        :return: The name of this OfferListingDtoV1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OfferListingDtoV1.


        :param name: The name of this OfferListingDtoV1.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def category(self):
        """Gets the category of this OfferListingDtoV1.  # noqa: E501


        :return: The category of this OfferListingDtoV1.  # noqa: E501
        :rtype: OfferListingDtoV1Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this OfferListingDtoV1.


        :param category: The category of this OfferListingDtoV1.  # noqa: E501
        :type: OfferListingDtoV1Category
        """

        self._category = category

    @property
    def primary_image(self):
        """Gets the primary_image of this OfferListingDtoV1.  # noqa: E501


        :return: The primary_image of this OfferListingDtoV1.  # noqa: E501
        :rtype: OfferListingDtoV1Image
        """
        return self._primary_image

    @primary_image.setter
    def primary_image(self, primary_image):
        """Sets the primary_image of this OfferListingDtoV1.


        :param primary_image: The primary_image of this OfferListingDtoV1.  # noqa: E501
        :type: OfferListingDtoV1Image
        """

        self._primary_image = primary_image

    @property
    def selling_mode(self):
        """Gets the selling_mode of this OfferListingDtoV1.  # noqa: E501


        :return: The selling_mode of this OfferListingDtoV1.  # noqa: E501
        :rtype: OfferListingDtoV1SellingMode
        """
        return self._selling_mode

    @selling_mode.setter
    def selling_mode(self, selling_mode):
        """Sets the selling_mode of this OfferListingDtoV1.


        :param selling_mode: The selling_mode of this OfferListingDtoV1.  # noqa: E501
        :type: OfferListingDtoV1SellingMode
        """

        self._selling_mode = selling_mode

    @property
    def sale_info(self):
        """Gets the sale_info of this OfferListingDtoV1.  # noqa: E501


        :return: The sale_info of this OfferListingDtoV1.  # noqa: E501
        :rtype: OfferListingDtoV1SaleInfo
        """
        return self._sale_info

    @sale_info.setter
    def sale_info(self, sale_info):
        """Sets the sale_info of this OfferListingDtoV1.


        :param sale_info: The sale_info of this OfferListingDtoV1.  # noqa: E501
        :type: OfferListingDtoV1SaleInfo
        """

        self._sale_info = sale_info

    @property
    def stock(self):
        """Gets the stock of this OfferListingDtoV1.  # noqa: E501


        :return: The stock of this OfferListingDtoV1.  # noqa: E501
        :rtype: OfferListingDtoV1Stock
        """
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Sets the stock of this OfferListingDtoV1.


        :param stock: The stock of this OfferListingDtoV1.  # noqa: E501
        :type: OfferListingDtoV1Stock
        """

        self._stock = stock

    @property
    def stats(self):
        """Gets the stats of this OfferListingDtoV1.  # noqa: E501


        :return: The stats of this OfferListingDtoV1.  # noqa: E501
        :rtype: OfferListingDtoV1Stats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this OfferListingDtoV1.


        :param stats: The stats of this OfferListingDtoV1.  # noqa: E501
        :type: OfferListingDtoV1Stats
        """

        self._stats = stats

    @property
    def publication(self):
        """Gets the publication of this OfferListingDtoV1.  # noqa: E501


        :return: The publication of this OfferListingDtoV1.  # noqa: E501
        :rtype: OfferListingDtoV1Publication
        """
        return self._publication

    @publication.setter
    def publication(self, publication):
        """Sets the publication of this OfferListingDtoV1.


        :param publication: The publication of this OfferListingDtoV1.  # noqa: E501
        :type: OfferListingDtoV1Publication
        """

        self._publication = publication

    @property
    def after_sales_services(self):
        """Gets the after_sales_services of this OfferListingDtoV1.  # noqa: E501


        :return: The after_sales_services of this OfferListingDtoV1.  # noqa: E501
        :rtype: AfterSalesServices
        """
        return self._after_sales_services

    @after_sales_services.setter
    def after_sales_services(self, after_sales_services):
        """Sets the after_sales_services of this OfferListingDtoV1.


        :param after_sales_services: The after_sales_services of this OfferListingDtoV1.  # noqa: E501
        :type: AfterSalesServices
        """

        self._after_sales_services = after_sales_services

    @property
    def additional_services(self):
        """Gets the additional_services of this OfferListingDtoV1.  # noqa: E501


        :return: The additional_services of this OfferListingDtoV1.  # noqa: E501
        :rtype: JustId
        """
        return self._additional_services

    @additional_services.setter
    def additional_services(self, additional_services):
        """Sets the additional_services of this OfferListingDtoV1.


        :param additional_services: The additional_services of this OfferListingDtoV1.  # noqa: E501
        :type: JustId
        """

        self._additional_services = additional_services

    @property
    def external(self):
        """Gets the external of this OfferListingDtoV1.  # noqa: E501


        :return: The external of this OfferListingDtoV1.  # noqa: E501
        :rtype: JustId
        """
        return self._external

    @external.setter
    def external(self, external):
        """Sets the external of this OfferListingDtoV1.


        :param external: The external of this OfferListingDtoV1.  # noqa: E501
        :type: JustId
        """

        self._external = external

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
        if not isinstance(other, OfferListingDtoV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other