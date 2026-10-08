Python
```python
w, u = map(int, input().split())
fee = 8
if w > 1000:
    extra_kg = (w - 1000 + 999) // 1000  # 不足 1 公斤按 1 公斤算
    fee += extra_kg * 4
if u == 1:
    fee += 5
print(fee)
```
