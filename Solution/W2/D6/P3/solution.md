Python
```python
n = int(input())

digits = 0
m = n
while m:
    digits += 1
    m //= 10

total = 0
m = n
while m:
    d = m % 10
    total += d ** digits
    m //= 10

print(1 if total == n else 0)
```
