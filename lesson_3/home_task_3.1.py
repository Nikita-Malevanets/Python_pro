class Fraction:
    """
    A class to represent a fraction (numerator/denominator) and perform
    arithmetic operations (addition, subtraction, multiplication, division)
    between Fraction objects.
    """

    def __init__(self, numerator: int, denominator: int):
        """
        Initialize a Fraction object.

        Parameters:
        numerator (int): The numerator of the fraction.
        denominator (int): The denominator of the fraction.

        Returns:
        None
        """
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        """
        Add two Fraction objects.

        Parameters:
        other (Fraction): Another Fraction object to add.

        Returns:
        Fraction: A new Fraction object representing the sum.
        """
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """
        Subtract two Fraction objects.

        Parameters:
        other (Fraction): Another Fraction object to subtract.

        Returns:
        Fraction: A new Fraction object representing the difference.
        """
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """
        Multiply two Fraction objects.

        Parameters:
        other (Fraction): Another Fraction object to multiply.

        Returns:
        Fraction: A new Fraction object representing the product.
        """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """
        Divide two Fraction objects.

        Parameters:
        other (Fraction): Another Fraction object to divide by.

        Returns:
        Fraction: A new Fraction object representing the quotient.
        """
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __repr__(self) -> str:
        """
        Return a string representation of the Fraction object.

        Returns:
        str: The fraction in "numerator/denominator" format.
        """
        return f'{self.numerator}/{self.denominator}'
