import unittest

from stactools.esa_worldcover import stac
from tests import test_data


class StacTest(unittest.TestCase):

    def test_create_item(self) -> None:
        href = test_data.get_path(
            "data-files/ESA_WorldCover_10m_2020_v100_N66E177_Map/ESA_WorldCover_10m_2020_v100_N66E177_Map.tif"  # noqa
        )
        item = stac.create_item(href)
        self.assertEqual(item.id, "ESA_WorldCover_10m_2020_v100_N66E177")
        self.assertEqual(len(item.assets), 1)
        item.validate()

    def test_create_item_quality_assets(self) -> None:
        href = test_data.get_path(
            "data-files/ESA_WorldCover_10m_2020_v100_N66E177_Map/ESA_WorldCover_10m_2020_v100_N66E177_Map.tif"  # noqa
        )
        item = stac.create_item(href, quality_asset=True)
        self.assertEqual(item.id, "ESA_WorldCover_10m_2020_v100_N66E177")
        self.assertEqual(len(item.assets), 2)
        item.validate()

    def test_read_href_modifier(self) -> None:
        href = test_data.get_path(
            "data-files/ESA_WorldCover_10m_2020_v100_N66E177_Map/ESA_WorldCover_10m_2020_v100_N66E177_Map.tif"  # noqa
        )
        did_it = False

        def read_href_modifier(href: str) -> str:
            nonlocal did_it
            did_it = True
            return href

        _ = stac.create_item(href, read_href_modifier=read_href_modifier)
        assert did_it

    def test_create_collection(self) -> None:
        collection = stac.create_collection("esa-worldcover")
        collection.set_self_href("")
        self.assertEqual(collection.id, "esa-worldcover")
        collection.validate()
