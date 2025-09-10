def analyze_object(obj):
    """
    Analyzes an object by printing its type, attributes, and methods.

    Parameters:
    obj : object
        Any Python object to analyze.

    Prints:
    - Type of the object.
    - Attributes of the object with their types.
    - Methods of the object with their types (excluding magic methods).
    """
    # Print the type of the object
    print("Тип об'єкта:", type(obj))

    # Print attributes of the object and their types
    for name, value in obj.__dict__.items():
        print(f"- {name}: {type(value)}")

    # Print methods of the object's class (excluding magic methods)
    for name in dir(type(obj)):
        if not name.startswith("__"):  # skip magic or special methods
            attr = getattr(obj, name)
            if callable(attr):  # only include callable methods
                print(f"- {name}: {type(attr)}")


# Test example
class MyClass:
    def __init__(self, value):
        self.value = value

    def say_hello(self):
        return f"Hello, {self.value}"


obj = MyClass("World")
analyze_object(obj)
