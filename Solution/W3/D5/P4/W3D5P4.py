class Shape:
    def area(self):
        return 0

    def __add__(self, other):
        return Sum(self, other)

    def __str__(self):
        return "shape"


class Rect(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def __str__(self):
        return "rect"


class Square(Rect):
    def __init__(self, s):
        super().__init__(s, s)

    def __str__(self):
        return "square"


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def __str__(self):
        return "circle"


class Sum(Shape):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def area(self):
        return self.left.area() + self.right.area()

    def __str__(self):
        return "sum"


tokens = input().split()
n = int(tokens[0])
pos = 1
shapes = []
for _ in range(n):
    kind = tokens[pos]
    pos += 1
    if kind == "rect":
        shapes.append(Rect(int(tokens[pos]), int(tokens[pos + 1])))
        pos += 2
    elif kind == "square":
        shapes.append(Square(int(tokens[pos])))
        pos += 1
    else:
        shapes.append(Circle(int(tokens[pos])))
        pos += 1

total = shapes[0]
for s in shapes[1:]:
    total = total + s
print(f"{total.area():.2f}")
