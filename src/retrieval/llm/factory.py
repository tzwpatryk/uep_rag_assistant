from src.config.settings import settings
from src.retrieval.llm.gemini_client import GeminiClient, GeminiAsyncClient
from src.retrieval.llm.openai_client import OpenAIClient, OpenAIAsyncClient
#from src.retrieval.llm.deepseek_client import DeepseekClient
from src.retrieval.llm.fallback_client import FallbackLLMClient, AsyncFallbackLLMClient

CLIENT_MAP = {
    "google": {
        "sync": GeminiClient,
        "async": GeminiAsyncClient
    },
    "openai": {
        "sync": OpenAIClient,
        "async": OpenAIAsyncClient
    }#,
#    "deepseek": {
#        "sync": DeepseekClient,
#        "async": DeepseekAsyncClient
#    },
}

def get_llm_client(async_mode: bool = False):
    clients = []

    mode = "async" if async_mode else "sync"

    for provider in settings.llm_fallback_order:
        client_group = CLIENT_MAP.get(provider)
        if not client_group:
            continue

        client_cls = client_group.get(mode)
        api_key = getattr(settings, f"{provider}_api_key", None)

        if client_cls and api_key:
            clients.append(client_cls())

    if not clients:
        raise ValueError("No LLM clients available with configured API keys.")

    if async_mode:
        return AsyncFallbackLLMClient(clients=clients)
    return FallbackLLMClient(clients=clients)