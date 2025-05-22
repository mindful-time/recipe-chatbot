# Recipe Chatbot


> 📝 **Note:** This project serves as a foundation for ongoing development throughout the AI Evals course. We will be incrementally adding features and refining its capabilities in subsequent lessons and homework assignments.

This project provides a starting point for building and evaluating an AI-powered Recipe Chatbot. You will be working with a web application that uses FastAPI for the backend and a simple HTML/CSS/JavaScript frontend. The core of the chatbot involves interacting with a Large Language Model (LLM) via LiteLLM to get recipe recommendations.

Your main tasks will be to refine the chatbot's persona and intelligence by crafting a detailed system prompt, expanding its test query dataset, and evaluating its performance.

![Recipe Chatbot UI](./screenshots/hw1.png)

## System Prompt Enhancements

The system prompt, located in `prompts/sys.yaml` and loaded by `backend/utils.py`, has been significantly enhanced to guide the LLM's behavior more precisely. Key improvements include:

*   **Detailed Persona Definition**: The bot is established as an "expert chef."
*   **Clear Objectives with Specific Criteria**:
    *   **"Deliciousness"**: Defined by flavor balance, texture, proper cooking, and general appeal.
    *   **"Usefulness"**: Defined by practicality, ingredient efficiency, dietary adaptability, teaching techniques, and scalability.
*   **Strict Operational Rules**:
    *   **Phased Recipe Presentation**: Initially offers 3 brief options, then provides a full recipe upon user selection.
    *   **Structured Information Gathering**: Prioritizes safety (allergies first), then ingredients, then time/skill.
    *   **Handling of Vague Requests**: Provides a strategy for clarifying ambiguous user input.
    *   **Detailed Recipe Content**: Mandates inclusion of cooking times, temperatures, technique explanations, visual cues, and common pitfalls.
*   **Advanced Adaptive Behavior**:
    *   The prompt includes an "Adaptive Rule" allowing the bot to bypass standard information gathering if the user's initial query is sufficiently detailed or specific.
    *   This includes identifying "Complete Information Markers" and "Highly Specific Request Detection" to adjust its flow.
    *   A crucial **Safety Override** ensures allergy questions are always asked if not volunteered.
    *   Recipe quantity is flexible (1 to 3 options) based on context, avoiding forced or irrelevant suggestions.
*   **Prescribed Markdown Formatting**:
    *   Extensive examples and rules dictate the exact Markdown structure for all types of responses: initial questions, recipe options, full recipes, and error messages. This ensures consistency and readability.
    *   Specific heading levels (H1, H2, H3), emphasis, and time formats are enforced.
*   **Modular Prompt Management**: The system prompt has been moved from being hardcoded in Python (`backend/utils.py`) to a dedicated YAML file (`prompts/sys.yaml`). This separation enhances modularity and supports CI/CD workflows by allowing automated evaluations or processes to be triggered specifically upon prompt modifications, independent of code changes.

These enhancements aim to create a more intelligent, safe, helpful, and consistently formatted recipe assistant.
![Recipe Chatbot User Interaction Screenshot 1](./screenshots/1.png)
![Recipe Chatbot User Interaction Screenshot 2](./screenshots/2.png)
![Recipe Chatbot User Interaction Screenshot 3](./screenshots/3.png)
![Recipe Chatbot User Interaction Screenshot 4](./screenshots/4.png)
![Recipe Chatbot User Interaction Screenshot 5](./screenshots/5.png)
![Recipe Chatbot User Interaction Screenshot 6](./screenshots/6.png)



## Table of Contents

- [Core Components Provided](#core-components-provided)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Provided Application](#running-the-provided-application)
  - [1. Run the Web Application (Frontend and Backend)](#1-run-the-web-application-frontend-and-backend)
  - [2. Run the Bulk Test Script](#2-run-the-bulk-test-script)
- [Homework Assignment 1: Write a Starting Prompt](#homework-assignment-1-write-a-starting-prompt)

## Core Components Provided

This initial setup includes:

*   **Backend (FastAPI)**: Serves the frontend and provides an API endpoint (`/chat`) for the chatbot logic.
*   **Frontend (HTML/CSS/JS)**: A basic, modern chat interface where users can send messages and receive responses.
    *   Renders assistant responses as Markdown.
    *   Includes a typing indicator for better user experience.
*   **LLM Integration (LiteLLM)**: The backend connects to an LLM (configurable via `.env`) to generate recipe advice.
*   **Bulk Testing Script**: A Python script (`scripts/bulk_test.py`) to send multiple predefined queries (from `data/sample_queries.csv`) to the chatbot's core logic and save the responses for evaluation. This script uses `rich` for pretty console output.

## Project Structure

```
recipe-chatbot/
├── backend/
│   ├── __init__.py
│   ├── main.py         # FastAPI application, routes
│   └── utils.py        # LiteLLM wrapper, system prompt, env loading
├── data/
│   └── sample_queries.csv # Sample queries for bulk testing (ID, Query)
├── frontend/
│   └── index.html      # Chat UI (HTML, CSS, JavaScript)
├── results/            # Output folder for bulk_test.py
├── scripts/
│   └── bulk_test.py    # Bulk testing script
├── .env.example        # Example environment file
├── env.example         # Backup env example (can be removed if .env.example is preferred)
├── requirements.txt    # Python dependencies
└── README.md           # This file (Your guide!)
```

## Setup Instructions

1.  **Clone the Repository (if you haven't already)**
    ```bash
    git clone https://github.com/ai-evals-course/recipe-chatbot.git
    cd recipe-chatbot
    ```

2.  **Create and Activate a Python Virtual Environment**
    ```bash
    python -m venv .venv
    ```
    *   On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```
    *   On Windows:
        ```bash
        .venv\Scripts\activate
        ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables (`.env` file)**
    *   Copy the example environment file:
        ```bash
        cp env.example .env
        ```
        (or `cp .env.example .env` if you have that one)
    *   Edit the `.env` file. You will need to:
        1.  Set the `MODEL_NAME` to the specific model you want to use (e.g., `openai/gpt-3.5-turbo`, `anthropic/claude-3-opus-20240229`, `ollama/llama2`).
        2.  Set the **appropriate API key environment variable** for the chosen model provider. 
            Refer to your `env.example` for common API key names like `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, etc. 
            LiteLLM will automatically use these provider-specific keys.

        Example of a configured `.env` file if using an OpenAI model:
        ```env
        MODEL_NAME=openai/gpt-3.5-turbo
        OPENAI_API_KEY=sk-yourActualOpenAIKey...
        ```
        Example for an Anthropic model:
        ```env
        MODEL_NAME=anthropic/claude-3-haiku-20240307
        ANTHROPIC_API_KEY=sk-ant-yourActualAnthropicKey...
        ```

    *   **Important - Model Naming and API Keys with LiteLLM**:
        LiteLLM supports a wide array of model providers. To use a model from a specific provider, you generally need to:
        *   **Prefix the `MODEL_NAME`** correctly (e.g., `openai/`, `anthropic/`, `mistral/`, `ollama/`).
        *   **Set the corresponding API key variable** in your `.env` file (e.g., `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `MISTRAL_API_KEY`). Some local models like Ollama might not require an API key.

        Please refer to the official LiteLLM documentation for the correct model prefixes and required environment variables for your chosen provider: [LiteLLM Supported Providers](https://docs.litellm.ai/docs/providers).

## Running the Provided Application

### 1. Run the Web Application (Frontend and Backend)

*   Ensure your virtual environment is activated and your `.env` file is configured.
*   From the project root directory, start the FastAPI server using Uvicorn:
    ```bash
    uvicorn backend.main:app --reload
    ```
*   Open your web browser and navigate to: `http://127.0.0.1:8000`

    You should see the chat interface.


### 2. Run the Bulk Test Script

The bulk test script allows you to evaluate your chatbot's responses to a predefined set of queries. It sends queries from `data/sample_queries.csv` directly to the backend agent logic and saves the responses to the `results/` directory.

*   Ensure your virtual environment is activated and your `.env` file is configured.
*   From the project root directory, run:
    ```bash
    python scripts/bulk_test.py
    ```
*   To use a different CSV file for queries:
    ```bash
    python scripts/bulk_test.py --csv path/to/your/queries.csv
    ```
    The CSV file must have `id` and `query` columns.
*   Check the `results/` folder for a new CSV file containing the IDs, queries, and their corresponding responses. This will be crucial for evaluating your system prompt changes.

---

## Homework Assignment 1: Write a Starting Prompt

Your main task is to get the repo to a starting point for Lesson 2.

1.  **Write an Effective System Prompt**:
    *   Open `backend/utils.py` and locate the `SYSTEM_PROMPT` constant. Currently, it's a naive placeholder.
    *   Replace it with a well-crafted system prompt. Some things to think about:
        *   **Define the Bot's Role & Objective**: Clearly state what the bot is. (e.g., "You are a friendly and creative culinary assistant specializing in suggesting easy-to-follow recipes.")
        *   **Instructions & Response Rules**: Be specific.
            *   What should it *always* do? (e.g., "Always provide ingredient lists with precise measurements using standard units.", "Always include clear, step-by-step instructions.")
            *   What should it *never* do? (e.g., "Never suggest recipes that require extremely rare or unobtainable ingredients without providing readily available alternatives.", "Never use offensive or derogatory language.")
            *   Safety Clause: (e.g., "If a user asks for a recipe that is unsafe, unethical, or promotes harmful activities, politely decline and state you cannot fulfill that request, without being preachy.")
        *   **LLM Agency – How Much Freedom?**:
            *   Define its creativity level. (e.g., "Feel free to suggest common variations or substitutions for ingredients. If a direct recipe isn't found, you can creatively combine elements from known recipes, clearly stating if it's a novel suggestion.")
            *   Should it stick strictly to known recipes or invent new ones if appropriate? (Be explicit).
        *   **Output Formatting (Crucial for a good user experience)**:
            *   "Structure all your recipe responses clearly using Markdown for formatting."
            *   "Begin every recipe response with the recipe name as a Level 2 Heading (e.g., `## Amazing Blueberry Muffins`)."
            *   "Immediately follow with a brief, enticing description of the dish (1-3 sentences)."
            *   "Next, include a section titled `### Ingredients`. List all ingredients using a Markdown unordered list (bullet points)."
            *   "Following ingredients, include a section titled `### Instructions`. Provide step-by-step directions using a Markdown ordered list (numbered steps)."
            *   "Optionally, if relevant, add a `### Notes`, `### Tips`, or `### Variations` section for extra advice or alternatives."
            *   **Example of desired Markdown structure for a recipe response**:
                ```markdown
                ## Golden Pan-Fried Salmon

                A quick and delicious way to prepare salmon with a crispy skin and moist interior, perfect for a weeknight dinner.

                ### Ingredients
                * 2 salmon fillets (approx. 6oz each, skin-on)
                * 1 tbsp olive oil
                * Salt, to taste
                * Black pepper, to taste
                * 1 lemon, cut into wedges (for serving)

                ### Instructions
                1. Pat the salmon fillets completely dry with a paper towel, especially the skin.
                2. Season both sides of the salmon with salt and pepper.
                3. Heat olive oil in a non-stick skillet over medium-high heat until shimmering.
                4. Place salmon fillets skin-side down in the hot pan.
                5. Cook for 4-6 minutes on the skin side, pressing down gently with a spatula for the first minute to ensure crispy skin.
                6. Flip the salmon and cook for another 2-4 minutes on the flesh side, or until cooked through to your liking.
                7. Serve immediately with lemon wedges.

                ### Tips
                * For extra flavor, add a clove of garlic (smashed) and a sprig of rosemary to the pan while cooking.
                * Ensure the pan is hot before adding the salmon for the best sear.
                ```

2.  **Expand and Diversify the Query Dataset**:
    *   Open `data/sample_queries.csv`.
    *   Add at least **10 new, diverse queries** to this file. Ensure each new query has a unique `id` and a corresponding query text.
    *   Your queries should test various aspects of a recipe chatbot. Consider including requests related to:
        *   Specific cuisines (e.g., "Italian pasta dish", "Spicy Thai curry")
        *   Dietary restrictions (e.g., "Vegan dessert recipe", "Gluten-free breakfast ideas")
        *   Available ingredients (e.g., "What can I make with chicken, rice, and broccoli?")
        *   Meal types (e.g., "Quick lunch for work", "Easy dinner for two", "Healthy snack for kids")
        *   Cooking time constraints (e.g., "Recipe under 30 minutes")
        *   Skill levels (e.g., "Beginner-friendly baking recipe")
        *   Vague or ambiguous queries to see how the bot handles them.
    * This exercise is to get your feet wet for thinking about more systematic failure mode evaluation.

3.  **Run the Bulk Test & Evaluate**:
    *   After you have updated the system prompt in `backend/utils.py` and expanded the queries in `data/sample_queries.csv`, run the bulk test script:
        ```bash
        python scripts/bulk_test.py
        ```
    * Make sure a new CSV has been written.
    
Good luck!