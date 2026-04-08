from typing import Dict, Any
from config import TOP_K_DOCUMENTS
from llm.llm_service import generate_response
from memory.memory_service import get_user_memory, store_interaction
from rag.loader import load_documents
from rag.retriever import retrieve_relevant_docs
from prompts.prompt_builder import build_prompt

# Load documents at startup
_company_documents: Dict[str, Dict[str, Any]] = load_documents()

async def handle_message(user_id: str, message: str) -> str:
    """
    Orchestrator function taking all pieces together.
    Returns the string text to send back to the user.
    """
    # 1. Retrieve memory
    memory = get_user_memory(user_id)
    
    # 2. Retrieve knowledge
    knowledge = retrieve_relevant_docs(message, _company_documents, top_k=TOP_K_DOCUMENTS)
    
    # 3. Build prompt
    prompt = build_prompt(knowledge, memory, message)
    
    # 4. Call LLM
    response = await generate_response(prompt)
    
    # 5. Store interaction
    store_interaction(user_id, message, response)
    
    # 6. Return response
    return response
