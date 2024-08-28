import logging
import os
from typing import List, Dict, Union, Optional
from utils.settings.logger_settings import LOGDIR


class LOGGER:
    def __init__(self, name: str, log_file: str, level: int = logging.INFO):
        self.log_path = f"{LOGDIR}{log_file}"
        logging.basicConfig(
            filename=self.log_path,
            level=logging.INFO,
            format="[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s",
        )
        self.logger = logging.getLogger(name)
        print(self.logger)
        # Set the log level to capture all log messages above the set level
        self.logger.setLevel(level)
        self._create_log_file()

        # # Create handlers
        # c_handler = logging.StreamHandler()
        # formatter = logging.Formatter(
        #     "[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s"
        # )
        # c_handler.setFormatter(formatter)
        # self.logger.addHandler(c_handler)

        # f_handler = logging.FileHandler(self.log_path)
        # f_handler.setFormatter(formatter)
        # self.logger.addHandler(f_handler)

    def _create_log_file(self):
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True),
        if not os.path.exists(self.log_path):
            with open(self.log_path, "w"):
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
        """Logs an error message along with the traceback of an exception (use within an except block)."""
        self.logger.exception(msg)
