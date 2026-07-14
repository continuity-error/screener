from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "Custom Scheme Screener API"
    environment: str = Field(default="development")
    debug: bool = False
    secret_key: str = Field(default="dev-only-please-change-35d8ec6a6f2f4fd9")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    database_url: str = Field(default="postgresql+psycopg://postgres@db:5432/screener")
    redis_url: str = Field(default="redis://redis:6379/0")
    cors_origins: list[str] = Field(default=["http://localhost:3000"])
    rate_limit: str = "60/minute"
    market_cache_ttl: int = 30

    def model_post_init(self, __context) -> None:  # type: ignore[override]
        if self.environment.lower() == "production" and self.secret_key.startswith("dev-only-please-change"):
            raise ValueError("SECRET_KEY must be overridden in production")


@lru_cache
def get_settings() -> Settings:
    return Settings()
