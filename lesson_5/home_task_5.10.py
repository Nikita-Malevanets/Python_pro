class SingletonMeta(type):
    """
    Metaclass that ensures a class can have only one instance (Singleton pattern).
    """

    # Dictionary to store one instance per class
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Called when a class is instantiated.
        If an instance already exists, return it; otherwise, create a new one.
        """
        if cls not in cls._instances:
            # No instance exists yet, create and store it
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating instance")


obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)