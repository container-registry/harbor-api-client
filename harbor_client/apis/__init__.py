
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.retention_api import RetentionApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from harbor_client.api.retention_api import RetentionApi
from harbor_client.api.artifact_api import ArtifactApi
from harbor_client.api.auditlog_api import AuditlogApi
from harbor_client.api.gc_api import GcApi
from harbor_client.api.icon_api import IconApi
from harbor_client.api.ping_api import PingApi
from harbor_client.api.preheat_api import PreheatApi
from harbor_client.api.project_api import ProjectApi
from harbor_client.api.replication_api import ReplicationApi
from harbor_client.api.repository_api import RepositoryApi
from harbor_client.api.robot_api import RobotApi
from harbor_client.api.robotv1_api import Robotv1Api
from harbor_client.api.scan_api import ScanApi
from harbor_client.api.scan_all_api import ScanAllApi
from harbor_client.api.systeminfo_api import SysteminfoApi
