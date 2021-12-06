from pydantic import BaseSettings
import urllib.parse


class Settings(BaseSettings):
    server_host: str = '0.0.0.0'
    server_port: int = 8000
    database_url: str = ""
    database_url_dev = ""


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
