# Sundaram 筛法 — 输出所有 ≤ n 的素数

## 思路

原解法使用**埃氏筛**（Sieve of Eratosthenes）直接标记合数。本解法改用 **Sundaram 筛法**（Sieve of Sundaram），一种生成所有奇素数的筛法。

Sundaram 筛法的核心思想：对于任意合数，可以表示为 (2i+1)(2j+1) = 2(2ij+i+j) + 1。因此，对于每个 k = i + j + 2ij，数 2k + 1 必为合数。

## 算法步骤

1. 单独处理 2（唯一的偶素数），先输出
2. 计算 k = (n-1)/2，只需要处理奇数部分
3. 创建大小为 k+1 的标记数组
4. 对于所有 i, j ≥ 1 满足 i + j + 2ij ≤ k，标记该位置
5. 遍历 1 到 k，若未标记，则 2i+1 为奇素数

## 复杂度

- 时间复杂度：约为 O(n log n)，介于埃氏筛 O(n log log n) 与简单试除法 O(n√n) 之间
- 空间复杂度：O(n/2)，约为埃氏筛的一半（因为只处理奇数）

## 与埃氏筛对比

| 方面 | 埃氏筛 | Sundaram 筛 |
|------|--------|-------------|
| 标记方式 | i*i 到 n，步长 i | i+j+2ij |
| 数组大小 | n+1 | (n-1)/2 + 1 |
| 处理"2" | 内置在筛中 | 需要单独处理 |
| 直观性 | 更直观 | 较不直观 |

C语言
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int n;
    scanf("%d", &n);

    if (n < 2) {
        printf("\n");
        return 0;
    }

    printf("2");

    if (n == 2) {
        printf("\n");
        return 0;
    }

    int k = (n - 1) / 2;
    char* marked = (char*)malloc(k + 1);
    memset(marked, 0, k + 1);

    for (int i = 1; i <= k; i++) {
        for (int j = i; i + j + 2 * i * j <= k; j++) {
            marked[i + j + 2 * i * j] = 1;
        }
    }

    for (int i = 1; i <= k; i++) {
        if (!marked[i]) {
            printf(" %d", 2 * i + 1);
        }
    }
    printf("\n");

    free(marked);
    return 0;
}
```

Python
```python
n = int(input())
if n < 2:
    print()
    exit()

primes = [2]
if n == 2:
    print(2)
    exit()

k = (n - 1) // 2
marked = [False] * (k + 1)

for i in range(1, k + 1):
    for j in range(i, k + 1):
        idx = i + j + 2 * i * j
        if idx > k:
            break
        marked[idx] = True

for i in range(1, k + 1):
    if not marked[i]:
        primes.append(2 * i + 1)

print(' '.join(map(str, primes)))
```
