from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name = "Fast Try"
    cors = [
        'localhost:8000',
        'localhost:3000'
    ]
    debug = True
    db_url = ''
    