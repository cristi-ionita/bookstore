from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql://bookuser:parola123@localhost:5432/bookstore"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
