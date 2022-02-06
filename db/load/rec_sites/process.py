from re import sub
from json import dumps
from typing import Optional

from fiona.collection import Collection

from db.core.exceptions import DataQualityError, DataTypeError
from db.load.common import DBTable
from db.load.rec_sites.schema import REC_SITES_SCHEMA

TABLE_INFO = DBTable(
    table_name="rec_sites",
    columns=tuple(REC_SITES_SCHEMA.schema_map.values()) + ("geometry",),
    geometry_transform="ST_SetSRID(ST_GeomFromGeoJSON(%s), 7844)",
)


def clean_uppercase(value: str) -> Optional[str]:
    value = sub(" +", " ", value).strip().capitalize()
    if value == "None":
        return None

    return value


def clean_descr(value: str) -> str:
    value = sub(" +", " ", value).strip()
    if not value.endswith("."):
        value += "."

    return value


def collect_rows(collection: Collection) -> list[tuple[str, ...]]:
    rows: list = []

    for item in collection:
        geometry = item["geometry"]
        properties = item["properties"]

        if geometry is None:
            raise DataQualityError("Empty geometry_transform found in dataset")

        if geometry["type"] != "Point":
            raise DataTypeError("Unexpected geometry_transform type found in dataset")

        if properties["TB_VISITOR"] == "TRAIL BIKE VISITOR AREA":
            properties["TB_VISITOR"] = "Y"

        for column, value in properties.items():
            # If the column is uppercase, strip and NULLify it.
            if column in REC_SITES_SCHEMA.uppercase_attributes and value is not None:
                properties[column] = clean_uppercase(properties[column])

            # If the column is a description, strip and add a full stop.
            if column in REC_SITES_SCHEMA.descr_attributes and value is not None:
                properties[column] = clean_descr(properties[column])

        rows.append(
            tuple([properties[col] for col in REC_SITES_SCHEMA.schema_map])
            + (dumps(geometry),)
        )

    return rows
