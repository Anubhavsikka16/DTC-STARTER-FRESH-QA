import pytest
from framework.config.settings import settings
from framework.utils.testdata import generate_product_data

class TestCreateProductE2E:

    @pytest.mark.smoke
    def test_product_creation(self,login_service,product_service):
        dashboard=login_service.login(
                    settings.admin_email,
                    settings.admin_password
                )
        product=generate_product_data()
        dashboard.is_dashboard_loaded()

        details_page=product_service.create_product(
            product["title"],
            product["usd_price"]
        )
        
        details_page.is_product_details_page_loaded()
        
        