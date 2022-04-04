import logging
import os

import click

from stactools.esa_worldcover import stac

logger = logging.getLogger(__name__)


def create_esaworldcover_command(cli):
    """Creates the stactools-esa-worldcover command line utility."""

    @cli.group(
        "esaworldcover",
        short_help=("Commands for working with ESA 10m 2020 WorldCover"),
    )
    def esaworldcover():
        pass

    # @esaworldcover.command(
    #     "create-collection",
    #     short_help="Creates a STAC collection",
    # )
    # @click.argument("destination")
    # def create_collection_command(destination: str):
    #     """Creates a STAC Collection

    #     Args:
    #         destination (str): An HREF for the Collection JSON
    #     """
    #     collection = stac.create_collection()

    #     collection.set_self_href(destination)

    #     collection.save_object()

    #     return None

    @esaworldcover.command("create-item",
                           short_help=(
                               "Create a STAC Item from an ESA WorldCover Map "
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
