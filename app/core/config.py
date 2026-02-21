import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ASSEMBLYAI_API_KEY: str = os.getenv("ASSEMBLYAI_API_KEY", "")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    # Add your new local API key here:
    MY_BACKEND_API_KEY: str = os.getenv("MY_BACKEND_API_KEY", "default-insecure-key")
    
    PROJECT_NAME: str = "Conversation Intelligence API"
    VERSION: str = "1.0.0"

settings = Settings()