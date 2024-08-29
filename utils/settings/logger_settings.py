LOGDIR = ".log/"
DEFAULT_LOG_LEVEL = 0  # 0 equals to NOTSET level
LOGGING_FORMAT = "[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s"

# TODO: Add filer handler
# TODO: Add filter to handle non related logging messages (https://stackoverflow.com/questions/879732/logging-with-filters)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"simple": {"format": LOGGING_FORMAT}},
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {"root": {"level": "DEBUG", "handlers": ["stdout"]}},
}
