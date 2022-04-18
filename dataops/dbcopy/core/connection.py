from logging import getLogger

from psycopg2 import connect, DatabaseError
from psycopg2.extensions import connection

from loader.core.constants import DATABASE_URL

logger = getLogger(__name__)


def get_connection() -> connection:
    try:
        conn = connect(DATABASE_URL)
    except DatabaseError as ex:
        raise RuntimeError("Database connection failed") from ex
    else:
        return conn
