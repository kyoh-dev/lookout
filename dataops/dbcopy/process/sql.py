from logging import getLogger
from pathlib import Path

import fiona

from psycopg2.extensions import connection
from psycopg2.sql import Identifier, SQL

logger = getLogger(__name__)


def execute_copy(conn: connection, filepath: Path, destination_table: str) -> None:
    logger.info(f"Loading {filepath.name} to {destination_table} ...")
    with fiona.open(filepath) as data_stream:
        cursor = conn.cursor()

        cursor.copy_expert(
            SQL("COPY {} FROM STDIN").format(Identifier(destination_table)), data_stream
        )

        cursor.execute(
            SQL("SELECT COUNT(*) FROM {}").format(Identifier(destination_table))
        )
        copied_rows = cursor.fetchone()[0]
        conn.commit()
        logger.info(
            f"Successfully loaded {copied_rows} records to {destination_table} ..."
        )
