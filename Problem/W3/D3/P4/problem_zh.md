# 内容

构建一个形状体系：

- 基类 `Shape`：方法 `name()` 返回 `shape`，方法 `area()` 返回 0；
- `Rect`：用长 a、宽 b 初始化，`name()` 返回 `rect`，`area()` 返回 a·b；
- `Square`：**继承 `Rect`**，用边长 s 初始化（长宽都是 s），`name()` 返回 `square`；
- `Triangle`：用底 b、高 h 初始化，`name()` 返回 `triangle`，`area()` 返回 b·h/2。

输入一行描述，先是一个整数 n，接着 n 组数据，每组第一个字母表示类型：

- `r a b`：矩形
- `s s`：正方形
- `t b h`：三角形

按输入顺序输出每个图形的一行：`类型 面积`，面积保留 1 位小数。

提示：`Square` 继承 `Rect` 后直接复用父类的 `area()`，只重写 `name()` 即可。

# 格式

## 输入

一行：`n r 3 4 s 5 t 6 8` 这样的形式，类型字母与数字与数字之间用空格分开（1 ≤ n ≤ 20，各边长 1 ≤ 数值 ≤ 1000）。

## 输出

共 n 行，每行 `类型 面积`，面积保留 1 位小数。

# 测例

```input1
3 r 3 4 s 5 t 6 8
```
```output1
rect 12.0
square 25.0
triangle 24.0
```

```input2
2 s 1 t 1 2
```
```output2
square 1.0
triangle 1.0
```

# 限制

Python: 100ms, 10MB
