import hashlib
import json

from framework.pages.base_page import BasePage
from framework.pages.dashboardpage import DashboardPage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.email = self.page.get_by_placeholder("Email")
        self.password = self.page.get_by_placeholder("Password")
        self.login_button = self.page.get_by_text(
            "Continue with Email"
        )

    @staticmethod
    def _fingerprint(value: str) -> str:
        """Create a safe fingerprint without exposing the value."""
        return hashlib.sha256(
            value.encode("utf-8")
        ).hexdigest()[:12]

    def enter_email(self, email: str):
        self.logger.info(
            f"Current URL: {self.page.url}"
        )

        self.logger.info(
            f"Page title: {self.page.title()}"
        )

        self.logger.info(
            "Entering email. "
            f"Length={len(email)}, "
            f"Fingerprint={self._fingerprint(email)}"
        )

        self.email.fill(email)

    def enter_password(self, password: str):
        self.logger.info(
            "Entering password. "
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
        # Inspect browser request
        # ----------------------------------------------

        request = response.request
        post_data = request.post_data

        if post_data:

            try:
                payload = json.loads(post_data)

                request_email = payload.get("email")
                request_password = payload.get("password")

                if request_email is not None:
                    self.logger.info(
                        "Browser request email fingerprint: "
                        f"{self._fingerprint(request_email)}"
                    )

                    self.logger.info(
                        "Browser request email length: "
                        f"{len(request_email)}"
                    )

                if request_password is not None:
                    self.logger.info(
                        "Browser request password fingerprint: "
                        f"{self._fingerprint(request_password)}"
                    )

                    self.logger.info(
                        "Browser request password length: "
                        f"{len(request_password)}"
                    )

            except json.JSONDecodeError:
                self.logger.warning(
                    "Unable to parse login request body as JSON."
                )

        # ----------------------------------------------
        # Response body
        # ----------------------------------------------

        response_body = response.text()

        self.logger.info(
            f"Login response body: {response_body}"
        )

        return response, DashboardPage(self.page)