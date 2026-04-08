import ollama
from config import OLLAMA_MODEL, SYSTEM_PROMPT

async def generate_response(prompt: str) -> str:
    """
    Calls the Ollama Mistral model asynchronously.
    """
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]
    
    # We use a synchronous ollama.chat as fallback if async is not strictly needed or Ollama Python client changes.
    # Note: ollama-python does have AsyncClient, we will use it for better discord compatibility.
    client = ollama.AsyncClient()
    try:
        response = await client.chat(
            model=OLLAMA_MODEL,
            messages=messages
        )
        return response['message']['content']
    except Exception as e:
        print(f"Error calling LLM: {e}")
        return "I apologize, but my core processors are currently unreachable."
