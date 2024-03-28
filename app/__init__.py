from fastapi import FastAPI
from .routers import openai, anthropic, anyscale

app = FastAPI()

app.include_router(openai.router, prefix="/openai", tags=["OpenAI"])
app.include_router(anthropic.router, prefix="/anthropic", tags=["Anthropic"])
app.include_router(anyscale.router, prefix="/anyscale", tags=["Anyscale"])
