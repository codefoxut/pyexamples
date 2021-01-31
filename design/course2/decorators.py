

def decorator_function(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} inside decorator")
        result = func(*args, **kwargs)
        return result
    return wrapper


@decorator_function
def my_function():
    print("inside aFunction")


class entry_exit_class:

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)


@entry_exit_class
def func1():
    print("inside func1()")

@entry_exit_class
def func2():
    print("inside func2()")


def entry_exit_function(f):
    def new_f():
        print("Entering function", f.__name__)
        f()
        print("Exited function", f.__name__)
    new_f.__name__ = f.__name__
    return new_f


@entry_exit_function
def func3():
    print("inside func3()")


@entry_exit_function
def func4():
    print("inside func4()")


class decorator_with_arguments:

    def __init__(self, *args, **kwargs):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print("Inside __init__()", args, kwargs)
        self.args = args
        self.kwargs = kwargs

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print("Inside __call__()", f.__name__)
        def wrapped_f(*args, **kwargs):
            print("Inside wrapped_f()")
            print("Decorator arguments:", args, kwargs, self.args, self.kwargs)
            f(*args, **kwargs)
            print("After f(*args)")
        wrapped_f.__name__ = f.__name__
        return wrapped_f


@decorator_with_arguments("hello", "world", x=42)
def sayHello(a1, a2, a3, a4=""):
    print('sayHello arguments:', a1, a2, a3, a4)


if __name__ ==  '__main__':
    my_function()
    func1()
    func2()
    func3()
    func4()

    print("After decoration")

    print("Preparing to call sayHello()")
    sayHello("say", "hello", "argument", a4="list")
    print("after first sayHello() call")
    sayHello("a", "different", "set of", a4="arguments")
    print("after second sayHello() call", sayHello.__name__)
