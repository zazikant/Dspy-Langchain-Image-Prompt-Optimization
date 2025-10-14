import os
import logging
from dotenv import load_dotenv
import requests
import json

# Load environment variables
load_dotenv('/home/zazikant/.env')

# API configuration for GLM-4.5-Air
API_KEY = os.getenv("OPENROUTER_API_KEY") or ""
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def process_with_glm(prompt):
    """Process with GLM-4.5-Air API and return the response"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "z-ai/glm-4.5-air:free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False,
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data), timeout=60)
        if response.status_code == 200:
            response_data = response.json()
            if 'choices' in response_data and len(response_data['choices']) > 0:
                content = response_data['choices'][0]['message']['content']
                return content
            else:
                return "Error: No content in response"
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

def demonstrate_chain_of_thought():
    """Demonstrate DSPy Chain of Thought reasoning concept."""
    print("=== DSPy Chain of Thought Reasoning Demo ===\n")
    
    # Example request
    taste = "anime"
    user_input = "a car drivng on streets of mumbai"
    
    print(f"Request: {taste} style image of '{user_input}'")
    print("\n" + "="*60)
    
    # Step 1: Chain of Thought Analysis
    print("🧠 STEP 1: Chain of Thought Analysis")
    analysis_prompt = f"""
Analyze this image generation request step by step:

REQUEST: {taste} style image of "{user_input}"

Step 1: Identify key elements in the user input
Step 2: Determine style-specific requirements for {taste}
Step 3: Plan technical specifications needed
Step 4: Consider mood and atmosphere
Step 5: Plan artistic techniques

Provide your reasoning in this format:
REASONING: [Your step-by-step analysis]
"""
    
    print("Sending analysis request to GLM...")
    reasoning = process_with_glm(analysis_prompt)
    print(f"REASONING:\n{reasoning}\n")
    
    # Step 2: Generate optimized prompt based on reasoning
    print("📝 STEP 2: Generate Optimized Prompt")
    optimization_prompt = f"""
You are an expert at creating optimized image generation prompts using Chain of Thought reasoning.

Based on this reasoning:
{reasoning}

Create an optimized prompt for:
Taste: {taste}
User Input: {user_input}

Requirements:
1. Follow the reasoning pattern
2. Incorporate elements that enhance the "{taste}" style
3. Add relevant details, textures, and atmosphere
4. Include appropriate camera/technical specifications if applicable
5. Keep the prompt concise but descriptive

Return your response in this format:
REASONING: [Your detailed reasoning]
OPTIMIZED_PROMPT: [The optimized prompt]
"""
    
    print("Sending optimization request to GLM...")
    optimization_result = process_with_glm(optimization_prompt)
    print(f"OPTIMIZATION RESULT:\n{optimization_result}\n")
    
    # Step 3: Enhance with LangChain-style + CoT
    print("✨ STEP 3: LangChain Enhancement with CoT")
    enhancement_prompt = f"""
You are an expert at refining image generation prompts using Chain of Thought reasoning.

ORIGINAL PROMPT: {optimization_result}
STYLE: {taste}

Step 1: Analyze what's missing from the original prompt
Step 2: Identify technical details to add
Step 3: Plan mood and atmosphere enhancements
Step 4: Consider artistic techniques and references
Step 5: Plan lighting and color palette improvements

Create an enhanced prompt that maintains the {taste} style while adding depth.

Return your response in this format:
REASONING: [Your enhancement reasoning]
ENHANCED_PROMPT: [The enhanced prompt with technical details, mood, artistic techniques, lighting]
"""
    
    print("Sending enhancement request to GLM...")
    enhancement_result = process_with_glm(enhancement_prompt)
    print(f"ENHANCEMENT RESULT:\n{enhancement_result}\n")
    
    print("🎯 FINAL RESULT: Complete Chain of Thought Process")
    print("="*60)
    print("The system used explicit reasoning steps to:")
    print("1. Analyze the request step by step")
    print("2. Generate an optimized prompt based on reasoning")
    print("3. Enhance the prompt with additional technical and artistic details")
    print("\nThis demonstrates DSPy's Chain of Thought reasoning concept!")
    
    return enhancement_result

if __name__ == "__main__":
    if not API_KEY:
        print("Error: OPENROUTER_API_KEY not found in /home/zazikant/.env")
    else:
        result = demonstrate_chain_of_thought()
        print(f"\nFinal enhanced prompt: {result}")