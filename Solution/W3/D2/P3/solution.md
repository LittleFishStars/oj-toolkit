Python
```python
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


a, b, c = map(int, input().split())
t = Triangle(a, b, c)
print(t.perimeter())
print(f"{t.area():.2f}")
```
