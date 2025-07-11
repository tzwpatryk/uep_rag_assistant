import google.generativeai as genai
from google.genai.client import Client
from src.config.settings import settings
from src.retrieval.llm.base import LLMClient

class GeminiClient(LLMClient):
    def __init__(self):
        self.client = Client(api_key=settings.google_api_key)

    def generate(self, prompt: str) -> str:
        chat = self.client.chats.create(
            model=settings.google_model_name
        )
        response = chat.send_message(prompt)
        return response.text