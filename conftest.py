pytest_plugins = [
    "framework.fixtures.browser", # it like framework folder -> fixture_folder -> file_name
    # we don't use / because conceptually it's like import
    "framework.fixtures.services",
    "framework.fixtures.auth",
    "framework.fixtures.database",
    "framework.fixtures.api",
]