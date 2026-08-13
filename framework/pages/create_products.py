from framework.pages.base_page import BasePage
from framework.pages.product_details import ProductDetailsPage

class CreateProductPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.title=self.page.locator("input[placeholder='Winter jacket']").nth(1)
        self.continue_button=self.page.locator("div[role='dialog']>form>div>div:nth-child(1)>button:nth-child(3)").nth(1)
        
        self.save_button=self.page.locator("button[data-name='publish-button']")

    def enter_title(self, title):
        

        self.logger.info(f"Entering title: {title}")

        self.title.fill(title)
        
    def continue_to_organization(self):
        self.continue_button.click()

    def continue_to_pricing(self):
        self.continue_button.click()
        

    def save(self):
        self.logger.info("Publishing product")

        self.save_button.click()

        return ProductDetailsPage(self.page)


