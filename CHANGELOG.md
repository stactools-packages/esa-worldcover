# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/). This project attempts to match the major and minor versions of [stactools](https://github.com/stac-utils/stactools) and increments the patch number as needed.

## [Unreleased]

### Fixed

- Raster footprints no longer clip corners ([08099f4](https://github.com/stactools-packages/esa-worldcover/commit/08099f4cbbcc9e72088c77572e45c5df2c0a6973))

## [0.2.0] - 2023-03-24

### Added

- Support for the 2021 product (version 2.0.0) ([#10](https://github.com/stactools-packages/esa-worldcover/pull/10))
- `create_examples.py` script ([#10](https://github.com/stactools-packages/esa-worldcover/pull/10))
- DOI, User Manual, and Validation links for 2020 and 2021 to the Collection ([#10](https://github.com/stactools-packages/esa-worldcover/pull/10))
- Grid extension ([#10](https://github.com/stactools-packages/esa-worldcover/pull/10))
- Option to use the Map data raster footprint for the Item geometry ([#10](https://github.com/stactools-packages/esa-worldcover/pull/10))

### Removed

- `scientific` extension from Collection ([#10](https://github.com/stactools-packages/esa-worldcover/pull/10))
- Verbiage specific to the 2020 product year and v1.0.0 version ([#10](https://github.com/stactools-packages/esa-worldcover/pull/10))

### Changed

- Command name now matches the package name (`esa-worldcover`) ([#10](https://github.com/stactools-packages/esa-worldcover/pull/10))

### Fixed

- Single asset Items now place all `projection` extension fields in Item properties rather than on the asset ([#10](https://github.com/stactools-packages/esa-worldcover/pull/10))

## [0.1.0] - 2022-04-27

Initial release.

[Unreleased]: <https://github.com/stactools-packages/esa-worldcover/compare/v0.2.0..main>
[0.2.0]: <https://github.com/stactools-packages/esa-worldcover/compare/v0.1.0..v0.2.0>
[0.1.0]: <https://github.com/stactools-packages/esa-worldcover/releases/tag/v0.1.0>
