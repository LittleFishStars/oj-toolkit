Python
```python
words = input().split()

counts = {}
for w in words:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1

items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
for w, c in items:
    print(w, c)
```
