Python
```python
def matmul(a, b):
    n = len(a)
    k = len(b)
    m = len(b[0])
    c = []
    for r in range(n):
        row = []
        for col in range(m):
            total = 0
            for t in range(k):
                total += a[r][t] * b[t][col]
            row.append(total)
        c.append(row)
    return c


n, k, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
b = []
for _ in range(k):
    b.append(list(map(int, input().split())))

for row in matmul(a, b):
    print(*row)
```
