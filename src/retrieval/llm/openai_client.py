import openai
from openai import OpenAI, AsyncOpenAI
from src.config.settings import settings
from src.retrieval.llm.base import LLMClient

class OpenAIClient(LLMClient):
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)

    def generate(self, prompt: str) -> str:
        try:
            completion = self.client.chat.completions.create(
                model=settings.openai_model_name,
                messages=[{"role": "user", "content": prompt}],
            )
            return completion.choices[0].message.content
        except openai.APIError as e:
            raise RuntimeError(f"OpenAI sync API call failed: {e}")


class OpenAIAsyncClient(LLMClient):
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)

    async def generate(self, prompt: str) -> str:
        try:
            completion = await self.client.chat.completions.create(
                model=settings.openai_model_name,
                messages=[{"role": "user", "content": prompt}],
            )
            return completion.choices[0].message.content
        except openai.APIError as e:
            raise RuntimeError(f"OpenAI async API call failed: {e}")