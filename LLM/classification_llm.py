from LLM.abstract_llm import LLM
from utils.settings.assistant_settings import ASSISTANTS


class CLASSIFICATION_LLM(LLM):

    def __init__(self):
        super().__init__()
        self.assistants = ", ".join(
            list(ASSISTANTS.keys())
        )  # Get all available assistants

    def process(self, *args, **kwargs):
        speech = kwargs.get("speech", "")
        if not speech:
            return "Unknown"
        prompt = self.format_prompt(speech)
        assistant = self.ask(prompt)
        if not assistant in self.assistants:
            return "Unknown"
        return assistant

    def format_prompt(self, prompt: str = ""):
        formatted_prompt = f"""
                Du bekommst eine Frage. Deine Antwort soll die Frage eine der folgenden Klassen zuordnen: {self.assistants}.
                Beispiel Frage: "Wie spät ist es gerade?"
                Beispiel Antwort: Time
                Frage: "{prompt}"
                Antwort: """
        return formatted_prompt
