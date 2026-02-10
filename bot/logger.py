import logging
import sys


def setup_logger() -> logging.Logger:
    logger = logging.getLogger("discord-intel-bot")
    logger.setLevel(logging.INFO)

    # Prevent duplicate logs if root logger is configured elsewhere
    logger.propagate = False

    # Avoid adding handlers multiple times (important for reloads)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


logger = setup_logger()
