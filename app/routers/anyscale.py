from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()

@router.post("/completions/anyscale")
async def create_completion_anyscale(prompt: str, max_tokens: int, temperature: float, top_p: float):
    try:
        # Replace with actual Anyscale API endpoint and parameters
        url = "https://api.anyscale.com/v1/completions/anyscale"
        headers = {"Authorization": "Bearer your_anyscale_api_key"}
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
