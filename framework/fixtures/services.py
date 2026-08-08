import pytest

from services.login_service import LoginService


@pytest.fixture
def login_service(page):
    return LoginService(page)