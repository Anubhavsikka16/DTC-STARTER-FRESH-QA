import pytest

from framework.config.settings import settings
from framework.db.connection import Database
from framework.db.product_repository import ProductRepository


@pytest.fixture
def product_repository():

    db = Database(
        host=settings.db_host,
        port=settings.db_port,
        database=settings.db_name,
        user=settings.db_user,
        password=settings.db_password
    )

    repository = ProductRepository(db)

    yield repository

    db.close()