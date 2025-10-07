from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
from typing import Dict, Any, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_enhancement_chain(openai_api_key: str):
    """Create the LangChain chain for enhancing prompts."""
    langchain_template = PromptTemplate(
        input_variables=["optimized_prompt", "taste"],
        template="""
        You are an expert at refining image generation prompts for {taste} style.
        
        Base prompt: {optimized_prompt}
        
        Enhance this prompt with:
        - Technical details (resolution, camera angles, focal length)
        - Mood and atmosphere
        - Artistic techniques and references
        - Lighting and color palette specifics
        
        Make sure the enhanced prompt maintains the {taste} style characteristics.
        
        Enhanced prompt:
        """
    )
    
    # Create the LLM chain with GLM model
    llm_chain = LLMChain(
        llm=OpenAI(api_key=openai_api_key, model="gpt-3.5-turbo", temperature=0.7),
        prompt=langchain_template
    )
    
    return llm_chain

def enhance_prompt(optimized_prompt: str, taste: str, openai_api_key: str) -> str:
    """
    Enhance a DSPy-optimized prompt using LangChain.
    
    Args:
        optimized_prompt: The DSPy-optimized prompt
        taste: The artistic style
        openai_api_key: API key for OpenAI
        
    Returns:
        Enhanced prompt or fallback if enhancement fails
    """
    try:
        llm_chain = create_enhancement_chain(openai_api_key)
        enhanced_prompt = llm_chain.invoke({"optimized_prompt": optimized_prompt, "taste": taste})
        # The output of invoke is a dictionary, get the text
        return enhanced_prompt.get('text', '').strip()
    except Exception as e:
        logger.error(f"Error enhancing prompt with LangChain: {e}")
        # Fallback to a simple enhancement
        return f"{taste} style image of {optimized_prompt}, high quality, detailed"
