import pytest

from services.login_service import LoginService
from services.product_service import ProductService
from framework.config.settings import settings


@pytest.fixture
def login_service(page):
    return LoginService(page)

@pytest.fixture
def product_service(page):
    return ProductService(page)


@pytest.fixture
def authenticated_product_service(authenticated_context):
    page = authenticated_context.new_page()
    page.goto(f"{settings.base_url}/products")

    return ProductService(page)