# 内容

定义一个矩形类 `Rect`，用长和宽初始化，提供两个方法：

- `area()`：返回面积；
- `perimeter()`：返回周长。

输入长和宽（整数），输出面积和周长，各占一行。

提示：`class Rect:` 里写 `__init__(self, a, b)` 保存长宽，再写 `area(self)` / `perimeter(self)` 返回计算结果。

# 格式

## 输入

一行两个整数 a b，用空格分开（1 ≤ a, b ≤ 1000）。

## 输出

共两行：第一行面积，第二行周长。

# 测例

```input1
3 4
```
```output1
12
14
```

```input2
1 1
```
```output2
1
4
```

# 限制

Python: 100ms, 10MB
