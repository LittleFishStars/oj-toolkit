Python
```python
n = int(input())

steps = 0
while n != 6174:
    digits = sorted([n // 1000, n // 100 % 10, n // 10 % 10, n % 10])
    big = digits[3] * 1000 + digits[2] * 100 + digits[1] * 10 + digits[0]
    small = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]
    n = big - small
    steps += 1
print(steps)
```
