import pytest
from framework.config.settings import settings
class TestCreateProductE2E:

    @pytest.mark.smoke
    def test_product_creation(self,login_service,product_service):
        dashboard=login_service.login(
                    settings.admin_email,
                    settings.admin_password
                )
        
        dashboard.is_dashboard_loaded()

        details_page=product_service.create_product("Bomber Jacket", 60)
        
        details_page.is_product_details_page_loaded()
        
        