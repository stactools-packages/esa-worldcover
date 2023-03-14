import logging
from datetime import datetime, timezone
from typing import Optional

from pystac import Collection, Item
from pystac.extensions.item_assets import ItemAssetsExtension
from pystac.extensions.projection import ItemProjectionExtension
from pystac.extensions.raster import RasterExtension
from stactools.core.io import ReadHrefModifier

from stactools.esa_worldcover import constants
from stactools.esa_worldcover.metadata import Metadata

logger = logging.getLogger(__name__)


def create_item(
    map_href: str,
    include_quality_asset: bool = False,
    read_href_modifier: Optional[ReadHrefModifier] = None,
) -> Item:
    """Create a STAC Item with a single Asset for a 3x3 degree COG tile of the
    ESA 10m WorldCover classification product.

    Optionally creates an additional Asset for an input quality COG, which is
    assumed to exist alongside the map COG.

    Args:
        map_href (str): An href to a COG containing a tile of classication data.
        include_quality_asset (bool): Flag to add an input quality asset. Requires
            an input quality COG to exist alongside the map COG.
        read_href_modifier (Callable[[str], str]): An optional function to
            modify the MTL and USGS STAC hrefs (e.g. to add a token to a url).

    Returns:
        Item: STAC Item object representing the worldcover tile
    """
    map_metadata = Metadata(map_href, read_href_modifier)

    item = Item(
        id=map_metadata.item_id,
        geometry=map_metadata.geometry,
        bbox=map_metadata.bbox,
        datetime=None,
        properties={
            "start_datetime": map_metadata.start_datetime,
            "end_datetime": map_metadata.end_datetime,
            "esa_worldcover:product_version": map_metadata.version,
            "esa_worldcover:product_tile": map_metadata.tile,
        },
    )

    item.common_metadata.description = constants.ITEM_DESCRIPTION
    item.common_metadata.created = datetime.now(tz=timezone.utc)
    item.common_metadata.mission = constants.MISSION
    item.common_metadata.platform = constants.PLATFORM
    item.common_metadata.instruments = constants.INSTRUMENTS

    item.add_asset("map", map_metadata.asset)

    item_proj = ItemProjectionExtension.ext(item, add_if_missing=True)
    item_proj.epsg = constants.EPSG

    if include_quality_asset:
        quality_href = Metadata.quality_href(map_href)
        quality_metadata = Metadata(quality_href, read_href_modifier)
        item.add_asset("input_quality", quality_metadata.asset)
    else:
        item_proj.shape = item.assets["map"].extra_fields.pop("proj:shape")
        item_proj.transform = item.assets["map"].extra_fields.pop("proj:transform")

    RasterExtension.add_to(item)
    item.stac_extensions.append(constants.CLASSIFICATION_SCHEMA)

    item.validate()

    return item


def create_collection(
    collection_id: str, include_quality_asset: bool = False
) -> Collection:
    """Creates a STAC Collection for the ESA WorldCover classification
    product for years 2020-2021 (product versions 1.0.0 and 2.0.0).

    Args:
        collection_id (str): Desired ID for the STAC Collection.
        include_quality_asset (bool): Flag to include the 'input_quality' asset
            in the item_assets dictionary.

    Returns:
        Collection: The created STAC Collection.
    """
    collection = Collection(
        id=collection_id,
        title=constants.COLLECTION_TITLE,
        description=constants.COLLECTION_DESCRIPTION,
        license=constants.LICENSE,
        keywords=constants.KEYWORDS,
        providers=constants.PROVIDERS,
        extent=constants.EXTENT,
        summaries=constants.SUMMARIES,
    )

    item_assets_ext = ItemAssetsExtension.ext(collection, add_if_missing=True)
    item_assets = constants.ITEM_ASSETS.copy()
    if not include_quality_asset:
        item_assets.pop("input_quality")
    item_assets_ext.item_assets = item_assets

    RasterExtension.add_to(collection)
    collection.stac_extensions.append(constants.CLASSIFICATION_SCHEMA)

    collection.add_links(
        [
            constants.LICENSE_LINK,
            constants.CITE_AS_LINK_2020,
            constants.CITE_AS_LINK_2021,
            constants.USER_MANUAL_2020_LINK,
            constants.USER_MANUAL_2021_LINK,
            constants.VALIDATION_2020_LINK,
            constants.VALIDATION_2021_LINK,
        ]
    )

    return collection
