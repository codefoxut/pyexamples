import select
import threading

from design.course1.decorator.functional_decorator import time_it


def slow_system_call():
    print("slowing it...")
    select.select([], [], [], 0.1)


@time_it
def processing1():
    for _ in range(5):
        slow_system_call()


def compute_helicopter_location(index):
    # some actual work goes in here.
    pass


@time_it
def processing2():
    threads = []
    for _ in range(5):
        thread = threading.Thread(target=slow_system_call)
        thread.start()
        threads.append(thread)
    for i in range(5):
        compute_helicopter_location(i)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    processing1()
    processing2()
    