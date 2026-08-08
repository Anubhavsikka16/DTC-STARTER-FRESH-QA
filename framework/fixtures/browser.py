import pytest
from playwright.sync_api import sync_playwright
from framework.utils.logger import get_logger
from framework.config.settings import settings
logger = get_logger(__name__)


@pytest.fixture(scope="session")
def playwright_instance():
    logger.info("Starting Playwright instance....")
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    
    logger.info("Launching browser....")
    browser=playwright_instance.chromium.launch(headless=settings.headless, slow_mo=settings.slow_mo)
    yield browser
    logger.info("Closing browser....")
    browser.close()




@pytest.fixture(scope="function")
def browser_context(browser):
    logger.info("Creating new browser context....")
    context = browser.new_context()
    yield context
    logger.info("Closing browser context....")
    context.close()


@pytest.fixture(scope="function")
def page(browser_context):
    logger.info("Launching new page....")
    page=browser_context.new_page()
    page.goto(settings.base_url)

    yield page
    logger.info("Closing page....")
    page.close()