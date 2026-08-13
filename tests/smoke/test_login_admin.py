import hashlib

import pytest

from framework.config.settings import settings


def fingerprint(value):
    return hashlib.sha256(
        value.encode("utf-8")
    ).hexdigest()[:12]


@pytest.mark.smoke
def test_admin_login(login_service):

    print(
        "Test email fingerprint:",
        fingerprint(settings.admin_email)
    )

    print(
        "Test password fingerprint:",
        fingerprint(settings.admin_password)
    )

    print(
        "Admin password configured:",
        bool(settings.admin_password)
    )

    dashboard = login_service.login(
        settings.admin_email,
        settings.admin_password
    )

    dashboard.is_dashboard_loaded