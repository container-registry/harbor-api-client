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
from harbor_client.api.jobservice_api import JobserviceApi  # noqa: E501
from harbor_client.rest import ApiException


class TestJobserviceApi(unittest.TestCase):
    """JobserviceApi unit test stubs"""

    def setUp(self):
        self.api = api.jobservice_api.JobserviceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_action_pending_jobs(self):
        """Test case for action_pending_jobs

        stop and clean, pause, resume pending jobs in the queue  # noqa: E501
        """
        pass

    def test_get_worker_pools(self):
        """Test case for get_worker_pools

        Get worker pools  # noqa: E501
        """
        pass

    def test_get_workers(self):
        """Test case for get_workers

        Get workers  # noqa: E501
        """
        pass

    def test_list_job_queues(self):
        """Test case for list_job_queues

        list job queues  # noqa: E501
        """
        pass

    def test_stop_running_job(self):
        """Test case for stop_running_job

        Stop running job  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
