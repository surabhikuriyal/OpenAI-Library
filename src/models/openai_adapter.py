from models import ModelProvider
import openai

class OpenAIAdapter(ModelProvider):
    def set_api_key(self, api_key):
        openai.api_key = api_key

    def create_completion(self, prompt, **kwargs):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            **kwargs
        )
        return response.choices[0].text.strip()
