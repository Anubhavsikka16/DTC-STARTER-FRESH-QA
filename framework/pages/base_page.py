from playwright.sync_api import Page
from framework.utils.logger import get_logger


class BasePage:

    def __init__(self, page: Page):#"The page argument is expected to be a Playwright Page object."
        self.page = page
        self.logger = get_logger(self.__class__.__name__)