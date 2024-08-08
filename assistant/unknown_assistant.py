from assistant.abstract_assistant import AbstractAssistant
from typing import Optional


class UnknownAssistant(AbstractAssistant):

    def __init__(self) -> None:
        super().__init__()
        self.assistant_id = "Unknown"

    def respond(self, speech: Optional[str] = "") -> None:
        self.say(
            "Ich konnte dich leider nicht verstehen. Bitte versuche es später erneut."
        )
