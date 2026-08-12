from framework.config.settings import settings
from framework.db.connection import Database
from framework.db.product_repository import ProductRepository


def test_get_product(product_repository):


    product = product_repository.get_product(
        "prod_01KZQDCGYDQH8K8PW8W1CDAHCA"
    )

    assert product is not None
    assert product[0] == "prod_01KZQDCGYDQH8K8PW8W1CDAHCA"
    assert product[1] == "Bomber Jacket"

   