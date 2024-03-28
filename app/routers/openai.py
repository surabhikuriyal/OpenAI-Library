from fastapi import APIRouter, HTTPException
import openai

router = APIRouter()

@router.post("/completions/openai")
async def create_completion_openai(prompt: str, max_tokens: int, temperature: float, top_p: float):
    try:
        openai.api_key = 'your_openai_api_key'
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
        )
        return {"text": response.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
