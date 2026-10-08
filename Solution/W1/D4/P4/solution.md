Python
```python
w, h = map(float, input().split())
bmi = w / (h * h)
if bmi < 18.5:
    cat = "偏瘦"
elif bmi < 24:
    cat = "正常"
elif bmi < 28:
    cat = "偏胖"
else:
    cat = "肥胖"
print(f"{bmi:.1f} {cat}")
```
