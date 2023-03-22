#!/usr/bin/env python3

"""Creates the example STAC Item and Collection"""

import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

from pystac import CatalogType

from stactools.esa_worldcover import stac

root = Path(__file__).parent.parent
examples = root / "examples"
data_files = root / "tests" / "data-files"
file_list = [
    "ESA_WorldCover_10m_2020_v100_N00E006/ESA_WorldCover_10m_2020_v100_N00E006_Map.tif",
    "ESA_WorldCover_10m_2021_v200_N00E006/ESA_WorldCover_10m_2021_v200_N00E006_Map.tif",
]

with TemporaryDirectory() as tmp_dir:
    print("Creating ESA WorldCover collection...")
    collection = stac.create_collection("esa-worldcover", include_quality_asset=True)
    for file in file_list:
        item = stac.create_item(
            str(data_files / file),
            include_quality_asset=True,
            raster_footprint=True,
        )
        item.properties.pop("created")
        collection.add_item(item)
    collection.update_extent_from_items()

    print("Saving collection...")
    collection.normalize_hrefs(str(examples))
    if examples.exists():
        shutil.rmtree(examples)
    for item in collection.get_all_items():
        item.make_asset_hrefs_relative()
    collection.save(catalog_type=CatalogType.SELF_CONTAINED)

    print("Done!")
