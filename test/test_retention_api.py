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
from api.retention_api import RetentionApi  # noqa: E501
from harbor_client.rest import ApiException


class TestRetentionApi(unittest.TestCase):
    """RetentionApi unit test stubs"""

    def setUp(self):
        self.api = api.retention_api.RetentionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_retention(self):
        """Test case for create_retention

        Create Retention Policy  # noqa: E501
        """
        pass

    def test_delete_retention(self):
        """Test case for delete_retention

        Delete Retention Policy  # noqa: E501
        """
        pass

    def test_get_rentenition_metadata(self):
        """Test case for get_rentenition_metadata

        Get Retention Metadatas  # noqa: E501
        """
        pass

    def test_get_retention(self):
        """Test case for get_retention

        Get Retention Policy  # noqa: E501
        """
        pass

    def test_get_retention_task_log(self):
        """Test case for get_retention_task_log

        Get Retention job task log  # noqa: E501
        """
        pass

    def test_list_retention_executions(self):
        """Test case for list_retention_executions

        Get Retention executions  # noqa: E501
        """
        pass

    def test_list_retention_tasks(self):
        """Test case for list_retention_tasks

        Get Retention tasks  # noqa: E501
        """
        pass

    def test_operate_retention_execution(self):
        """Test case for operate_retention_execution

        Stop a Retention execution  # noqa: E501
        """
        pass

    def test_trigger_retention_execution(self):
        """Test case for trigger_retention_execution

        Trigger a Retention Execution  # noqa: E501
        """
        pass

    def test_update_retention(self):
        """Test case for update_retention

        Update Retention Policy  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
