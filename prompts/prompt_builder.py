def build_prompt(knowledge: str, memory_str: str, message: str) -> str:
    """
    Builds the structured text prompt that contextually situates the user's query.
    """
    
    prompt = f"""
--- COMPANY KNOWLEDGE ---
{knowledge}

--- USER MEMORY ---
{memory_str}

--- USER MESSAGE ---
{message}
"""
    return prompt.strip()
