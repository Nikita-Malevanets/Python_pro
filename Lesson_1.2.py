class Rectangle:
    """A class that represents a rectangle with width and height."""

    def __init__(self, width: int, height: int):
        """Initialize a rectangle with given width and height."""
        self.width = width
        self.height = height

    def area(self) -> int:
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimetr(self) -> int:
        """Calculate and return the perimeter of the rectangle."""
        return (self.width + self.height) * 2

    def is_square(self) -> bool:
        """ Checking if sides are equal: if Yes return 'True', if not return 'False' """
        if self.height == self.width:
            return True
        else:
            return False

    def resize(self, new_width: int, new_height: int) -> None:
        """Rectangle gets new Width and Height """
        self.width = new_width
        self.height = new_height


rect = Rectangle(2,3)


print(f'size of rectangle: {rect.width} x {rect.height}')
print(f'area of rectangle: {rect.area()}')
print(f'perimetr of rectangle {rect.perimetr()}')
print(f'is it square {rect.is_square()}')


rect.resize(3,3)


print(f'new size {rect.width} x {rect.height}')
print(f'is it square {rect.is_square()}')