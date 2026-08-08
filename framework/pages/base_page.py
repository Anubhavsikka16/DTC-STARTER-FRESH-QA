from playwright.sync_api import Page
from framework.utils.logger import get_logger


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)