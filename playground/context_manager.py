import logging
from contextlib import contextmanager


@contextmanager
def swallow_exception(cls):
    try:
        yield
    except cls:
        logging.exception("Swallowing Exception.")


if __name__ == '__main__':

    with swallow_exception(ZeroDivisionError):
        value = 20 / 0

    print("Done")

    with open("/tmp/my_output.txt", 'w') as handle:
        handle.write('Hello there!')

    handle = open('/tmp/my_output.txt', 'w')
    try:
        handle.write("Hello there!")
    finally:
        handle.close()
