Python
```python
a, b, c = map(int, input().split())
if a + b <= c or a + c <= b or b + c <= a:
    print("不能构成三角形")
elif a == b == c:
    print("等边三角形")
elif a == b or b == c or a == c:
    print("等腰三角形")
else:
    print("普通三角形")
```
