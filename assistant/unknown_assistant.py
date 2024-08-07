from assistant.abstract_assistant import AbstractAssistant
from typing import Optional


class UnknownAssistant(AbstractAssistant):

    def __init__(self):
        super().__init__()
        self.assistant_id = "Unknown"

    def respond(self, speech: Optional[str] = "") -> None:
        self.say(
            "Ich konnte dich leider nicht verstehen. Bitter versuche es später erneut."
        )
