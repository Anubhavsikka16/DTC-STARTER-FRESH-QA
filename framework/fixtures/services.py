import pytest

from services.login_service import LoginService
from services.product_service import ProductService


@pytest.fixture
def login_service(page):
    return LoginService(page)

@pytest.fixture
def product_service(page):
    return ProductService(page)