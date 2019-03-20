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


class Rates(object):
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
        'delivery': 'int',
        'delivery_cost': 'int',
        'description': 'int',
        'service': 'int'
    }

    attribute_map = {
        'delivery': 'delivery',
        'delivery_cost': 'deliveryCost',
        'description': 'description',
        'service': 'service'
    }

    def __init__(self, delivery=None, delivery_cost=None, description=None, service=None):  # noqa: E501
        """Rates - a model defined in OpenAPI"""  # noqa: E501

        self._delivery = None
        self._delivery_cost = None
        self._description = None
        self._service = None
        self.discriminator = None

        self.delivery = delivery
        self.delivery_cost = delivery_cost
        self.description = description
        self.service = service

    @property
    def delivery(self):
        """Gets the delivery of this Rates.  # noqa: E501

        Delivery rate value  # noqa: E501

        :return: The delivery of this Rates.  # noqa: E501
        :rtype: int
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this Rates.

        Delivery rate value  # noqa: E501

        :param delivery: The delivery of this Rates.  # noqa: E501
        :type: int
        """
        if delivery is None:
            raise ValueError("Invalid value for `delivery`, must not be `None`")  # noqa: E501
        allowed_values = [1, 2, 3, 4, 5]  # noqa: E501
        if delivery not in allowed_values:
            raise ValueError(
                "Invalid value for `delivery` ({0}), must be one of {1}"  # noqa: E501
                .format(delivery, allowed_values)
            )

        self._delivery = delivery

    @property
    def delivery_cost(self):
        """Gets the delivery_cost of this Rates.  # noqa: E501

        Delivery cost rate value  # noqa: E501

        :return: The delivery_cost of this Rates.  # noqa: E501
        :rtype: int
        """
        return self._delivery_cost

    @delivery_cost.setter
    def delivery_cost(self, delivery_cost):
        """Sets the delivery_cost of this Rates.

        Delivery cost rate value  # noqa: E501

        :param delivery_cost: The delivery_cost of this Rates.  # noqa: E501
        :type: int
        """
        if delivery_cost is None:
            raise ValueError("Invalid value for `delivery_cost`, must not be `None`")  # noqa: E501
        allowed_values = [1, 2, 3, 4, 5]  # noqa: E501
        if delivery_cost not in allowed_values:
            raise ValueError(
                "Invalid value for `delivery_cost` ({0}), must be one of {1}"  # noqa: E501
                .format(delivery_cost, allowed_values)
            )

        self._delivery_cost = delivery_cost

    @property
    def description(self):
        """Gets the description of this Rates.  # noqa: E501

        Description rate value  # noqa: E501

        :return: The description of this Rates.  # noqa: E501
        :rtype: int
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Rates.

        Description rate value  # noqa: E501

        :param description: The description of this Rates.  # noqa: E501
        :type: int
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        allowed_values = [1, 2, 3, 4, 5]  # noqa: E501
        if description not in allowed_values:
            raise ValueError(
                "Invalid value for `description` ({0}), must be one of {1}"  # noqa: E501
                .format(description, allowed_values)
            )

        self._description = description

    @property
    def service(self):
        """Gets the service of this Rates.  # noqa: E501

        Service rate value  # noqa: E501

        :return: The service of this Rates.  # noqa: E501
        :rtype: int
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this Rates.

        Service rate value  # noqa: E501

        :param service: The service of this Rates.  # noqa: E501
        :type: int
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501
        allowed_values = [1, 2, 3, 4, 5]  # noqa: E501
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"  # noqa: E501
                .format(service, allowed_values)
            )

        self._service = service

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
        if not isinstance(other, Rates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
