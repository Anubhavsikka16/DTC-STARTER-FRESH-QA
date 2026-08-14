from framework.utils.logger import get_logger
from framework.pages.login_page import LoginPage


class LoginService:

    def __init__(self, page):

        self.page = page
        self.login_page = LoginPage(page)
        self.logger = get_logger(__name__)

    def login(self, email: str, password: str):

        self.logger.info(
            "Starting login workflow"
        )

        # Remove accidental whitespace/newlines
        # from CI environment variables.
        email = email.strip()
        password = password.strip()

        self.login_page.enter_email(
            email
        )

        self.login_page.enter_password(
            password
        )

        response, dashboard_page = (
            self.login_page.click_login_button()
        )

        self.logger.info(
            f"Authentication response status: "
            f"{response.status}"
        )

        # ==================================================
        # Validate authentication
        # ==================================================

        if response.status != 200:

            self.logger.error(
                f"Login failed with status "
                f"{response.status}"
            )

            self.logger.error(
                f"Login response: "
                f"{response.text()}"
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