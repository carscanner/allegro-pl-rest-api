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


class ShippingRate(object):
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
        'delivery_method': 'ShippingRateDeliveryMethod',
        'max_quantity_per_package': 'int',
        'first_item_rate': 'ShippingRateFirstItemRate',
        'next_item_rate': 'ShippingRateNextItemRate',
        'shipping_time': 'ShippingRateShippingTime'
    }

    attribute_map = {
        'delivery_method': 'deliveryMethod',
        'max_quantity_per_package': 'maxQuantityPerPackage',
        'first_item_rate': 'firstItemRate',
        'next_item_rate': 'nextItemRate',
        'shipping_time': 'shippingTime'
    }

    def __init__(self, delivery_method=None, max_quantity_per_package=None, first_item_rate=None, next_item_rate=None, shipping_time=None, local_vars_configuration=None):  # noqa: E501
        """ShippingRate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._delivery_method = None
        self._max_quantity_per_package = None
        self._first_item_rate = None
        self._next_item_rate = None
        self._shipping_time = None
        self.discriminator = None

        self.delivery_method = delivery_method
        self.max_quantity_per_package = max_quantity_per_package
        self.first_item_rate = first_item_rate
        self.next_item_rate = next_item_rate
        if shipping_time is not None:
            self.shipping_time = shipping_time

    @property
    def delivery_method(self):
        """Gets the delivery_method of this ShippingRate.  # noqa: E501


        :return: The delivery_method of this ShippingRate.  # noqa: E501
        :rtype: ShippingRateDeliveryMethod
        """
        return self._delivery_method

    @delivery_method.setter
    def delivery_method(self, delivery_method):
        """Sets the delivery_method of this ShippingRate.


        :param delivery_method: The delivery_method of this ShippingRate.  # noqa: E501
        :type: ShippingRateDeliveryMethod
        """
        if self.local_vars_configuration.client_side_validation and delivery_method is None:  # noqa: E501
            raise ValueError("Invalid value for `delivery_method`, must not be `None`")  # noqa: E501

        self._delivery_method = delivery_method

    @property
    def max_quantity_per_package(self):
        """Gets the max_quantity_per_package of this ShippingRate.  # noqa: E501

        Maximum quantity per package for the given delivery method. Minimum value is 1.  # noqa: E501

        :return: The max_quantity_per_package of this ShippingRate.  # noqa: E501
        :rtype: int
        """
        return self._max_quantity_per_package

    @max_quantity_per_package.setter
    def max_quantity_per_package(self, max_quantity_per_package):
        """Sets the max_quantity_per_package of this ShippingRate.

        Maximum quantity per package for the given delivery method. Minimum value is 1.  # noqa: E501

        :param max_quantity_per_package: The max_quantity_per_package of this ShippingRate.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and max_quantity_per_package is None:  # noqa: E501
            raise ValueError("Invalid value for `max_quantity_per_package`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_quantity_per_package is not None and max_quantity_per_package < 1):  # noqa: E501
            raise ValueError("Invalid value for `max_quantity_per_package`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_quantity_per_package = max_quantity_per_package

    @property
    def first_item_rate(self):
        """Gets the first_item_rate of this ShippingRate.  # noqa: E501


        :return: The first_item_rate of this ShippingRate.  # noqa: E501
        :rtype: ShippingRateFirstItemRate
        """
        return self._first_item_rate

    @first_item_rate.setter
    def first_item_rate(self, first_item_rate):
        """Sets the first_item_rate of this ShippingRate.


        :param first_item_rate: The first_item_rate of this ShippingRate.  # noqa: E501
        :type: ShippingRateFirstItemRate
        """
        if self.local_vars_configuration.client_side_validation and first_item_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `first_item_rate`, must not be `None`")  # noqa: E501

        self._first_item_rate = first_item_rate

    @property
    def next_item_rate(self):
        """Gets the next_item_rate of this ShippingRate.  # noqa: E501


        :return: The next_item_rate of this ShippingRate.  # noqa: E501
        :rtype: ShippingRateNextItemRate
        """
        return self._next_item_rate

    @next_item_rate.setter
    def next_item_rate(self, next_item_rate):
        """Sets the next_item_rate of this ShippingRate.


        :param next_item_rate: The next_item_rate of this ShippingRate.  # noqa: E501
        :type: ShippingRateNextItemRate
        """
        if self.local_vars_configuration.client_side_validation and next_item_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `next_item_rate`, must not be `None`")  # noqa: E501

        self._next_item_rate = next_item_rate

    @property
    def shipping_time(self):
        """Gets the shipping_time of this ShippingRate.  # noqa: E501


        :return: The shipping_time of this ShippingRate.  # noqa: E501
        :rtype: ShippingRateShippingTime
        """
        return self._shipping_time

    @shipping_time.setter
    def shipping_time(self, shipping_time):
        """Sets the shipping_time of this ShippingRate.


        :param shipping_time: The shipping_time of this ShippingRate.  # noqa: E501
        :type: ShippingRateShippingTime
        """

        self._shipping_time = shipping_time

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
        if not isinstance(other, ShippingRate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShippingRate):
            return True

        return self.to_dict() != other.to_dict()
