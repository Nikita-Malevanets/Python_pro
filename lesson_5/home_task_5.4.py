def create_class(class_name, methods):
    """
    Dynamically creates a class with the given name and methods.

    Args:
        class_name (str): Name of the class to create.
        methods (dict): A dictionary where keys are method names (str)
                        and values are functions.

    Returns:
        type: The dynamically created class.
    """
    # Use type(name, bases, dict) to create a class dynamically
    # bases=(object,) means the class inherits from object explicitly
    return type(class_name, (object,), methods)


# Example methods
def say_hello(self):
    return "Hello!"


def say_goodbye(self):
    return "Goodbye!"


# Dictionary of methods
methods = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}

# Create class dynamically
MyDynamicClass = create_class("MyDynamicClass", methods)

# Create an instance of the class
obj = MyDynamicClass()

# Test method calls
print(obj.say_hello())  # Hello!
print(obj.say_goodbye())  # Goodbye!
