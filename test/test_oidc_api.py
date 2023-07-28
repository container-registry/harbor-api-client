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
from harbor_client.api.oidc_api import OidcApi  # noqa: E501
from harbor_client.rest import ApiException


class TestOidcApi(unittest.TestCase):
    """OidcApi unit test stubs"""

    def setUp(self):
        self.api = api.oidc_api.OidcApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ping_oidc(self):
        """Test case for ping_oidc

        Test the OIDC endpoint.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
