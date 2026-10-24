import os
from openai import OpenAI
from dotenv import load_dotenv
from .config import PROVIDERS
from .models import Provider

load_dotenv()

def select_provider() -> Provider:
    for provider in PROVIDERS:
        if os.getenv(provider.env_var):
            return provider
    
    expected = ", ".join(p.env_var for p in PROVIDERS)
    return f"No Provider key set. Add one of {expected} to your environment variables"


def build_client(provider: Provider):
    api_key = os.getenv(provider.env_var)
    base_url = os.getenv(provider.base_url)
    return OpenAI(
        api_key = api_key,
        base_url = base_url
    )
