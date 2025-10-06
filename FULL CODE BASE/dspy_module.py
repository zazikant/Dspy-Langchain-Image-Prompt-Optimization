import dspy
from typing import List, Dict, Any, Optional

class ImagePromptSignature(dspy.Signature):
    """Generate an image prompt based on user taste and description."""
    taste = dspy.Input(desc="Artistic style preference")
    user_input = dspy.Input(desc="User's description of desired image")
    optimized_prompt = dspy.Output(desc="Optimized prompt for image generation")

class ImagePromptGenerator(dspy.Module):
    """DSPy module for generating optimized image prompts."""
    
    def __init__(self):
        self.generate_prompt = dspy.Predict(ImagePromptSignature)
    
    def forward(self, taste: str, user_input: str):
        return self.generate_prompt(taste=taste, user_input=user_input)

def create_training_examples() -> List[dspy.Example]:
    """Create initial training examples for the DSPy model."""
    training_data = [
        {
            'taste': 'photorealistic',
            'user_input': 'a cat sitting on a windowsill',
            'optimized_prompt': 'Ultra realistic photograph of a ginger cat sitting on a sunlit windowsill, detailed fur texture, sharp focus, natural lighting, 85mm lens, shallow depth of field'
        },
        {
            'taste': 'oil painting',
            'user_input': 'a mountain landscape',
            'optimized_prompt': 'Oil painting of majestic mountain landscape at sunset, impressionist style, visible brushstrokes, warm golden hour light, textured canvas, rich color palette'
        },
        {
            'taste': 'anime',
            'user_input': 'a futuristic city',
            'optimized_prompt': 'Anime style illustration of a futuristic cyberpunk cityscape at night, neon lights, flying vehicles, detailed architecture, vibrant colors, high contrast'
        },
        {
            'taste': 'cyberpunk',
            'user_input': 'a person in a rain-soaked street',
            'optimized_prompt': 'Cyberpunk style digital art of a lone figure in a rain-soaked neon-lit street, holographic advertisements, reflective surfaces, cinematic lighting, gritty atmosphere'
        },
        {
            'taste': 'watercolor',
            'user_input': 'a field of flowers',
            'optimized_prompt': 'Watercolor painting of a vibrant field of wildflowers, soft blended colors, loose brushstrokes, watercolor paper texture, delicate details, ethereal atmosphere'
        },
        {
            'taste': '3d render',
            'user_input': 'a futuristic spaceship',
            'optimized_prompt': '3D render of a sleek futuristic spaceship, detailed metallic surfaces, volumetric lighting, studio quality, 4K resolution, cinematic composition'
        },
        {
            'taste': 'photorealistic',
            'user_input': 'a sunset over mountains',
            'optimized_prompt': 'Photorealistic landscape of sunset over mountain range, golden hour lighting, dramatic clouds, detailed terrain, atmospheric haze, 35mm lens'
        },
        {
            'taste': 'anime',
            'user_input': 'a dragon flying over a castle',
            'optimized_prompt': 'Anime style digital painting of a majestic dragon soaring over a medieval castle, detailed scales and wings, dynamic perspective, vibrant sunset colors, dramatic clouds'
        },
        {
            'taste': 'oil painting',
            'user_input': 'a portrait of an old man',
            'optimized_prompt': 'Oil painting portrait of an elderly man with weathered features, Rembrandt lighting, rich textures, detailed brushwork, classical composition'
        },
        {
            'taste': 'cyberpunk',
            'user_input': 'a futuristic vehicle',
            'optimized_prompt': 'Cyberpunk concept art of a futuristic hover vehicle, neon accents, metallic surfaces, detailed mechanical elements, rainy city background'
        }
    ]
    
    return [dspy.Example(**example) for example in training_data]

def prompt_quality(example, pred, trace=None):
    """Quality evaluation function for DSPy teleprompter."""
    quality_indicators = [
        'detailed' in pred.optimized_prompt.lower(),
        'style' in pred.optimized_prompt.lower(),
        len(pred.optimized_prompt.split()) > 10,  # Sufficient detail
        any(tech_word in pred.optimized_prompt.lower() 
            for tech_word in ['lighting', 'focus', 'texture', 'composition'])
    ]
    return sum(quality_indicators) / len(quality_indicators)

def initialize_dspy_model(openai_api_key: str, trainset: Optional[List[dspy.Example]] = None):
    """
    Initialize and compile the DSPy model with training examples.
    
    Args:
        openai_api_key: API key for OpenAI
        trainset: Optional training examples to use for initialization
        
    Returns:
        Compiled DSPy model
    """
    # Configure DSPy with the GLM model
    lm = dspy.OpenAI(model="gpt-3.5-turbo", api_key=openai_api_key, max_tokens=200)
    dspy.settings.configure(lm=lm)
    
    # Create training examples if not provided
    if trainset is None:
        trainset = create_training_examples()
    
    # Initialize the generator
    dspy_generator = ImagePromptGenerator()
    
    # Set up the teleprompter with BootstrapFewShot
    teleprompter = dspy.BootstrapFewShot(metric=prompt_quality)
    
    # Compile the model
    print("Compiling DSPy model with training examples...")
    optimized_dspy = teleprompter.compile(dspy_generator, trainset=trainset, train_kwargs={"num_threads": 4})
    print("DSPy model compiled successfully.")
    
    return optimized_dspy

def retrain_dspy_model(openai_api_key: str, training_examples: List[dspy.Example]):
    """
    Retrain the DSPy model with new training examples.
    
    Args:
        openai_api_key: API key for OpenAI
        training_examples: List of training examples to use for retraining
        
    Returns:
        Newly compiled DSPy model
    """
    print(f"Retraining DSPy model with {len(training_examples)} examples...")
    return initialize_dspy_model(openai_api_key, trainset=training_examples)
