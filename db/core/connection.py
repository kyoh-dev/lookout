from logging import getLogger

from psycopg2.extensions import connection
from psycopg2 import connect, DatabaseError

from db.core.constants import DATABASE_URL

logger = getLogger(__name__)


def get_connection() -> connection:
    try:
        conn = connect(DATABASE_URL)
    except DatabaseError as ex:
        logger.exception("Database connection failed.", ex)
    else:
        return conn
