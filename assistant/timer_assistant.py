from assistant.abstract_assistant import AbstractAssistant
from utils.settings.default_messages_settings import DEFAULT_RESPONSES, TIMER_RESPONSES
from utils.timer_utils.elapsed_timer import ElapsedTimer
from LLM.timer_llm import TIMER_LLM
from typing import Optional, Dict
from utils.logging.logger import LOGGER


class TimerAssistant(AbstractAssistant):

    def __init__(self) -> None:
        super().__init__()
        self.assistant_id = "Timer"
        self.active_timer: Dict[str, ElapsedTimer] = {}
        self.timer_llm = TIMER_LLM()
        self.logger = LOGGER("TimerAssistant", "assistant/timer_assistant.log")

    def respond(self, speech: Optional[str] = "") -> None:
        if not speech:
            return
        response = self.timer_llm.process(speech=speech)
        # Check if the response is empty, i. e. if the llm did not format the response correctly
        if not response:
            self.logger.error(f"No response or wrong format {response}")
            self.say(DEFAULT_RESPONSES.get("ERROR", ""))
        self.classify_task(response)

    def classify_task(self, response: Dict[str, str]):
        task = response.get("function", None)
        match task:
            case "start_timer":
                self.start_timer(
                    id=response.get("id", ""),
                    duration=response.get("duration", ""),
                    time_text=response.get("time_text", ""),
                )
                self.logger.debug("start_timer")
            case "end_timer":
                self.end_timer(response.get("id", ""))
                self.logger.debug("end_timer")
            case "time_left":
                self.tell_time(response.get("id", ""))
                self.logger.debug("time_left")
            case _:
                self.say(DEFAULT_RESPONSES.get("ERROR", ""))
                self.logger.error("Could not determine the task")

    def start_timer(
        self,
        id: Optional[str] = "",
        duration: Optional[str] = "",
        time_text: Optional[str] = "",
    ):
        if not duration:
            self.logger.debug("Timer duration is missing")
            self.say(TIMER_RESPONSES.get("TIMER_DURATION_MISSING", ""))
            return

        if not id:
            id = str(len(self.active_timer) + 1)
            self.logger.debug(f"Timer id is missing setting id to: {id}")

        try:
            duration = float(duration)
        except ValueError:
            self.logger.exception("Could not convert duration to float")
            self.say(TIMER_RESPONSES.get("ERROR", ""))
            return

        timer_instance = ElapsedTimer(duration, self.notify_user, args=(id,))
        timer_instance.start()
        self.active_timer[id] = timer_instance
        self.say(f"Der Timer {id} wurde für {time_text} gestartet.")

    def end_timer(self, timer_id: str):
        if not timer_id:
            self.logger.debug(f"Timer id is missing")
            self.say(DEFAULT_RESPONSES.get("ERROR", ""))
            return

        if timer_id not in self.active_timer:
            self.logger.debug(
                f"Timer with id: {timer_id} could not be found in: {self.active_timer}"
            )
            self.say(TIMER_RESPONSES.get("TIMER_NOT_FOUND", ""))
            return

        self.remove_timer(timer_id)
        self.say(f"Der Timer {timer_id} wurde beendet.")

    def tell_time(self, timer_id: str):
        if not timer_id:
            self.logger.debug(f"Timer id is missing")

            self.say(DEFAULT_RESPONSES.get("ERROR", ""))
            return

        if timer_id not in self.active_timer:
            self.logger.debug(
                f"Timer with id: {timer_id} could not be found in: {self.active_timer}"
            )
            self.say(TIMER_RESPONSES.get("TIMER_NOT_FOUND", ""))
            return

        timer_instance: ElapsedTimer = self.active_timer[timer_id]
        remaining_time = timer_instance.remaining()

        # Determine how to display the remaining time based on its length
        if remaining_time < 60:
            # Display in seconds if less than a minute
            self.say(
                f"Verbleibende Zeit für Timer {timer_id}: {int(remaining_time)} Sekunden."
            )
        else:
            # Convert remaining time to minutes and seconds for durations longer than a minute
            minutes, seconds = divmod(int(remaining_time), 60)
            self.say(
                f"Verbleibende Zeit für Timer {timer_id}: {int(minutes)} Minuten und {int(seconds)} Sekunden."
            )

    def remove_timer(self, timer_id: str):
        # Remove the timer instance from the list
        if timer_id in self.active_timer:
            timer = self.active_timer[timer_id]
            timer.cancel()
            del self.active_timer[timer_id]
            self.logger.debug(f"Removed timer {timer_id}")

    def notify_user(self, timer_id):
        self.remove_timer(timer_id)
        self.say(f"Der timer {timer_id} ist abgelaufen")
