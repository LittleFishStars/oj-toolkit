# 内容

定义一个基类 `Counter`，用起始值 n 初始化，提供方法 `value()` 返回 n。

再定义子类 `TwiceCounter`：

- 用 n 初始化时，先调用父类的 `__init__` 把 n 存好；
- 重写 `value()`：返回父类 `value()` 结果的 2 倍。

输入一个整数 n，输出 `TwiceCounter(n).value()`。

提示：子类里用 `super().__init__(n)` 调用父类构造，用 `super().value()` 调用父类方法。

# 格式

## 输入

一行一个整数 n（0 ≤ n ≤ 10000）。

## 输出

一行一个整数，等于 2n。

# 测例

```input1
7
```
```output1
14
```

```input2
0
```
```output2
0
```

# 限制

Python: 100ms, 10MB
