from services.login_service import LoginService
from framework.config.settings import settings
import pytest

class TestAdminLogin:
    @pytest.mark.smoke 
    def test_admin_login(self, login_service):

        dashboard=login_service.login(
            settings.admin_email,
            settings.admin_password
        )

        dashboard.is_dashboard_loaded()


        
