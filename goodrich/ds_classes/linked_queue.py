from exceptions import Empty


class LinkedQueue(object):
    """FIFO queue implementation using a singly linked list for storage."""

    # -------------------------- nested _Node class --------------------------
    class _Node(object):
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

        def __str__(self):
            return str(self._element)

    # ------------------------------- queue methods -------------------------------
    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
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
        return self._head._element  # front aligned with head of list

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():  # special case as queue is empty
            self._tail = None  # removed head had been the tail
        return answer

    def enqueue(self, elem):
        """Add an element to the back of queue."""
        newest = self._Node(elem, None)  # node will be new tail node
        if self.is_empty():
            self._head = newest  # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest  # update reference to tail node
        self._size += 1
        print("QUEUE-->", self)

    def __str__(self):
        """String representation of queue """
        n = self._head
        s = ""
        for i in range(self._size):
            s += "{}, ".format(n)
            n = n._next
        s = s[:-2]
        return s

if __name__ == '__main__':
    s = LinkedQueue()
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
