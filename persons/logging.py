import logging

date_fmt = "%Y-%m-%d %H:%M:%S"
fmt = "[%(levelname)s] %(message)s"

logger = logging.getLogger("example_app")

logger.propagate = False
logger.setLevel(logging.INFO)

stdout_formatter = logging.Formatter(fmt, date_fmt)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(stdout_formatter)

logger.addHandler(stream_handler)
