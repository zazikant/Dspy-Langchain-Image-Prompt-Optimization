import re
from datetime import datetime
from typing import Optional

def validate_taste(taste: str) -> str:
    """Validate the artistic taste category."""
    valid_tastes = ['photorealistic', 'oil painting', 'anime', 'cyberpunk', 'watercolor', '3d render']
    if taste.lower() not in valid_tastes:
        raise ValueError(f"Invalid taste. Choose from: {', '.join(valid_tastes)}")
    return taste.lower()

def validate_input(user_input: str) -> str:
    """Validate the user input description."""
    if not user_input or len(user_input.strip()) < 3:
        raise ValueError("Please provide a description (at least 3 characters)")
    return user_input.strip()

def sanitize_input(text: str) -> str:
    """Sanitize user input to remove potentially harmful characters."""
    # Remove potentially harmful characters
    text = re.sub(r'[^\w\s,.\-!?]', '', text)
    # Limit length
    return text[:500]

def generate_timestamp() -> str:
    """Generate a timestamp string for current datetime."""
    return datetime.now().isoformat()

def prompt_quality_score(prompt: str) -> float:
    """Calculate a quality score for the prompt (0-1 scale)."""
    quality_indicators = [
        'detailed' in prompt.lower(),
        'style' in prompt.lower(),
        len(prompt.split()) > 10,  # Sufficient detail
        any(tech_word in prompt.lower() 
            for tech_word in ['lighting', 'focus', 'texture', 'composition', 'resolution']),
        'high' in prompt.lower() or 'quality' in prompt.lower(),
        'color' in prompt.lower() or 'palette' in prompt.lower()
    ]
    return sum(quality_indicators) / len(quality_indicators)
