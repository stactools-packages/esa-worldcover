import unittest

from stactools.esa_worldcover import stac


class StacTest(unittest.TestCase):

    def test_create_item(self) -> None:
        item = stac.create_item(
            "tests/data-files/ESA_WorldCover_10m_2020_v100_N27W099_Map/ESA_WorldCover_10m_2020_v100_N27W099_Map.tif"  # noqa
        )
        self.assertEqual(item.id, "esa_worldcover_10m_2020_v100_n27w099")
        item.validate()

    def test_read_href_modifier(self) -> None:
        href = "tests/data-files/ESA_WorldCover_10m_2020_v100_N27W099_Map/ESA_WorldCover_10m_2020_v100_N27W099_Map.tif"  # noqa
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
