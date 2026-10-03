from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    app_name: str = "Fast Try"
    cors: list = [
        'localhost:8000',
        'localhost:3000'
    ]
    debug: bool = True
    model_config = SettingsConfigDict(env_file=".env")
    username: str = Field(alias="POSTGRES_USER")
    password: str = Field(alias="POSTGRES_PASS")
    host: str = Field(alias="POSTGRES_HOST")
    port: int = Field(alias="POSTGRES_PORT")
    database: str = Field(alias="POSTGRES_DB")
    
    
settings = Settings()