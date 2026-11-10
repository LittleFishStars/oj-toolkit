Python
```python
class Frac:
    def __init__(self, p, q):
        g = self.gcd(p, q)
        self.p = p // g
        self.q = q // g

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other):
        return Frac(self.p * other.q + other.p * self.q, self.q * other.q)

    def __str__(self):
        return f"{self.p}/{self.q}"


p1, q1 = map(int, input().split())
p2, q2 = map(int, input().split())
print(Frac(p1, q1) + Frac(p2, q2))
```
