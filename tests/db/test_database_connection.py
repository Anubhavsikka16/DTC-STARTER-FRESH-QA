from framework.config.settings import settings
from framework.db.connection import Database


def test_database_connection():

    db = Database(
        host=settings.db_host,
        port=settings.db_port,
        database=settings.db_name,
        user=settings.db_user,
        password=settings.db_password
    )

    assert db.connection is not None
    db.fetch_one("Select 1")
    db.close()