import time
from queue import Queue
from threading import Thread

queue = Queue()
queue1 = Queue(1)


def consumer():
    print('Consumer waiting..')
    queue.get()
    print('consumer done..')


def consumer1():
    time.sleep(0.1)
    print('Consumer waiting..')
    queue1.get()
    print('consumer got 1..')
    queue1.get()
    print('consumer got 2..')


def producer1():
    thread = Thread(target=consumer)
    thread.start()

    print('Producer putting.')
    queue.put(object())
    thread.join()
    print('Producer done..')


def producer2():
    thread = Thread(target=consumer1)
    thread.start()

    print('Producer putting.')
    queue1.put(object())
    print('Producer put 1')
    queue1.put(object())
    print('Producer put 2')
    thread.join()
    print('Producer done..')


def producer_many():
    thread = Thread(target=consumer)
    thread.start()

    print('Producer putting.')
    queue.put(object())
    queue.put(object())
    queue.put(object())
    queue.put(object())
    thread.join()
    print('Producer done..')


if __name__ == '__main__':
    producer1()
    producer_many()
    producer2()