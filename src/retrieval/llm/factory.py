# src/retrieval/llm/factory.py
from src.config.settings import settings
from src.retrieval.llm.base import LLMClient
from src.retrieval.llm.gemini import GeminiClient
from src.retrieval.llm.gemini_async import GeminiAsyncClient

def get_llm_client(async_mode: bool = True) -> LLMClient:
    if settings.llm_provider == "google":
        return GeminiAsyncClient() if async_mode else GeminiClient()
    ...