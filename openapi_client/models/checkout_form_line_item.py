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


class CheckoutFormLineItem(object):
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
        'offer': 'OfferReference',
        'quantity': 'float',
        'original_price': 'Price',
        'price': 'Price',
        'selected_additional_services': 'list[CheckoutFormAdditionalService]',
        'bought_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'offer': 'offer',
        'quantity': 'quantity',
        'original_price': 'originalPrice',
        'price': 'price',
        'selected_additional_services': 'selectedAdditionalServices',
        'bought_at': 'boughtAt'
    }

    def __init__(self, id=None, offer=None, quantity=None, original_price=None, price=None, selected_additional_services=None, bought_at=None):  # noqa: E501
        """CheckoutFormLineItem - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._offer = None
        self._quantity = None
        self._original_price = None
        self._price = None
        self._selected_additional_services = None
        self._bought_at = None
        self.discriminator = None

        self.id = id
        self.offer = offer
        self.quantity = quantity
        self.original_price = original_price
        self.price = price
        if selected_additional_services is not None:
            self.selected_additional_services = selected_additional_services
        if bought_at is not None:
            self.bought_at = bought_at

    @property
    def id(self):
        """Gets the id of this CheckoutFormLineItem.  # noqa: E501

        Line item identifier  # noqa: E501

        :return: The id of this CheckoutFormLineItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CheckoutFormLineItem.

        Line item identifier  # noqa: E501

        :param id: The id of this CheckoutFormLineItem.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def offer(self):
        """Gets the offer of this CheckoutFormLineItem.  # noqa: E501


        :return: The offer of this CheckoutFormLineItem.  # noqa: E501
        :rtype: OfferReference
        """
        return self._offer

    @offer.setter
    def offer(self, offer):
        """Sets the offer of this CheckoutFormLineItem.


        :param offer: The offer of this CheckoutFormLineItem.  # noqa: E501
        :type: OfferReference
        """
        if offer is None:
            raise ValueError("Invalid value for `offer`, must not be `None`")  # noqa: E501

        self._offer = offer

    @property
    def quantity(self):
        """Gets the quantity of this CheckoutFormLineItem.  # noqa: E501

        quantity  # noqa: E501

        :return: The quantity of this CheckoutFormLineItem.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CheckoutFormLineItem.

        quantity  # noqa: E501

        :param quantity: The quantity of this CheckoutFormLineItem.  # noqa: E501
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def original_price(self):
        """Gets the original_price of this CheckoutFormLineItem.  # noqa: E501


        :return: The original_price of this CheckoutFormLineItem.  # noqa: E501
        :rtype: Price
        """
        return self._original_price

    @original_price.setter
    def original_price(self, original_price):
        """Sets the original_price of this CheckoutFormLineItem.


        :param original_price: The original_price of this CheckoutFormLineItem.  # noqa: E501
        :type: Price
        """
        if original_price is None:
            raise ValueError("Invalid value for `original_price`, must not be `None`")  # noqa: E501

        self._original_price = original_price

    @property
    def price(self):
        """Gets the price of this CheckoutFormLineItem.  # noqa: E501


        :return: The price of this CheckoutFormLineItem.  # noqa: E501
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this CheckoutFormLineItem.


        :param price: The price of this CheckoutFormLineItem.  # noqa: E501
        :type: Price
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def selected_additional_services(self):
        """Gets the selected_additional_services of this CheckoutFormLineItem.  # noqa: E501


        :return: The selected_additional_services of this CheckoutFormLineItem.  # noqa: E501
        :rtype: list[CheckoutFormAdditionalService]
        """
        return self._selected_additional_services

    @selected_additional_services.setter
    def selected_additional_services(self, selected_additional_services):
        """Sets the selected_additional_services of this CheckoutFormLineItem.


        :param selected_additional_services: The selected_additional_services of this CheckoutFormLineItem.  # noqa: E501
        :type: list[CheckoutFormAdditionalService]
        """

        self._selected_additional_services = selected_additional_services

    @property
    def bought_at(self):
        """Gets the bought_at of this CheckoutFormLineItem.  # noqa: E501

        ISO date when offer was bought  # noqa: E501

        :return: The bought_at of this CheckoutFormLineItem.  # noqa: E501
        :rtype: datetime
        """
        return self._bought_at

    @bought_at.setter
    def bought_at(self, bought_at):
        """Sets the bought_at of this CheckoutFormLineItem.

        ISO date when offer was bought  # noqa: E501

        :param bought_at: The bought_at of this CheckoutFormLineItem.  # noqa: E501
        :type: datetime
        """

        self._bought_at = bought_at

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
        if not isinstance(other, CheckoutFormLineItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
