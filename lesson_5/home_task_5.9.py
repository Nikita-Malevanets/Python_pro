class DynamicProperties:
    """
    A class that allows dynamic addition of properties at runtime.
    """

    def add_property(self, property_name: str, initial_value):
        """
        Dynamically adds a property with getter and setter.

        :param property_name: Name of the property
        :param initial_value: Initial value of the property
        """
        # Internal storage for the property value
        private_name = f"_{property_name}"
        setattr(self, private_name, initial_value)

        # Create getter function
        def getter(self):
            return getattr(self, private_name)

        # Create setter function
        def setter(self, value):
            setattr(self, private_name, value)

        # Add the property to the class dynamically
        setattr(self.__class__, property_name, property(getter, setter))


obj = DynamicProperties()
obj.add_property('name', 'default_name')
print(obj.name)  # default_name
obj.name = "Python"
print(obj.name)  # Python
