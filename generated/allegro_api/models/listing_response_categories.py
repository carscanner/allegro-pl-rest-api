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


class ListingResponseCategories(object):
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
        'subcategories': 'list[ListingCategoryWithCount]',
        'path': 'list[ListingCategory]'
    }

    attribute_map = {
        'subcategories': 'subcategories',
        'path': 'path'
    }

    def __init__(self, subcategories=None, path=None, local_vars_configuration=None):  # noqa: E501
        """ListingResponseCategories - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._subcategories = None
        self._path = None
        self.discriminator = None

        if subcategories is not None:
            self.subcategories = subcategories
        if path is not None:
            self.path = path

    @property
    def subcategories(self):
        """Gets the subcategories of this ListingResponseCategories.  # noqa: E501

        Categories with counters, which can be used to refine search results.  # noqa: E501

        :return: The subcategories of this ListingResponseCategories.  # noqa: E501
        :rtype: list[ListingCategoryWithCount]
        """
        return self._subcategories

    @subcategories.setter
    def subcategories(self, subcategories):
        """Sets the subcategories of this ListingResponseCategories.

        Categories with counters, which can be used to refine search results.  # noqa: E501

        :param subcategories: The subcategories of this ListingResponseCategories.  # noqa: E501
        :type: list[ListingCategoryWithCount]
        """

        self._subcategories = subcategories

    @property
    def path(self):
        """Gets the path of this ListingResponseCategories.  # noqa: E501

        Categories path to the current listing category (breadcrumbs).  # noqa: E501

        :return: The path of this ListingResponseCategories.  # noqa: E501
        :rtype: list[ListingCategory]
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ListingResponseCategories.

        Categories path to the current listing category (breadcrumbs).  # noqa: E501

        :param path: The path of this ListingResponseCategories.  # noqa: E501
        :type: list[ListingCategory]
        """

        self._path = path

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
        if not isinstance(other, ListingResponseCategories):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListingResponseCategories):
            return True

        return self.to_dict() != other.to_dict()
