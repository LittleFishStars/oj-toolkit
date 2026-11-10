# 内容

实现一个简单库存系统：

- 基类 `Item`：用名称 name、单价 price、库存 qty 初始化，方法 `value()` 返回 price × qty；
- 子类 `Food`：多一个保质期天数 days，`value()` 返回父类结果打 9 折（乘 0.9）；
- 子类 `Tool`：多一个是否进口字段（`1`/`0`），进口时 `value()` 返回父类结果的 1.1 倍。

输入若干商品和操作：

1. `add 类型 名称 单价 库存 附加`：加入商品；
2. `sell 名称 数量`：卖出若干件，库存不足时只卖到 0（不报错）；
3. `report`：按 `value()` 从大到小输出所有商品的一行，格式 `名称 总价值`（保留 1 位小数），价值相同按名称字典序。

# 格式

## 输入

共两段：

- 第一行一个整数 m（1 ≤ m ≤ 20），表示操作数；
- 接下来 m 行，每行是上面三种操作之一（名称是 1 ~ 10 个小写字母，单价 1 ~ 1000，库存 0 ~ 1000，附加为天数 1 ~ 365 或 0/1）。

数据保证：第一条操作一定是 `add`；`report` 至少出现一次。

## 输出

每个 `report` 输出若干行（商品个数行），每行 `名称 总价值`；不同 `report` 之间不空行。

# 测例

```input1
3
add food apple 10 5 30
add tool hammer 100 2 1
report
```
```output1
hammer 220.0
apple 45.0
```

```input2
4
add tool saw 10 3 0
sell saw 2
add food milk 5 4 7
report
```
```output2
milk 18.0
saw 10.0
```

# 限制

Python: 100ms, 10MB
