from framework.utils.testdata import generate_product_data


class TestCreateNewProduct:

    def test_create_product_e2e(
        self,
        authenticated_product_service,
        product_api,
        product_repository
    ):

        # Generate unique test data
        product = generate_product_data()

        # Create product through UI
        details_page = (
            authenticated_product_service.create_product(
                product["title"],
                product["usd_price"]
            )
        )

        # Verify UI
        details_page.is_product_details_page_loaded()

        # Get product ID
        product_id = details_page.get_product_id()

        # -------------------------
        # API validation
        # -------------------------

        api_response = product_api.get_product(product_id)

        assert api_response.status_code == 200

        api_product = api_response.json()["product"]

        assert api_product["id"] == product_id
        assert api_product["title"] == product["title"]
        assert api_product["status"] == "published"

        # -------------------------
        # DB validation
        # -------------------------

        db_product = product_repository.get_product(
            product_id
        )

        assert db_product is not None

        db_product_id = db_product[0]
        db_title = db_product[1]
        db_status = db_product[3]

        assert db_product_id == product_id
        assert db_title == product["title"]
        assert db_status == "published"