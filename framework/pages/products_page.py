
from framework.pages.create_products import CreateProductPage
from framework.pages.base_page import BasePage

class ProductsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.click_products_link=self.page.locator("div[data-state='closed']>a[href='/app/products']>p").first
        self.create_button=self.page.get_by_role('link', name='Create')

    def go_to_create_product(self):
        self.logger.info("Clicking Products link on left side panel")
        self.click_products_link.click()    
        self.logger.info("Clicking Create Product button")
        self.create_button.click()

        return CreateProductPage(self.page) # it's a surety that will go to Create Product page

    