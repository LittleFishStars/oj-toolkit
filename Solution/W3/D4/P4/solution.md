Python
```python
class Group:
    def __init__(self, n):
        self.n = n % 7

    def __add__(self, other):
        return Group(self.n + other.n)

    def __sub__(self, other):
        return Group(self.n - other.n)

    def __mul__(self, other):
        return Group(self.n * other.n)

    def __truediv__(self, other):
        return Group(self.n * pow(other.n, 5, 7))

    def __str__(self):
        return f"[{self.n}]"


m = int(input())
for _ in range(m):
    parts = input().split()
    a = Group(int(parts[0]))
    if len(parts) == 2:
        print(a + Group(int(parts[1])))
    else:
        op = parts[1]
        b = Group(int(parts[2]))
        if op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        elif op == "*":
            print(a * b)
        else:
            print(a / b)
```
