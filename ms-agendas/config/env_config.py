from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

class Settings(BaseSettings):
    db_url: str


    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")


settings = Settings() # type: ignore