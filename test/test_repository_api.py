# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import harbor_client
from harbor_client.repository_api import RepositoryApi  # noqa: E501
from harbor_client.rest import ApiException


class TestRepositoryApi(unittest.TestCase):
    """RepositoryApi unit test stubs"""

    def setUp(self):
        self.api = harbor_client.repository_api.RepositoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_repository(self):
        """Test case for delete_repository

        Delete repository  # noqa: E501
        """
        pass

    def test_get_repository(self):
        """Test case for get_repository

        Get repository  # noqa: E501
        """
        pass

    def test_list_all_repositories(self):
        """Test case for list_all_repositories

        List all authorized repositories  # noqa: E501
        """
        pass

    def test_list_repositories(self):
        """Test case for list_repositories

        List repositories  # noqa: E501
        """
        pass

    def test_update_repository(self):
        """Test case for update_repository

        Update repository  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
