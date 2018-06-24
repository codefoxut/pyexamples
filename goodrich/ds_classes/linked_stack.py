from ds_classes.exceptions import Empty


class LinkedStack(object):
    """LIFO Stack implementation using a singly linked list for storage."""

    # -------------------------- nested _Node class --------------------------
    class _Node(object):
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element  # reference to user's element
            self._next = next  # reference to next node

        def __str__(self):
            return str(self._element)

    # ------------------------------- stack methods -------------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head = None  # reference to the head node
        self._size = 0  # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, elem):
        """Add element e to the top of the stack."""
        self._head = self._Node(elem, self._head)  # create and link a new node
        self._size += 1
        print("STACK-->", self)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element  # top of stack is at head of list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next  # bypass the former top node
        self._size -= 1
        return answer

    def __str__(self):
        """String representation of stack """
        n = self._head
        s = ""
        for i in range(self._size):
            s += "{} ,".format(n)
            n = n._next
        s = s[:-2][::-1]
        return s


if __name__ == '__main__':
    S = LinkedStack()  # contents: [ ]
    S.push(5)  # contents: [5]
    S.push(3)  # contents: [5, 3]

    print("LENGTH-", len(S))  # contents: [5, 3];    outputs 2
    print(S.pop())  # contents: [5];       outputs 3
    print("is_empty-", S.is_empty())  # contents: [5];       outputs False
    print(S.pop())  # contents: [ ];       outputs 5

    print('is_empty-', S.is_empty())  # contents: [ ];       outputs True
    S.push(7)  # contents: [7]
    S.push(9)  # contents: [7, 9]
    print(S.top())  # contents: [7, 9];    outputs 9
    S.push(4)  # contents: [7, 9, 4]
    print("LENGTH-", len(S))  # contents: [7, 9, 4]; outputs 3
    print(S.pop())  # contents: [7, 9];    outputs 4

    S.push(6)  # contents: [7, 9, 6]
    S.push(8)  # contents: [7, 9, 6, 8]
    print(S.pop())  # contents: [7, 9, 6]; outputs 8
