# Step 1: Add examples
Example(
    taste="watercolor",
    user_input="a peaceful mountain landscape",
    enhanced_prompt="""You are an expert image prompt engineer. Transform this image concept into a watercolor AI image generation prompt.

**Input**:
- Image Concept: "a peaceful mountain landscape"
- Quality Style: "watercolor"

**Output**:
Serene watercolor painting of distant mountains with soft blue and purple hues, visible brush strokes, wet-on-wet technique creating soft edges, textured paper showing through, loose and expressive style, light washes of color creating depth, subtle details with fine brushwork, gentle gradations of color, ethereal atmosphere, by a contemporary watercolor artist"""
)

# Step 2: Update prompt generation logic
if taste == "watercolor":
    style_instructions = """
    For "watercolor" style, make sure to include these key elements:
    - "visible brush strokes"
    - "wet-on-wet technique"
    - "textured paper showing through"
    - "loose and expressive style"
    - "light washes of color"
    - "ethereal atmosphere"
    """

# Step 3: Add term verification
def has_watercolor_terms(self, prompt: str) -> bool:
    """
    Check if a prompt contains watercolor style terms

    Args:
        prompt: The prompt to check

    Returns:
        True if watercolor terms are found, False otherwise
    """
    watercolor_terms = [
        'watercolor', 'brush strokes', 'wet-on-wet', 'textured paper',
        'loose style', 'light washes', 'ethereal', 'watercolor painting',
        'watercolor artist', 'watercolor technique', 'watercolor style'
    ]
    return any(term in prompt.lower() for term in watercolor_terms)

# Step 4: Update fallback method
if taste == "watercolor":
    return f"""Watercolor painting of {user_input}, visible brush strokes, wet-on-wet technique, textured paper showing through, loose and expressive style, light washes of color, ethereal atmosphere."""

# Step 5: Add to test cases
test_cases = [
    # ... existing test cases ...
    ("watercolor", "a peaceful mountain landscape")
]
