from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    app_name: str = "Fast Try"
    cors: list = [
        'localhost:8000',
        'localhost:3000',
    ]
    debug: bool = True
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    username: str = Field(validation_alias="POSTGRES_USER")
    password: str = Field(validation_alias="POSTGRES_PASSWORD")
    host: str = Field(validation_alias="POSTGRES_HOST")
    port: int = Field(validation_alias="POSTGRES_PORT")
    database: str = Field(validation_alias="POSTGRES_DB")
    redis_url: str = Field(validate_default="REDIS_URL")
    
settings = Settings()