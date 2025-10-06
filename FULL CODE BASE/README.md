DSPy + LangChain Image Prompt Optimization System
An intelligent image prompt generation system that combines DSPy's optimization capabilities with LangChain's LLM reasoning to transform simple user descriptions into high-quality, detailed prompts for image generation models.

Features
Two-stage AI system with DSPy optimization and LangChain enhancement

Support for multiple artistic styles (photorealistic, oil painting, anime, cyberpunk, watercolor, 3d render)

Continuous learning from user feedback stored in Pandas DataFrames

Transparent data storage using CSV files

Analytics and insights about prompt generation patterns

Automatic model retraining based on high-quality examples

Setup
Install the required dependencies:

pip install -r requirements.txt

Set up your OpenAI API key in a .env file or as an environment variable:

OPENAI_API_KEY=your-openai-api-key-here

Run the main script:

python main.py

System Architecture
Data Flow
User Input (taste + description) → DSPy Module (structured, style-specific) → LangChain LLM Chain (detailed, technically enriched) → Pandas DataFrame Storage → Future Retraining / Analytics

Key Components
DSPy Module: Learns optimal prompt patterns for each artistic taste category

LangChain Chain: Adds contextual reasoning and creative enhancement

Data Manager: Handles all data storage and retrieval operations

Prompt Generator: Orchestrates the entire process from user input to final prompt generation

Usage
from src.prompt_generator import PromptGenerator

# Initialize the prompt generator
generator = PromptGenerator(openai_api_key="your-api-key")

# Generate a prompt
result = generator.generate(
    taste="anime",
    user_input="a dragon flying over a castle"
)
print(result)

# Get analytics
analytics = generator.get_analytics()
print(analytics)

Quality Metrics
The system tracks several quality indicators:

Presence of descriptive terms

Style-specific language

Technical details (lighting, composition, etc.)

Prompt length

User feedback (when available)

Model Retraining
The system automatically collects high-quality examples and can be periodically retrained to improve performance:

# Update the model with recent high-quality examples
generator.update_model()

Analytics
The system provides analytics on:

Distribution of taste categories

Average prompt length by taste

Quality trends over time

Top performing prompts

Notes
The DSPy model uses BootstrapFewShot which requires example-driven compilation, which may take time and API calls on first run.

The system includes error handling and fallback mechanisms for robust operation.

All data is stored in human-readable CSV files for transparency and version control.