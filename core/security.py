import re
from typing import Tuple
from config import MAX_INPUT_LENGTH

# Basic heuristic keywords for prompt injection detection
INJECTION_KEYWORDS = [
    "ignore previous",
    "ignore all previous",
    "system prompt",
    "forget all",
    "instructions",
    "you are now",
    "bypassing",
    "developer mode",
    "jailbreak"
]

def sanitize_input(text: str) -> str:
    """
    Sanitizes user input by removing extra whitespaces, zero-width characters,
    and enforcing a maximum length.
    """
    if not text:
        return ""
        
    # Remove control characters and zero-width spaces
    text = re.sub(r'[\x00-\x1F\x7F-\x9F\u200B-\u200D\uFEFF]', '', text)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Cap length (using configured maximum)
    if len(text) > MAX_INPUT_LENGTH:
        text = text[:MAX_INPUT_LENGTH] + "..."
        
    return text

def contains_prompt_injection(text: str) -> bool:
    """
    Checks if the user input contains common prompt injection phrases.
    """
    text_lower = text.lower()
    for keyword in INJECTION_KEYWORDS:
        if keyword in text_lower:
            return True
    return False

def validate_and_sanitize(message: str) -> Tuple[bool, str]:
    """
    Wrapper that sanitizes and checks for injection.
    Returns (is_passed, processed_message).
    """
    cleaned = sanitize_input(message)
    if contains_prompt_injection(cleaned):
        return False, "I cannot fulfill that request as it appears to violate my security protocols."
    return True, cleaned
