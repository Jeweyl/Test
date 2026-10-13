from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    app_name:str = "test_db"
    debug:bool = True
    cors:list[str] = [
        "localhost:8000",
        "localhost:3000"
    ]
    model_config = SettingsConfigDict(env_file=".env")
    username:str = Field(alias="POSTGRES_USER_TEST")
    password:str = Field(alias="POSTGRES_PASSWORD_TEST")
    host:str = Field(alias="POSTGRES_HOST_TEST")
    port:int = Field(alias="POSTGRES_PORT_TEST")
    database:str = Field(alias="POSTGRES_DB_TEST")

settings = Settings()