from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# The .env file lives at the repository root, shared with docker-compose.
ROOT_ENV_FILE = Path(__file__).resolve().parents[2] / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ROOT_ENV_FILE, extra="ignore")

    database_url: str = "postgresql+psycopg://omnibus:omnibus@localhost:5432/omnibus"
    comicvine_api_key: str = ""


settings = Settings()
