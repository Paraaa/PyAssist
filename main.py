import psutil
import logging.config
from wake_word.astra import Astra
from utils.settings.logger_settings import LOGGING_CONFIG


# This line sets the logging configuration
logging.config.dictConfig(config=LOGGING_CONFIG)

if __name__ == "__main__":
    astra = Astra()

    while True:
        astra.listen_to_wake_word()
        # process = psutil.Process()
        # print(process.memory_info().rss)
        # print(
        #     f"Memory usage: {process.memory_info().rss / (1024 * 1024 * 1024):.2f} GB"
        # )
