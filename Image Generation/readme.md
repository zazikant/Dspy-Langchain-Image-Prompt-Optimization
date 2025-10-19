outpainting query input: refer to image and zoom out to outpaint maintaining character consistency

### outpainting prompt (this is for illustration style alice lee.. similarly make one for photorealistic or any) : '\n**Enhanced Image Prompt:**  \nFlat illustration of the original scene extended by zooming out and outpainting the background while maintaining character consistency, by Alice Lee style, Wax crayon brushes procreate style, hand drawn, a poster by Tom Whalen, featured on behance, context art, behance hd, art on instagram, storybook illustration, Pro freelance, Illustration agency, Popular on Dribbble, soft shadows, no contrast, clean ultrasharp focus, premium vector, hand drawn people, timeless art, human illustration, freepik, flat colours, their faces are visible, show less details, clean lines and smooth curves, 2d flat illustration, contemporary art illustration, contemporary painting, use minimum props, limited Colors, use light grey color overlay for shadow, use light white color overlay for highlights, delicate art, whimsy and wonder, whimsical.  \n\n### Key Enhancements & Reasoning:  \n1. **Core Action Clarification**:  \n   - Explicitly states "extended by zooming out and outpainting the background" to define the outpainting process.  \n   - Emphasizes "maintaining character consistency" to ensure the original subjects remain unchanged.  \n\n2. **Mandatory Style Inclusion**:  \n   - Includes **"by Alice Lee style, Wax crayon brushes procreate style, hand drawn"** (required for flat illustration).  \n\n3. **Optimal Style Elements**:  \n   - **Professional Context**: "a poster by Tom Whalen, featured on behance, context art, behance hd, art on instagram..." (aligns with outpainting as a creative/illustrative process).  \n   - **Flat Illustration Essentials**: "soft shadows, no contrast, clean ultrasharp focus, premium vector, flat colours, show less details, clean lines and smooth curves, 2d flat illustration" (ensures minimalist, modern aesthetics).  \n   - **Character Focus**: "their faces are visible, hand drawn people, human illustration" (prioritizes subject consistency during zooming).  \n   - **Technical Specs**: "use light grey color overlay for shadow, use light white color overlay for highlights" (subtle depth for extended backgrounds).  \n   - **Artistic Nuance**: "delicate art, whimsy and wonder, whimsical" (adds charm to new background elements).  \n\n4. **Outpainting-Specific Adjustments**:  \n   - "use minimum props" avoids cluttering the newly extended space.  \n   - "limited Colors" maintains visual harmony with the original palette.  \n   - "timeless art, contemporary art illustration" ensures the outpainting feels cohesive with the source image.  \n\nThis prompt balances technical precision (for AI outpainting) with stylistic coherence, ensuring the zoomed-out scene retains flat illustration’s signature simplicity while expanding the narrative seamlessly.']
==


" Very important note:

the below For "flat illustration" style instructions in prompt template **supercedes** the priority of acceptance in final output than referring to examples given for training. (the examples with reference prompts are good for training dspy to answer. however it sometimes adds some other art style or elements. 

hence you must be adding additional inputs in prompt template to absolutely use this and give priority.)

 # Create a prediction with the LM
                pred = self.lm(
                    prompt=f"""You are an expert image prompt engineer. Generate an enhanced image generation prompt with the following details:

Taste: {taste}
User Input: {user_input}

Examples of {taste} prompts:
{examples_text}

For "flat illustration" style:
    - ALWAYS include: "by Alice Lee style, Wax crayon brushes procreate style, hand drawn" (this is required)
    - Include other style elements when they are suitable for the subject matter:
        "a poster by Tom Whalen, featured on behance, context art, behance hd, art on instagram, storybook illustration, Pro freelance, Illustration agency, Popular on Dribbble"
        "soft shadows, no contrast, clean ultrasharp focus, premium vector, hand drawn people, timeless art, human illustration, freepik, flat colours"
        "their faces are visible, show less details, clean lines and smooth curves, 2d flat illustration, contemporary art illustration, contemporary painting"
        "use minimum props, limited Colors, use light grey color overlay for shadow, use light white color overlay for highlights, delicate art, whimsy and wonder, whimsical"
    - Pick the best suitable elements based on the user input



Generate a detailed, enhanced image prompt that captures the essence of the input with the specified style.

Output:""",
            




# Implementation Guide: Adding Watercolor Style Support

## Step 1: Add Examples

Add the watercolor example to your examples collection:

```python
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
```

## Step 2: Update Prompt Generation Logic

Add watercolor-specific style instructions to your prompt generator:

```python
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
```

## Step 3: Add Term Verification

Implement a verification method to check for watercolor-specific terms:

```python
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
```

## Step 4: Update Fallback Method

Add a watercolor-specific fallback template:

```python
if taste == "watercolor":
    return f"""Watercolor painting of {user_input}, visible brush strokes, wet-on-wet technique, textured paper showing through, loose and expressive style, light washes of color, ethereal atmosphere."""
```

## Step 5: Add to Test Cases

Include watercolor in your test suite:

```python
test_cases = [
    # ... existing test cases ...
    ("watercolor", "a peaceful mountain landscape"),
    ("watercolor", "a cat sitting on a windowsill"),
    ("watercolor", "city street in the rain")
]
```

## Step 6: Integration Checklist

- [ ] Add watercolor example to examples collection
- [ ] Update style instructions in prompt generator
- [ ] Implement `has_watercolor_terms()` verification method
- [ ] Add watercolor fallback template
- [ ] Add test cases for watercolor style
- [ ] Run tests to verify watercolor prompts include required terms
- [ ] Test with various user inputs to ensure quality
- [ ] Document watercolor style characteristics in your style guide

## Expected Behavior

When a user requests watercolor style:
1. System uses the watercolor example as reference
2. Generates prompt with watercolor-specific terminology
3. Verifies required terms are present
4. Falls back to template if generation fails
5. Returns enhanced prompt with authentic watercolor characteristics    style_instructions = """
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
