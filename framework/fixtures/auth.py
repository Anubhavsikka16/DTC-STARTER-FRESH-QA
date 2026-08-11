import os
import pytest

from framework.config.settings import settings
from services.login_service import LoginService


AUTH_STATE = "storage/admin.json"


@pytest.fixture(scope="session")
def authenticated_storage(browser):

    os.makedirs("storage", exist_ok=True)

    context = browser.new_context()
    

    page = context.new_page()
    page.on(
        "response",
        lambda response: print(
            "RESPONSE:",
            response.status,
            response.url
        )
    )
    page.goto(settings.base_url)

    login_service = LoginService(page)

    login_service.login(
        settings.admin_email,
        settings.admin_password
    )
    print("URL AFTER LOGIN:", page.url)

    
    context.storage_state(path=AUTH_STATE)

    context.close()

    return AUTH_STATE


@pytest.fixture(scope="function")
def authenticated_context(browser, authenticated_storage):

    context = browser.new_context(
        storage_state=authenticated_storage
    )

    yield context

    context.close()