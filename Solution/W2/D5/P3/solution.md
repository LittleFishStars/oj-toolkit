Python
```python
n = int(input())

squares = {x: x * x for x in range(1, n + 1)}
print(" ".join(f"{x}:{squares[x]}" for x in range(1, n + 1)))
```
