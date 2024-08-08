from assistant.abstract_assistant import AbstractAssistant
from typing import Optional
from LLM.chat_llm import CHAT_LLM


class SimpleChatAssistant(AbstractAssistant):

    def __init__(self):
        super().__init__()
        self.assistant_id = "SimpleChat"
        self.chat_llm = CHAT_LLM()

    def respond(self, speech: Optional[str] = "") -> None:
        if not speech:
            return
        response = self.chat_llm.process(speech=speech)
        self.say(response)
