# 内容

定义一个银行账户类 `Account`：

- 用初始余额初始化（余额不会为负）；
- `deposit(x)`：存入 x，返回新的余额；
- `withdraw(x)`：取出 x。如果余额不足，不扣钱，返回字符串 `no`；否则扣钱并返回新的余额。

输入初始余额和若干次操作，按顺序输出每次操作的结果。

# 格式

## 输入

第一行一个整数 balance（0 ≤ balance ≤ 1000000），表示初始余额。

第二行一个整数 m（1 ≤ m ≤ 20），表示操作次数。

接下来 m 行，每行 `deposit x` 或 `withdraw x`（1 ≤ x ≤ 1000000）。

## 输出

共 m 行，每次操作的返回值：存入/取出成功输出新余额；取钱余额不足输出 `no`。

# 测例

```input1
100
3
deposit 50
withdraw 200
withdraw 30
```
```output1
150
no
120
```

```input2
0
1
withdraw 1
```
```output2
no
```

# 限制

Python: 100ms, 10MB
