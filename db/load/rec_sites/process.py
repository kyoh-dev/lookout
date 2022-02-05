from json import dumps

from fiona.collection import Collection

from db.core.exceptions import DataQualityError, DataTypeError
from db.load.rec_sites.schema_map import SCHEMA_MAP


def collect_rows(collection: Collection) -> list[tuple[str, ...]]:
    rows: list = []

    for item in collection:
        geometry = item["geometry"]
        properties = item["properties"]

        if geometry is None:
            raise DataQualityError("Empty geometry found in dataset")

        if geometry["type"] != "Point":
            raise DataTypeError("Unexpected geometry type found in dataset")

        data_row = [properties[col] for col in SCHEMA_MAP]
        data_row.append(dumps(geometry))

        data_row = tuple(data_row)
        rows.append(data_row)

    return rows
