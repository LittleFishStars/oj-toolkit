Python
```python
a, b = map(int, input().split())
if a == b:
    print("Draw")
elif (a - b) % 3 == 2:  # 石头(0)赢剪刀(1)、剪刀(1)赢布(2)、布(2)赢石头(0)
    print("Player 1 wins")
else:
    print("Player 2 wins")
```
