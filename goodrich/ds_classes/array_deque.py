from exceptions import Empty
from array_queue import ArrayQueue


class ArrayDeque(object):
    """A queue-like data structure that supports insertion and deletion
at both the front and the back of the queue. """
    DEFAULT_CAPACITY = 10    # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the deque."""
        return self._size

    def is_empty(self):
        """Return True if the deque is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the deque.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]

    def last(self):
        """Return (but do not remove) the last element of deque D;

        Raise Empty exception if the deque is empty."""
        if self.is_empty():
            raise Empty('Deque is empty.')
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def add_first(self, elem):
        """Add an element to the front of deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = elem
        self._size += 1
        # print("FRONT: {} END: {}". format(self._front, self._end))
        print("QUEUE-->", self)

    def add_last(self, elem):
        """Add an element to the back of deque ."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = elem
        self._size += 1
        print("QUEUE-->", self)

    def delete_first(self):
        """Remove and return the first element of the deque.

        Raise an empty exception if the deque us empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        print("QUEUE-->", self)
        return answer

    def delete_last(self):
        """Remove and return the last element of the deque.

        Raise an empty exception if the deque us empty."""
        # print(self._end, "END")
        if self.is_empty():
            raise Empty('Deque is empty')
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None  # help garbage collection
        self._size -= 1
        print("QUEUE-->", self)
        return answer

    def _resize(self, cap): # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size): # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0  # front has been realigned

    def __str__(self):
        """Representation in string"""
        queue = []
        # print("raw queue -->", self._data, self._front, self._size)
        for x in range(self._size):
            queue.append(str(self._data[(self._front + x) % len(self._data)]))
        return ", ".join(queue)


class ArrayDeque1(object):
    """A queue-like data structure that supports insertion and deletion
at both the front and the back of the queue. """
    DEFAULT_CAPACITY = 10    # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayDeque1.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._end = 0

    def __len__(self):
        """Return the number of elements in the deque."""
        return self._size

    def is_empty(self):
        """Return True if the deque is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the deque.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]

    def last(self):
        """Return (but do not remove) the last element of deque D;

        Raise Empty exception if the deque is empty."""
        if self.is_empty():
            raise Empty('Deque is empty.')
        return self._data[self._end]

    def add_first(self, elem):
        """Add an element to the front of deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data), blank_at_front=True)  # double the array size
        else:
            self._front = (self._front - 1) % len(self._data)

        self._data[self._front] = elem
        self._size += 1
        self._end = (self._front + self._size - 1) % len(self._data)
        # print("FRONT: {} END: {}". format(self._front, self._end))
        print("QUEUE-->", self)

    def add_last(self, elem):
        """Add an element to the back of deque ."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        self._end = (self._front + self._size) % len(self._data)
        self._data[self._end] = elem
        self._size += 1
        # print("FRONT: {} END: {}".format(self._front, self._end))
        print("QUEUE-->", self)

    def delete_first(self):
        """Remove and return the first element of the deque.

        Raise an empty exception if the deque us empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        self._end = (self._front + self._size - 1) % len(self._data)
        print("QUEUE-->", self)
        return answer

    def delete_last(self):
        """Remove and return the last element of the deque.

        Raise an empty exception if the deque us empty."""
        # print(self._end, "END")
        if self.is_empty():
            raise Empty('Deque is empty')
        answer = self._data[self._end]
        self._data[self._end] = None  # help garbage collection
        self._end = (self._end - 1) % len(self._data)
        self._size -= 1
        self._front = (self._end - self._size + 1) % len(self._data)
        print("QUEUE-->", self)
        return answer

    def _resize(self, cap, blank_at_front=False): # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        i = self._end
        for k in range(self._size): # only consider existing elements
            if blank_at_front:
                i = k + 1
            else:
                i = k
            self._data[i] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0  # front has been realigned
        self._end = i

    def __str__(self):
        """Representation in string"""
        queue = []
        print("raw queue -->", self._data, self._front, self._size, self._end)
        for x in range(self._size):
            queue.append(str(self._data[(self._front + x) % len(self._data)]))
        return ", ".join(queue)


if __name__ == '__main__':
    s = ArrayDeque()
    s.add_last(5)
    s.add_first(3)
    s.add_first(7)
    print("FIRST:", s.first())
    print(s.delete_last())
    print ("LENGTH:", len(s))
    print(s.delete_first())
    print(s.is_empty())
    print(s.delete_last())
    print(s.is_empty())
    s.add_first(6)
    print("LAST:", s.last())
    s.add_first(8)
    print("FIRST:", s.first())
    s.add_last(4)
    print("LENGTH-", len(s))
    print(s.delete_last())
    s.add_last(16)
    s.add_last(18)
    s.add_first(10)

