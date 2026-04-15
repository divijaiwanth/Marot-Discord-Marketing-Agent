def build_prompt(knowledge: str, memory_str: str, message: str) -> str:
    """
    Builds the structured text prompt that contextually situates the user's query.
    """
    
    prompt = f"""
<company_knowledge>
{knowledge}
</company_knowledge>

<user_memory>
{memory_str}
</user_memory>

<user_message>
{message}
</user_message>
"""
    return prompt.strip()
