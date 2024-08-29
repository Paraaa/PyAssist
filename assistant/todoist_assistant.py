import logging
from typing import Optional
from assistant.abstract_assistant import AbstractAssistant
from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Project, Task
from env import TODOIST_API_KEY
from utils.settings.todoist_settings import PROJECT_ID
from utils.settings.default_messages_settings import DEFAULT_RESPONSES
from typing import List, Dict, Union
from LLM.todoist_llm import TODOIST_LLM

logger = logging.getLogger("TodoistAssistant")


class TodoistAssistant(AbstractAssistant):

    def __init__(self):
        super().__init__()
        self.assistant_id = "Todoist"
        self.todoist_api = TodoistAPI(TODOIST_API_KEY)
        self.todoist_llm = TODOIST_LLM()

    def respond(self, speech: Optional[str] = "") -> None:
        if not speech:
            return
        project = self.get_project()
        response = self.todoist_llm.process(speech=speech, project=project)
        if not response:
            return
        function = response.get("function", None)
        match function:
            case "create_task":
                self.create_task(response)
                logger.debug("create_task")
            case "list_tasks":
                self.list_tasks(response)
                logger.debug("list_tasks")
            case _:
                self.say(DEFAULT_RESPONSES.get("ERROR", ""))
                logger.error("Could not determine the task")

    def create_task(self, response: Dict[str, str]):
        # If the section_id is an empty string set it to None
        section_id = response.get("section_id", "") or None
        tasks_content = response.get("tasks_content", [])
        try:
            for task_content in tasks_content:
                self.todoist_api.add_task(
                    task_content, project_id=PROJECT_ID, section_id=section_id
                )
                logger.info(f"Task '{task_content}' created successfully")
                self.say(f"Die Aufgabe '{task_content}' wurde erstellt.")
        except Exception as e:
            logger.exception(f"Error creating task: {str(e)}")
            self.say(DEFAULT_RESPONSES.get("ERROR", ""))

    def list_tasks(self, response: Dict[str, str]):
        tasks_content = response.get("tasks_content", [])
        if not tasks_content:
            logger.debug("No tasks found")
            self.say(f"Du hast keine passenden aktiven Aufgaben")

        self.say(f"Auf deine Lister stehen folgende Aufgaben")
        for task in tasks_content:
            self.say(f"{task}")

    def get_project(self) -> Dict[str, Union[Project, Task]]:
        # This is done to filter out the unnecessary information for the llm
        sections = {
            section.id: section.name
            for section in self.todoist_api.get_sections(project_id=PROJECT_ID)
        }
        active_tasks = {
            task.content: {
                "task_id": task.id,
                "section": sections.get(task.section_id, ""),
            }
            for task in self.todoist_api.get_tasks(project_id=PROJECT_ID)
        }
        project = {
            "active_tasks": active_tasks,
            "sections": sections,
        }
        logger.debug(f"Retrieved project data: {project}")
        return project
