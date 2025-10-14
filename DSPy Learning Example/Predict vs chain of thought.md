Below is a concise “cheat-sheet” style answer that shows  
(1) what Chain-of-Thought (CoT) means in DSPy,  
(2) the two lines of code you actually need, and  
(3) a minimal but complete runnable example.

------------------------------------------------
1. One-sentence definition
------------------------------------------------
In DSPy, CoT is **not** a new class—it is just the built-in `ChainOfThought` (alias `CoT`) teleprompter that wraps any `Predict` and **automatically appends**  
“Let’s think step-by-step.” (or a better learned variant) to the prompt, then parses the LM’s reasoning trace and the final answer.

------------------------------------------------
2. The only two lines you need
------------------------------------------------
```python
import dspy

# 1. Declare the signature
class Answer(dspy.Signature):
    question = dspy.InputField()
    answer   = dspy.OutputField()

# 2. Use Chain-of-Thought instead of Predict
cot = dspy.ChainOfThought(Answer)      # or dspy.CoT(Answer)
```

------------------------------------------------
3. End-to-end micro-example
------------------------------------------------
```python
import dspy

lm = dspy.OpenAI(model="gpt-3.5-turbo", max_tokens=250)
dspy.settings.configure(lm=lm)

class Answer(dspy.Signature):
    """Answer factual questions step-by-step."""
    question = dspy.InputField()
    answer   = dspy.OutputField()

cot = dspy.ChainOfThought(Answer)

response = cot(question="How many days does it take for the moon to orbit Earth?")
print("Reasoning:", response.rationale)
print("Answer:", response.answer)
```

Typical console output:

```
Reasoning: The Moon completes one full orbit around the Earth in approximately 27.3 days (sidereal month). However, because the Earth is also moving around the Sun, the synodic month (the cycle of lunar phases) is about 29.5 days.
Answer: ~27.3 days (sidereal) or ~29.5 days (synodic).
```

------------------------------------------------
4. Customising the rationale
------------------------------------------------
You can change the prefix that triggers reasoning:

```python
class CustomCoT(dspy.Signature):
    """Solve math problems."""
    problem  = dspy.InputField()
    solution = dspy.OutputField(desc="final number only")

cot = dspy.ChainOfThought(CustomCoT, rationale_type="justify_each_step")
```

------------------------------------------------
5. Inside a larger pipeline
------------------------------------------------
```python
class MathSolver(dspy.Module):
    def __init__(self):
        super().__init__()
        self.cot = dspy.ChainOfThought("problem -> solution")

    def forward(self, problem):
        return self.cot(problem=problem).solution
```

------------------------------------------------
6. Key points to remember
------------------------------------------------
- `ChainOfThought` is **drop-in** for `Predict`.  
- The rationale is **always** returned in `response.rationale`.  
- No extra parsing code is required—DSPy strips the reasoning for you.
