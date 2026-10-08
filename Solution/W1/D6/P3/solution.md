Python
```python
y, m, d = map(int, input().split())
if m < 1 or m > 12 or d < 1:
    print("No")
else:
    leap = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
    days = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if d <= days[m - 1]:
        print("Yes")
    else:
        print("No")
```
