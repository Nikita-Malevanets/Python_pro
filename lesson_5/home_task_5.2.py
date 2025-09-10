class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

def call_function(obj, method_name, *args):
    """
    Dynamically calls a method of an object by its name.

    Parameters:
    obj : object
        The object whose method should be called.
    method_name : str
        The name of the method to call.
    *args :
        Arbitrary arguments to pass to the method.

    Returns:
    The result of the method call.

    Raises:
    AttributeError : if the method does not exist or is not callable.
    """
    # Get the method from the object by name; if not found, return None
    method = getattr(obj, method_name, None)

    # Check if the attribute exists and is callable
    if method and callable(method):
        return method(*args)  # Call the method with the provided arguments
    else:
        # Raise an error if the method doesn't exist or isn't callable
        raise AttributeError(f"Method '{method_name}' not found or not callable")

# Test
calc = Calculator()
print(call_function(calc, "add", 10, 5))       # 15
print(call_function(calc, "subtract", 10, 5))  # 5

