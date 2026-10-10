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
    
    jwt_secret_key: str = Field(validation_alias="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(
        default="HS256",
        validation_alias="JWT_ALGORITHM",
    )
    access_token_expire_minutes: int = Field(
        default=30,
        validation_alias="ACCESS_TOKEN_EXPIRE_MINUTES",
    )
    
settings = Settings()