from assistant.abstract_assistant import AbstractAssistant
from typing import Optional


class SimpleChatAssistant(AbstractAssistant):

    def __init__(self):
        super().__init__()
        self.assistant_id = "SimpleChat"

    def respond(self, speech: Optional[str] = "") -> None:
        if not speech:
            return
        self.say("Hi ich bin Astra")
