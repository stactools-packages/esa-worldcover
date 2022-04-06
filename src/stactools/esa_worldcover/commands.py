import logging
import os

import click
from click import Command, Group
from pystac import CatalogType

from stactools.esa_worldcover import stac

logger = logging.getLogger(__name__)


def create_esaworldcover_command(cli: Group) -> Command:
    """Creates the stactools-esa-worldcover command line utility."""

    @cli.group(
        "esaworldcover",
        short_help=("Commands for working with ESA 10m 2020 WorldCover"),
    )
    def esaworldcover():
        pass

    @esaworldcover.command(
        "create-collection",
        short_help="Creates a STAC collection of ESA WorldCover product tiles.",
    )
    @click.argument("INFILE")
    @click.argument("OUTDIR")
    @click.option("-i",
                  "--id",
                  default="esa-worldcover",
                  show_default=True,
                  help="collection id string")
    def create_collection_command(infile: str, outdir: str, id: str) -> None:
        """Creates a STAC Collection for Items defined by the hrefs in INFILE"

        \b
        Args:
            infile (str): Text file containing one href per line. The hrefs
                should point to ESA WorldCover 3x3 degree tile Map COGs.
            outdir (str): Directory that will contain the collection.
            id (str): Collection id. Defaults to "esa-worldcover".
        """
        with open(infile) as file:
            hrefs = [line.strip() for line in file.readlines()]

        collection = stac.create_collection(id)
        collection.set_self_href(os.path.join(outdir, "collection.json"))
        collection.catalog_type = CatalogType.SELF_CONTAINED
        for href in hrefs:
            item = stac.create_item(href)
            collection.add_item(item)
        collection.make_all_asset_hrefs_relative()
        collection.validate_all()
        collection.save()

    @esaworldcover.command(
        "create-item",
        short_help=("Create a STAC Item from an ESA WorldCover Map "
                    "COG file."))
    @click.argument("INFILE")
    @click.argument("OUTDIR")
    def create_item_command(infile: str, outdir: str) -> None:
        """Creates a STAC Item for a 3x3 degree tile of the ESA 10m WorldCover
        classification product.

        \b
        Args:
            infile (str): HREF of the classification map COG.
            outdir (str): Directory that will contain the STAC Item.
        """
        item = stac.create_item(infile)
        item_path = os.path.join(outdir, f"{item.id}.json")
        item.set_self_href(item_path)
        item.make_asset_hrefs_relative()
        item.validate()
        item.save_object()

    return esaworldcover
