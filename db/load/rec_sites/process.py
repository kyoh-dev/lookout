import json

from fiona.collection import Collection

from db.load.transforms import clean_descr, clean_uppercase
from db.core.exceptions import DataQualityError
from db.load.common import DBTable
from db.load.rec_sites.schema import REC_SITES_SCHEMA

TABLE_INFO = DBTable(
    table_name="rec_site",
    columns=tuple(REC_SITES_SCHEMA.schema_map.values()) + ("geometry",),
    geometry_transform="ST_SetSRID(ST_GeomFromGeoJSON(%s), 7844)",
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
            if column in REC_SITES_SCHEMA.uppercase_attributes and value is not None:
                properties[column] = clean_uppercase(properties[column])

            if column in REC_SITES_SCHEMA.descr_attributes and value is not None:
                properties[column] = clean_descr(properties[column])

        rows.append(
            tuple([properties[col] for col in REC_SITES_SCHEMA.schema_map])
            + (json.dumps(geometry),)
        )

    return rows
