Python
```python
class Shape:
    def name(self):
        return "shape"

    def area(self):
        return 0


class Rect(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def name(self):
        return "rect"

    def area(self):
        return self.a * self.b


class Square(Rect):
    def __init__(self, s):
        super().__init__(s, s)

    def name(self):
        return "square"


class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def name(self):
        return "triangle"

    def area(self):
        return self.b * self.h / 2


tokens = input().split()
n = int(tokens[0])
pos = 1
shapes = []
for _ in range(n):
    kind = tokens[pos]
    pos += 1
    if kind == "r":
        shapes.append(Rect(int(tokens[pos]), int(tokens[pos + 1])))
        pos += 2
    elif kind == "s":
        shapes.append(Square(int(tokens[pos])))
        pos += 1
    else:
        shapes.append(Triangle(int(tokens[pos]), int(tokens[pos + 1])))
        pos += 2

for s in shapes:
    print(f"{s.name()} {s.area():.1f}")
```
