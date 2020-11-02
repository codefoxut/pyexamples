import logging
from contextlib import contextmanager


logging.getLogger().setLevel(logging.WARNING)


def my_function():
    logging.debug("Some debug info!")
    logging.error("Some Error msg!")
    logging.debug("other debug info!")


@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


if __name__ == '__main__':
    my_function()

    with debug_logging(logging.DEBUG):
        my_function()

    my_function()

    with log_level(logging.DEBUG, 'my-log') as logger:
        logging.debug("This is the global loggger.")
        logger.debug("This is the my-log logger")

    logger = logging.getLogger('my-log')
    logger.debug("this is my log debug log.")
    logger.error("This is error log.")
