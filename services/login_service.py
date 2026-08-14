from loguru import logger

from framework.pages.login_page import LoginPage


class LoginService:

    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)
        self.logger = logger

    def login(self, email: str, password: str):

        # Remove accidental whitespace/newlines from CI secrets
        email = email.strip()
        password = password.strip()

        self.logger.info("Starting login workflow")

        self.login_page.enter_email(email)

        self.login_page.enter_password(password)

        response, dashboard_page = (
            self.login_page.click_login_button()
        )

        self.logger.info(
            f"Authentication response status: "
            f"{response.status}"
        )

        if response.status != 200:

            self.logger.error(
                f"Login failed with status "
                f"{response.status}"
            )

            self.logger.error(
                f"Login response: {response.text()}"
            )

            raise AssertionError(
                f"Login failed. "
                f"Expected 200, "
                f"got {response.status}. "
                f"Response: {response.text()}"
            )

        self.logger.info(
            "Login successful"
        )

        return dashboard_page