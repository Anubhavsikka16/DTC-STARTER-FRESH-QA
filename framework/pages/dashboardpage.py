from playwright.sync_api import expect

from framework.utils.logger import get_logger

logger= get_logger(__name__)
class DashboardPage:

    def __init__(self, page):
            self.page=page

    def is_dashboard_loaded(self):
        logger.info("Verifying dashboard loaded")

        expect(self.page).to_have_url("http://localhost:9000/app/orders")
        print(f"Title of the page is: {self.page.title()}")