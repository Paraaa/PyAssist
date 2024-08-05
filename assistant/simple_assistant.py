from assistant.abstract_assistant import AbstractAssistant
from typing import Optional


class SimpleAssistant(AbstractAssistant):

    def __init__(self):
        super().__init__()
        self.assistant_id = "Simple"

    def respond(self, speech: Optional[str] = "") -> None:
        self.say("Hi ich bin Astra")
