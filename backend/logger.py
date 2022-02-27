import logging


LOG_FORMATTER = logging.Formatter(
    '%(asctime)s | %(levelname)s | Message : %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S')
handler = logging.StreamHandler()
handler.setFormatter(LOG_FORMATTER)
logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)
