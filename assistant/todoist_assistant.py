from typing import Optional
from assistant.abstract_assistant import AbstractAssistant
from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Project
from utils.env import TODOIST_API_KEY
from utils.settings.todoist_settings import EXCLUDE_PROJECTS
from utils.settings.default_messages_settings import DEFAULT_RESPONSES
from typing import List, Dict
from LLM.todoist_llm import TODOIST_LLM


class TodoistAssistant(AbstractAssistant):

    def __init__(self):
        super().__init__()
        self.assistant_id = "Todoist"
        self.todoist_api = TodoistAPI(TODOIST_API_KEY)
        self.projects: Dict[str, Project] = self._setup_projects()
        self.todoist_llm = TODOIST_LLM(projects=self.projects)

    def _setup_projects(self):
        projects = {}
        projects_api = self.todoist_api.get_projects()
        for project in projects_api:
            project_id = project.id
            if project_id in EXCLUDE_PROJECTS:
                continue
            projects[project_id] = project
        return projects

    def respond(self, speech: Optional[str] = "") -> None:
        if not speech:
            return
        response = self.todoist_llm.process(speech=speech)
        if not response:
            return
        task = response.get("function", None)
        match task:
            case "create_task":
                # TODO: Implement this
                pass
            case "complete_task":
                # TODO: Implement this
                pass
            case "delete_task":
                # TODO: Implement this
                pass
            case "list_tasks":
                # TODO: Implement this
                pass
            case _:
                self.say(DEFAULT_RESPONSES.get("ERROR", ""))

        print(response)
