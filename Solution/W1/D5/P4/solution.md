Python
```python
n = int(input())
book = {}
for _ in range(n):
    name, phone = input().split()
    book[name] = phone
m = int(input())
for _ in range(m):
    q = input()
    if q in book:
        print(book[q])
    else:
        print("Not Found")
```
