from LLM.abstract_llm import LLM


class TODOIST_LLM(LLM):

    def __init__(self, **kwargs):
        super().__init__()

    def process(self, *args, **kwargs):
        speech = kwargs.get("speech", "")
        if not speech:
            return

        project = kwargs.get("project", {})
        if not project:
            return

        prompt = self.format_prompt(speech, project=project)
        response = self.ask(prompt)
        response_json = self.to_json(response)
        return response_json

    def format_prompt(self, prompt: str = "", **kwargs):
        project = kwargs.get("project", {})
        tasks = project.get("active_tasks", {})
        sections = project.get("sections", {})

        formatted_prompt = f"""
                Du bekommst die Aufgabe, aus dem gegebenen Text Informationen für eine Todoist Assistenten zu extrahieren. Dabei gibt es verschiedene Funktionen bei dem Todoist Assistenten: create_task. Deine Antwort soll in einem Json Format sein und verwende keine JSON md markers.

                Die section_id muss die id für den passenden Abschnitt sein. Wenn kein passender Abschnitt existiert schreibe keine section_id rein.

                Beispiel Aufgaben aus beispiel Projekt: {{ 
                    "Kaffee": {{"task_id": "8308098151", "section_id": "Einkaufsliste"}}, 
                    "Zwiebel": {{"task_id": "8308098211", "section_id": "Einkaufsliste" }}, 
                    "Paprika": {{"task_id": "8308098260", "section_id": "Einkaufsliste" }}, 
                    "Spühlmaschine ausräumen": {{"task_id": "8308098235", "section_id": "Haushalt"}}
                    }}
                    
                Beispiel Abschnitte: {{"263357699": "Einkaufsliste", "263358345": "Haushalt"}}

                Beispiel Todoist Text: "Schreibe Karroten auf meine Einkaufsliste"
                Beispiel Antwort: {{ "section_id": "263358345", "function":"create_task", "tasks_content": ["Karroten"]}}

                Beispiel Todoist Text: "Schreibe Brot und Butter auf meine Einkaufsliste"
                Beispiel Antwort: {{ "section_id": "263358345", "function":"create_task", "tasks_content": ["Brot", "Butter"]}}

                Beispiel Todoist Text: "Was steht auf meiner Einkaufsliste"
                Beispiel Antwort: {{ "section_id": "263357699", "function":"list_tasks", "tasks_content": ["Kaffee", "Zwiebel", "Paprika"]}}

                Beispiel Todoist Text: "Erinnere mich daran in der Küche zu Staubsaugen"
                Beispiel Antwort: {{ "section_id": "263358345", "function":"create_task", "tasks_content": ["Staubsaugen in Küche"]}}
                
                Beispiel Todoist Text: "Was muss ich heute im Haushalt erledigen?"
                Beispiel Antwort: {{ "section_id": "263358345", "function":"list_tasks", "tasks_content": ["Spühlmaschine ausräumen"]}}

                Beispiel Todoist Text: "Muss ich heute etwas am Auto machen?"
                Beispiel Antwort: {{ "section_id": "", "function":"list_tasks", "tasks_content": []}}

                Beispiel Todoist Text: "Erinnere mich daran mich für die Linear Algebra Prüfung anzumelden"
                Beispiel Antwort: {{ "section_id": "", "function":"create_task", "tasks_content": ["Anmelden Prüfung Lineare Algebra"]}}                

                Aktuell sind folgende Aufgaben im Project: { tasks }
                Aktuell gibt es folgende Abschnitte: { sections }

                Todoist Text: "{prompt}"
                Antwort: 
        """
        return formatted_prompt
