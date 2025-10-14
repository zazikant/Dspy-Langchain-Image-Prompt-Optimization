#!/usr/bin/env python3
"""
Model implementation based on .env configuration for DSPy-LangChain integration
"""

import os
import logging
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Import required libraries
import dspy
from dspy import Example
from langchain.prompts import PromptTemplate
from langchain.schema import BasePromptTemplate
from langchain.chains import LLMChain

class OpenRouterLLM:
    """
    Custom LLM implementation for OpenRouter API
    """
    
    def __init__(self, model: str = None, api_key: str = None, temperature: float = 0.7):
        """
        Initialize OpenRouter LLM
        
        Args:
            model: Model name from environment
            api_key: API key from environment
            temperature: Temperature setting
        """
        self.model = model or os.getenv('MODEL', 'z-ai/glm-4.5-air:free')
        self.api_key = api_key or os.getenv('OPENROUTER_API_KEY')
        self.temperature = float(temperature or os.getenv('TEMPERATURE', 0.7))
        
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables")
        
        logger.info(f"Initialized OpenRouter LLM with model: {self.model}, temperature: {self.temperature}")
    
    def __call__(self, prompt: str, **kwargs) -> str:
        """
        Call the LLM with the given prompt
        
        Args:
            prompt: Input prompt
            **kwargs: Additional parameters
            
        Returns:
            Model response
        """
        try:
            # Use DSPy's LM wrapper with OpenRouter for GLM 4.5 Air
            lm = dspy.LM(
                model="openai/" + self.model,  # Prefix with provider
                api_key=self.api_key,
                temperature=self.temperature,
                base_url="https://openrouter.ai/api/v1"
            )
            
            # Create a simple DSPy program
            class SimpleQA(dspy.Module):
                def __init__(self):
                    super().__init__()
                    self.generate = dspy.Predict("prompt -> response")
                
                def forward(self, prompt):
                    return self.generate(prompt=prompt)
            
            program = SimpleQA()
            result = program(prompt=prompt)
            
            return result.response if hasattr(result, 'response') else str(result)
            
        except Exception as e:
            logger.error(f"Error calling OpenRouter LLM: {str(e)}")
            raise
    
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate method for LangChain compatibility
        """
        return self(prompt, **kwargs)

class DSPyPromptTemplate(BasePromptTemplate):
    """
    A custom prompt template that integrates DSPy optimization with LangChain.
    This template uses DSPy's signature-based approach for prompt engineering.
    """
    
    def __init__(self, input_variables: List[str], template: str,
                 dspy_signature: str = None, examples: List[Dict] = None):
        """
        Initialize the DSPy prompt template.
        
        Args:
            input_variables: List of input variable names
            template: Base template string
            dspy_signature: DSPy signature for optimization
            examples: List of example inputs/outputs for few-shot learning
        """
        super().__init__(input_variables=input_variables, template=template)
        # Store as instance variable instead of class field
        self._dspy_signature = dspy_signature or "input -> output"
        self._examples = examples or []
        
        # Initialize DSPy
        self._setup_dspy()
    
    @property
    def dspy_signature(self):
        """Get the DSPy signature"""
        return self._dspy_signature
    
    @property
    def examples(self):
        """Get the examples"""
        return self._examples
    
    def _setup_dspy(self):
        """Set up DSPy with configured backend"""
        try:
            api_key = os.getenv('OPENROUTER_API_KEY')
            model = os.getenv('MODEL', 'z-ai/glm-4.5-air:free')
            temperature = float(os.getenv('TEMPERATURE', 0.3))
            
            if not api_key:
                raise ValueError("No API key found. Please set OPENROUTER_API_KEY in .env file")
            
            logger.info(f"Setting up DSPy with model: {model}")
            
            # Configure DSPy with the selected model using OpenRouter
            # Use the correct DSPy API for GLM 4.5 Air
            lm = dspy.LM(
                model="openai/" + model,  # Prefix with provider
                api_key=api_key,
                temperature=temperature,
                base_url="https://openrouter.ai/api/v1"
            )
            dspy.settings.configure(lm=lm)
            
            logger.info("DSPy setup completed successfully")
            
        except Exception as e:
            logger.error(f"Failed to setup DSPy: {str(e)}")
            raise
    
    def format_prompt(self, **kwargs) -> str:
        """
        Format the prompt using DSPy optimization if examples are provided.
        """
        try:
            logger.debug(f"Formatting prompt with input variables: {self.input_variables}")
            logger.debug(f"Input kwargs: {kwargs}")
            
            # Create a DSPy module for prompt optimization
            class OptimizedPrompt(dspy.Module):
                def __init__(self, signature):
                    super().__init__()
                    self.generate_answer = dspy.ChainOfThought(signature)
                
                def forward(self, **inputs):
                    return self.generate_answer(**inputs)
            
            # If we have examples, use them for few-shot optimization
            if self._examples:
                logger.info(f"Using {len(self._examples)} examples for DSPy optimization")
                
                # Create DSPy examples
                dspy_examples = []
                for ex in self._examples:
                    dspy_examples.append(Example(**ex).with_inputs(*self.input_variables))
                
                # Create and optimize the prompt
                optimizer = dspy.BootstrapFewShot()
                optimized_prompt = optimizer.compile(OptimizedPrompt(self._dspy_signature), trainset=dspy_examples)
                
                # Use the optimized prompt
                result = optimized_prompt(**kwargs)
                output = result.output if hasattr(result, 'output') else str(result)
                logger.debug(f"DSPy optimization result: {output}")
                return output
            
            # Fallback to standard template formatting
            formatted = self.template.format(**kwargs)
            logger.debug(f"Standard template formatting result: {formatted}")
            return formatted
            
        except Exception as e:
            logger.error(f"Error formatting prompt: {str(e)}")
            logger.error(f"Input variables: {self.input_variables}")
            logger.error(f"Template: {self.template}")
            logger.error(f"Examples: {self.examples}")
            # Fallback to basic template formatting with error handling
            try:
                return self.template.format(**kwargs)
            except Exception as fallback_error:
                logger.error(f"Fallback formatting also failed: {str(fallback_error)}")
                raise

    def format(self, **kwargs) -> str:
        """
        Legacy method for backward compatibility
        """
        return self.format_prompt(**kwargs)

def create_qa_chain():
    """Create a question-answering chain with DSPy optimization"""
    try:
        logger.info("Creating QA chain with DSPy optimization")
        
        # Define the DSPy signature for QA
        qa_signature = "question -> answer"
        
        # Create examples for few-shot learning
        examples = [
            {
                "question": "What is the capital of France?",
                "answer": "Paris"
            },
            {
                "question": "What is 2 + 2?",
                "answer": "4"
            },
            {
                "question": "Who wrote Romeo and Juliet?",
                "answer": "William Shakespeare"
            }
        ]
        
        # Create the DSPy prompt template
        template = """Answer the following question based on your knowledge.
        
Question: {question}
Answer: """
        
        dspy_prompt = DSPyPromptTemplate(
            input_variables=["question"],
            template=template,
            dspy_signature=qa_signature,
            examples=examples
        )
        
        logger.info("QA chain created successfully")
        
        return dspy_prompt
        
    except Exception as e:
        logger.error(f"Failed to create QA chain: {str(e)}")
        raise

def create_summarization_chain():
    """Create a text summarization chain with DSPy optimization"""
    try:
        logger.info("Creating summarization chain with DSPy optimization")
        
        # Define the DSPy signature for summarization
        summarization_signature = "text -> summary"
        
        # Create examples for few-shot learning
        examples = [
            {
                "text": "The quick brown fox jumps over the lazy dog. This is a simple sentence used for typing practice.",
                "summary": "A fox jumps over a dog in a typing practice sentence."
            },
            {
                "text": "Machine learning is a subset of artificial intelligence that focuses on algorithms that can learn from data without being explicitly programmed.",
                "summary": "ML is AI that learns from data without explicit programming."
            }
        ]
        
        # Create the DSPy prompt template
        template = """Summarize the following text in a concise manner.
        
Text: {text}
Summary: """
        
        dspy_prompt = DSPyPromptTemplate(
            input_variables=["text"],
            template=template,
            dspy_signature=summarization_signature,
            examples=examples
        )
        
        logger.info("Summarization chain created successfully")
        
        return dspy_prompt
        
    except Exception as e:
        logger.error(f"Failed to create summarization chain: {str(e)}")
        raise

if __name__ == "__main__":
    # Test the model implementation
    print("🚀 Testing Model Implementation")
    print("=" * 40)
    
    try:
        # Test LLM initialization
        llm = OpenRouterLLM()
        print(f"✅ LLM initialized with model: {llm.model}")
        
        # Test QA chain
        qa_chain = create_qa_chain()
        print("✅ QA chain created successfully")
        
        # Test summarization chain
        summary_chain = create_summarization_chain()
        print("✅ Summarization chain created successfully")
        
        # Test a simple question
        test_question = "What is the capital of Japan?"
        print(f"\n🔍 Testing QA: {test_question}")
        answer = qa_chain.format_prompt(question=test_question)
        print(f"Answer: {answer.strip()}")
        
        # Test summarization
        test_text = "Artificial intelligence is transforming the way we live and work. From self-driving cars to virtual assistants, AI is becoming increasingly integrated into our daily lives."
        print(f"\n📝 Testing Summarization:")
        summary = summary_chain.format_prompt(text=test_text)
        print(f"Summary: {summary.strip()}")
        
        print("\n✅ Model implementation test completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during testing: {str(e)}")
        logger.error(f"Model test failed: {str(e)}")