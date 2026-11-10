Python
```python
nums = list(map(int, input().split()))

arr = map(lambda x: x * x if x % 2 == 0 else x * 3 + 1, nums)
print(*arr)
```
