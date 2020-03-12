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


class CompatibilityListSupportedCategoriesDtoSupportedCategories(object):
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
        'category_id': 'str',
        'name': 'str',
        'items_type': 'str',
        'input_type': 'str',
        'validation_rules': 'CompatibilityListSupportedCategoriesDtoValidationRules'
    }

    attribute_map = {
        'category_id': 'categoryId',
        'name': 'name',
        'items_type': 'itemsType',
        'input_type': 'inputType',
        'validation_rules': 'validationRules'
    }

    def __init__(self, category_id=None, name=None, items_type=None, input_type=None, validation_rules=None, local_vars_configuration=None):  # noqa: E501
        """CompatibilityListSupportedCategoriesDtoSupportedCategories - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._category_id = None
        self._name = None
        self._items_type = None
        self._input_type = None
        self._validation_rules = None
        self.discriminator = None

        if category_id is not None:
            self.category_id = category_id
        if name is not None:
            self.name = name
        if items_type is not None:
            self.items_type = items_type
        if input_type is not None:
            self.input_type = input_type
        if validation_rules is not None:
            self.validation_rules = validation_rules

    @property
    def category_id(self):
        """Gets the category_id of this CompatibilityListSupportedCategoriesDtoSupportedCategories.  # noqa: E501

        Identifier of the category, where you can use the compatibility list in an offer listed in the category or in all subcategories, which belongs to returned category.  # noqa: E501

        :return: The category_id of this CompatibilityListSupportedCategoriesDtoSupportedCategories.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this CompatibilityListSupportedCategoriesDtoSupportedCategories.

        Identifier of the category, where you can use the compatibility list in an offer listed in the category or in all subcategories, which belongs to returned category.  # noqa: E501

        :param category_id: The category_id of this CompatibilityListSupportedCategoriesDtoSupportedCategories.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def name(self):
        """Gets the name of this CompatibilityListSupportedCategoriesDtoSupportedCategories.  # noqa: E501

        Name of supported category.  # noqa: E501

        :return: The name of this CompatibilityListSupportedCategoriesDtoSupportedCategories.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CompatibilityListSupportedCategoriesDtoSupportedCategories.

        Name of supported category.  # noqa: E501

        :param name: The name of this CompatibilityListSupportedCategoriesDtoSupportedCategories.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def items_type(self):
        """Gets the items_type of this CompatibilityListSupportedCategoriesDtoSupportedCategories.  # noqa: E501

        Type of the compatible item.  # noqa: E501

        :return: The items_type of this CompatibilityListSupportedCategoriesDtoSupportedCategories.  # noqa: E501
        :rtype: str
        """
        return self._items_type

    @items_type.setter
    def items_type(self, items_type):
        """Sets the items_type of this CompatibilityListSupportedCategoriesDtoSupportedCategories.

        Type of the compatible item.  # noqa: E501

        :param items_type: The items_type of this CompatibilityListSupportedCategoriesDtoSupportedCategories.  # noqa: E501
        :type: str
        """

        self._items_type = items_type

    @property
    def input_type(self):
        """Gets the input_type of this CompatibilityListSupportedCategoriesDtoSupportedCategories.  # noqa: E501

        Type of the representation of compatible item. <ul> <li>`TEXT` - item on compatibility list has to be provided as plain text.</li> <li>`ID` - item on compatibility list has to be provided as identifier of compatible product. To obtain it please use <a href=\"/documentation/#tag/Compatibility-List/paths/~1sale~1compatible-products/get\">compatible-products</a> resource together with `itemsType` supported in particular category. </li> </ul>   # noqa: E501

        :return: The input_type of this CompatibilityListSupportedCategoriesDtoSupportedCategories.  # noqa: E501
        :rtype: str
        """
        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        """Sets the input_type of this CompatibilityListSupportedCategoriesDtoSupportedCategories.

        Type of the representation of compatible item. <ul> <li>`TEXT` - item on compatibility list has to be provided as plain text.</li> <li>`ID` - item on compatibility list has to be provided as identifier of compatible product. To obtain it please use <a href=\"/documentation/#tag/Compatibility-List/paths/~1sale~1compatible-products/get\">compatible-products</a> resource together with `itemsType` supported in particular category. </li> </ul>   # noqa: E501

        :param input_type: The input_type of this CompatibilityListSupportedCategoriesDtoSupportedCategories.  # noqa: E501
        :type: str
        """
        allowed_values = ["TEXT", "ID"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and input_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `input_type` ({0}), must be one of {1}"  # noqa: E501
                .format(input_type, allowed_values)
            )

        self._input_type = input_type

    @property
    def validation_rules(self):
        """Gets the validation_rules of this CompatibilityListSupportedCategoriesDtoSupportedCategories.  # noqa: E501


        :return: The validation_rules of this CompatibilityListSupportedCategoriesDtoSupportedCategories.  # noqa: E501
        :rtype: CompatibilityListSupportedCategoriesDtoValidationRules
        """
        return self._validation_rules

    @validation_rules.setter
    def validation_rules(self, validation_rules):
        """Sets the validation_rules of this CompatibilityListSupportedCategoriesDtoSupportedCategories.


        :param validation_rules: The validation_rules of this CompatibilityListSupportedCategoriesDtoSupportedCategories.  # noqa: E501
        :type: CompatibilityListSupportedCategoriesDtoValidationRules
        """

        self._validation_rules = validation_rules

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
        if not isinstance(other, CompatibilityListSupportedCategoriesDtoSupportedCategories):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompatibilityListSupportedCategoriesDtoSupportedCategories):
            return True

        return self.to_dict() != other.to_dict()
