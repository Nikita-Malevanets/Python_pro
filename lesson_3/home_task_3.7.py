class Vector:
    """
    Vector class representing a vector in n-dimensional space.
    Supports addition, subtraction, and scalar (dot) product.
    """

    def __init__(self, coordinates):
        """
        Initialize a Vector with a list of coordinates.

        :param coordinates: list of numbers representing the vector
        """
        self.coordinates = coordinates

    def __add__(self, other):
        """
        Add two vectors element-wise.

        :param other: another Vector of the same dimension
        :return: a new Vector representing the sum
        :raises ValueError: if vectors have different dimensions
        """
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError('Vectors must have same length!')
        return Vector([a + b for a, b in zip(self.coordinates, other.coordinates)])

    def __sub__(self, other):
        """
        Subtract two vectors element-wise.

        :param other: another Vector of the same dimension
        :return: a new Vector representing the difference
        :raises ValueError: if vectors have different dimensions
        """
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError('Vectors must have same length!')
        return Vector([a - b for a, b in zip(self.coordinates, other.coordinates)])

    def __mul__(self, other):
        """
        Compute the scalar (dot) product of two vectors.

        :param other: another Vector of the same dimension
        :return: scalar (number) representing the dot product
        :raises ValueError: if vectors have different dimensions
        """
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError('Vectors must have same length!')
        return sum(a * b for a, b in zip(self.coordinates, other.coordinates))
