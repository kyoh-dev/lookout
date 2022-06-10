from logging import getLogger
from dataclasses import dataclass
from argparse import ArgumentParser
from pathlib import Path

from .config import setup_logging
from .connection import get_connection
from .sql import execute_copy

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
        "--table",
        "-t",
        type=str,
        required=True,
        help="Name of the table to load the dataset to",
    )

    return ProgramArguments(**parser.parse_args().__dict__)


def main(filepath: Path, destination_table: str) -> None:
    execute_copy(get_connection(), filepath, destination_table)


if __name__ == "__main__":
    setup_logging()
    args = parse_args()
    main(args.filepath, args.destination_table)
