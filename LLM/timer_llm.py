from LLM.abstract_llm import LLM
from utils.settings.llm_settings import HISTORY_LENGTH
from typing import List, Dict


class TIMER_LLM(LLM):

    def __init__(self):
        super().__init__()

    def process(self, *args, **kwargs):
        speech = kwargs.get("speech", "")
        if not speech:
            return

        prompt = self.format_prompt(speech)
        response = self.ask(prompt, max_tokens=100)
        response_json = self.to_json(response)
        return response_json

    def format_prompt(self, prompt: str = ""):
        formatted_prompt = f"""
                Du bekommst die Aufgabe, aus dem gegebenen Text Informationen für einen Timer zu extrahieren. Deine Antwort soll in einem Json Format sein.

                Beispiel Timer Text: "Stell einen Timer auf 10 Minuten"
                Beispiel Antwort: {{ "id": "", "duration": "600", "time_text": "10 Minuten" }}

                Beispiel Timer Text: "Stell einen Eier-Timer auf 7 Minuten und 30 Sekunden"
                Beispiel Antwort: {{ "id": "Eier", "duration": "450", "time_text": "7 Minuten und 30 Sekunden" }}

                Timer Text: "{prompt}"
                Antwort: 
        """
        return formatted_prompt
