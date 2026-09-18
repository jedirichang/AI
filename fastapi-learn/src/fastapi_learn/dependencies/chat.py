from fastapi import Depends
from fastapi_learn.clients.openai_client import OpenaiClient
from fastapi_learn.clients.ollama_client import OllamaClient

from fastapi_learn.core.config import Settings, settings
from fastapi_learn.clients.ollama_client import OllamaClient
from fastapi_learn.services.chat_service import ChatService
from fastapi_learn.clients.protocol import LLMClientProtocol

def get_settings()->Settings:
    return settings

def get_llm_client(config:Settings = Depends(get_settings))-> LLMClientProtocol:
    if config.llmm_provider == "openai":
        return OpenaiClient(config)
    elif config.llmm_provider == "ollama":
        return OllamaClient(config)
    else:
        raise ValueError(f"Unsupported LLM provider: {config.llmm_provider}")

def get_chat_service(
    client:LLMClientProtocol=Depends(get_llm_client)
)-> ChatService:
    return ChatService(client)