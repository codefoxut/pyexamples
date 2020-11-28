# waste_memory.py
# ! /usr/bin/env python

import os
import hashlib


class MyObject:
    def __init__(self):
        self.x = os.urandom(100)
        self.y = hashlib.sha1(self.x).hexdigest()


def get_data():
    values = []
    for _ in range(100):
        obj = MyObject()
        values.append(obj)
    return values


def run():
    deep_values = []
    for _ in range(100):
        deep_values.append(get_data())
    return deep_values


if __name__ == '__main__':
    import gc

    found_objects = gc.get_objects()
    print("%d objects before" % len(found_objects))

    run()

    found_objects1 = gc.get_objects()
    print("%d objects after" % len(found_objects1))

    import tracemalloc

    tracemalloc.start(10)
    time1 = tracemalloc.take_snapshot()

    run()

    time2 = tracemalloc.take_snapshot()

    stats = time2.compare_to(time1, 'lineno')
    for stat in stats[:3]:
        print(stat)

    stats = time2.compare_to(time1, 'traceback')
    top = stats[0]
    print('\n'.join(top.traceback.format()))

