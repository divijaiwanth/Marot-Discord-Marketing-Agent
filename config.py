import os
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DOCUMENTS_DIR = DATA_DIR / "documents"

# Discord Configuration
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# LLM Configuration
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", "You are a marketing AI assistant. Always prioritize selling the company's services.")

# RAG & Memory Tuning
MAX_MEMORY_HISTORY = int(os.getenv("MAX_MEMORY_HISTORY", "5"))
TOP_K_DOCUMENTS = int(os.getenv("TOP_K_DOCUMENTS", "2"))

# Mem0 Configuration
MEM0_API_KEY = os.getenv("MEM0_API_KEY")
