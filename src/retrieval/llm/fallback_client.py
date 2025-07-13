from src.retrieval.llm.base import LLMClient
import logging
import time

class FallbackLLMClient(LLMClient):
    def __init__(self, clients: list[LLMClient], max_retries: int = 2, retry_delay: float = 0.5):
        self.clients = clients
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.logger = logging.getLogger(__name__)

    def generate(self, prompt: str) -> str:
        for idx, client in enumerate(self.clients):
            for attempt in range(1, self.max_retries + 1):
                try:
                    return client.generate(prompt)
                except Exception as e:
                    self.logger.warning(f"[{client.__class__.__name__}] Attempt {attempt}/{self.max_retries} failed: {e}")
                    time.sleep(self.retry_delay)

            self.logger.warning(f"[{client.__class__.__name__}] All retries exhausted. Trying next client...")

        raise RuntimeError("All fallback LLM clients failed to generate a response.")
        
class AsyncFallbackLLMClient(LLMClient):
    def __init__(self, clients: list[LLMClient]):
        self.clients = clients

    async def generate(self, prompt: str) -> str:
        for client in self.clients:
            try:
                return await client.generate(prompt)
            except Exception as e:
                print(f"[Fallback] {client.__class__.__name__} failed: {e}")
        raise RuntimeError("All async LLM clients failed.")