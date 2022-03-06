from logging import getLogger
from dataclasses import dataclass
from argparse import ArgumentParser
from pathlib import Path

from fiona import open as open_geofile

from core.connection import get_connection
from core.exceptions import MetadataError
from .config import setup_logging
from .table_process_map import TABLE_PROCESS_MAP
from .common import execute_insert

logger = getLogger(__package__)


@dataclass
class ProgramArguments:
    filepath: Path
    destination_table: str
    truncate: bool


def parse_args() -> ProgramArguments:
    parser = ArgumentParser(
        prog=f"python -m {__package__}",
        description="Load a geographic data file to the lookout database",
    )

    parser.add_argument(
        "--filepath",
        "-f",
        type=Path,
        required=True,
        help="File path of the dataset to be loaded",
    )

    parser.add_argument(
        "--destination-table",
        "-d",
        type=str,
        required=True,
        help="Name of the table to load the dataset to",
    )

    parser.add_argument(
        "--truncate",
        "-t",
        type=bool,
        default=False,
        help="Truncate the table before loading",
    )

    return ProgramArguments(**parser.parse_args().__dict__)


def main(filepath: Path, destination_table: str, truncate: bool) -> None:
    if destination_table not in TABLE_PROCESS_MAP.keys():
        raise RuntimeError(f"No process defined for {destination_table}")

    process = TABLE_PROCESS_MAP[destination_table]

    with open_geofile(filepath) as stream:
        if stream.crs["init"] != "epsg:7844":
            raise MetadataError(f"Unexpected CRS found in dataset: {stream.crs}")

        if not (
            process.expected_columns.issubset(
                set(stream.meta["schema"]["properties"].keys())
            )
        ):
            raise MetadataError("Unexpected schema found in source dataset")

        rows = process.row_collector(stream)
        execute_insert(
            get_connection(),
            rows,
            process.table_info,
            truncate,
        )

    logger.info("Process finished")


if __name__ == "__main__":
    setup_logging()
    args = parse_args()
    main(args.filepath, args.destination_table, args.truncate)
