from json import dumps

from fiona.collection import Collection

from db.core.exceptions import DataQualityError, DataTypeError
from db.load.common import DbTable
from db.load.rec_sites.schema import SCHEMA_MAP

table_info = DbTable(
    table_name="rec_sites",
    columns=tuple(SCHEMA_MAP.values()),
    geometry="ST_SetSRID(ST_GeomFromGeoJSON(%(geometry)s), 7844)"
)


def collect_rows(collection: Collection) -> list[tuple[str, ...]]:
    rows: list = []

    for item in collection:
        geometry = item["geometry"]
        properties = item["properties"]

        if geometry is None:
            raise DataQualityError("Empty geometry found in dataset")

        if geometry["type"] != "Point":
            raise DataTypeError("Unexpected geometry type found in dataset")

        rows.append(tuple(SCHEMA_MAP.keys()) + (dumps(geometry),))

    return rows
