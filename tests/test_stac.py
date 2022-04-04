import unittest

from stactools.esa_worldcover import stac


class StacTest(unittest.TestCase):

    # def test_create_collection(self):
    #     # Write tests for each for the creation of a STAC Collection
    #     # Create the STAC Collection...
    #     collection = stac.create_collection()
    #     collection.set_self_href("")

    #     # Check that it has some required attributes
    #     self.assertEqual(collection.id, "my-collection-id")
    #     # self.assertEqual(collection.other_attr...

    #     # Validate
    #     collection.validate()

    def test_create_item(self):
        # Write tests for each for the creation of STAC Items
        # Create the STAC Item...
        item = stac.create_item(
            "tests/data-files/ESA_WorldCover_10m_2020_v100_N27W099_Map/ESA_WorldCover_10m_2020_v100_N27W099_Map.tif"  # noqa
        )

        # Check that it has some required attributes
        self.assertEqual(item.id, "esa_worldcover_10m_2020_v100_n27w099")
        # self.assertEqual(item.other_attr...

        # Validate
        item.validate()

    # def test_create_collection(self):
    #     collection = stac.create_collection("esa-worldcover")
    #     self.assertEqual(collection.id, "test")
    #     # collection.validate()
