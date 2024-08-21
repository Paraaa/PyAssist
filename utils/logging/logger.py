import logging
import os
from typing import List, Dict, Union, Optional
from utils.settings.logger_settings import LOGDIR


class LOGGER:
    def __init__(self, name: str, log_file: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Create handlers
        c_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        c_handler.setFormatter(formatter)
        self.logger.addHandler(c_handler)

        self._create_log_file(log_file)
        f_handler = logging.FileHandler(log_file)
        f_handler.setFormatter(formatter)
        self.logger.addHandler(f_handler)

    def _create_log_file(self, log_file: str) -> None:
        PATH = f"{LOGDIR}{log_file}"
        os.makedirs(os.path.dirname(PATH), exist_ok=True),
        if not os.path.exists(PATH):
            with open(PATH, "w"):
                pass

    def debug(self, msg: str):
        self.logger.debug(msg)

    def info(self, msg: str):
        self.logger.info(msg)

    def warning(self, msg: str):
        self.logger.warning(msg)

    def error(self, msg: str):
        self.logger.error(msg)

    def critical(self, msg: str):
        self.logger.critical(msg)

    def exception(self, msg: str):
        self.logger.exception(msg)
