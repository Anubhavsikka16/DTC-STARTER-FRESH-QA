from framework.config.settings import settings
from framework.pages.dashboardpage import DashboardPage

from framework.pages.base_page import BasePage
class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.email= self.page.get_by_placeholder("Email")
        self.password=self.page.get_by_placeholder("Password")
        self.login_button=self.page.get_by_text("Continue with Email")

    def enter_email(self, email):
        self.logger.info(f"entering email address: {email}")
        self.email.fill(email)

    def enter_password(self, password):
        self.logger.info(f"entering password")
        self.password.fill(password)

    def click_login_button(self):
        self.logger.info(f"clicking continue with email button")
        with self.page.expect_response(
            lambda response: "/auth/" in response.url
        ) as response_info:
            self.login_button.click()
            response = response_info.value

            assert response.status == 200

        return DashboardPage(self.page)