from dataclasses import dataclass
from argparse import ArgumentParser
from pathlib import Path


@dataclass
class ProgramArguments:
    filepath: Path
    destination_table: str


def parse_args() -> ProgramArguments:
    parser = ArgumentParser(
        prog=f"python -m {__package__}",
        description="Load a geographic data file to the lookout database",
    )

    parser.add_argument(
        "--filepath", "-f", type=Path, help="File path of the dataset to be loaded"
    )

    parser.add_argument(
        "--destination-table",
        "-d",
        type=str,
        help="Name of the table to load the dataset to",
    )

    return ProgramArguments(**parser.parse_args().__dict__)


def main(filepath: Path, destination_table: str) -> None:
    # TODO: Read header and check expected columns exist in schema.
    # TODO: Check source CRS is in expected projection.
    ...


if __name__ == "__main__":
    args = parse_args()
    main(args.filepath, args.destination_table)
