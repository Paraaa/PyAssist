from LLM.abstract_llm import LLM
from utils.settings.llm_settings import HISTORY_LENGTH
from typing import List, Dict


class CHAT_LLM(LLM):

    def __init__(self):
        super().__init__()
        self.history: List[Dict[str, str]] = []

    def process(self, *args, **kwargs):
        speech = kwargs.get("speech", "")
        if not speech:
            return

        prompt = self.format_prompt(speech)
        response = self.ask(prompt, max_tokens=100, history=self.history)

        self.history.append({"role": "user", "content": prompt})
        self.history.append({"role": "assistant", "content": response})

        # Remove oldest history items if the length exceeds the limit
        while len(self.history) > HISTORY_LENGTH:
            self.history.pop(0)

        return response

    def format_prompt(self, prompt: str = ""):
        return prompt
