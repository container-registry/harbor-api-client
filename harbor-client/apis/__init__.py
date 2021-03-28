
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.artifact_api import ArtifactApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from harbor-client.api.artifact_api import ArtifactApi
from harbor-client.api.auditlog_api import AuditlogApi
from harbor-client.api.project_api import ProjectApi
from harbor-client.api.repository_api import RepositoryApi
from harbor-client.api.scan_api import ScanApi
