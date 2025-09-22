class MutableClass:
    """A class that allows adding and removing attributes dynamically."""

    def add_attribute(self, name: str, value) -> None:
        """
        Adds a new attribute to the object.

        :param name: Name of the attribute
        :param value: Value of the attribute
        """
        setattr(self, name, value)

    def remove_attribute(self, name: str) -> None:
        """
        Removes an attribute from the object if it exists.

        :param name: Name of the attribute
        """
        if hasattr(self, name):
            delattr(self, name)
        else:
            raise AttributeError(f"Attribute '{name}' does not exist.")


obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)  # Python

obj.remove_attribute("name")
# print(obj.name)  # Виникне помилка, атрибут видалений
