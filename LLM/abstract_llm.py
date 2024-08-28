import json
from openai import OpenAI
from env import OPEN_AI_API_KEY
from utils.settings.llm_settings import MODEL
from abc import ABC, abstractmethod
from typing import List, Dict
from utils.logging.logger import LOGGER


class LLM(ABC):

    def __init__(self):
        self.client = OpenAI(api_key=OPEN_AI_API_KEY)  # Initialize the OpenAI client
        self.logger = LOGGER("LLM", "llm/abstract_llm.log")

    def ask(
        self, prompt: str, max_tokens: int = 60, history: List[Dict[str, str]] = []
    ) -> str:
        message = []
        message.append(
            {
                "role": "system",
                "content": "You are an AI assistant that helps people find information.",
            }
        )
        # If the history is not empty
        if history:
            message.extend(history)
        message.append({"role": "user", "content": prompt})
        response = self.client.chat.completions.create(
            model=MODEL,
            messages=message,
            max_tokens=max_tokens,
            temperature=0.7,
            n=1,
        )
        return response.choices[0].message.content

    def to_json(self, response: str) -> Dict:
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            self.logger.exception(f"JSON decoding failed for {response}")
            return {}

    @abstractmethod
    def process(self, *args, **kwargs):
        pass  # Implement this method in subclasses to handle processing of messages

    @abstractmethod
    def format_prompt(self, prompt: str = ""):
        pass  # Implement this method in subclasses format the prompt for the desired function
