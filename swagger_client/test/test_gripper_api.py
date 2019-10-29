# coding: utf-8

"""
    Pick Master Web API Reference

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0-alpha.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.gripper_api import GripperApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGripperApi(unittest.TestCase):
    """GripperApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.gripper_api.GripperApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_gripper_put_activation(self):
        """Test case for gripper_put_activation

        Activate gripper, need after start gripper.  # noqa: E501
        """
        pass

    def test_gripper_put_close(self):
        """Test case for gripper_put_close

        Close gripper, move to 20 position with 100 force and 30 speed.  # noqa: E501
        """
        pass

    def test_gripper_put_move(self):
        """Test case for gripper_put_move

        Move gripper to position with specific speed and force.  # noqa: E501
        """
        pass

    def test_gripper_put_open(self):
        """Test case for gripper_put_open

        Opens gripper, move to 0 position with 200 force and 200 speed.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()