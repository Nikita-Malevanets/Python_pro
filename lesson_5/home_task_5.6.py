class Proxy:
    """
    A simple Proxy class that intercepts method calls.
    It logs the method name and arguments before
    calling the original method on the target object.
    """

    def __init__(self, obj) -> None:
        """
        Initialize the proxy with the target object.

        :param obj: The original object to be proxied
        """
        self._obj = obj

    def __getattr__(self, name: str):
        """
        Intercept attribute access. If it is a method,
        return a wrapper that logs the call and then executes it.

        :param name: Attribute name
        :return: Attribute value or wrapped method
        """
        attr = getattr(self._obj, name)

        if callable(attr):
            def wrapper(*args, **kwargs):
                """
                Wrapper function for method calls.
                Logs the method call and delegates execution
                to the original method.
                """
                print("Calling method:")
                print(f"{name} with args: {args}, kwargs: {kwargs}")
                return attr(*args, **kwargs)

            return wrapper

        return attr


class MyClass:
    def greet(self, name):
        return f"Hello, {name}!"


obj = MyClass()
proxy = Proxy(obj)

print(proxy.greet("Alice"))
