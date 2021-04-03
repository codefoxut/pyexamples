"""
A metaclass instantiates and defines behavior for a class just like a class instantiates
and defines behavior for an instance.
"""

class ParentClass:
    pass


class SomeClass(ParentClass):
    classvar = 1
    def init(self):
        self.somevar = 'Some value'


if __name__ ==  '__main__':
    pass
