from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    base_url: str
    api_base_url: str

    # Admin
    admin_email: str
    admin_password: str

    # Browser
    browser: str
    headless: bool
    slow_mo: int
    timeout: int

    # Database
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False
    )


settings = Settings() #settings.base_url: easy access instead of adding Settings() every time

if __name__ == "__main__":
    print(settings)