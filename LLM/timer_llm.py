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
                Du bekommst die Aufgabe, aus dem gegebenen Text Informationen für einen Timer zu extrahieren. Dabei gibt es verschiedene Funktionen bei dem Timer: start_timer, end_timer, time_left. Deine Antwort soll in einem Json Format sein.

                Beispiel Timer Text: "Stell einen Timer auf 10 Minuten"
                Beispiel Antwort: {{ "id": "", function:"start_timer", "duration": "600", "time_text": "10 Minuten"}}

                Beispiel Timer Text: "Stell einen Eier-Timer auf 7 Minuten und 30 Sekunden"
                Beispiel Antwort: {{ "id": "Eier", function:"start_timer", "duration": "450", "time_text": "7 Minuten und 30 Sekunden"}}

                Beispiel Timer Text: "Beende den Eier-Timer"
                Beispiel Antwort: {{ "id": "Eier", function:"end_timer"}}

                Beispiel Timer Text: "Beende den zweiten Timer"
                Beispiel Antwort: {{ "id": "2", function:"end_timer"}}

                Beispiel Timer Text: "Wie lange geht der Eier-Timer?"
                Beispiel Antwort: {{ "id": "Eier", function:"time_left"}}

                Beispiel Timer Text: "Wie lange geht der erste Timer?"
                Beispiel Antwort: {{ "id": "1", function:"time_left"}}

                Timer Text: "{prompt}"
                Antwort: 
        """
        return formatted_prompt
