# Marot - Discord Marketing Agent

An autonomous, context-aware AI system designed to act as a marketing representative on Discord. Powered by **Mistral (via Ollama)**, it features a dual-layered recall system using **Mem0** for long-term user personalization and a high-speed **RAG architecture** for fetching exact company knowledge.

## Features

- **Dual-Layered Context**: 
  - Keeps *User Knowledge* (their behaviors, preferences) and *Company Knowledge* (pricing, services, FAQs) strictly separated to avoid AI hallucinations.
- **Mem0 Persistent memory**:
  - As users talk, it remembers behavioral signals permanently against their ID without bloating the prompt.
- **Blazing Fast RAG**: 
  - Loads flat `.txt` files directly into RAM at runtime and uses a highly optimized `metadata.json` keyword-mapping layer to bypass expensive chunk indexing.
- **Modular & Clean Architecture**: 
  - The orchestrator seamlessly manages dependencies without massive monolithic blocks. It avoids heavy unneeded frameworks like LangChain in favor of speed and stability.

---

## Architecture Breakdown

| Directory/File | Purpose |
| -------------- | ------- |
| `main.py` | Entrypoint for the application. Evaluates your `.env` constraints securely. |
| `config.py` | Handles all internal configurations mapping to `.env`. |
| `core/orchestrator.py` | The main brain. Fetches user memory, grabs RAG data, and funnels it into the prompt. |
| `interfaces/discord_bot.py` | Asynchronous discord connection loop mapping `handle_message`. |
| `llm/llm_service.py` | Uses Ollama's Async Python API to fetch inference efficiently. |
| `memory/memory_service.py` | Native integration with `Mem0`. Searches and synthesizes bullet-pointed facts automatically. |
| `rag/loader.py` & `retriever.py` | Keyword-optimized static file loaders that index `.txt` data efficiently. |
| `data/documents/` | The root folder for your company's knowledge. (Powered by `metadata.json`). |

---

## 🚀 Setup & Installation

### 1. Prerequisites
You will need Python 3 installed, as well as the [Ollama Engine](https://ollama.com/) running locally.

### 2. Pull the Base Model
Ensure your Mistral model is pulled into your local system:
```bash
ollama serve
ollama pull mistral
```

### 3. Environment Variables
Create a file named `.env` in the root directory (if not already there) and add the following context variables:
```env
# Discord Connection
DISCORD_TOKEN="your-discord-bot-token"

# LLM Profile
OLLAMA_MODEL="mistral"
SYSTEM_PROMPT="You are a marketing AI assistant for DXJ, a premium graphic design company. Your primary goal is to provide helpful answers while strategically steering the conversation toward buying our graphic design services (like Brand Launch or 3D services)."

# Tuning
MAX_MEMORY_HISTORY=5
TOP_K_DOCUMENTS=2

# Mem0 User Data Engine API Key
MEM0_API_KEY="your-mem0-api-key-here"
```

### 4. Install Dependencies
Install all modules via pip:
```bash
pip install -r requirements.txt
```

### 5. Start the Agent
Since the RAG documents are ingested at runtime for peak speeds, whenever you update your `.txt` files you must restart the engine.
```bash
python main.py
```

---

## 🧠 Managing Company Knowledge

Adding more knowledge to your AI is extremely simple and requires no code changes:

1. Create a new `.txt` file inside `data/documents/` (e.g., `refund_policy.txt`).
2. Write raw text explaining the subject.
3. Open `data/documents/metadata.json` and map the file to a few keywords:
   ```json
   {
       "refund_policy.txt": ["refund", "cancel", "money", "break", "leave"]
   }
   ```
4. Restart the bot! The Orchestrator will now recall your rules intelligently.
