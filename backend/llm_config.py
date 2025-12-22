"""
LLM Configuration for Ollama Integration
Provides centralized configuration for all CrewAI agents using Ollama
"""

import os
from typing import Optional

# Set environment to prevent OpenAI requirement
os.environ["OPENAI_API_KEY"] = "not-needed"

try:
    from langchain_ollama import OllamaLLM
except ImportError:
    from langchain_community.llms import Ollama as OllamaLLM


class OllamaConfig:
    """Centralized Ollama configuration for all agents"""
    
    def __init__(
        self,
        model: str = "llama3",
        base_url: str = "http://localhost:11434",
        temperature: float = 0.2,
        timeout: int = 120
    ):
        self.model = model
        self.base_url = base_url
        self.temperature = temperature
        self.timeout = timeout
    
    def get_llm(self) -> OllamaLLM:
        """Get configured Ollama LLM instance"""
        return OllamaLLM(
            model=self.model,
            base_url=self.base_url,
            temperature=self.temperature,
            timeout=self.timeout
        )


# Global configuration instance
ollama_config = OllamaConfig()


def get_llm():
    """Get the configured LLM instance for agents"""
    try:
        # Try to use real Ollama first
        llm = ollama_config.get_llm()
        # Test if Ollama is accessible
        llm.invoke("Hello")
        return llm
    except Exception as e:
        print(f"Ollama not available ({e}), using mock LLM for demo")
        from mock_llm import get_mock_llm
        return get_mock_llm()


def set_model(model_name: str) -> None:
    """Change the model being used"""
    ollama_config.model = model_name


def health_check() -> dict:
    """Check if Ollama is accessible"""
    try:
        # Try real Ollama first
        real_llm = ollama_config.get_llm()
        response = real_llm.invoke("Hello")
        return {
            "status": "healthy",
            "model": ollama_config.model,
            "base_url": ollama_config.base_url,
            "response_length": len(response),
            "llm_type": "ollama"
        }
    except Exception as e:
        # Fall back to mock LLM
        try:
            from mock_llm import get_mock_llm
            mock_llm = get_mock_llm()
            response = mock_llm.invoke("Hello")
            return {
                "status": "healthy",
                "model": "mock-llama3",
                "base_url": "mock://localhost",
                "response_length": len(response),
                "llm_type": "mock",
                "note": "Using mock LLM for demo - Ollama not available"
            }
        except Exception as mock_e:
            return {
                "status": "unhealthy",
                "model": ollama_config.model,
                "base_url": ollama_config.base_url,
                "error": str(e),
                "mock_error": str(mock_e)
            }