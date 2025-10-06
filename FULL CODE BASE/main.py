import os
import logging
from dotenv import load_dotenv
import requests
import json

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# API configuration for GLM-4.5-Air
API_KEY = os.getenv("OPENROUTER_API_KEY") or ""
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Function to process with GLM-4.5-Air API
def process_with_api(prompt):
    """Process with GLM-4.5-Air API and return the response"""
    # Prepare the API request
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
        "stream": False
    }

    # Make the API call
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))

    # Process and return the response
    if response.status_code == 200:
        response_data = response.json()
        if 'choices' in response_data and len(response_data['choices']) > 0:
            content = response_data['choices'][0]['message']['content']
            return content
        else:
            return "Error: No content in response"
    else:
        return f"Error: {response.status_code}\n{response.text}"

def generate_prompt(taste, user_input):
    """Generate a prompt using GLM-4.5-Air"""
    prompt_template = f"""
    You are an expert at creating detailed image generation prompts. 
    Based on the user's input of "{user_input}" and their preferred style of "{taste}", 
    generate a highly detailed prompt that would work well with image generation AI.
    
    Guidelines:
    1. Incorporate elements that enhance the "{taste}" style
    2. Add relevant details, textures, and atmosphere
    3. Include appropriate camera/technical specifications if applicable
    4. Keep the prompt concise but descriptive
    
    Return only the optimized prompt without any additional explanation:
    """
    
    return process_with_api(prompt_template)

def main():
    """Main function to demonstrate the prompt generation system."""
    # Check if API key is set
    api_key = os.getenv("OPENROUTER_API_KEY") or ""
    if not api_key:
        print("Error: API key not found. Please set your OPENROUTER_API_KEY environment variable.")
        return
    
    # Example usage
    examples = [
        {
            "taste": "anime",
            "user_input": "a dragon flying over a castle"
        },
        {
            "taste": "photorealistic",
            "user_input": "a sunset over mountains"
        },
        {
            "taste": "oil painting",
            "user_input": "a portrait of an old man"
        },
        {
            "taste": "cyberpunk",
            "user_input": "a futuristic city street at night"
        },
        {
            "taste": "watercolor",
            "user_input": "a field of wildflowers"
        },
        {
            "taste": "3d render",
            "user_input": "a futuristic spaceship"
        }
    ]
    
    print("=== GLM-4.5-Air Image Prompt Optimization System ===\n")
    
    for i, example in enumerate(examples, 1):
        print(f"Example {i}:")
        print(f"Taste: {example['taste']}")
        print(f"User Input: {example['user_input']}")
        
        # Generate the prompt using GLM-4.5-Air
        result = generate_prompt(
            taste=example['taste'],
            user_input=example['user_input']
        )
        
        print(f"Generated Prompt: {result}\n")

if __name__ == "__main__":
    main()