from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    REDIS_HOST: str

    BOT_API_TOKEN: str

    IS_DEVELOPMENT: bool = False
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings() -> Settings:
    return Settings()  

settings = get_settings()
