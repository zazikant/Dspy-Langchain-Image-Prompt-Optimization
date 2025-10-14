# Adding New Taste Categories to the Prompt Optimization System

This guide explains how to add new taste categories (like "comedy", "vintage", "minimalist", etc.) to the DSPy-powered prompt optimization system.

## Overview

The system uses taste categories to guide how user inputs are transformed into optimized image generation prompts. Adding a new taste category requires updating training data, validation logic, and documentation across multiple files.

---

## Quick Start: 4-Step Process

### 1. **Update Validation** (`utils.py`)
Add your new taste to the validation list:

```python
# In utils.py, line 7
valid_tastes = [
    'photorealistic', 
    'oil painting', 
    'anime', 
    'cyberpunk', 
    'watercolor', 
    '3d render',
    'comedy'  # ← Add your new taste here
]
```

### 2. **Add Training Examples** (`dspy_module.py`)
Teach the model about your new taste by adding training examples:

```python
# In dspy_module.py, add to the training_data list (lines 19-74)
{
    'taste': 'comedy',
    'user_input': 'a funny cat trying to catch a laser pointer',
    'optimized_prompt': 'Humorous cartoon illustration of a determined ginger cat chasing a red laser dot, exaggerated facial expressions, comedic timing, vibrant colors, playful atmosphere, detailed fur texture'
},
{
    'taste': 'comedy',
    'user_input': 'a person slipping on a banana peel',
    'optimized_prompt': 'Classic comedy scene of a person slipping on a banana peel, slapstick style, exaggerated fall motion, surprised expression, comedic timing, cartoonish proportions, vibrant colors'
}
```

### 3. **Update Demo Examples** (`main.py`)
Add demonstration examples for users:

```python
# In main.py, add to the examples list (lines 81-106)
{
    "taste": "comedy",
    "user_input": "a penguin telling jokes at a comedy club"
}
```

### 4. **Update Documentation**
Update user-facing documentation files to include your new taste category.

---

## Detailed File Breakdown

### Mandatory Files (Must Update)

#### 1. **`utils.py`** - Validation Logic
**Location:** Line 7  
**Purpose:** Validates that taste categories are recognized by the system  
**What to change:**
```python
valid_tastes = ['photorealistic', 'oil painting', 'anime', 'cyberpunk', 'watercolor', '3d render', 'comedy']
```

#### 2. **`dspy_module.py`** - Training Data
**Location:** Lines 19-74 (inside `create_training_examples()` function)  
**Purpose:** Provides training examples that teach the DSPy model how to generate prompts for your taste  
**What to change:** Add 2-3 high-quality examples showing input → optimized prompt transformation

**Example:**
```python
{
    'taste': 'comedy',
    'user_input': 'a clumsy waiter dropping a tray of food',
    'optimized_prompt': 'Humorous cartoon illustration of a clumsy waiter dropping a tray of food, slapstick comedy style, exaggerated facial expressions, flying food items, comedic timing, vibrant colors, detailed restaurant background'
}
```

#### 3. **`main.py`** - Demonstration Code
**Location:** Lines 81-106 (inside `main()` function)  
**Purpose:** Shows users how the system works with example taste categories  
**What to change:** Add at least one example to the `examples` list

```python
examples = [
    {
        "taste": "photorealistic",
        "user_input": "a sunset over mountains"
    },
    {
        "taste": "comedy",  # ← Your new taste
        "user_input": "a penguin telling jokes at a comedy club"
    }
]
```

---

### Optional Files (Recommended Updates)

#### 4. **`HOW TO USE.md`** - User Documentation
**Location:** Lines 6-31  
**Purpose:** Teaches users how to use the system  
**What to change:** Add your new taste to the usage examples

#### 5. **`README.md`** - Project Documentation
**Location:** Lines 44-58  
**Purpose:** Main project documentation  
**What to change:** Update usage examples to include your new taste

#### 6. **`langchain_chains.py`** - LangChain Template (Optional)
**Location:** Lines 13-30  
**Purpose:** Enhances prompts using LangChain  
**What to change:** Add taste-specific guidance if needed

```python
template="""
You are an expert at refining image generation prompts for {taste} style.

Base prompt: {optimized_prompt}

Enhance this prompt with:
- Technical details (resolution, camera angles, focal length)
- Mood and atmosphere
- Artistic techniques and references
- Lighting and color palette specifics
- For comedy: add humor elements, exaggerated expressions, comedic timing  # ← Add specific guidance

Enhanced prompt:
"""
```

---

## Example: Adding "Comedy" Taste

Here's a complete example of adding a "comedy" taste category:

### Step 1: Update `utils.py`
```python
valid_tastes = ['photorealistic', 'oil painting', 'anime', 'cyberpunk', 'watercolor', '3d render', 'comedy']
```

### Step 2: Update `dspy_module.py`
```python
training_data = [
    # ... existing examples ...
    {
        'taste': 'comedy',
        'user_input': 'a funny cat trying to catch a laser pointer',
        'optimized_prompt': 'Humorous cartoon illustration of a determined ginger cat chasing a red laser dot, exaggerated facial expressions, comedic timing, vibrant colors, playful atmosphere, detailed fur texture'
    },
    {
        'taste': 'comedy',
        'user_input': 'a person slipping on a banana peel',
        'optimized_prompt': 'Classic comedy scene of a person slipping on a banana peel, slapstick style, exaggerated fall motion, surprised expression, comedic timing, cartoonish proportions, vibrant colors'
    },
    {
        'taste': 'comedy',
        'user_input': 'a clumsy waiter dropping a tray of food',
        'optimized_prompt': 'Humorous cartoon illustration of a clumsy waiter dropping a tray of food, slapstick comedy style, exaggerated facial expressions, flying food items, comedic timing, vibrant colors, detailed restaurant background'
    }
]
```

### Step 3: Update `main.py`
```python
examples = [
    {
        "taste": "photorealistic",
        "user_input": "a sunset over mountains"
    },
    {
        "taste": "comedy",
        "user_input": "a penguin telling jokes at a comedy club"
    }
]
```

### Step 4: Test Your Changes
```python
from prompt_generator import PromptGenerator

generator = PromptGenerator()
result = generator.generate(
    taste="comedy",
    user_input="a penguin telling jokes at a comedy club"
)

print(result['optimized_prompt'])
```

---

## Writing Good Training Examples

### Structure
Each training example needs three components:
```python
{
    'taste': 'comedy',              # The taste category
    'user_input': 'simple input',   # Basic user description
    'optimized_prompt': 'detailed, style-specific, enhanced prompt with technical details'
}
```

### Tips for Quality Examples

1. **Be Specific:** Include style-specific terminology
   - ❌ "a funny cat"
   - ✅ "Humorous cartoon illustration of a cat, exaggerated expressions, comedic timing"

2. **Add Technical Details:** Include rendering, lighting, composition details
   - Colors, textures, atmosphere
   - Camera angles, focal length (for photorealistic)
   - Artistic techniques (for painting styles)

3. **Show Progression:** Demonstrate simple → detailed transformation
   - User input: "a sunset"
   - Optimized: "Breathtaking photorealistic sunset over mountain range, golden hour lighting, dramatic cloud formations, 8K resolution, wide-angle lens, vibrant orange and purple hues"

4. **Maintain Consistency:** All examples for a taste should follow similar enhancement patterns

---

## File Dependency Chart

```
utils.py (validation)
    ↓
dspy_module.py (training data)
    ↓
prompt_generator.py (uses trained model)
    ↓
main.py (demonstrates usage)
    ↓
Documentation files (HOW TO USE.md, README.md)
```

---

## Checklist for Adding a New Taste

- [ ] Add taste to `valid_tastes` in `utils.py`
- [ ] Add 2-3 training examples in `dspy_module.py`
- [ ] Add demonstration example in `main.py`
- [ ] Update `HOW TO USE.md` with new examples
- [ ] Update `README.md` with new taste in usage examples
- [ ] (Optional) Add taste-specific guidance in `langchain_chains.py`
- [ ] Test the new taste category works correctly
- [ ] Verify validation accepts the new taste
- [ ] Check that generated prompts match the expected style

---

## Common Pitfalls

1. **Forgetting Validation:** If you don't add the taste to `valid_tastes`, the system will reject it
2. **Insufficient Training Examples:** Add at least 2-3 examples to give the model enough context
3. **Inconsistent Style:** Make sure all examples for a taste follow similar patterns
4. **Missing Documentation:** Users won't know about new tastes if you don't document them

---

## Testing Your Changes

After adding a new taste category, test it thoroughly:

```python
from prompt_generator import PromptGenerator

generator = PromptGenerator()

# Test your new taste
result = generator.generate(
    taste="comedy",
    user_input="a dog wearing sunglasses"
)

print("Optimized Prompt:", result['optimized_prompt'])
print("LangChain Enhanced:", result['langchain_prompt'])
```

Expected output should include style-specific enhancements matching your training examples.

---

## Questions or Issues?

If you encounter problems adding a new taste category:
1. Verify all 4 mandatory files are updated
2. Check that training examples follow the correct format
3. Ensure the taste name is consistent across all files
4. Test with simple examples first before complex ones

---

## Summary

**Minimum required updates:**
1. `utils.py` - Add to validation list
2. `dspy_module.py` - Add training examples (2-3 minimum)
3. `main.py` - Add demonstration example
4. Documentation files - Update user guides

**Time estimate:** 10-15 minutes per new taste category

**Key principle:** The quality of your training examples directly impacts the quality of generated prompts for that taste.