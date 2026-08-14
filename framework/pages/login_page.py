
import json

from framework.pages.base_page import BasePage
from framework.pages.dashboardpage import DashboardPage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.email = self.page.get_by_placeholder("Email")
        self.password = self.page.get_by_placeholder("Password")
        self.login_button = self.page.get_by_text("Continue with Email")

    @staticmethod
    def _fingerprint(value: str) -> str:
        

    def enter_email(self, email: str):
        self.logger.info(
            f"Current URL: {self.page.url}"
        )

        self.logger.info(
            f"Page title: {self.page.title()}"
        )

        self.logger.info(
            f"Entering email. "
            f"Length={len(email)}, "
            f"Fingerprint={self._fingerprint(email)}"
        )

        self.email.fill(email)

    def enter_password(self, password: str):
        self.logger.info(
            f"Entering password. "
            f"Length={len(password)}, "
            f"Fingerprint={self._fingerprint(password)}"
        )

        self.password.fill(password)

    def click_login_button(self):

        self.logger.info(
            "Clicking Continue with Email button"
        )

        with self.page.expect_response(
            lambda response:
            "/auth/user/emailpass" in response.url
        ) as response_info:

            self.login_button.click()

        response = response_info.value

        self.logger.info(
            f"Login response URL: {response.url}"
        )

        self.logger.info(
            f"Login response status: {response.status}"
        )

        # ----------------------------------------------
        # Inspect the actual browser request
        # ----------------------------------------------
        request = response.request

        post_data = request.post_data

        if post_data:

            try:
                payload = json.loads(post_data)

                email = payload.get("email")
                password = payload.get("password")

                if email is not None:

                    self.logger.info(
                        "Browser request email fingerprint: "
                        f"{self._fingerprint(email)}"
                    )

                    self.logger.info(
                        "Browser request email length: "
                        f"{len(email)}"
                    )

                if password is not None:

                    self.logger.info(
                        "Browser request password fingerprint: "
                        f"{self._fingerprint(password)}"
                    )

                    self.logger.info(
                        "Browser request password length: "
                        f"{len(password)}"
                    )

            except json.JSONDecodeError:

                self.logger.warning(
                    "Unable to parse login request body as JSON."
                )

        # ----------------------------------------------
        # Log response body
        # ----------------------------------------------
        response_body = response.text()

        self.logger.info(
            f"Login response body: {response_body}"
        )

        # ----------------------------------------------
        # Return response to service layer
        # ----------------------------------------------
        return response, DashboardPage(self.page)