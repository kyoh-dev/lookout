from sys import stdout
from logging import INFO, basicConfig, captureWarnings

from db_loader.load.common import LoadProcess
from db_loader.load.rec_sites.schema import REC_SITES_SCHEMA
from db_loader.load.rec_sites.process import TABLE_INFO
from db_loader.load.rec_sites.process import collect_rows as rec_sites_row_collector

REC_SITES_PROCESS = LoadProcess(
    expected_columns=set(REC_SITES_SCHEMA.schema_map.keys()),
    row_collector=rec_sites_row_collector,
    table_info=TABLE_INFO,
)

PROCESS_MAP: dict[str, LoadProcess] = {"rec_sites": REC_SITES_PROCESS}


def setup_logging() -> None:
    basicConfig(stream=stdout, level=INFO)
    captureWarnings(True)
