Python
```python
def total(*args):
    result = 0
    for x in args:
        result += x
    return result


line = input().strip()
if line:
    print(total(*map(int, line.split())))
else:
    print(total())
```
