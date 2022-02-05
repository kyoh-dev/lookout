from dataclasses import dataclass

from psycopg2.sql import Composed, SQL, Identifier, Placeholder
from psycopg2.extensions import connection


@dataclass
class DbTable:
    table_name: str
    columns: tuple[str, ...]
    geometry: str

    @property
    def truncate_stmt(self) -> Composed:
        return SQL("TRUNCATE TABLE {}").format(Identifier(self.table_name))

    @property
    def insert_stmt(self) -> Composed:
        column_identifiers = SQL(", ").join(map(Identifier, self.columns))
        value_placeholders = SQL(", ").join(map(Placeholder, self.columns))
        return Composed([
            SQL("INSERT INTO {table} ({column_names}) VALUES ({values}, ").format(
                table=Identifier(self.table_name),
                column_names=column_identifiers,
                values=value_placeholders),
            SQL(self.geometry), SQL(")")
        ])


def insert_rows(conn: connection, data_rows: list[tuple[str, ...]], table_info: DbTable) -> int:
    ...
