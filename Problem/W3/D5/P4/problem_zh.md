# 内容

用类来实现一个小的几何系统：

- 基类 `Shape`：方法 `area()` 返回 0，`__str__` 返回 `shape`；
- `Rect(a, b)`：`area()` 返回 a·b，`__str__` 返回 `rect`；
- `Square(s)` 继承 `Rect`：`__str__` 返回 `square`；
- `Circle(r)`：`area()` 返回 πr²（π 取 3.14），`__str__` 返回 `circle`；
- 基类还要实现 `__add__`：两个图形相加，返回一个 `Sum` 对象（`Sum` 的 `area()` 是两个图形面积之和，`__str__` 返回 `sum`）。

输入一行图形描述，先是一个整数 n，后面每三个 token 描述一个图形：

- `rect a b`、`square s`、`circle r`

把这些图形全部相加，输出最终的总面积（保留 2 位小数）。

# 格式

## 输入

一行，形如 `3 rect 3 4 square 5 circle 1`（1 ≤ n ≤ 10，各边长 1 ≤ 数值 ≤ 1000）。

## 输出

一行一个数，总面积保留 2 位小数。

# 测例

```input1
3 rect 3 4 square 5 circle 1
```
```output1
40.14
```

```input2
1 square 1
```
```output2
1.00
```

# 限制

Python: 100ms, 10MB
