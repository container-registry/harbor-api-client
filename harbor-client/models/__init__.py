# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from harbor-client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from harbor-client.model.addition_link import AdditionLink
from harbor-client.model.addition_links import AdditionLinks
from harbor-client.model.annotations import Annotations
from harbor-client.model.artifact import Artifact
from harbor-client.model.audit_log import AuditLog
from harbor-client.model.error import Error
from harbor-client.model.errors import Errors
from harbor-client.model.extra_attrs import ExtraAttrs
from harbor-client.model.label import Label
from harbor-client.model.native_report_summary import NativeReportSummary
from harbor-client.model.platform import Platform
from harbor-client.model.reference import Reference
from harbor-client.model.repository import Repository
from harbor-client.model.scan_overview import ScanOverview
from harbor-client.model.tag import Tag
from harbor-client.model.vulnerability_summary import VulnerabilitySummary
