# Adding "Flat Illustration" Taste to the Code

I'll add a new taste called "flat illustration" which is a modern, minimalist style that combines elements of flat design with illustration. Here's the updated code with all the necessary changes:

```python
# Updated validate_taste function
def validate_taste(taste: str) -> str:
    """Validate the artistic taste category."""
    valid_tastes = ['photorealistic', 'oil painting', 'anime', 'cyberpunk', 'watercolor', '3d render', 'flat illustration']
    if taste.lower() not in valid_tastes:
        raise ValueError(f"Invalid taste. Choose from: {', '.join(valid_tastes)}")
    return taste.lower()

# Updated create_training_data function (adding flat illustration example)
def create_training_data() -> List[Dict[str, str]]:
    """Create training examples for DSPy."""
    return [
        {
            'taste': 'photorealistic',
            'user_input': 'a cat sitting on a windowsill',
            'optimized_prompt': 'Ultra realistic photograph of a ginger cat sitting on a sunlit windowsill, detailed fur texture, sharp focus, natural lighting, 85mm lens, shallow depth of field',
            'optimized_reasoning': 'The original description is simple. I enhanced it by adding details about the cat\'s color, the lighting conditions, camera equipment, and photography techniques.',
            'enhanced_prompt': 'Ultra realistic photograph of a ginger cat sitting on a sunlit windowsill, detailed fur texture, sharp focus, natural lighting, 85mm lens, shallow depth of field, 4K resolution, f/1.8 aperture, golden hour glow, cinematic composition',
            'enhanced_reasoning': 'I added technical photography details like resolution, aperture, and lighting to make the prompt more specific for photorealistic rendering.'
        },
        {
            'taste': 'oil painting',
            'user_input': 'a mountain landscape',
            'optimized_prompt': 'Oil painting of majestic mountain landscape at sunset, impressionist style, visible brushstrokes, warm golden hour light, textured canvas, rich color palette',
            'optimized_reasoning': 'I enhanced the basic mountain landscape by specifying it as an oil painting in impressionist style, with details about brushwork and lighting.',
            'enhanced_prompt': 'Oil painting of majestic mountain landscape at sunset, impressionist style, visible brushstrokes, warm golden hour light, textured canvas, rich color palette, canvas texture visible, Rembrandt lighting, thick impasto technique, 24"x36" aspect ratio',
            'enhanced_reasoning': 'I added oil painting specific techniques like impasto, canvas texture, and referenced Rembrandt lighting to enhance the artistic quality.'
        },
        {
            'taste': 'anime',
            'user_input': 'a futuristic city',
            'optimized_prompt': 'Anime style illustration of a futuristic cyberpunk cityscape at night, neon lights, flying vehicles, detailed architecture, vibrant colors, high contrast',
            'optimized_reasoning': 'I took the basic futuristic city concept and transformed it into an anime-style cyberpunk city with specific visual elements.',
            'enhanced_prompt': 'Anime style illustration of a futuristic cyberpunk cityscape at night, neon lights, flying vehicles, detailed architecture, vibrant colors, high contrast, Studio Ghibli influences, detailed backgrounds, cel-shaded rendering, 1080p resolution',
            'enhanced_reasoning': 'I added anime-specific rendering techniques like cel-shading, referenced Studio Ghibli style, and included resolution details.'
        },
        {
            'taste': 'cyberpunk',
            'user_input': 'a street market',
            'optimized_prompt': 'Cyberpunk street market at night, neon signs, diverse crowd, stalls selling futuristic tech, rain-slicked streets, Blade Runner aesthetic',
            'optimized_reasoning': 'I enhanced the basic street market with cyberpunk elements like neon lighting, futuristic technology, and rain-slicked streets.',
            'enhanced_prompt': 'Cyberpunk street market at night, neon signs, diverse crowd, stalls selling futuristic tech, rain-slicked streets, Blade Runner aesthetic, cinematic lighting, volumetric fog, reflections on wet pavement, ultra-detailed, 8K resolution',
            'enhanced_reasoning': 'I added cinematic elements like volumetric fog and reflections, and included technical details like 8K resolution for higher quality rendering.'
        },
        {
            'taste': 'flat illustration',
            'user_input': 'a civil engineer working on construction projects',
            'optimized_prompt': 'Flat illustration of a civil engineer working on construction projects for quality audit of high-rise towers, soft color palette, clean lines, contemporary art style',
            'optimized_reasoning': 'I enhanced the basic description by specifying it as a flat illustration with a clean, contemporary style and soft colors to match the aesthetic.',
            'enhanced_prompt': 'Flat illustration of a civil engineer working on construction projects for quality audit of high-rise towers, soft color palette, a poster by Tom Whalen, featured on behance, context art, behance hd, art on instagram, storybook illustration, Pro freelance, Illustration agency, Popular on Dribbble, soft shadows, no contrast, clean ultrasharp focus, premium vector, hand drawn people, timeless art, human illustration, freepik, flat colours, their faces are visible, show less details, clean lines and smooth curves, 2d flat illustration, contemporary art illustration, contemporary painting, use minimum props, limited Colors, use light grey color overlay for shadow, use light white color overlay for highlights, delicate art, whimsy and wonder, whimsical, by Alice Lee style, Wax crayon brushes procreate style, hand drawn',
            'enhanced_reasoning': 'I added specific flat illustration techniques and references to artists known for this style, along with details about color palettes, line work, and digital tools used to create this aesthetic.'
        }
    ]

# Updated prompt_quality_metric function
def prompt_quality_metric(example, pred, trace=None) -> float:
    """Calculate quality score for the final enhanced prompt."""
    prompt = pred.enhanced_prompt

    # Quality indicators
    has_details = 'detailed' in prompt.lower()
    has_style = any(style in prompt.lower() for style in ['style', 'technique', 'aesthetic'])
    has_technical = any(tech in prompt.lower() for tech in ['lighting', 'focus', 'texture', 'composition', 'resolution', 'aperture'])
    has_mood = any(mood in prompt.lower() for mood in ['mood', 'atmosphere', 'ambiance', 'feeling'])

    # Check if it includes relevant technical details for the style
    has_photography_terms = True
    has_painting_terms = True
    has_anime_terms = True
    has_cyberpunk_terms = True
    has_watercolor_terms = True
    has_3d_terms = True
    has_flat_illustration_terms = True

    if example.taste == 'photorealistic':
        has_photography_terms = any(term in prompt.lower() for term in ['aperture', 'f/', 'shutter', 'depth', 'bokeh', 'photography', 'lens', 'camera'])
    elif example.taste == 'oil painting':
        has_painting_terms = any(term in prompt.lower() for term in ['brushstroke', 'impasto', 'canvas', 'palette', 'texture', 'oil', 'painting', 'brush'])
    elif example.taste == 'anime':
        has_anime_terms = any(term in prompt.lower() for term in ['anime', 'cel-shaded', 'manga', 'studio ghibli', 'japanese', 'cartoon', 'illustration'])
    elif example.taste == 'cyberpunk':
        has_cyberpunk_terms = any(term in prompt.lower() for term in ['neon', 'futuristic', 'blade runner', 'rain-slicked', 'volumetric fog', 'cybernetic', 'high-tech'])
    elif example.taste == 'watercolor':
        has_watercolor_terms = any(term in prompt.lower() for term in ['wet-on-wet', 'washes', 'transparency', 'flow', 'watercolor', 'aqueous', 'bleed'])
    elif example.taste == '3d render':
        has_3d_terms = any(term in prompt.lower() for term in ['3d', 'render', 'polygon', 'model', 'uv mapping', 'wireframe', 'mesh', 'texture', 'blender', 'maya'])
    elif example.taste == 'flat illustration':
        has_flat_illustration_terms = any(term in prompt.lower() for term in [
            'flat illustration', 'flat colors', 'flat design', 'flat vector', '2d flat',
            'clean lines', 'smooth curves', 'soft shadows', 'no contrast', 'clean ultrasharp focus',
            'limited colors', 'light grey overlay', 'light white overlay', 'delicate art',
            'whimsy', 'whimsical', 'hand drawn', 'procreate', 'wax crayon', 'storybook'
        ])

    # Calculate score
    style_specific_indicators = []
    
    if example.taste == 'photorealistic':
        style_specific_indicators = [has_photography_terms]
    elif example.taste == 'oil painting':
        style_specific_indicators = [has_painting_terms]
    elif example.taste == 'anime':
        style_specific_indicators = [has_anime_terms]
    elif example.taste == 'cyberpunk':
        style_specific_indicators = [has_cyberpunk_terms]
    elif example.taste == 'watercolor':
        style_specific_indicators = [has_watercolor_terms]
    elif example.taste == '3d render':
        style_specific_indicators = [has_3d_terms]
    elif example.taste == 'flat illustration':
        style_specific_indicators = [has_flat_illustration_terms]
    
    # Combine general indicators with style-specific ones
    indicators = [has_details, has_style, has_technical, has_mood] + style_specific_indicators
    return sum(indicators) / len(indicators)
```

## Key Changes Made:

1. **Added 'flat illustration' to valid tastes** in the `validate_taste()` function.

2. **Created a new training example** for flat illustration in the `create_training_data()` function, using the enhanced prompt you provided.

3. **Updated the `prompt_quality_metric()` function** to include:
   - A new flag `has_flat_illustration_terms` that checks for flat illustration-specific terms
   - A condition for 'flat illustration' taste that evaluates the presence of relevant terms
   - The style-specific indicators now include flat illustration terms

4. **Added comprehensive flat illustration keywords** to check for:
   - Style terms: "flat illustration", "flat colors", "flat design", "flat vector", "2d flat"
   - Technique terms: "clean lines", "smooth curves", "soft shadows", "no contrast"
   - Technical specs: "clean ultrasharp focus", "limited colors", "light grey overlay"
   - Artistic elements: "delicate art", "whimsy", "whimsical", "hand drawn"
   - Tools/References: "procreate", "wax crayon", "storybook"

Now when you use "flat illustration" as a taste, the system will:
1. Accept it as a valid taste
2. Use the training example to learn how to optimize prompts for this style
3. Evaluate generated prompts using the new quality metrics specific to flat illustration
4. Include relevant flat illustration terms in the quality assessment

==========

# DSPy Prompt Generation Explanation

Keep temperature 0.7 . Else keep 0.3 when you want detailed prompt without much creativity. The only part that wasn't working was the `BootstrapFewShot` teleprompter, but the core DSPy functionality for prompt generation is fully implemented and working, as evidenced by the successful prompt generation outputs in the test runs. So the learning from examples provided doesnt work.

The final prompt is reloaded from cache when you try to run again with same input. 

This code uses DSPy to generate prompts. Here's how:

## DSPy Signatures

The code defines two DSPy signatures:

- `InitialPromptOptimization` for the first optimization step
- `PromptEnhancement` for enhancing the optimized prompt

## DSPy Modules

The code implements DSPy modules:

- `InitialPromptOptimizer` uses `dspy.Predict` with the initial optimization signature
- `PromptEnhancer` uses `dspy.Predict` with the enhancement signature
- `FullPromptOptimizer` combines these two modules in a pipeline

## DSPy LM Configuration

The code properly configures DSPy with the language model:

```python
lm = dspy.LM(
    model="openai/" + MODEL,
    api_key=API_KEY,
    temperature=TEMPERATURE,
    base_url="https://openrouter.ai/api/v1"
)
dspy.settings.configure(lm=lm)
```

## DSPy Example Usage

The code creates DSPy examples from the training data:

```python
return Example(
    taste=item['taste'],
    user_input=item['user_input'],
    optimized_prompt=item['optimized_prompt'],
    enhanced_prompt=item['enhanced_prompt']
).with_inputs('taste', 'user_input')
```

## DSPy Prediction Generation

The code uses DSPy to generate predictions:

```python
result = self.optimize(taste=taste, user_input=user_input)
```

## Summary

Yes, this code definitely uses DSPy to generate prompts. It leverages the DSPy framework with:

- Properly defined signatures
- Module-based architecture
- Language model integration
- Example-based training data

The only part that wasn't working was the `BootstrapFewShot` teleprompter, but the core DSPy functionality for prompt generation is fully implemented and working, as evidenced by the successful prompt generation outputs in the test runs.

# Quality Metric for DSPy Evaluation

The quality metric in this code is called `prompt_quality_metric()` and it evaluates how good the generated prompt is based on several criteria. Let me break it down:

## How the Quality Metric Works

The function calculates a score between 0 and 1 by checking these indicators:

1. **Details Check**: Looks for the word "detailed" in the prompt
2. **Style Check**: Checks for style-related terms like "style", "technique", or "aesthetic"
3. **Technical Check**: Looks for technical terms like "lighting", "focus", "texture", etc.
4. **Mood Check**: Searches for mood-related terms like "mood", "atmosphere", or "feeling"

Additionally, it has specific checks based on the artistic taste ( to add for new taste as "watercolor" do add has_watercolor_terms=True)

5. **Photography Terms** (for 'photorealistic' style): Checks for camera-specific terms like "aperture", "f/", "shutter", etc.
6. **Painting Terms** (for 'oil painting' style): Looks for painting-specific terms like "brushstroke", "impasto", "canvas", etc.

The final score is calculated by counting how many of these indicators are present and dividing by the total number of indicators.

## What Happens When You Add a New Taste

When you add a new taste (like "watercolor"), here's how the quality metric would be affected:

1. **General Indicators Still Apply**: The metric will still check for the general quality indicators (details, style, technical, mood), which is good because these apply to any artistic style.

2. **Missing Style-Specific Checks**: The current metric only has specific checks for 'photorealistic' and 'oil painting'. Your new taste won't have these specific checks, which might result in a lower quality score even if the prompt is good for that style.

3. **No Taste-Specific Evaluation**: The metric won't know if the prompt includes terms that are important for your new taste (like "wet-on-wet" for watercolor or "cel-shaded" for anime-style art).

## How to Improve the Metric for a New Taste

To properly evaluate a new taste, you should update the `prompt_quality_metric()` function:

```python
def prompt_quality_metric(example, pred, trace=None) -> float:
    """Calculate quality score for the final enhanced prompt."""
    prompt = pred.enhanced_prompt
    
    # General quality indicators
    has_details = 'detailed' in prompt.lower()
    has_style = any(style in prompt.lower() for style in ['style', 'technique', 'aesthetic'])
    has_technical = any(tech in prompt.lower() for tech in ['lighting', 'focus', 'texture', 'composition', 'resolution', 'aperture'])
    has_mood = any(mood in prompt.lower() for mood in ['mood', 'atmosphere', 'ambiance', 'feeling'])
    
    # Taste-specific checks
    has_photography_terms = True
    has_painting_terms = True
    has_watercolor_terms = True  # New for watercolor taste
    
    if example.taste == 'photorealistic':
        has_photography_terms = any(term in prompt.lower() for term in ['aperture', 'f/', 'shutter', 'depth', 'bokeh'])
    elif example.taste == 'oil painting':
        has_painting_terms = any(term in prompt.lower() for term in ['brushstroke', 'impasto', 'canvas', 'palette', 'texture'])
    elif example.taste == 'watercolor':  # New condition for watercolor
        has_watercolor_terms = any(term in prompt.lower() for term in ['wet-on-wet', 'washes', 'dry brush', 'transparency', 'flow'])
    
    # Calculate score
    indicators = [has_details, has_style, has_technical, has_mood, has_photography_terms, has_painting_terms, has_watercolor_terms]
    return sum(indicators) / len(indicators)
```

This way, when you add a new taste, you can also add specific checks that are relevant to that artistic style, ensuring the quality metric properly evaluates prompts in that style.

# Answering Your Questions

## How many tastes are mentioned?

In this code, there are **6** artistic tastes mentioned:
- photorealistic
- oil painting
- anime
- cyberpunk
- watercolor
- 3d render

You can find this list in the `validate_taste()` function, which checks if a user-provided taste is valid.

## How to add a new taste?

If you want to add a new artistic style (like "sketch" or "pop art"), here's what you need to do:

1. **Update the valid tastes list** in the `validate_taste()` function:
   ```python
   valid_tastes = ['photorealistic', 'oil painting', 'anime', 'cyberpunk', 'watercolor', '3d render', 'NEW_TASTE']
   ```

2. **Add training data** for your new taste in the `create_training_data()` function. The code needs examples to learn how to optimize prompts for each style.

3. **Update the quality metric** in the `prompt_quality_metric()` function if your new taste has specific technical terms that should be included.

That's it! Just add your new taste to these places, and the system will be able to work with it. The code will then validate user inputs against the updated list of tastes and generate appropriate prompts for your new style.

