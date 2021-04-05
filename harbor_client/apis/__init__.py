
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.chart_repository_api import ChartRepositoryApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from harbor_client.api.chart_repository_api import ChartRepositoryApi
from harbor_client.api.label_api import LabelApi
from harbor_client.api.products_api import ProductsApi
from harbor_client.api.quota_api import QuotaApi
from harbor_client.api.scanners_api import ScannersApi
from harbor_client.api.system_api import SystemApi
