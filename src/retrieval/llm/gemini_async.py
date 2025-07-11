import google.generativeai as genai
from google.genai.client import AsyncClient
from src.config.settings import settings
from src.retrieval.llm.base import LLMClient

class GeminiAsyncClient(LLMClient):
    def __init__(self):
        self.client = AsyncClient(api_key=settings.google_api_key)

    async def generate(self, prompt: str) -> str:
        chat = await self.client.aio.chats.create(
            model=settings.google_model_name
        )
        response = await chat.send_message(prompt)
        return response.text