from json import dumps

from fiona.collection import Collection

from db.core.exceptions import DataQualityError, DataTypeError
from db.load.common import DBTable
from db.load.rec_sites.schema import REC_SITES_SCHEMA

TABLE_INFO = DBTable(
    table_name="rec_sites",
    columns=tuple(REC_SITES_SCHEMA.schema_map.values()) + ("geometry",),
    geometry_transform="ST_SetSRID(ST_GeomFromGeoJSON(%s), 7844)",
)


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

        # If the column is a description, make sure it's stripped and has a full stop at the end.
        for column, value in properties.keys():
            if (
                column in REC_SITES_SCHEMA.descr_attributes
                and value is not None
            ):
                value = value.strip()

                if not value.endswith("."):
                    value += "."

        # TODO: Cast string columns with a value of 'NONE' to None/NULL


        rows.append(
            tuple([properties[col] for col in REC_SITES_SCHEMA.schema_map])
            + (dumps(geometry),)
        )

    return rows
