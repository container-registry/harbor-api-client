"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import harbor_client
from harbor_client.model.cve_allowlist import CVEAllowlist
from harbor_client.model.project_metadata import ProjectMetadata
globals()['CVEAllowlist'] = CVEAllowlist
globals()['ProjectMetadata'] = ProjectMetadata
from harbor_client.model.project import Project


class TestProject(unittest.TestCase):
    """Project unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProject(self):
        """Test Project"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Project()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()