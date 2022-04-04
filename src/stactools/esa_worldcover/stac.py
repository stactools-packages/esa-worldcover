import logging
import os
from datetime import datetime, timezone
from typing import Optional

import rasterio
import shapely
from pystac import Asset, Collection, Item, MediaType
from pystac.extensions.projection import ProjectionExtension
from pystac.extensions.raster import RasterBand, RasterExtension
from pystac.utils import str_to_datetime
from stactools.core.io import ReadHrefModifier

from stactools.esa_worldcover import constants

logger = logging.getLogger(__name__)


def create_item(map_href: str,
                read_href_modifier: Optional[ReadHrefModifier] = None) -> Item:
    """Create a STAC Item for a 3x3 degree COG tile of the ESA 10m WorldCover
    classification product.

    Expects an input quality COG to exist alongside the classificaton map COG.

    Args:
        map_href (str): An href to a COG containing a tile of classication data.
        read_href_modifier (Callable[[str], str]): An optional function to
            modify the MTL and USGS STAC hrefs (e.g. to add a token to a url).
    Returns:
        Item: STAC Item object representing the worldcover tile
    """
    base_href = "_".join(map_href.split('_')[:-1])
    qua_href = f"{base_href}_InputQuality.tif"

    if read_href_modifier:
        modified_map_href = read_href_modifier(map_href)
        modified_qua_href = read_href_modifier(qua_href)
    else:
        modified_map_href = map_href
        modified_qua_href = qua_href
    with rasterio.open(modified_map_href) as dataset:
        bbox = dataset.bounds
        map_transform = list(dataset.transform)[0:6]
        map_shape = dataset.shape
        map_tags = dataset.tags()
    with rasterio.open(modified_qua_href) as dataset:
        qua_transform = list(dataset.transform)[0:6]
        qua_shape = dataset.shape
        qua_tags = dataset.tags()

    # --Item--
    geometry = shapely.geometry.mapping(shapely.geometry.box(*bbox))

    item = Item(id=os.path.basename(base_href).lower(),
                geometry=geometry,
                bbox=bbox,
                datetime=datetime.now(),
                properties={})
    item.common_metadata.description = constants.DESCRIPTION
    item.common_metadata.created = datetime.now(tz=timezone.utc)
    item.common_metadata.mission = constants.MISSION
    item.common_metadata.platform = constants.PLATFORM
    item.common_metadata.instruments = constants.INSTRUMENTS
    item.datetime = constants.START_TIME
    item.common_metadata.start_datetime = constants.START_TIME
    item.common_metadata.end_datetime = constants.END_TIME
    item.properties["esa_worldcover:product_tile"] = map_tags["product_tile"]
    item.properties["esa_worldcover:product_version"] = map_tags[
        "product_version"]

    item_proj = ProjectionExtension.ext(item, add_if_missing=True)
    item_proj.epsg = constants.EPSG

    # --Map asset--
    map_asset = Asset(href=map_href, roles=["data"])
    map_asset.title = constants.MAP_TITLE
    map_asset.description = constants.MAP_DESCRIPTION
    map_asset.media_type = MediaType.COG
    map_asset.common_metadata.created = str_to_datetime(
        map_tags["creation_time"])
    item.add_asset('map', map_asset)

    map_proj = ProjectionExtension.ext(map_asset, add_if_missing=True)
    map_proj.transform = map_transform
    map_proj.shape = map_shape

    map_raster = RasterExtension.ext(map_asset, add_if_missing=True)
    map_raster.bands = [RasterBand.create(**constants.MAP_RASTER)]

    map_asset.extra_fields = {"classification:classes": constants.MAP_CLASSES}
    item.stac_extensions.append(constants.CLASSIFICATION_SCHEMA)

    # --Input quality asset--
    qua_asset = Asset(href=qua_href, roles=["metadata"])
    qua_asset.title = constants.QUALITY_TITLE
    qua_asset.description = constants.QUALITY_DESCRIPTION
    qua_asset.media_type = MediaType.COG
    qua_asset.common_metadata.created = str_to_datetime(
        qua_tags["creation_time"])
    item.add_asset('input_quality', qua_asset)

    qua_proj = ProjectionExtension.ext(qua_asset, add_if_missing=True)
    qua_proj.transform = qua_transform
    qua_proj.shape = qua_shape
    
    qua_raster = RasterExtension.ext(qua_asset, add_if_missing=True)
    qua_raster.bands = [
        RasterBand.create(**band) for band in constants.QUALITY_RASTER
    ]

    return item


def create_collection(collection_id: str) -> Collection:
    """Creates a STAC Collection for the 2020 ESA 10m WorldCover classification
    product.

    Args:
        collection_id (str): Desired ID for the STAC Collection.
    Returns:
        Collection: The created STAC Collection
    """
    collection = Collection(id=collection_id,
                            title=constants.tit)






# def create_collection() -> Collection:
#     """Create a STAC Collection

#     This function includes logic to extract all relevant metadata from
#     an asset describing the STAC collection and/or metadata coded into an
#     accompanying constants.py file.

#     See `Collection<https://pystac.readthedocs.io/en/latest/api.html#collection>`_.

#     Returns:
#         Collection: STAC Collection object
#     """
#     providers = [
#         Provider(
#             name="The OS Community",
#             roles=[
#                 ProviderRole.PRODUCER, ProviderRole.PROCESSOR,
#                 ProviderRole.HOST
#             ],
#             url="https://github.com/stac-utils/stactools",
#         )
#     ]

#     # Time must be in UTC
#     demo_time = datetime.now(tz=timezone.utc)

#     extent = Extent(
#         SpatialExtent([[-180., 90., 180., -90.]]),
#         TemporalExtent([demo_time, None]),
#     )

#     collection = Collection(
#         id="my-collection-id",
#         title="A dummy STAC Collection",
#         description="Used for demonstration purposes",
#         license="CC-0",
#         providers=providers,
#         extent=extent,
#         catalog_type=CatalogType.RELATIVE_PUBLISHED,
#     )

#     return collection
