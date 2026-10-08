# 内容

小明和小红各自选了一些课程（课程名不含空格），找出他们**共同选择**的课程。

提示：把两行课程名分别转成集合，用 `&` 求交集，再 `sorted()` 排序。

# 格式

## 输入

两行，每行若干个课程名，用空格分开（每行 1 ~ 5 个课程名，课程名长度 ≤ 10）。

## 输出

一行，共同选择的课程名，按字典序从小到大，用空格分开；如果没有共同课程，输出 `None`。

# 测例

```input1
math english python
python art math
```
```output1
math python
```

```input2
math english
art music
```
```output2
None
```

# 限制

Python: 100ms, 10MB
