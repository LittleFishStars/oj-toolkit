# 内容

实现一个小型图书管理系统，用继承和魔法方法把各项功能串起来。

- 基类 `Book`：名称 title、价格 price、库存 stock；`value()` 返回 price × stock；`__str__` 返回 title。
- `Ebook`（继承 Book）：多一个文件大小 mb；`value()` 返回父类结果（电子书库存即份数），`__str__` 返回 `title[电子]`。
- `Paper`（继承 Book）：多一个重量 kg；`__str__` 返回 `title[纸质]`。
- 基类实现 `__lt__`：按 `value()` 从小到大比较；`__add__`：两个对象相加，返回一个 `Combo`，其 `value()` 是两者之和，`__str__` 返回 `组合`。

操作：

1. `add ebook 名称 价格 库存 大小` / `add paper 名称 价格 库存 重量`
2. `sell 名称 数量`（库存不足卖到 0）
3. `list`：按 `value()` 从大到小输出 `名称 价值`（价值保留 1 位小数，相同价值按名称字典序）
4. `total`：输出所有图书价值之和（保留 1 位小数）

# 格式

## 输入

第一行一个整数 m（1 ≤ m ≤ 20）。

接下来 m 行，每行一种操作。名称 1 ~ 10 个小写字母，价格 1 ~ 1000，库存 0 ~ 1000，大小为 1 ~ 10000 的整数，重量为 1 ~ 10000 的整数。

数据保证第一条是 `add`，且 `list` 与 `total` 至少各出现一次。

## 输出

每个 `list` 输出若干行 `名称 价值`（名称带 `[电子]` / `[纸质]` 后缀）；每个 `total` 输出一行一个数。

# 测例

```input1
3
add ebook pybook 10 5 100
add paper novel 20 2 500
list
```
```output1
pybook[电子] 50.0
novel[纸质] 40.0
```

```input2
4
add paper a 10 3 1
sell a 1
total
list
```
```output2
20.0
a[纸质] 20.0
```

# 限制

Python: 100ms, 10MB
