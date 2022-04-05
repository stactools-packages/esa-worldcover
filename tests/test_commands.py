import os.path
from tempfile import TemporaryDirectory
from typing import Callable, List

import pystac
from click import Command, Group
from stactools.testing import CliTestCase

from stactools.esa_worldcover.commands import create_esaworldcover_command


class ItemCommandTest(CliTestCase):

    def create_subcommand_functions(self) -> List[Callable[[Group], Command]]:
        return [create_esaworldcover_command]

    def test_create_item(self) -> None:
        infile = "tests/data-files/ESA_WorldCover_10m_2020_v100_N66E177_Map/ESA_WorldCover_10m_2020_v100_N66E177_Map.tif"  # noqa
        with TemporaryDirectory() as tmp_dir:
            cmd = f"esaworldcover create-item {infile} {tmp_dir}"
            self.run_command(cmd)
            item_path = os.path.join(
                tmp_dir, "esa_worldcover_10m_2020_v100_n66e177.json")
            item = pystac.read_file(item_path)
        item.validate()
