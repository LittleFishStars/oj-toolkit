# 内容

定义一个基类 `Animal`，它有一个方法 `speak()`，返回字符串 `...`（动物没叫声）。

再定义两个子类，各自重写 `speak()`：

- `Dog`：返回 `wang`
- `Cat`：返回 `miao`

输入一个单词（`dog` 或 `cat`），创建对应的对象，调用 `speak()` 并输出结果。

提示：`class Dog(Animal):` 括号里写父类名，子类里重新定义同名方法就是重写。

# 格式

## 输入

一行一个单词：`dog` 或 `cat`。

## 输出

一行，`Dog` 输出 `wang`，`Cat` 输出 `miao`。

# 测例

```input1
dog
```
```output1
wang
```

```input2
cat
```
```output2
miao
```

# 限制

Python: 100ms, 10MB
