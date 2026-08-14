from framework.pages.base_page import BasePage
from framework.pages.dashboardpage import DashboardPage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.email = self.page.get_by_placeholder("Email")
        self.password = self.page.get_by_placeholder("Password")
        self.login_button = self.page.get_by_text("Continue with Email")

    def enter_email(self, email: str):
        self.logger.info("Entering email")
        self.email.fill(email)

    def enter_password(self, password: str):
        self.logger.info("Entering password")
        self.password.fill(password)

    def click_login_button(self):
        self.logger.info("Clicking Continue with Email")

        with self.page.expect_response(lambda response: "/auth/user/emailpass" in response.url) as response_info:
            self.login_button.click()

        response = response_info.value

        self.logger.info(
            f"Login response status: {response.status}"
        )

        if response.status != 200:
            self.logger.error(
                f"Login failed: {response.text()}"
            )
            raise AssertionError(
                f"Login failed with status {response.status}"
            )

        return DashboardPage(self.page)