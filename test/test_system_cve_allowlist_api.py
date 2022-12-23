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
from harbor_client.system_cve_allowlist_api import SystemCVEAllowlistApi  # noqa: E501
from harbor_client.rest import ApiException


class TestSystemCVEAllowlistApi(unittest.TestCase):
    """SystemCVEAllowlistApi unit test stubs"""

    def setUp(self):
        self.api = harbor_client.system_cve_allowlist_api.SystemCVEAllowlistApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_system_cve_allowlist(self):
        """Test case for get_system_cve_allowlist

        Get the system level allowlist of CVE.  # noqa: E501
        """
        pass

    def test_put_system_cve_allowlist(self):
        """Test case for put_system_cve_allowlist

        Update the system level allowlist of CVE.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
