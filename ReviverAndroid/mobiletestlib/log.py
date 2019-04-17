import logging.handlers
import logging

FORMATTER_BASIC = logging.Formatter('%(asctime)s %(levelname)s - %(name)s %(filename)s:%(lineno)d %(message)s')
LOGGER_NAME = 'LOGGER'
LOG_FILE_PATH = "./output.log"


def get_log(name=LOGGER_NAME, console_level=logging.INFO, file_level=logging.DEBUG, formatter=FORMATTER_BASIC,
            log_path=LOG_FILE_PATH, custom_logger_class=None, use_stream=False):
    """
    Initialize logger. Enable console log with debug level by default.

    :param string log_path: Path to create log
    :param string name: use root as default
    :param string console_level: Info/Debug/Warn/Error for Stream handler
    :param string file_level: Info/Debug/Warn/Error for File handler
    :param string formatter: Format of logging. See https://docs.python.org/3/library/logging.html#logrecord-attributes
    :param custom_logger_class: to set custom logger class, if any
    :param use_stream: to enable stream handler
    :return: logger object
    """
    if custom_logger_class:
        logging.setLoggerClass(custom_logger_class)
    logger = logging.getLogger(name)

    # Reset the logger.handlers & logger.manager.root.handlers if it already exists.
    if logger.handlers:
        logger.handlers = []
    if logger.manager.root.handlers:
        logger.manager.root.handlers = []

    file_handler = logging.handlers.RotatingFileHandler(log_path, backupCount=4, maxBytes=1000000)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(file_level)

    if use_stream:
        # Set Stream Handler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(console_level)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger