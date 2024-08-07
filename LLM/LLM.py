from openai import OpenAI
from utils.env import OPEN_AI_API_KEY
from utils.settings.llm_settings import MODEL


class LLM:

    def ask(self, prompt: str, max_tokens: int = 60) -> str:
        message = []
        message.append(
            {
                "role": "system",
                "content": "You are an AI assistant that helps people find information.",
            }
        )
        message.append({"role": "user", "content": prompt})

        client = OpenAI(api_key=OPEN_AI_API_KEY)
        response = client.chat.completions.create(
            model=MODEL,
            messages=message,
            max_tokens=max_tokens,
            temperature=0.7,
            n=1,
        )
        return response.choices[0].message.content
