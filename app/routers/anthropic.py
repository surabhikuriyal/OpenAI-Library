from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()

@router.post("/completions/anthropic")
async def create_completion_anthropic(prompt: str, max_tokens: int, temperature: float, top_p: float):
    try:
        # Replace with actual Anthropic API endpoint and parameters
        url = "https://api.anthropic.com/v1/completions/anthropic"
        headers = {"Authorization": "Bearer your_anthropic_api_key"}
        data = {
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
