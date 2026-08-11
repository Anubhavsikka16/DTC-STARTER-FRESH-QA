from framework.pages.create_products import CreateProductPage
from framework.pages.products_page import ProductsPage
from framework.utils.logger import get_logger


class ProductService:

    def __init__(self, page):
        self.logger = get_logger(self.__class__.__name__)

        self.products_page = ProductsPage(page)

    def create_product(self, title, usd_price):

        self.logger.info("Starting Create Product workflow")

        create_page = self.products_page.click_create_product_button()

        create_page.enter_title(title)

        create_page.continue_to_organization()

        create_page.continue_to_pricing()


        details_page = create_page.save()
        #create_page.save returns ProductsDetailsPage(self.page)
        self.logger.info("Product created successfully")

        return details_page


