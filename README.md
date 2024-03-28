This applicationb uses Python and FastAPI to create LLM router that will support OpenAI, Anthropic and Anyscale.

Folder structure:
app/main.py -> entry point for the aplication
app/__init__.py -> initializes the FastAPI application and includes routers
app/routers/openai.py -> router for openAI
app/routers/anthropic.py -> router for Anthropic
app/routers/anyscale.py -> router for Anyscale
app/dependencies.py -> we can add shared dependencies or utility functions in this file

To run the app uvicorn server is used, in the terminal run command : python -m app.main

API endpoints for the models for POST method:
/completions/openai
/completions/anthropic
/completions/anyscale

Request body :
{
 "prompt": "What is the capital of France?",
 "max_tokens": 50,
 "temperature": 0.7,
 "top_p": 1
}

Response body:
{
 "text": "The capital of France is Paris."
}
