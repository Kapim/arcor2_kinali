# coding: utf-8

"""
    Pick Master Web API Reference

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0-alpha.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.robot_joint import RobotJoint  # noqa: F401,E501


class RobotJoints(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'joints': 'list[RobotJoint]'
    }

    attribute_map = {
        'joints': 'joints'
    }

    def __init__(self, joints=None):  # noqa: E501
        """RobotJoints - a model defined in Swagger"""  # noqa: E501

        self._joints = None
        self.discriminator = None

        if joints is not None:
            self.joints = joints

    @property
    def joints(self):
        """Gets the joints of this RobotJoints.  # noqa: E501

        Gets or sets list with joints.  # noqa: E501

        :return: The joints of this RobotJoints.  # noqa: E501
        :rtype: list[RobotJoint]
        """
        return self._joints

    @joints.setter
    def joints(self, joints):
        """Sets the joints of this RobotJoints.

        Gets or sets list with joints.  # noqa: E501

        :param joints: The joints of this RobotJoints.  # noqa: E501
        :type: list[RobotJoint]
        """

        self._joints = joints

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(RobotJoints, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RobotJoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
