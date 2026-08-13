import pytest

from framework.api.auth_api import AuthAPI
from framework.api.api_client import APIClient
from framework.api.product_api import ProductAPI
from framework.config.settings import settings


@pytest.fixture
def api_client():

    auth_api = AuthAPI( #Fetch the base URL
        settings.api_base_url
    )

    token = auth_api.login( #login method: login using email and pwd
        settings.admin_email,
        settings.admin_password
    )

    client = APIClient( #api client needs the base URL and token and creates the session
        settings.api_base_url,
        token
    )

    return client # authenticated client and give to anybody who request fixture product_api        


@pytest.fixture
def product_api(api_client):

    return ProductAPI(api_client)