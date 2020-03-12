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


class CheckoutForms(object):
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
        'checkout_forms': 'list[CheckoutForm]',
        'count': 'float',
        'total_count': 'float'
    }

    attribute_map = {
        'checkout_forms': 'checkoutForms',
        'count': 'count',
        'total_count': 'totalCount'
    }

    def __init__(self, checkout_forms=None, count=None, total_count=None, local_vars_configuration=None):  # noqa: E501
        """CheckoutForms - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._checkout_forms = None
        self._count = None
        self._total_count = None
        self.discriminator = None

        self.checkout_forms = checkout_forms
        self.count = count
        self.total_count = total_count

    @property
    def checkout_forms(self):
        """Gets the checkout_forms of this CheckoutForms.  # noqa: E501


        :return: The checkout_forms of this CheckoutForms.  # noqa: E501
        :rtype: list[CheckoutForm]
        """
        return self._checkout_forms

    @checkout_forms.setter
    def checkout_forms(self, checkout_forms):
        """Sets the checkout_forms of this CheckoutForms.


        :param checkout_forms: The checkout_forms of this CheckoutForms.  # noqa: E501
        :type: list[CheckoutForm]
        """
        if self.local_vars_configuration.client_side_validation and checkout_forms is None:  # noqa: E501
            raise ValueError("Invalid value for `checkout_forms`, must not be `None`")  # noqa: E501

        self._checkout_forms = checkout_forms

    @property
    def count(self):
        """Gets the count of this CheckoutForms.  # noqa: E501

        number of returned objects  # noqa: E501

        :return: The count of this CheckoutForms.  # noqa: E501
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CheckoutForms.

        number of returned objects  # noqa: E501

        :param count: The count of this CheckoutForms.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and count is None:  # noqa: E501
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def total_count(self):
        """Gets the total_count of this CheckoutForms.  # noqa: E501

        Number of all objects of requested status(es) available (regardless of the provided limit and offset)   # noqa: E501

        :return: The total_count of this CheckoutForms.  # noqa: E501
        :rtype: float
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this CheckoutForms.

        Number of all objects of requested status(es) available (regardless of the provided limit and offset)   # noqa: E501

        :param total_count: The total_count of this CheckoutForms.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_count is None:  # noqa: E501
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

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
        if not isinstance(other, CheckoutForms):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CheckoutForms):
            return True

        return self.to_dict() != other.to_dict()
