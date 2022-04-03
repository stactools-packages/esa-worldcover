# import math
# from typing import Optional
# import re
# import os
# from datetime import datetime, timezone
# from pathlib import Path
# from typing import Any, Dict, List

# import rasterio
# from rasterio.crs import CRS
# from rasterio.warp import transform_bounds
# from shapely.geometry import box, mapping
# from stactools.core.io import ReadHrefModifier

# JsonDict = Dict[str, Any]

# class Metadata:

#     def __init__(self, href:str, read_href_modifier: Optional[ReadHrefModifier] = None):
#         self.href = href
#         with rasterio.open(self.href) as ds:
#             self.crs = ds.crs
#             self.transform = ds.transform
#             self.shape = ds.shape
#             self.bbox = list(ds.bounds)

#             self.tags = ds.tags()
#             # creation_time, product_tile, product_version,

#     @property
#     def time_utc(self) -> datetime:
#         # Time must be in UTC
#         yyyymmdd = re.findall(r'\d+', self.id)[0]
#         time_utc = datetime.strptime(yyyymmdd, '%Y%m%d')
#         # Timezone of data in filename is unknown in reality
#         time_utc = datetime(time_utc.year,
#                             time_utc.month,
#                             time_utc.day,
#                             tzinfo=timezone.utc)
#         return time_utc

#     @property
#     def epsg(self) -> int:
#         if self.crs.to_epsg() is not None:
#             return self.crs.to_epsg()
#         else:
#             raise ValueError('Unable to generate EPSG code')

#     @property
#     def footprint(self) -> JsonDict:
#         return mapping(box(*self.bbox))

#     @property
#     def bbox_wgs84(self) -> List:
#         # See also rasterio.warp.transform_geom and rasterio.warp.transform
#         dst_crs = CRS.from_epsg(4326)
#         bbox_wgs84 = list(transform_bounds(self.crs, dst_crs, *self.bbox))
#         return (bbox_wgs84)

#     @property
#     def footprint_wgs84(self) -> JsonDict:
#         footprint_wgs84 = mapping(box(*self.bbox_wgs84))
#         return footprint_wgs84
