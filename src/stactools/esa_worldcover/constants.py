from datetime import datetime, timezone
from typing import Any, Dict, List

from pystac import Link, Provider, ProviderRole

LICENSE = "CC-BY-4.0"
LICENSE_LINK = Link(
    rel="license",
    target="https://creativecommons.org/licenses/by/4.0/",
    title="Creative Commons Attribution 4.0 International License")
DOI = "10.5281/zenodo.5571936"
CITATION = (
    "Zanaga, D., Van De Kerchove, R., De Keersmaecker, W., Souverijns, N., "
    "Brockmann, C., Quast, R., Wevers, J., Grosu, A., Paccini, A., Vergnaud, "
    "S., Cartus, O., Santoro, M., Fritz, S., Georgieva, I., Lesiv, M., Carter, "
    "S., Herold, M., Li, Linlin, Tsendbazar, N.E., Ramoino, F., Arino, O., "
    "2021. ESA WorldCover 10m 2020 v100. https://doi.org/10.5281/zenodo.5571936"
)
CITATION_LINK = Link(
    rel="cite-as",
    target="https://doi.org/10.5281/zenodo.5571936",
    title="ESA WorldCover 10m 2020 v100",
    extra_fields={
        "copyright":
        ("Copyright ESA WorldCover project 2020 / Contains modified "
         "Copernicus Sentinel data (2020) processed by ESA WorldCover "
         "consortium")
    })
PROVIDERS = [
    Provider(
        name="ESA WorldCover Consortium",
        description=(
            "The WorldCover product is developed by a consortium led by VITO "
            "Remote Sensing together with partners Brockmann Consult, CS SI, "
            "Gamma Remote Sensing AG, IIASA and Wageningen University"),
        roles=[ProviderRole.PROCESSOR],
        url="https://worldcover2020.esa.int/"),
    Provider(name="ESA",
             roles=[
                 ProviderRole.LICENSOR, ProviderRole.PRODUCER,
                 ProviderRole.HOST
             ],
             url="https://esa-worldcover.org/en")
]
KEYWORDS = ["Sentinel, ESA, Satellite, Global, Classification"]

DESCRIPTION = "ESA WorldCover product at 10m resolution for year 2020"
# Per the discussion in
# https://github.com/radiantearth/stac-spec/issues/216, it seems like
# the recommendation for multi-platform datasets is to include all platforms
# and use a string seperator. Same logic is applied to the mission.
MISSION = "Sentinel-1, Sentinel-2"
PLATFORM = "Sentinel-1A, Sentinel-1B, Sentinel-2A, Sentinel-2B"
INSTRUMENTS = ["C-SAR", "MSI"]
EPSG = 4326
START_TIME = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
END_TIME = datetime(2020, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
CLASSIFICATION_SCHEMA = "https://stac-extensions.github.io/classification/v1.0.0/schema.json"

QUALITY_TITLE = "Classification Input Data Quality"
QUALITY_DESCRIPTION = (
    "Per pixel quality indicator showing the quality of the electro-optical "
    "input data. Band 1 contains the number of Sentinel-1 GAMMA0 observations "
    "used in the classification workflow. Band 2 contains the number of "
    "Sentinel-2 L2A observations used in the classification workflow. Band 3 "
    "contains the percentage (0-100) of invalid S2 observations discarded in "
    "the classification workflow (after cloud and cloud shadow filtering).")
QUALITY_RASTER: List[Dict[str, Any]] = [{
    "nodata": -1,
    "sampling": "area",
    "data_type": "int16",
    "spatial_resolution": 60
}, {
    "nodata": -1,
    "sampling": "area",
    "data_type": "int16",
    "spatial_resolution": 60
}, {
    "nodata": -1,
    "sampling": "area",
    "data_type": "int16",
    "spatial_resolution": 60
}]

MAP_TITLE = "Land Cover Classes"
MAP_DESCRIPTION = (
    "Discrete classification according to the Land Cover Classification System "
    "scheme developed by the United Nations Food and Agriculture Organization")
MAP_RASTER: Dict[str, Any] = {
    "nodata": 0,
    "sampling": "area",
    "data_type": "uint16",
    "spatial_resolution": 10
}
MAP_CLASSES = [{
    "value": 10,
    "description": "Tree cover",
    "color-hint": "006400"
}, {
    "value": 20,
    "description": "Shrubland",
    "color-hint": "FFBB22"
}, {
    "value": 30,
    "description": "Grassland",
    "color-hint": "FFFF4C"
}, {
    "value": 40,
    "description": "Cropland",
    "color-hint": "F096FF"
}, {
    "value": 50,
    "description": "Built-up",
    "color-hint": "FA0000"
}, {
    "value": 60,
    "description": "Bare / sparse vegetation",
    "color-hint": "B4B4B4"
}, {
    "value": 70,
    "description": "Snow and ice",
    "color-hint": "F0F0F0"
}, {
    "value": 80,
    "description": "Permanent water bodies",
    "color-hint": "0064C8"
}, {
    "value": 90,
    "description": "Herbaceous wetland",
    "color-hint": "0096A0"
}, {
    "value": 95,
    "description": "Mangroves",
    "color-hint": "00CF75"
}, {
    "value": 100,
    "description": "Moss and lichen",
    "color-hint": "FAE6A0"
}]
