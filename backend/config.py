from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Fast Try"
    cors: list = [
        'localhost:8000',
        'localhost:3000'
    ]
    debug: bool = True
    db_url: str = ''
    