from pydantic_settings import BaseSettings

import os




class Settings(BaseSettings):
    app_name: str = "Fast Try"
    cors: list = [
        'localhost:8000',
        'localhost:3000'
    ]
    debug: bool = True
    username: str = os.getenv(POSTGRES_USER)
    password: str = os.getenv(POSTGRES_PASS)
    host: str = os.getenv(POSTGRES_HOST)
    port: int = os.getenv(POSTGRES_PORT)
    database: str = os.getenv(POSTGRES_DB)
    
    
settings = Settings()