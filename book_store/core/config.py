from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(
    BaseSettings
):  # TODO: lets use dynaconfig instead of pydantic_settings since Pydantic is a tool for validation at first place,
    # not for configuration management
    # FIXME: this connection string looks different from the one in docker-compose.yaml, why?
    database_url: str = "postgresql://bookuser:parola123@localhost:5432/bookstore"
    model_config = SettingsConfigDict(env_file=".env")


# TODO: Create settings for test environment
# TODO: Create settings for production environment
# TODO: lets say we will use yaml files for storing settings

settings = Settings()
