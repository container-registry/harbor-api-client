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
from harbor_client.member_api import MemberApi  # noqa: E501
from harbor_client.rest import ApiException


class TestMemberApi(unittest.TestCase):
    """MemberApi unit test stubs"""

    def setUp(self):
        self.api = harbor_client.member_api.MemberApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_project_member(self):
        """Test case for create_project_member

        Create project member  # noqa: E501
        """
        pass

    def test_delete_project_member(self):
        """Test case for delete_project_member

        Delete project member  # noqa: E501
        """
        pass

    def test_get_project_member(self):
        """Test case for get_project_member

        Get the project member information  # noqa: E501
        """
        pass

    def test_list_project_members(self):
        """Test case for list_project_members

        Get all project member information  # noqa: E501
        """
        pass

    def test_update_project_member(self):
        """Test case for update_project_member

        Update project member  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
