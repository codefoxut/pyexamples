from weakref import WeakValueDictionary

class Foo:
    x = "a"


class Other:
    something = None # Static: visible to all classes
    def __init__(self, x):
        if not self.something:
            self.something = [] # New local version for this object
        self.something.append(x)



class Counter:
    # Now cleanup happens properly without the need for an explicit call to del.
    _instances = WeakValueDictionary()
    @property
    def Count(self):
        return len(self._instances)

    def __init__(self, name):
        self.name = name
        self._instances[id(self)] = self
        print(name, 'created')

    def __del__(self):
        print(self.name, 'deleted')
        if self.Count == 0:
            print('Last Counter object deleted')
        else:
            print(self.Count, 'Counter objects remaining')
        print(list(self._instances.items()))


if __name__ == '__main__':
    f1 = Foo()
    print("f1.x", f1.x, Foo.x)

    f2 = Foo()
    f2.x = "a2"
    print("f2.x", f2.x, Foo.x)

    Foo.x = "b"

    print("f1.x", f1.x, Foo.x)
    print("f2.x", f2.x)

    f3 = Foo()
    print("f3.x", f3.x, Foo.x)

    Foo.x = "c"
    print("f3.x", f3.x, Foo.x)
    print("f2.x", f2.x, Foo.x)

    o1 = Other('a')
    Other.something = ['b']
    print(o1.something)

    o2 = Other("c")
    print(o2.something, o1.something)

    # clean up
    x = Counter("First")
    y = Counter("Second")
    z = Counter("Third")






