from assistant.abstract_assistant import AbstractAssistant
from LLM.timer_llm import TIMER_LLM
from typing import Optional, Dict
from threading import Timer


class TimerAssistant(AbstractAssistant):

    def __init__(self) -> None:
        super().__init__()
        self.assistant_id = "Timer"
        self.active_timer: Dict[str, Timer] = {}
        self.timer_llm = TIMER_LLM()

    def respond(self, speech: Optional[str] = "") -> None:
        if not speech:
            return
        response = self.timer_llm.process(speech=speech)
        # Check if the response is empty, i. e. if the llm did not format the response correctly
        if not response:
            self.say(
                "Ich konnte dich leider nicht verstehen. Bitte versuche es später erneut."
            )
        self.setup_timer(**response)

    def setup_timer(
        self,
        id: Optional[str] = "",
        duration: Optional[str] = "",
        time_text: Optional[str] = "",
    ):
        if not duration:
            self.say("Wie lange soll der Timer gehen? Bitte versuchen Sie es erneut.")
            return
        if not id:
            id = str(len(self.active_timer) + 1)
        try:
            duration = float(duration)
        except ValueError:
            self.say("Es ist etwas schiefgegangen. Bitte versuche es später erneut.")
            return

        timer_instance = Timer(duration, self.end_timer, args=(id,))
        timer_instance.start()
        self.active_timer[id] = timer_instance
        self.say(f"Der Timer {id} wurde für {time_text} gestartet.")

    def end_timer(self, timer_id: str):
        self.notify_user(timer_id)
        # Remove the timer instance from the list
        if timer_id in self.active_timer:
            timer = self.active_timer[timer_id]
            timer.cancel()
            del self.active_timer[timer_id]

    def notify_user(self, timer_id):
        self.say(f"Der timer {timer_id} ist abgelaufen")
