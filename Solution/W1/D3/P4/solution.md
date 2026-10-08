Python
```python
a, op, b = input().split()
a, b = int(a), int(b)
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif b == 0:
    print("Error")
else:
    print(f"{a / b:.2f}")
```
