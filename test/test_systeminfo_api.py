"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import harbor_client
from harbor_client.api.systeminfo_api import SysteminfoApi  # noqa: E501


class TestSysteminfoApi(unittest.TestCase):
    """SysteminfoApi unit test stubs"""

    def setUp(self):
        self.api = SysteminfoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_systeminfo_get(self):
        """Test case for systeminfo_get

        Get general system info  # noqa: E501
        """
        pass

    def test_systeminfo_getcert_get(self):
        """Test case for systeminfo_getcert_get

        Get default root certificate.  # noqa: E501
        """
        pass

    def test_systeminfo_volumes_get(self):
        """Test case for systeminfo_volumes_get

        Get system volume info (total/free size).  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()