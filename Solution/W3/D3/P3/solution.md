Python
```python
class Counter:
    def __init__(self, n):
        self.n = n

    def value(self):
        return self.n


class TwiceCounter(Counter):
    def __init__(self, n):
        super().__init__(n)

    def value(self):
        return super().value() * 2


n = int(input())
print(TwiceCounter(n).value())
```
