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
from harbor_client.statistic_api import StatisticApi  # noqa: E501
from harbor_client.rest import ApiException


class TestStatisticApi(unittest.TestCase):
    """StatisticApi unit test stubs"""

    def setUp(self):
        self.api = harbor_client.statistic_api.StatisticApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_statistic(self):
        """Test case for get_statistic

        Get the statistic information about the projects and repositories  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
