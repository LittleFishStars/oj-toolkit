Python
```python
class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x},{self.y})"


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
print(Vec(x1, y1) + Vec(x2, y2))
```
