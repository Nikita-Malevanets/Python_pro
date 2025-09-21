class PriceDescriptor:
    """
    Descriptor to control access to the 'amount' attribute of Price.
    Ensures the value is non-negative and rounded to 2 decimal places.
    """

    def __get__(self, instance, owner):
        return instance._amount

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        instance._amount = round(float(value), 2)


class Price:
    """
    Price class representing a monetary value.
    Supports addition, subtraction, comparison operations,
    and guarantees rounding to 2 decimal places.

    Attributes:
        amount (float): The price amount, always rounded to 2 decimal places and non-negative.
    """

    amount = PriceDescriptor()  # Descriptor to control 'amount'

    def __init__(self, amount: float):
        """
        Initialize Price object.

        Args:
            amount (float): initial price value
        """
        self.amount = amount

    # Arithmetic operations
    def __add__(self, other):
        """
        Add two Price objects.

        Args:
            other (Price): another Price object to add

        Returns:
            Price: new Price object representing the sum
        """
        return Price(self.amount + other.amount)

    def __sub__(self, other):
        """
        Subtract two Price objects.

        Args:
            other (Price): another Price object to subtract

        Returns:
            Price: new Price object representing the difference
        """
        return Price(self.amount - other.amount)

    # Comparison operations
    def __eq__(self, other):
        """Check if two Price objects are equal."""
        return self.amount == other.amount

    def __lt__(self, other):
        """Check if this Price is less than another Price or float."""
        if isinstance(other, Price):
            return self.amount < other.amount
        return self.amount < other

    def __le__(self, other):
        """Check if this Price is less than or equal to another Price or float."""
        if isinstance(other, Price):
            return self.amount <= other.amount
        return self.amount <= other

    def __gt__(self, other):
        """Check if this Price is greater than another Price or float."""
        if isinstance(other, Price):
            return self.amount > other.amount
        return self.amount > other

    def __ge__(self, other):
        """Check if this Price is greater than or equal to another Price or float."""
        if isinstance(other, Price):
            return self.amount >= other.amount
        return self.amount >= other

    def __repr__(self):
        """String representation of Price object."""
        return f"Price({self.amount})"
