# coding: utf-8

"""
    playground

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.default_api import DefaultApi  # noqa: E501
from openapi_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_session(self):
        """Test case for create_session

        """
        pass

    def test_delete_filesystem_entry(self):
        """Test case for delete_filesystem_entry

        """
        pass

    def test_delete_session(self):
        """Test case for delete_session

        """
        pass

    def test_list_filesystem_dir(self):
        """Test case for list_filesystem_dir

        """
        pass

    def test_make_filesystem_dir(self):
        """Test case for make_filesystem_dir

        """
        pass

    def test_read_filesystem_file(self):
        """Test case for read_filesystem_file

        """
        pass

    def test_run_process(self):
        """Test case for run_process

        """
        pass

    def test_write_filesystem_file(self):
        """Test case for write_filesystem_file

        """
        pass


if __name__ == '__main__':
    unittest.main()
