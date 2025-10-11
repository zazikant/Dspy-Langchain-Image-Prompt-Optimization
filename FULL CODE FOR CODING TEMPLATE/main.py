import os
import logging
import requests
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# API configuration for GLM-4.5-Air with hardcoded API key
API_KEY = ""
API_URL = "https://openrouter.ai/api/v1/chat/completions "

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
        "stream": False,
        "max_tokens": 4000  # Increase token limit
    }

    try:
        # Make the API call
        response = requests.post(API_URL, headers=headers, data=json.dumps(data), timeout=60)

        # Log the raw response for debugging
        logging.info(f"Response Status: {response.status_code}")

        # Check if response is successful
        if response.status_code == 200:
            try:
                response_data = response.json()
                if 'choices' in response_data and len(response_data['choices']) > 0:
                    content = response_data['choices'][0]['message']['content']
                    return content
                else:
                    logging.error(f"No choices in response: {response_data}")
                    return "Error: No content in response"
            except json.JSONDecodeError as e:
                # Log the raw text response for debugging
                logging.error(f"JSON Decode Error: {e}")
                logging.error(f"Raw response text (first 500 chars): {response.text[:500]}")
                return f"Error: Invalid JSON response from API. Response: {response.text[:200]}..."
        else:
            logging.error(f"API Error: {response.status_code} - {response.text}")
            return f"Error: {response.status_code}\n{response.text}"

    except requests.exceptions.Timeout:
        return "Error: API request timeout. The prompt might be too long."
    except requests.exceptions.RequestException as e:
        logging.error(f"Request Exception: {e}")
        return f"Error: Request failed - {str(e)}"

def generate_prompt(taste, user_input):
    """Generate a coherent full-stack coding project prompt using GLM-4.5-Air"""
    prompt_template = f"""You are an expert full-stack architect. Transform this project idea into a coherent, actionable technical specification.

**Input**:
- Project Idea: "{user_input}"
- Development Approach: "{taste}"

**🔒 CRITICAL OUTPUT MODE**:
Generate ARCHITECTURAL PATTERNS and DECISION FRAMEWORKS, not literal implementation details.

For all conventions (naming, structure, flow), provide:
- The PATTERN with reasoning
- EXAMPLE FORMAT to illustrate the pattern
- IMPLEMENTATION GUIDANCE for applying the pattern

Do NOT specify literal names unless the user explicitly provides them. The goal is TRANSFERABLE ARCHITECTURE that adapts to any domain.

**🔒 ABSOLUTE GROUNDING LAW**:
Once you define ANY PATTERN in Phase 1 (database schema patterns, API structure patterns, naming conventions, data flow patterns, file organization patterns, error handling patterns), that pattern becomes IMMUTABLE LAW for ALL subsequent phases.

EVERY new feature MUST:
- Follow the EXACT PATTERNS from Phase 1 (not literal examples, but the pattern rules)
- Apply patterns contextually to the specific domain
- Reference pattern rules explicitly: "Uses Phase 1 [pattern name]"

**Output Structure**:

**1. Project Understanding** (3-4 sentences)
- What problem are we solving and for whom?
- What is the core user value?
- What defines success for this MVP?

**2. Architecture Decisions**
- Frontend: [Choose technology] - justify based on project needs
- Backend: [Choose technology] - justify based on project needs
- Database: [Choose technology] - justify based on data patterns
- **Naming Philosophy**: [Describe approach - e.g., "verbose self-documenting" vs "terse industry-standard" based on user input]
- **Critical**: Explain how these form a coherent system

**3. 🔒 FOUNDATIONAL PATTERN ANCHORS (Phase 1 - IMMUTABLE LAW)**

**A. DATABASE SCHEMA PATTERN ANCHORS**:

**Table Naming Pattern**:
- Pattern Rule: [Define the pattern structure with placeholders]
- Reasoning: [Why this pattern?]
- Example Format: [Show 2-3 examples illustrating the pattern]
- Implementation Guidance: When creating tables, ask: [decision framework]

**Column Naming Pattern**:
- Pattern Rule: [Define convention]
- Reasoning: [Why this approach?]
- Example Format: [Show examples]

**Primary Key Pattern**:
- Pattern Rule: [Define PK approach]
- Example Format: [Show structure]

**Foreign Key Pattern**:
- Pattern Rule: [Define FK naming]
- Example Format: [Show how to derive FK names]

**Timestamp Pattern**:
- Pattern Rule: [Define timestamp approach]
- Example Format: [Show structure]

**Relationship Pattern**:
- Pattern Rule: [Define how relationships work]
- Example Format: [Show 1:M and M:M examples]

ALL future tables MUST follow these PATTERN RULES. Apply rules to your specific domain - don't copy examples literally.

**B. API PATTERN ANCHORS**:

**Endpoint Structure Pattern**:
- Pattern Rule: [Define URL structure with placeholders]
- Reasoning: [Why this structure?]
- Example Format: [Show pattern applied to sample resources]

**HTTP Method Pattern**:
- Pattern Rule: [Define which verbs for which operations]
- Example Format: [Show the mapping]

**Request/Response Pattern**:
- Pattern Rule: [Define data format structure]
- Example Format: [Show success and error response patterns]

ALL future endpoints MUST follow these PATTERN RULES applied to your domain.

**C. AUTHENTICATION PATTERN ANCHOR**:

**Auth Flow Pattern**:
- Pattern Rule: [Define auth mechanism]
- Reasoning: [Why this approach for this project type?]
- Implementation Guidance: [How to apply to protected routes]

ALL protected features MUST follow this EXACT auth pattern.

**D. DATA ACCESS PATTERN ANCHOR**:

**Layer Structure Pattern**:
- Pattern Rule: [Define layer separation with responsibilities]
- Reasoning: [Why these layers?]
- File Naming Pattern: [Define naming rule with placeholders]
- Example Format: [Show pattern applied to sample feature]

ALL features MUST follow this EXACT layer pattern.

**E. ERROR HANDLING PATTERN ANCHOR**:

**Error Response Pattern**:
- Pattern Rule: [Define error structure]
- Error Code Pattern: [Define code naming convention]
- Example Format: [Show pattern in use]

ALL endpoints MUST follow this EXACT error pattern.

**F. FRONTEND PATTERN ANCHORS**:

**State Management Pattern**:
- Global State Rule: [When/how to use]
- Server State Rule: [When/how to use]
- Local State Rule: [When/how to use]

**Component Pattern**:
- Pattern Rule: [Define component organization]
- File Naming Pattern: [Define naming rule]
- Example Format: [Show pattern applied]

ALL components MUST follow these EXACT patterns.

**4. MVP Feature Set** (3-5 core features)

For EACH feature write:

**Feature: [Name based on domain]**

**Pattern Application** (show how Phase 1 patterns apply):
- 🔒 Database: Applies [Pattern A rules] → In this domain: [show contextual application]
- 🔒 API: Applies [Pattern B rules] → Endpoint: [derive from pattern]
- 🔒 Auth: Applies [Pattern C rules] → [how it's used here]
- 🔒 Data Flow: Applies [Pattern D rules] → [show layers for this feature]
- 🔒 Errors: Applies [Pattern E rules] → [show error handling]
- 🔒 Frontend: Applies [Pattern F rules] → [show state/component usage]

**Complete Data Flow**:
[Show user action through system using the patterns, with domain-specific examples]

**Dependencies**: [What must exist first?]

**5. Implementation Phases**

**Phase 1 - Pattern Foundation**:
- Define ALL pattern anchors (A-F) with reasoning
- Create initial schema applying patterns to domain
- Implement first feature as pattern reference
- **Output**: "Phase 1 establishes these PATTERN RULES: [list patterns, not examples]"

**Phase 2 - Core Features**:
- Feature 1: **PATTERN CHECK** - Uses [Pattern A, B, C...] applied to [domain context]
- Feature 2: **PATTERN CHECK** - Uses [same patterns] applied differently for [context]
- **VALIDATION**: Confirm patterns are reused, not redefined

**Phase 3 - Enhancement**:
- Feature 1: **PATTERN CHECK** - Extends Phase 1-2 patterns to [new context]
- **VALIDATION**: Confirm zero new patterns, only new applications of existing patterns

**6. MVP Scope**
- **IN**: [Essential features] - why essential?
- **OUT**: [Deferred features] - why defer?

**7. 🔒 PATTERN CONSISTENCY CHECKLIST**

Verify pattern reuse (not literal copying):
- [ ] All tables follow Phase 1 naming PATTERN RULE
- [ ] All APIs follow Phase 1 endpoint PATTERN RULE
- [ ] All auth uses Phase 1 flow PATTERN
- [ ] All data access follows Phase 1 layer PATTERN
- [ ] All errors follow Phase 1 response PATTERN
- [ ] All components follow Phase 1 organization PATTERN
- [ ] Phase 2-3 features APPLY patterns to their specific context
- [ ] ZERO new patterns introduced - only new applications

**Meta-Architecture Principle**:
You're defining the "rules of the game," not the specific moves. Patterns should be transferable across similar projects. Implementation details emerge from applying patterns to the specific domain in user input.

Generate the pattern-driven, coherent full-stack architectural specification now:"""

    return process_with_api(prompt_template)

def main():
    """Main function to demonstrate the coding project prompt generation system."""
    # Check if API key is set
    if API_KEY == "sk-or-xxxx" or not API_KEY:
        print("Error: API key not set. Please replace 'sk-or-xxxx' with your actual OpenRouter API key.")
        return

    # Example usage with coding project examples
    examples = [
        {
            "taste": "MVP coding",
            "user_input": "a simple quiz app using next js and tailwind css"
        },
    ]

    print("=== GLM-4.5-Air Coding Project Prompt Generation System ===\n")

    for i, example in enumerate(examples, 1):
        print(f"Example {i}:")
        print(f"Taste: {example['taste']}")
        print(f"User Input: {example['user_input']}")

        # Generate the coding project prompt using GLM-4.5-Air
        result = generate_prompt(
            taste=example['taste'],
            user_input=example['user_input']
        )

        print(f"Generated Prompt:\n{result}\n{'='*50}\n")

if __name__ == "__main__":
    main()