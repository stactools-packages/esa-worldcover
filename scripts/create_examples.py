#!/usr/bin/env python3

"""Creates the example STAC Item and Collection"""

import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

from pystac import CatalogType

from stactools.esa_worldcover import stac

root = Path(__file__).parent.parent
examples = root / "examples"
data_files = root / "tests" / "data-files" / "ESA_WorldCover_10m_2020_v100_N66E177_Map"

with TemporaryDirectory() as tmp_dir:
    print("Creating ESA WorldCover collection...")
    collection = stac.create_collection("esa-worldcover", include_quality_asset=True)
    item = stac.create_item(
        str(data_files / "ESA_WorldCover_10m_2020_v100_N66E177_Map.tif"),
        include_quality_asset=True,
    )
    item.properties.pop("created")
    collection.add_item(item)

    print("Saving collection...")
    collection.normalize_hrefs(str(examples))
    shutil.rmtree(examples)
    for item in collection.get_all_items():
        item.make_asset_hrefs_relative()
    collection.save(catalog_type=CatalogType.SELF_CONTAINED)

    print("Done!")
