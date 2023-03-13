import unittest

import stactools.esa_worldcover


class TestModule(unittest.TestCase):
    def test_version(self) -> None:
        self.assertIsNotNone(stactools.esa_worldcover.__version__)
