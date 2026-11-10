class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


kind, x = input().split()
x = int(x)
if kind == "square":
    s = Square(x)
else:
    s = Circle(x)
print(f"{s.area():.2f}")
