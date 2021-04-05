"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import harbor_client
from harbor_client.api.quota_api import QuotaApi  # noqa: E501


class TestQuotaApi(unittest.TestCase):
    """QuotaApi unit test stubs"""

    def setUp(self):
        self.api = QuotaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_quotas_id_get(self):
        """Test case for quotas_id_get

        Get the specified quota  # noqa: E501
        """
        pass

    def test_quotas_id_put(self):
        """Test case for quotas_id_put

        Update the specified quota  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()