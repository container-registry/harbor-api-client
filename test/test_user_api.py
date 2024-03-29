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
from harbor_client.api.user_api import UserApi  # noqa: E501
from harbor_client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user(self):
        """Test case for create_user

        Create a local user.  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Mark a registered user as be removed.  # noqa: E501
        """
        pass

    def test_get_current_user_info(self):
        """Test case for get_current_user_info

        Get current user info.  # noqa: E501
        """
        pass

    def test_get_current_user_permissions(self):
        """Test case for get_current_user_permissions

        Get current user permissions.  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get a user's profile.  # noqa: E501
        """
        pass

    def test_list_users(self):
        """Test case for list_users

        List users  # noqa: E501
        """
        pass

    def test_search_users(self):
        """Test case for search_users

        Search users by username  # noqa: E501
        """
        pass

    def test_set_cli_secret(self):
        """Test case for set_cli_secret

        Set CLI secret for a user.  # noqa: E501
        """
        pass

    def test_set_user_sys_admin(self):
        """Test case for set_user_sys_admin

        Update a registered user to change to be an administrator of Harbor.  # noqa: E501
        """
        pass

    def test_update_user_password(self):
        """Test case for update_user_password

        Change the password on a user that already exists.  # noqa: E501
        """
        pass

    def test_update_user_profile(self):
        """Test case for update_user_profile

        Update user's profile.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
