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


class ListingOffer(object):
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
        'seller': 'OfferSeller',
        'promotion': 'OfferPromotion',
        'delivery': 'OfferDelivery',
        'images': 'list[OfferImages]',
        'selling_mode': 'OfferSellingMode',
        'stock': 'OfferStock',
        'vendor': 'OfferVendor',
        'category': 'OfferCategory',
        'publication': 'OfferPublication'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'seller': 'seller',
        'promotion': 'promotion',
        'delivery': 'delivery',
        'images': 'images',
        'selling_mode': 'sellingMode',
        'stock': 'stock',
        'vendor': 'vendor',
        'category': 'category',
        'publication': 'publication'
    }

    def __init__(self, id=None, name=None, seller=None, promotion=None, delivery=None, images=None, selling_mode=None, stock=None, vendor=None, category=None, publication=None, local_vars_configuration=None):  # noqa: E501
        """ListingOffer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._seller = None
        self._promotion = None
        self._delivery = None
        self._images = None
        self._selling_mode = None
        self._stock = None
        self._vendor = None
        self._category = None
        self._publication = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if seller is not None:
            self.seller = seller
        if promotion is not None:
            self.promotion = promotion
        if delivery is not None:
            self.delivery = delivery
        if images is not None:
            self.images = images
        if selling_mode is not None:
            self.selling_mode = selling_mode
        if stock is not None:
            self.stock = stock
        if vendor is not None:
            self.vendor = vendor
        if category is not None:
            self.category = category
        if publication is not None:
            self.publication = publication

    @property
    def id(self):
        """Gets the id of this ListingOffer.  # noqa: E501

        The offer ID.  # noqa: E501

        :return: The id of this ListingOffer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListingOffer.

        The offer ID.  # noqa: E501

        :param id: The id of this ListingOffer.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ListingOffer.  # noqa: E501

        The title of the offer.  # noqa: E501

        :return: The name of this ListingOffer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListingOffer.

        The title of the offer.  # noqa: E501

        :param name: The name of this ListingOffer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def seller(self):
        """Gets the seller of this ListingOffer.  # noqa: E501


        :return: The seller of this ListingOffer.  # noqa: E501
        :rtype: OfferSeller
        """
        return self._seller

    @seller.setter
    def seller(self, seller):
        """Sets the seller of this ListingOffer.


        :param seller: The seller of this ListingOffer.  # noqa: E501
        :type: OfferSeller
        """

        self._seller = seller

    @property
    def promotion(self):
        """Gets the promotion of this ListingOffer.  # noqa: E501


        :return: The promotion of this ListingOffer.  # noqa: E501
        :rtype: OfferPromotion
        """
        return self._promotion

    @promotion.setter
    def promotion(self, promotion):
        """Sets the promotion of this ListingOffer.


        :param promotion: The promotion of this ListingOffer.  # noqa: E501
        :type: OfferPromotion
        """

        self._promotion = promotion

    @property
    def delivery(self):
        """Gets the delivery of this ListingOffer.  # noqa: E501


        :return: The delivery of this ListingOffer.  # noqa: E501
        :rtype: OfferDelivery
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this ListingOffer.


        :param delivery: The delivery of this ListingOffer.  # noqa: E501
        :type: OfferDelivery
        """

        self._delivery = delivery

    @property
    def images(self):
        """Gets the images of this ListingOffer.  # noqa: E501

        The gallery of images. Only the URL of the original sized image is provided. The first image represents the thumbnail image used on listing.  # noqa: E501

        :return: The images of this ListingOffer.  # noqa: E501
        :rtype: list[OfferImages]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this ListingOffer.

        The gallery of images. Only the URL of the original sized image is provided. The first image represents the thumbnail image used on listing.  # noqa: E501

        :param images: The images of this ListingOffer.  # noqa: E501
        :type: list[OfferImages]
        """

        self._images = images

    @property
    def selling_mode(self):
        """Gets the selling_mode of this ListingOffer.  # noqa: E501


        :return: The selling_mode of this ListingOffer.  # noqa: E501
        :rtype: OfferSellingMode
        """
        return self._selling_mode

    @selling_mode.setter
    def selling_mode(self, selling_mode):
        """Sets the selling_mode of this ListingOffer.


        :param selling_mode: The selling_mode of this ListingOffer.  # noqa: E501
        :type: OfferSellingMode
        """

        self._selling_mode = selling_mode

    @property
    def stock(self):
        """Gets the stock of this ListingOffer.  # noqa: E501


        :return: The stock of this ListingOffer.  # noqa: E501
        :rtype: OfferStock
        """
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Sets the stock of this ListingOffer.


        :param stock: The stock of this ListingOffer.  # noqa: E501
        :type: OfferStock
        """

        self._stock = stock

    @property
    def vendor(self):
        """Gets the vendor of this ListingOffer.  # noqa: E501


        :return: The vendor of this ListingOffer.  # noqa: E501
        :rtype: OfferVendor
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this ListingOffer.


        :param vendor: The vendor of this ListingOffer.  # noqa: E501
        :type: OfferVendor
        """

        self._vendor = vendor

    @property
    def category(self):
        """Gets the category of this ListingOffer.  # noqa: E501


        :return: The category of this ListingOffer.  # noqa: E501
        :rtype: OfferCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ListingOffer.


        :param category: The category of this ListingOffer.  # noqa: E501
        :type: OfferCategory
        """

        self._category = category

    @property
    def publication(self):
        """Gets the publication of this ListingOffer.  # noqa: E501


        :return: The publication of this ListingOffer.  # noqa: E501
        :rtype: OfferPublication
        """
        return self._publication

    @publication.setter
    def publication(self, publication):
        """Sets the publication of this ListingOffer.


        :param publication: The publication of this ListingOffer.  # noqa: E501
        :type: OfferPublication
        """

        self._publication = publication

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
        if not isinstance(other, ListingOffer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListingOffer):
            return True

        return self.to_dict() != other.to_dict()
