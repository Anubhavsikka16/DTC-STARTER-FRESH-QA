

import pytest

from framework.config.settings import settings



@pytest.mark.smoke
def test_admin_login(login_service):

    dashboard = login_service.login(
        settings.admin_email,
        settings.admin_password
    )

    dashboard.is_dashboard_loaded