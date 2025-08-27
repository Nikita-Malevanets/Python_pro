class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimetr(self):
        return (self.width + self.height) * 2

    def is_square(self):
        if self.height == self.width:
            return True
        else:
            return False

    def resize(self, new_width, new_height):
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