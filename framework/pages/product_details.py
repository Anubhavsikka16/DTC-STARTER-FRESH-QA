
from framework.pages.base_page import BasePage
from playwright.sync_api import expect
import re
import time
class ProductDetailsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def is_product_details_page_loaded(self):
        self.logger.info("Verifying Product Details page")

        expect(self.page).to_have_url(re.compile(r".*/products/prod_.*"))
        time.sleep(5)
        expect(self.page.get_by_role("heading")).to_be_visible

