from db.load.common import LoadProcess
from db.load.rec_site.schema import REC_SITE_SCHEMA
from db.load.rec_site.process import (
    TABLE_INFO as REC_SITE_TABLE,
    collect_rows as rec_site_row_collector,
)
from db.load.park.schema import PARK_SCHEMA
from db.load.park.process import (
    TABLE_INFO as PARK_TABLE,
    collect_rows as park_row_collector,
)

REC_SITE_PROCESS = LoadProcess(
    expected_columns=set(REC_SITE_SCHEMA.schema_map.keys()),
    row_collector=rec_site_row_collector,
    table_info=REC_SITE_TABLE,
)
PARK_PROCESS = LoadProcess(
    expected_columns=set(PARK_SCHEMA.schema_map.keys()),
    row_collector=park_row_collector,
    table_info=PARK_TABLE,
)

TABLE_PROCESS_MAP: dict[str, LoadProcess] = {
    "rec_site": REC_SITE_PROCESS,
    "park": PARK_PROCESS,
}
