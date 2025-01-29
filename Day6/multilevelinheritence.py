class Shape:
    def __init__(self):
        pass
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    def area(self):
        return self.side ** 2
circle = Circle(5)
print(f"Area of circle: {circle.area()}")
square = Square(4)
print(f"Area of square: {square.area()}")