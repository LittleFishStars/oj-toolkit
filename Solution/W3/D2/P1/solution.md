Python
```python
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


a, b = map(int, input().split())
r = Rect(a, b)
print(r.area())
print(r.perimeter())
```
