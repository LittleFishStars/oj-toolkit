# 试除法 — 求素数的序号

## 思路

原解法使用**埃氏筛**预先筛出所有 ≤ p 的素数再计数。本解法改用最简单的**试除法**（Trial Division），逐个判断每个整数是否为素数，边判断边计数。

试除法是最直观的素数判定方法：若 n 不能被 2 到 √n 之间的任何整数整除，则 n 为素数。

## 算法步骤

1. 从 2 开始遍历到 p
2. 对每个数 i，用试除法判断其是否为素数：
   - 若 i < 2，不是素数
   - 若 i = 2，是素数
   - 若 i 为偶数，不是素数
   - 否则检查 3, 5, 7, ... 到 √i
3. 每找到一个素数，计数器加 1
4. 当 i == p 时，输出当前计数器的值

## 复杂度

- 时间复杂度：O(p√p)，对于 p ≤ 10000，总共约 10^6 次运算，完全可行
- 空间复杂度：O(1)，不需要额外数组

## 与筛法对比

| 方面 | 埃氏筛 | 试除法 |
|------|--------|--------|
| 空间 | O(p) | O(1) |
| 单次判断 | O(1)（查表） | O(√p) |
| 总体 | O(p log log p) | O(p√p) |
| 实现复杂度 | 中等 | 最简单 |
| 适用场景 | 多次查询、批量求素数 | 单次判断、小数据量 |

对于 p ≤ 10000 的数据范围，试除法虽然 O(p√p) 但实际运算量很小（所有判断加起来不到 20 万次），完全可以在时限内完成。

C语言
```c
#include <stdio.h>

int is_prime(int n) {
    if (n < 2) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0) return 0;
    for (int d = 3; d * d <= n; d += 2) {
        if (n % d == 0) return 0;
    }
    return 1;
}

int main() {
    int p;
    scanf("%d", &p);

    int idx = 0;
    for (int i = 2; i <= p; i++) {
        if (is_prime(i)) {
            idx++;
            if (i == p) {
                printf("%d\n", idx);
                return 0;
            }
        }
    }
}
```

Python
```python
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


p = int(input())
idx = 0
for i in range(2, p + 1):
    if is_prime(i):
        idx += 1
        if i == p:
            print(idx)
            break
```
