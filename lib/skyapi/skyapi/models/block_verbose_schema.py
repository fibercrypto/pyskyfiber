# coding: utf-8

"""
    Skycoin REST API.

    Skycoin is a next-generation cryptocurrency.  # noqa: E501

    OpenAPI spec version: 0.26.0
    Contact: contact@skycoin.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BlockVerboseSchema(object):
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
        'header': 'BlockVerboseSchemaHeader',
        'body': 'BlockVerboseSchemaBody',
        'size': 'int'
    }

    attribute_map = {
        'header': 'header',
        'body': 'body',
        'size': 'size'
    }

    def __init__(self, header=None, body=None, size=None):  # noqa: E501
        """BlockVerboseSchema - a model defined in OpenAPI"""  # noqa: E501

        self._header = None
        self._body = None
        self._size = None
        self.discriminator = None

        if header is not None:
            self.header = header
        if body is not None:
            self.body = body
        if size is not None:
            self.size = size

    @property
    def header(self):
        """Gets the header of this BlockVerboseSchema.  # noqa: E501


        :return: The header of this BlockVerboseSchema.  # noqa: E501
        :rtype: BlockVerboseSchemaHeader
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this BlockVerboseSchema.


        :param header: The header of this BlockVerboseSchema.  # noqa: E501
        :type: BlockVerboseSchemaHeader
        """

        self._header = header

    @property
    def body(self):
        """Gets the body of this BlockVerboseSchema.  # noqa: E501


        :return: The body of this BlockVerboseSchema.  # noqa: E501
        :rtype: BlockVerboseSchemaBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BlockVerboseSchema.


        :param body: The body of this BlockVerboseSchema.  # noqa: E501
        :type: BlockVerboseSchemaBody
        """

        self._body = body

    @property
    def size(self):
        """Gets the size of this BlockVerboseSchema.  # noqa: E501


        :return: The size of this BlockVerboseSchema.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BlockVerboseSchema.


        :param size: The size of this BlockVerboseSchema.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if not isinstance(other, BlockVerboseSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other