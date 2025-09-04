import math


class Vector:
    """
    A class to represent a 2D vector and perform arithmetic operations
    and comparisons based on vector length.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Initialize a Vector object.

        Parameters:
        x (float): The x-coordinate.
        y (float): The y-coordinate.
        """
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector') -> 'Vector':
        """
        Add two vectors component-wise.

        Parameters:
        other (Vector): Another vector to add.

        Returns:
        Vector: New vector representing the sum.
         """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        """
        Subtract two vectors component-wise.

        Parameters:
        other (Vector): Another vector to subtract.

        Returns:
        Vector: New vector representing the difference.
        """
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> 'Vector':
        """
        Multiply vector by a scalar.

        Parameters:
        scalar (float): Number to multiply the vector by.

        Returns:
        Vector: New vector scaled by the scalar.
        """
        return Vector(self.x * scalar, self.y * scalar)

    def length(self) -> float:
        """
        Calculate the length (magnitude) of the vector.

        Returns:
        float: The Euclidean length of the vector.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other: 'Vector') -> bool:
        """
        Compare two vectors by length (less than).

        Parameters:
        other (Vector): Another vector to compare with.

        Returns:
        bool: True if this vector's length is less than the other's.
        """
        return self.length() < other.length()

    def __eq__(self, other: 'Vector') -> bool:
        """
        Check if two vectors are the same

        Parameters:
        other (Vector): Another vector.

        Returns:
        bool: True if x and y are the same.
        """
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        """
        Show the vector as text.

        Returns:
        str: The vector in (x, y) form.
        """
        return f"({self.x}, {self.y})"
