from .dspy_module import initialize_dspy_model, retrain_dspy_model
from .langchain_chains import enhance_prompt
from .data_manager import DataManager
from .utils import validate_taste, validate_input, prompt_quality_score
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class PromptGenerator:
    """Main class for generating optimized image prompts."""
    
    def __init__(self, data_path: str = "project/data/training_data.csv", openai_api_key: str = None):
        """Initialize the PromptGenerator with data manager and models."""
        self.data_manager = DataManager(data_path)
        self.openai_api_key = openai_api_key
        self.dspy_model = initialize_dspy_model(openai_api_key)
        self.retraining_needed = False
    
    def generate(self, taste: str, user_input: str, 
                additional_context: Optional[str] = None) -> str:
        """
        Generate an enhanced image prompt based on user input and taste.
        
        Args:
            taste: Artistic style preference
            user_input: User's description of desired image
            additional_context: Optional additional context
            
        Returns:
            Enhanced image prompt
        """
        try:
            # Validate inputs
            taste = validate_taste(taste)
            user_input = validate_input(user_input)
            
            # Stage 1: DSPy optimization
            dspy_result = self.dspy_model(taste=taste, user_input=user_input)
            dspy_prompt = dspy_result.optimized_prompt
            
            # Stage 2: LangChain enhancement
            final_prompt = enhance_prompt(dspy_prompt, taste, self.openai_api_key)
            
            # Calculate quality score for the final enhanced prompt
            quality_score = prompt_quality_score(final_prompt)
            
            # Stage 3: Data storage
            self.data_manager.add_entry(
                taste=taste,
                user_input=user_input,
                dspy_prompt=dspy_prompt,
                final_prompt=final_prompt,
                quality_score=quality_score
            )
            
            # Mark model for retraining if we have enough new data
            if len(self.data_manager.df) % 10 == 0 and len(self.data_manager.df) > 0:
                self.retraining_needed = True
            
            return final_prompt
            
        except Exception as e:
            logger.error(f"Error in prompt generation: {e}")
            # Create a simple fallback prompt
            fallback_prompt = f"{taste} style image of {user_input}, detailed, high quality"
            logger.info(f"Using fallback prompt: {fallback_prompt}")
            return fallback_prompt
    
    def update_model(self):
        """
        Update the DSPy model with recent high-quality examples.
        
        Returns:
            bool: True if model was updated, False otherwise
        """
        if not self.retraining_needed:
            logger.info("Model retraining not needed")
            return False
        
        try:
            # Get high-quality examples for retraining (score is 0-1)
            high_quality_examples = self.data_manager.get_high_quality_examples(
                min_quality=0.7, days=30 
            )
            
            if not high_quality_examples:
                logger.info("No high-quality examples available for retraining")
                return False
            
            # Convert examples to DSPy format
            from .dspy_module import dspy
            dspy_examples = [
                dspy.Example(
                    taste=example['taste'],
                    user_input=example['user_input'],
                    optimized_prompt=example['optimized_prompt']
                )
                for example in high_quality_examples
            ]
            
            # Retrain the model
            self.dspy_model = retrain_dspy_model(self.openai_api_key, dspy_examples)
            
            # Reset retraining flag
            self.retraining_needed = False
            
            logger.info(f"Model retrained successfully with {len(dspy_examples)} examples")
            return True
            
        except Exception as e:
            logger.error(f"Error updating model: {e}")
            return False
    
    def get_analytics(self):
        """Get analytics about the generated prompts."""
        return self.data_manager.get_analytics()
