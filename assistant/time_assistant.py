import datetime
from typing import Optional
from assistant.abstract_assistant import AbstractAssistant


class TimeAssistant(AbstractAssistant):

    def __init__(self):
        super().__init__()
        self.assistant_id = "Time"

    def respond(self, speech: Optional[str] = "") -> None:
        now = datetime.datetime.now()
        time_str = now.strftime("%H:%M")
        response = f"Die aktuelle Uhrzeit is {time_str} "
        self.say(response)
