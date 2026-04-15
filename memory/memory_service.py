from mem0 import MemoryClient
from config import MEM0_API_KEY
import logging

# Initialize Mem0 Client safely
_client = MemoryClient(api_key=MEM0_API_KEY)

def get_user_memory(user_id: str) -> str:
    """
    Retrieves the synthesized facts/memories from Mem0 for the given user_id.
    Uses the exact search and format-parsing structure provided by the user.
    """
    if not _client:
        return "Internal Error: Memory service disabled (Check API Key)."
        
    try:
        # We use a broad sweeping query suited for graphic design and preferences
        res = _client.search(
            query="like prefer want need buy graphic design",
            filters={"user_id": str(user_id)},
            limit=50
        )
        
        # Handle Mem0 response properly based on snippet
        if isinstance(res, dict):
            if "results" in res:
                parsed_results = res["results"]
            else:
                parsed_results = [res]
        elif isinstance(res, list):
            parsed_results = res
        else:
            parsed_results = []
            
        if not parsed_results:
            return "No previous memory or behavior facts retrieved."
            
        memory_str = ""
        for mem in parsed_results:
            # Memory dictionaries returned from Mem0 often have the fact in the 'memory' key
            fact = mem.get("memory", str(mem))
            memory_str += f"- {fact}\n"
            
        return memory_str.strip()

    except Exception as e:
        logging.error(f"Error fetching from Mem0: {e}")
        return "Internal Error: Could not retrieve memory context."

def store_interaction(user_id: str, message: str, response: str) -> None:
    """
    Passes the conversation turn into Mem0 based on the provided snippet.
    """
    if not _client:
        return
        
    try:
        # We mimic the provided snippet exactly, passing the user message. 
        # (We also include the assistant response so Mem0 understands the context)
        payload = [
            {"role": "user", "content": message},
            {"role": "assistant", "content": response}
        ]
        
        _client.add(
            payload,
            user_id=str(user_id)
        )
    except Exception as e:
        logging.error(f"Error storing interaction in Mem0: {e}")
