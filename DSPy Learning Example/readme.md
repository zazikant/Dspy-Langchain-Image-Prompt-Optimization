python model.py
2025-10-14 06:04:46,160 - __main__ - INFO - Initialized OpenRouter LLM with model: z-ai/glm-4.5-air:free, temperature: 0.7
2025-10-14 06:04:46,160 - __main__ - INFO - Creating QA chain with DSPy optimization
2025-10-14 06:04:46,160 - __main__ - INFO - Setting up DSPy with model: z-ai/glm-4.5-air:free
2025-10-14 06:04:46,161 - __main__ - INFO - DSPy setup completed successfully
2025-10-14 06:04:46,161 - __main__ - INFO - QA chain created successfully
2025-10-14 06:04:46,161 - __main__ - INFO - Creating summarization chain with DSPy optimization
2025-10-14 06:04:46,161 - __main__ - INFO - Setting up DSPy with model: z-ai/glm-4.5-air:free
2025-10-14 06:04:46,161 - __main__ - INFO - DSPy setup completed successfully
2025-10-14 06:04:46,161 - __main__ - INFO - Summarization chain created successfully
2025-10-14 06:04:46,161 - __main__ - INFO - Using 3 examples for DSPy optimization
🚀 Testing Model Implementation
========================================
✅ LLM initialized with model: z-ai/glm-4.5-air:free
✅ QA chain created successfully
✅ Summarization chain created successfully

🔍 Testing QA: What is the capital of Japan?
100%|██████████| 3/3 [00:00<00:00, 19.76it/s]
2025-10-14 06:04:46,323 - __main__ - INFO - Using 2 examples for DSPy optimization
Bootstrapped 3 full traces after 2 examples for up to 1 rounds, amounting to 3 attempts.
Answer: Prediction(
    reasoning="The capital of Japan is Tokyo. Tokyo has been the capital of Japan since 1868, when the imperial residence was moved from Kyoto to Edo (which was then renamed Tokyo). Tokyo is the largest city in Japan and serves as the country's political, economic, and cultural center.",
    answer='Tokyo'
)

📝 Testing Summarization:
100%|██████████| 2/2 [00:00<00:00, 317.41it/s]
Bootstrapped 2 full traces after 1 examples for up to 1 rounds, amounting to 2 attempts.
Summary: Prediction(
    reasoning="The text discusses the transformative impact of artificial intelligence on daily life and work. It provides specific examples of AI applications (self-driving cars, virtual assistants) and notes the increasing integration of AI into everyday experiences. I will summarize these key points concisely while maintaining the core message about AI's growing influence.",
    summary='Artificial intelligence is transforming daily life and work through applications like self-driving cars and virtual assistants, with increasing integration into everyday experiences.'
)

✅ Model implementation test completed successfully!


I'll break down the output step by step to explain what happened when the script ran:

Step 1: Initialization Phase
2025-10-14 06:04:46,160 - __main__ - INFO - Initialized OpenRouter LLM with model: z-ai/glm-4.5-air:free, temperature: 0.7
The script started by initializing an OpenRouter LLM (Language Model)
It used the model z-ai/glm-4.5-air:free (a free tier model)
Temperature was set to 0.7 (controls randomness - higher = more creative, lower = more focused)
Step 2: DSPy Setup
2025-10-14 06:04:46,160 - __main__ - INFO - Creating QA chain with DSPy optimization
2025-10-14 06:04:46,160 - __main__ - INFO - Setting up DSPy with model: z-ai/glm-4.5-air:free
2025-10-14 06:04:46,161 - __main__ - INFO - DSPy setup completed successfully
DSPy is a framework for programming with language models
It created a Question-Answering (QA) chain with optimization
Successfully configured DSPy to work with the OpenRouter model
Step 3: Summarization Chain Setup
2025-10-14 06:04:46,161 - __main__ - INFO - Creating summarization chain with DSPy optimization
2025-10-14 06:04:46,161 - __main__ - INFO - DSPy setup completed successfully
Created a text summarization chain also with DSPy optimization
This chain will be used to create concise summaries of longer texts
Step 4: Testing Phase
🚀 Testing Model Implementation
========================================
✅ LLM initialized with model: z-ai/glm-4.5-air:free
✅ QA chain created successfully
✅ Summarization chain created successfully
The script began its testing phase
All components were successfully initialized and ready for testing
Step 5: QA Test Execution
🔍 Testing QA: What is the capital of Japan?
100%|██████████| 3/3 [00:00<00:00, 19.76it/s]
2025-10-14 06:04:46,323 - __main__ - INFO - Using 3 examples for DSPy optimization
Bootstrapped 3 full traces after 2 examples for up to 1 rounds, amounting to 3 attempts.
Answer: Prediction(
    reasoning="The capital of Japan is Tokyo. Tokyo has been the capital of Japan since 1868, when the imperial residence was moved from Kyoto to Edo (which was then renamed Tokyo). Tokyo is the largest city in Japan and serves as the country's political, economic, and cultural center.",
    answer='Tokyo'
)
What happened:

Asked: "What is the capital of Japan?"
The system used 3 examples for few-shot learning (training the model on similar questions/answers)
DSPy "bootstrapped" 3 full traces (meaning it tried 3 different approaches to find the best answer)
The model correctly answered "Tokyo" with detailed reasoning about Tokyo's history and significance
Step 6: Summarization Test Execution
📝 Testing Summarization:
100%|██████████| 2/2 [00:00<00:00, 317.41it/s]
2025-10-14 06:04:46,323 - __main__ - INFO - Using 2 examples for DSPy optimization
Bootstrapped 2 full traces after 1 examples for up to 1 rounds, amounting to 2 attempts.
Summary: Prediction(
    reasoning="The text discusses the transformative impact of artificial intelligence on daily life and work. It provides specific examples of AI applications (self-driving cars, virtual assistants) and notes the increasing integration of AI into everyday experiences. I will summarize these key points concisely while maintaining the core message about AI's growing influence.",
    summary='Artificial intelligence is transforming daily life and work through applications like self-driving cars and virtual assistants, with increasing integration into everyday experiences.'
)
What happened:

The system was given a text about AI transforming daily life
It used 2 examples for few-shot learning to learn how to summarize
DSPy tried 2 different approaches to create the best summary
The result was a concise summary that captured the main points about AI's impact
Final Result
✅ Model implementation test completed successfully!
All tests passed successfully
The DSPy-LangChain integration is working properly
Both QA and summarization functions are operational
In simple terms: The script successfully tested a smart AI system that can answer questions and summarize text. It used a technique called "few-shot learning" where it learned from examples to improve its performance, and it worked perfectly for both question answering and text summarization tasks.
