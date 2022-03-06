import json

from fiona.collection import Collection

from core.exceptions import DataQualityError
from load.transforms import strip_and_punctuate, strip_and_capitalise
from load.common import DbTable
from .schema import REC_SITE_SCHEMA

TABLE_INFO = DbTable(
    table_name="rec_site",
    columns=tuple(REC_SITE_SCHEMA.schema_map.values()) + ("geometry",),
    geometry_transform="ST_GeomFromGeoJSON(%s)",
)


def collect_rows(collection: Collection) -> list[tuple[str, ...]]:
    rows: list = []

    for item in collection:
        geometry = item["geometry"]
        properties = item["properties"]

        if geometry is None:
            raise DataQualityError("Empty geometry found in dataset")

        if properties["TB_VISITOR"] == "TRAIL BIKE VISITOR AREA":
            properties["TB_VISITOR"] = "Y"

        for column, value in properties.items():
            if column in REC_SITE_SCHEMA.uppercase_attributes and value is not None:
                properties[column] = strip_and_capitalise(properties[column])

            if column in REC_SITE_SCHEMA.descr_attributes and value is not None:
                properties[column] = strip_and_punctuate(properties[column])

        rows.append(
            tuple([properties[col] for col in REC_SITE_SCHEMA.schema_map])
            + (json.dumps(geometry),)
        )

    return rows
