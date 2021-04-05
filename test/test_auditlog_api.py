"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import harbor_client
from harbor_client.api.auditlog_api import AuditlogApi  # noqa: E501


class TestAuditlogApi(unittest.TestCase):
    """AuditlogApi unit test stubs"""

    def setUp(self):
        self.api = AuditlogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_audit_logs(self):
        """Test case for list_audit_logs

        Get recent logs of the projects which the user is a member of  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()