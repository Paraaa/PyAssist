from wake_word.astra import Astra
import psutil
from utils.logging.logger import LOGGER


if __name__ == "__main__":
    # This fixed the logger issue sort of?
    logger = LOGGER("AbstractAssistant", "assistant/abstract_assistant.log")
    logger = LOGGER("JokeAssistant", "assistant/joke_assistant.log")
    logger = LOGGER("TimerAssistant", "assistant/timer_assistant.log")
    logger = LOGGER("TodoistAssistant", "assistant/todoist_assistant.log")
    logger = LOGGER("LLM", "llm/abstract_llm.log")
    logger = LOGGER("Astra", "astra/astra.log")

    astra = Astra()

    while True:
        astra.listen_to_wake_word()
        process = psutil.Process()
        # print(process.memory_info().rss)
        # print(
        #     f"Memory usage: {process.memory_info().rss / (1024 * 1024 * 1024):.2f} GB"
        # )
