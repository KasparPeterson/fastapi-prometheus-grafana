import logging

LOGGING_MESSAGE_FORMAT = "%(asctime)s %(name)-12s %(levelname)s %(message)s"

name = "app-name"
log_path = "logs/logs.log"
loggers = {}


def get():
    global loggers
    if loggers.get(name):
        return loggers.get(name)
    else:
        file_handler = get_file_logger()
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.handlers = []
        logger.addHandler(file_handler)
        apply_default_formatter(file_handler)
        return logger


def get_file_logger() -> logging.FileHandler:
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.DEBUG)
    return file_handler


def get_console_logger() -> logging.StreamHandler:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    return console_handler


def apply_default_formatter(handler: logging.Handler):
    formatter = logging.Formatter(LOGGING_MESSAGE_FORMAT)
    handler.setFormatter(formatter)
