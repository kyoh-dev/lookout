import json

from fiona.collection import Collection

from db.load.transforms import clean_uppercase
from db.core.exceptions import DataQualityError
from db.load.common import DbTable
from db.load.park.schema import PARK_SCHEMA

TABLE_INFO = DbTable(
    table_name="park",
    columns=tuple(PARK_SCHEMA.schema_map.values()) + ("geometry",),
    geometry_transform="ST_GeomFromGeoJSON(%s)",
)


def collect_rows(collection: Collection) -> list[tuple[str, ...]]:
    rows: list = []

    for item in collection:
        geometry = item["geometry"]
        properties = item["properties"]

        if geometry is None:
            raise DataQualityError("Empty geometry found in dataset")

        for column, value in properties.items():
            if column in PARK_SCHEMA.uppercase_attributes and value is not None:
                properties[column] = clean_uppercase(properties[column])

        rows.append(
            tuple([properties[col] for col in PARK_SCHEMA.schema_map])
            + (json.dumps(geometry),)
        )

    return rows
