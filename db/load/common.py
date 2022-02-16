from logging import getLogger
from dataclasses import dataclass, field
from collections.abc import Callable

from psycopg2.sql import Composed, SQL, Identifier, Placeholder
from psycopg2.extensions import connection
from psycopg2.extras import execute_values

logger = getLogger(__package__)


@dataclass
class DbTable:
    """Class for storing database table information and formatting queries"""

    table_name: str
    columns: tuple[str, ...]
    geometry_transform: str
    schema_name: str = "public"

    @property
    def truncate_stmt(self) -> Composed:
        return SQL("TRUNCATE TABLE {};").format(
            Identifier(self.schema_name, self.table_name)
        )

    @property
    def insert_stmt(self) -> Composed:
        return SQL(
            "INSERT INTO {table} ({column_names}) VALUES %s RETURNING id;"
        ).format(
            table=Identifier(self.schema_name, self.table_name),
            column_names=SQL(", ").join(map(Identifier, self.columns)),
        )

    @property
    def values_template(self) -> Composed:
        return Composed(
            [
                SQL("({}").format(
                    SQL(", ").join(Placeholder() * (len(self.columns) - 1))
                ),
                SQL(", %s)"),
            ]
        )


@dataclass
class DataSchema:
    """Class for holding information about a dataset's schema"""

    schema_map: dict[str, str]
    descr_attributes: set[str] = field(default_factory=set)
    uppercase_attributes: set[str] = field(default_factory=set)


@dataclass
class LoadProcess:
    """Class for holding a load process's relevant objects and functions"""

    expected_columns: set[str]
    row_collector: Callable
    table_info: DbTable


def execute_insert(
    conn: connection,
    data_rows: list[tuple[str, ...]],
    table_info: DbTable,
    truncate: bool = False,
) -> None:
    with conn:
        with conn.cursor() as cursor:
            if truncate:
                logger.info(
                    f"Truncating table `{table_info.schema_name}.{table_info.table_name}` before insert starts"
                )
                cursor.execute(table_info.truncate_stmt)

            inserted = execute_values(
                cursor,
                sql=table_info.insert_stmt,
                argslist=data_rows,
                template=table_info.values_template,
                fetch=True,
            )

    logger.info(
        f"Successfully inserted {len(inserted)} records into `{table_info.schema_name}.{table_info.table_name}`"
    )
    conn.close()
