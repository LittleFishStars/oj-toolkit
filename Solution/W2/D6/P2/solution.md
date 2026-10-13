Python
```python
n = int(input())
scores = list(map(int, input().split()))

highest = scores[0]
lowest = scores[0]
total = 0
passed = 0
for s in scores:
    if s > highest:
        highest = s
    if s < lowest:
        lowest = s
    total += s
    if s >= 60:
        passed += 1

print(highest, lowest)
print(f"{total / n:.2f}")
print(passed)
```
