from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Literal

class Settings(BaseSettings):
    env: str = "dev"
    debug: bool = True
    llm_provider: Literal["google", "openai", "deepseek"] = "google"
    llm_fallback_order: list[Literal["google", "openai", "deepseek"]] = Field(
        default_factory=lambda: ["google", "openai", "deepseek"]
    )
    google_api_key: str | None
    google_model_name: str = Field(default="gemini-2.5-flash-lite-preview-06-17")
    openai_api_key: str | None
    openai_model_name: str | None = Field(default="gpt-4o-mini")
    deepseek_api_key: str | None
    deepseek_model_name: str | None = None
    study_programs_path: str = "data/study_programs"
    subject_programs_path: str = "data/subject_programs"
    embedding_model: str = "jina"

    class Config:
        env_file = ".env"

settings = Settings()
