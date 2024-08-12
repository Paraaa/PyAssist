import datetime
from typing import Optional
from assistant.abstract_assistant import AbstractAssistant


class TodoistAssistant(AbstractAssistant):

    def __init__(self):
        super().__init__()
        self.assistant_id = "Todoist"

    def respond(self, speech: Optional[str] = "") -> None:
        # TODO: implement this
        pass
