

class ProductAPI:

    def __init__(self, api_client):
        self.api_client = api_client

    def get_product(self, product_id):

        return self.api_client.get(
            f"/admin/products/{product_id}"
        )