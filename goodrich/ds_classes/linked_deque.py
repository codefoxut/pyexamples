from ds_classes.doubly_linked_list import _DoublyLinkedBase
from ds_classes.exceptions import Empty


class LinkedDeque(_DoublyLinkedBase):  # note the use of inheritance
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element  # real item just after header

    def last(self):
        """Return (but do not remove) the element at the back of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element  # real item just before trailer

    def insert_first(self, elem):
        """Add an element to the front of the deque."""
        self._insert_between(elem, self._header, self._header._next)  # after header

    def insert_last(self, elem):
        """Add an element to the back of the deque."""
        self._insert_between(elem, self._trailer._prev, self._trailer)  # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)  # use inherited method

    def delete_last(self):
        """Remove and return the element from the back of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)  # use inherited method


if __name__ == '__main__':
    s = LinkedDeque()
    s.insert_last(5)
    s.insert_first(3)
    s.insert_first(7)
    print("FIRST:", s.first())
    print(s.delete_last())
    print ("LENGTH:", len(s))
    print(s.delete_first())
    print(s.is_empty())
    print(s.delete_last())
    print(s.is_empty())
    s.insert_first(6)
    print("LAST:", s.last())
    s.insert_last(8)
    print("FIRST:", s.first())
    s.insert_last(4)
    print("LENGTH-", len(s))
    print(s.delete_last())
    s.insert_last(16)
    s.insert_first(18)
    s.insert_first(10)
