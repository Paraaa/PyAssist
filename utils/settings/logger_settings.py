import os
import logging
from logging.handlers import RotatingFileHandler

LOGDIR = ".log/"
LOGFILE = "astra.log"
LOGPATH = os.path.join(LOGDIR, LOGFILE)

os.makedirs(LOGDIR, exist_ok=True)


LOGGING_FORMAT = "[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s"
DEFAULT_LOG_LEVEL = 0  # 0 equals to NOTSET level

# Estimate maxBytes based on average log entry size (assume 100 bytes per entry)
MAX_BYTES = 10000 * 100  # ~1 MB assuming each entry is about 100 bytes

WHITELISTED_LOGGERS = [
    "AbstractAssistant",
    "JokeAssistant",
    "TimerAssistant",
    "TodoistAssistant",
    "LLM",
    "Astra",
]


class WhitelistFilter(logging.Filter):
    def __init__(self, whitelist=None):
        super().__init__()
        if whitelist is None:
            whitelist = []
        self.whitelist = whitelist

    def filter(self, record):
        return record.name in self.whitelist


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"simple": {"format": LOGGING_FORMAT}},
    "filters": {
        "whitelist_filter": {
            "()": WhitelistFilter,
            "whitelist": WHITELISTED_LOGGERS,
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
            "filters": ["whitelist_filter"],
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "simple",
            "filename": os.path.join(LOGDIR, LOGFILE),
            "maxBytes": MAX_BYTES,
            "backupCount": 1,  # Keep a backup file in case the original log file is filled
            "filters": ["whitelist_filter"],
        },
    },
    "loggers": {"root": {"level": "DEBUG", "handlers": ["stdout", "file"]}},
}
