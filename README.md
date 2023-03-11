# stactools-esa-worldcover

[![PyPI](https://img.shields.io/pypi/v/stactools-esa-worldcover)](https://pypi.org/project/stactools-esa-worldcover/)

- Name: esa-worldcover
- Package: `stactools.esa-worldcover`
- PyPI: <https://pypi.org/project/stactools-esa-worldcover/>
- Owner: @pjhartzell
- Dataset homepage: <https://esa-worldcover.org/en>
- STAC extensions used:
  - [classification](https://github.com/stac-extensions/classification)
  - [item-assets](https://github.com/stac-extensions/item-assets)
  - [proj](https://github.com/stac-extensions/projection/)
  - [raster](https://github.com/stac-extensions/raster)
  - [scientific](https://github.com/stac-extensions/scientific)
- Extra fields:
  - `esa_worldcover:product_tile`: The lat/lon coordinates of the tile southwest corner
  - `esa_worldcover:product_version`: The version of the classification product

Generate STAC Items and Collections for [ESA's 10m resolution global land cover product](https://esa-worldcover.org/en) for the year 2020 based on Sentinel-1 and Sentinel-2 data.

## Examples

### STAC objects

- [Item](examples/ESA_WorldCover_10m_2020_v100_N66E177/ESA_WorldCover_10m_2020_v100_N66E177.json)
- [Collection](examples/collection.json)

### Command-line usage

To create a STAC `Item`:

```bash
stac esaworldcover create-item tests/data-files/ESA_WorldCover_10m_2020_v100_N66E177_Map/ESA_WorldCover_10m_2020_v100_N66E177_Map.tif . --include-quality-asset
```

To create a STAC `Collection` from a text file containing a list of WorldCover Map tile COG files:

```bash
stac esaworldcover create-collection tests/data-files/file-list.txt examples --include-quality-assets
```

The above `create-collection` command will create the contents of the `examples` directory.

Use `stac esaworldcover --help` to see all subcommands and options.
