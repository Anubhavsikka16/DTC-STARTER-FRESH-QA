from services.login_service import LoginService
from framework.config.settings import settings
import time
class TestAdminLogin:

    def test_admin_login(login_service):

        dashboard=login_service.login(
            settings.admin_email,
            settings.admin_password
        )

        dashboard.is_dashboard_loaded()
        time.sleep(2)