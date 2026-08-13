from framework.pages.login_page import LoginPage
from framework.utils.logger import get_logger
from framework.pages.dashboardpage import DashboardPage

logger= get_logger(__name__)

class LoginService:

    def __init__(self, page):
        self.login_page=LoginPage(page) # uses page objects and login_page will access page objects methods

    def login(self, email ,password):
        logger.info("Starting login workflow")

        self.login_page.enter_email(email)
        self.login_page.enter_password(password)
        #self.login_page.click_login_button()

        dashboard_page = self.login_page.click_login_button()

        dashboard_page.is_dashboard_loaded()

        logger.info("Login successful")

        return dashboard_page # this returned object goes into dashboard
    '''         dashboard=login_service.login(
                    settings.admin_email,
                    settings.admin_password
            )'''