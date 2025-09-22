def log_methods(cls):
    """
    Class decorator that logs calls to all methods of the class.
    """

    def make_wrapper(method, method_name):
        def wrapper(self, *args, **kwargs):
            print(f"Logging: {method_name} called with {args}")
            return method(self, *args, **kwargs)

        return wrapper

    for name, attr in cls.__dict__.items():
        if callable(attr):
            setattr(cls, name, make_wrapper(attr, name))
    return cls


@log_methods
class MyClass:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


obj = MyClass()
print(obj.add(5, 3))  # Logging: add called with (5, 3)
print(obj.subtract(5, 3))  # Logging: subtract called with (5, 3)
