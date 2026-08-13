from framework.config.settings import settings
import pytest

class TestAdminLogin:
    @pytest.mark.smoke 
    def test_admin_login(self, login_service):

        print("Admin email:", settings.admin_email)
        print("Admin password configured:", bool(settings.admin_password))

        dashboard=login_service.login(
            settings.admin_email,
            settings.admin_password
        )
        '''
        Run the login workflow and give me the DashboardPage object that represents the page we're now on."
        '''

        dashboard.is_dashboard_loaded()


        
