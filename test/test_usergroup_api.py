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
from api.usergroup_api import UsergroupApi  # noqa: E501
from harbor_client.rest import ApiException


class TestUsergroupApi(unittest.TestCase):
    """UsergroupApi unit test stubs"""

    def setUp(self):
        self.api = api.usergroup_api.UsergroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user_group(self):
        """Test case for create_user_group

        Create user group  # noqa: E501
        """
        pass

    def test_delete_user_group(self):
        """Test case for delete_user_group

        Delete user group  # noqa: E501
        """
        pass

    def test_get_user_group(self):
        """Test case for get_user_group

        Get user group information  # noqa: E501
        """
        pass

    def test_list_user_groups(self):
        """Test case for list_user_groups

        Get all user groups information  # noqa: E501
        """
        pass

    def test_search_user_groups(self):
        """Test case for search_user_groups

        Search groups by groupname  # noqa: E501
        """
        pass

    def test_update_user_group(self):
        """Test case for update_user_group

        Update group information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
