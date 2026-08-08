from framework.pages.login_page import LoginPage
from framework.utils.logger import get_logger
from framework.pages.dashboardpage import DashboardPage

logger= get_logger(__name__)

class LoginService:

    def __init__(self, page):
        self.login_page=LoginPage(page)

    def login(self, email ,password):
        logger.info("Starting login workflow")

        self.login_page.enter_email(email)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()

        logger.info("Ending login workflow")

        return DashboardPage(self.login_page.page)