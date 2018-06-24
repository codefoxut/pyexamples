from ds_classes.exceptions import Empty


class CircularQueue(object):
    """Queue implementation using circularly linked list for storage."""

    # ---------------------------------------------------------------------------------
    # nested _Node class
    class _Node(object):
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

        def __str__(self):
            return str(self._element)

    # end of _Node class
    # ---------------------------------------------------------------------------------

    def __init__(self):
        """Create an empty queue."""
        self._tail = None  # will represent tail of queue
        self._size = 0  # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:  # removing only element
            self._tail = None  # queue becomes empty
        else:
            self._tail._next = oldhead._next  # bypass the old head
        self._size -= 1
        return oldhead._element

    def enqueue(self, elem):
        """Add an element to the back of queue."""
        newest = self._Node(elem, None)  # node will be new tail node
        if self.is_empty():
            newest._next = newest  # initialize circularly
        else:
            newest._next = self._tail._next  # new node points to head
            self._tail._next = newest  # old tail points to new node
        self._tail = newest  # new node becomes the tail
        self._size += 1
        print("CIRCULAR QUEUE -->", self)

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next  # old head becomes new tail

    def __str__(self):
        """String representation of queue """
        n = self._tail._next
        s = ""
        for i in range(self._size):
            s += "{}, ".format(n)
            n = n._next
        s = s[:-2]
        return s


if __name__ == '__main__':
    s = CircularQueue()
    s.enqueue(5)
    s.enqueue(3)
    print ("LENGTH:", len(s))
    print(s.dequeue())
    print(s.is_empty())
    print(s.dequeue())
    print(s.is_empty())
    s.enqueue(7)
    s.enqueue(9)
    print("FIRST:", s.first())
    s.enqueue(4)
    print("LENGTH-", len(s))
    print(s.dequeue())
    s.enqueue(6)
    s.enqueue(8)
    s.enqueue(10)
    s.rotate()
    s.enqueue(5)