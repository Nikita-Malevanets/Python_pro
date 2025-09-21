class ProductWithGetSet:
    """
    Product class using explicit getters and setters for 'price'.

    Attributes:
        name (str): Product name.
        _price (float): Private attribute for price.
    """

    def __init__(self, name: str, price: float) -> None:
        self.name: str = name
        self._price: float = 0
        self.set_price(price)

    def get_price(self) -> float:
        """Get the product price."""
        return self._price

    def set_price(self, value: float) -> None:
        """Set the product price, raises ValueError if negative."""
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number.")
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = float(value)


class ProductWithProperty:
    """
    Product class using @property for 'price'.

    Attributes:
        name (str): Product name.
        price (float): Product price (validated).
    """

    def __init__(self, name: str, price: float) -> None:
        self.name: str = name
        self.price: float = price

    @property
    def price(self) -> float:
        """Get the product price."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Set the product price, raises ValueError if negative."""
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number.")
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = float(value)


class PriceDescriptor:
    """
    Descriptor that manages the 'price' attribute.
    Ensures that the price is never negative.
    """

    def __get__(self, instance: object, owner: type) -> float:
        if instance is None:
            return self
        return instance.__dict__["_price"]

    def __set__(self, instance: object, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number.")
        if value < 0:
            raise ValueError("Price cannot be negative!")
        instance.__dict__["_price"] = float(value)


class ProductWithDescriptor:
    """
    Product class that uses a descriptor for managing the 'price' attribute.

    Attributes:
        name (str): The product name.
        price (float): The product price (validated by PriceDescriptor).
    """

    price = PriceDescriptor()

    def __init__(self, name: str, price: float) -> None:
        self.name: str = name
        self.price: float = price


def test_all():
    print("=== ProductWithGetSet ===")
    p1 = ProductWithGetSet("Apple", 10.5)
    print(p1.get_price())
    p1.set_price(20)
    print(p1.get_price())
    try:
        p1.set_price(-5)
    except ValueError as e:
        print("Error:", e)

    print("\n=== ProductWithProperty ===")
    p2 = ProductWithProperty("Banana", 15)
    print(p2.price)
    p2.price = 30
    print(p2.price)
    try:
        p2.price = -7
    except ValueError as e:
        print("Error:", e)

    print("\n=== ProductWithDescriptor ===")
    p3 = ProductWithDescriptor("Orange", 25)
    print(p3.price)
    p3.price = 40
    print(p3.price)
    try:
        p3.price = -10
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    test_all()
