import logging
import os

def setup_logging(log_level=logging.INFO, log_file='app.log'):
    log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Configure root logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)
