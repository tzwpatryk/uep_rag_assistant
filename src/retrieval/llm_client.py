from config.settings import settings

if settings.llm_provider == "google":
    pass  # call Gemini client
elif settings.llm_provider == "openai":
    pass  # call OpenAI client
elif settings.llm_provider == "deepseek":
    pass  # call Deepseek client

