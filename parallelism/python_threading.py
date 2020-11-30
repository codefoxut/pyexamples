import threading

from design.course1.decorator.functional_decorator import time_it

numbers = [2139079, 12232472, 3213932, 2314921]


def factorize1(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


class FactorizeThread(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize1(self.number))


@time_it
def processing1():
    for number in numbers:
        list(factorize1(number))


@time_it
def processing2():
    threads = []
    for number in numbers:
        thd = FactorizeThread(number)
        thd.start()
        threads.append(thd)

    for thread in threads:
        thread.join()
        # print("Factors: %r" % thread.factors)


if __name__ == '__main__':
    print(list(factorize1(21)))
    processing1()

    _thread = FactorizeThread(21)
    _thread.start()
    _thread.join()
    print(_thread.factors)
    processing2()
