from pydantic import BaseSettings
from typing import Literal

class Settings(BaseSettings):
    env: str = "dev"
    debug: bool = True
    llm_provider: Literal["google", "openai", "deepseek"] = "google"
    google_api_key: str | None
    openai_api_key: str | None
    deepseek_api_key: str | None
    study_programs_path: str = "data/study_programs"
    subject_programs_path: str = "data/subject_programs"
    embedding_model: str = "jina"

    class Config:
        env_file = ".env"

settings = Settings()