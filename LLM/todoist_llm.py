from LLM.abstract_llm import LLM


class TODOIST_LLM(LLM):

    def __init__(self, **kwargs):
        super().__init__()
        self.projects = kwargs.get("projects", {})

    def process(self, *args, **kwargs):
        speech = kwargs.get("speech", "")
        if not speech:
            return "Unknown"
        prompt = self.format_prompt(speech)
        response = self.ask(prompt)
        response_json = self.to_json(response)
        return response_json

    def format_prompt(self, prompt: str = ""):
        formatted_prompt = f"""
                Du bekommst die Aufgabe, aus dem gegebenen Text Informationen für eine Todoist Assistenten zu extrahieren. Dabei gibt es verschiedene Funktionen bei dem Todoist Assistenten: create_task. Deine Antwort soll in einem Json Format sein.

                Beispiel Todoist Text: "Schreibe Karroten auf meine Einkaufsliste"
                Beispiel Antwort: {{ "id": "", "function":"create_task", "task_content": ["Karroten"]}}


                Beispiel Todoist Text: "Schreibe Brot und Butter auf meine Einkaufsliste"
                Beispiel Antwort: {{ "id": "", "function":"create_task", "task_content": ["Brot", "Butter"]}}

                Todoist Text: "{prompt}"
                Antwort: 
        """
        return formatted_prompt
