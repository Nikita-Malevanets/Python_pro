def analyze_inheritance(cls):
    """
    Analyze a class and print all methods inherited from base classes.

    :param cls: The class to analyze
    """
    print(f"Class {cls.__name__} inherits:")

    # Get all methods defined in this class itself
    own_methods = set(cls.__dict__.keys())

    # Go through all base classes (parents)
    for base in cls.__bases__:
        # Check each attribute in the base class
        for name, attr in base.__dict__.items():
            # If it is a callable (method) and not defined in the child
            if callable(attr) and name not in own_methods:
                print(f"- {name} from {base.__name__}")


class Parent:
    def parent_method(self):
        pass


class Child(Parent):
    def child_method(self):
        pass


analyze_inheritance(Child)
