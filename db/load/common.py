from psycopg2.sql import Composed, SQL, Identifier


def truncate_table(table_name: str) -> Composed:
    return SQL("TRUNCATE TABLE {}").format(Identifier(table_name))
