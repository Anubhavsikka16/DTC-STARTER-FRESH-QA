from framework.pages.login_page import LoginPage


class LoginService:

    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)

    def login(self, email: str, password: str):

        self.logger.info(
            "Starting login workflow"
        )

        self.login_page.enter_email(email)

        self.login_page.enter_password(password)

        response, dashboard_page = (
            self.login_page.click_login_button()
        )

        assert response.status == 200, (
            f"Login failed. "
            f"Status={response.status}, "
            f"Response={response.text()}"
        )

        return dashboard_page