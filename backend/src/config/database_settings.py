from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    db_dialect: str
    db_driver: str
    db_username: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
