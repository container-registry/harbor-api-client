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
from api.project_api import ProjectApi  # noqa: E501
from harbor_client.rest import ApiException


class TestProjectApi(unittest.TestCase):
    """ProjectApi unit test stubs"""

    def setUp(self):
        self.api = api.project_api.ProjectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_project(self):
        """Test case for create_project

        Create a new project.  # noqa: E501
        """
        pass

    def test_delete_project(self):
        """Test case for delete_project

        Delete project by projectID  # noqa: E501
        """
        pass

    def test_get_logs(self):
        """Test case for get_logs

        Get recent logs of the projects  # noqa: E501
        """
        pass

    def test_get_project(self):
        """Test case for get_project

        Return specific project detail information  # noqa: E501
        """
        pass

    def test_get_project_deletable(self):
        """Test case for get_project_deletable

        Get the deletable status of the project  # noqa: E501
        """
        pass

    def test_get_project_summary(self):
        """Test case for get_project_summary

        Get summary of the project.  # noqa: E501
        """
        pass

    def test_get_scanner_of_project(self):
        """Test case for get_scanner_of_project

        Get project level scanner  # noqa: E501
        """
        pass

    def test_head_project(self):
        """Test case for head_project

        Check if the project name user provided already exists.  # noqa: E501
        """
        pass

    def test_list_projects(self):
        """Test case for list_projects

        List projects  # noqa: E501
        """
        pass

    def test_list_scanner_candidates_of_project(self):
        """Test case for list_scanner_candidates_of_project

        Get scanner registration candidates for configurating project level scanner  # noqa: E501
        """
        pass

    def test_set_scanner_of_project(self):
        """Test case for set_scanner_of_project

        Configure scanner for the specified project  # noqa: E501
        """
        pass

    def test_update_project(self):
        """Test case for update_project

        Update properties for a selected project.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
