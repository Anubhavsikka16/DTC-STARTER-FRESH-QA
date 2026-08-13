from framework.api.auth_api import AuthAPI
from framework.config.settings import settings
from framework.api.api_client import APIClient
from framework.api.product_api import ProductAPI


def test_api_login():

    auth_api = AuthAPI(
        settings.api_base_url #fetching the API Base URL
    )

    token = auth_api.login( #login using email and pwd by sending the POST requesr
        settings.admin_email,
        settings.admin_password
    )

    client = APIClient(
        settings.api_base_url,
        token
    )

    # response = client.get(
    #     "/admin/products"
    # )

    product_api = ProductAPI(client)

    response = product_api.get_product(
        "prod_01KZDYGGH965EPCKP9C4D2GH01"
    )

    print("Status:", response.status_code)
    print("URL:", response.url)
    print("Response:", response.text)

    assert response.status_code == 200
    print("Status:", response.status_code)

