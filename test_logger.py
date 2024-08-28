from utils.logging.logger import LOGGER


def main():
    logger: LOGGER = LOGGER(__name__, "test/test_logger.log")

    logger.debug("This is a test debug log message")  # Logs at DEBUG level
    logger.info("This is an info log message")  # Logs at INFO level
    logger.warning("This is a warning log message")  # Logs at WARNING level
    logger.error("This is an error log message")  # Logs at ERROR level
    logger.critical("This is a critical log message")  # Logs at CRITICAL level

    try:
        # Your code that might raise an exception
        raise ValueError("This is a test exception")
    except Exception as e:
        logger.exception("An exception occurred")


if __name__ == "__main__":
    main()
