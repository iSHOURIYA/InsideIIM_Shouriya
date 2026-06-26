from functools import lru_cache
from os import getenv


class Settings:
    def __init__(self) -> None:
        self.app_name = getenv("APP_NAME", "InsideIIM API")
        self.app_version = getenv("APP_VERSION", "0.1.0")
        self.environment = getenv("ENVIRONMENT", "development")
        self.debug = getenv("DEBUG", "true").lower() == "true"
        self.api_v1_prefix = getenv("API_V1_PREFIX", "/api/v1")
        self.database_url = getenv("DATABASE_URL", "postgresql+psycopg://user:password@localhost:5432/insideiim")
        raw_origins = getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:5173")
        self.cors_origins = [origin.strip() for origin in raw_origins.split(",") if origin.strip()]
        self.log_level = getenv("LOG_LEVEL", "INFO")
        self.secret_key = getenv("SECRET_KEY", "change-me")


@lru_cache
def get_settings() -> Settings:
    return Settings()
