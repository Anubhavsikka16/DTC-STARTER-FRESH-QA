import pytest

from framework.api.auth_api import AuthAPI
from framework.api.api_client import APIClient
from framework.api.product_api import ProductAPI
from framework.config.settings import settings


@pytest.fixture
def api_client():

    auth_api = AuthAPI(
        settings.api_base_url
    )

    token = auth_api.login(
        settings.admin_email,
        settings.admin_password
    )

    client = APIClient(
        settings.api_base_url,
        token
    )

    return client


@pytest.fixture
def product_api(api_client):

    return ProductAPI(api_client)