import logging
import os
import sys

initialized = False


def setup_logging():
    FORMAT = f"[%(asctime)s] - {os.getpid()} - %(levelname)s | %(name)s | %(funcName)s | %(message)s"

    logging.basicConfig(
        level=logging.DEBUG, format=FORMAT, filename="debug.log", filemode="w"
    )

    formatter = logging.Formatter("[%(asctime)s] - %(levelname)s | %(message)s")

    stream_handler = logging.StreamHandler(stream=sys.stdout)

    stream_handler.setLevel(logging.INFO)

    stream_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(stream_handler)

    logger.debug("LOGGING INITIALIZED")


if not initialized:
    setup_logging()
    initialized = True
