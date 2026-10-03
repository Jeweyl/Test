from pydantic_settings import BaseSettings
from database import db_url

class Settings(BaseSettings):
    app_name: str = "Fast Try"
    cors: list = [
        'localhost:8000',
        'localhost:3000'
    ]
    debug: bool = True
    db_url: str = db_url
    