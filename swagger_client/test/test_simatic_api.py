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
from swagger_client.api.simatic_api import SimaticApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSimaticApi(unittest.TestCase):
    """SimaticApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.simatic_api.SimaticApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_actual_position(self):
        """Test case for get_actual_position

        Gets actual position of simatic engine.  # noqa: E501
        """
        pass

    def test_get_io(self):
        """Test case for get_io

        Gets analog/digital input/output value.  # noqa: E501
        """
        pass

    def test_move_home(self):
        """Test case for move_home

        Move engine to home position, need after start simatic.  # noqa: E501
        """
        pass

    def test_move_to_position(self):
        """Test case for move_to_position

        Move engine to absolute or relative position with specific speed.  # noqa: E501
        """
        pass

    def test_set_io(self):
        """Test case for set_io

        Sets analog/digital output value.  # noqa: E501
        """
        pass

    def test_stop_machine(self):
        """Test case for stop_machine

        Stop engine.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
