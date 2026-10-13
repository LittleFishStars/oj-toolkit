Python
```python
n = int(input())
nums = list(map(int, input().split()))
x = int(input())

position = -1
for i in range(n):
    if nums[i] == x:
        position = i + 1
        break
print(position)
```
