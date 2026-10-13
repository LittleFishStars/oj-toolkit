Python
```python
n = int(input())

total = 0
for x in range(1, n + 1):
    if x % 2 == 0:
        continue
    total += x
print(total)
```
