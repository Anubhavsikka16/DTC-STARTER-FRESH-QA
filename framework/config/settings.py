from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # ==================================================
    # Application
    # ==================================================
    base_url: str
    api_base_url: str

    # ==================================================
    # Admin
    # ==================================================
    admin_email: str
    admin_password: str

    # ==================================================
    # Browser
    # ==================================================
    browser: str = "chromium"
    headless: bool = True
    slow_mo: int = 0
    timeout: int = 30000

    # ==================================================
    # Database
    # ==================================================
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "medusa-backend"
    db_user: str = "postgres"
    db_password: str = "postgres"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()


if __name__ == "__main__":
    print("Base URL:", settings.base_url)
    print("API Base URL:", settings.api_base_url)
    print("Admin Email:", settings.admin_email)
    print("Admin Password Configured:", bool(settings.admin_password))