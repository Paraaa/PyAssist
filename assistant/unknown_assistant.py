from assistant.abstract_assistant import AbstractAssistant
from utils.settings.default_messages_settings import DEFAULT_RESPONSES
from typing import Optional


class UnknownAssistant(AbstractAssistant):

    def __init__(self) -> None:
        super().__init__()
        self.assistant_id = "Unknown"

    def respond(self, speech: Optional[str] = "") -> None:
        self.say(DEFAULT_RESPONSES.get("ERROR", ""))
