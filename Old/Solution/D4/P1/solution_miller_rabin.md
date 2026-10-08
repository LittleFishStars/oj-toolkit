# Miller-Rabin 素性测试 — 求第 n 个素数

## 思路

原解法使用**埃氏筛**（Sieve of Eratosthenes），需要先估算素数上界再筛出所有素数。本解法改用 **Miller-Rabin 素性测试**，逐个判断每个整数是否为素数，计数直到找到第 n 个。

Miller-Rabin 是一种**概率素性测试算法**。对于 32 位整数，使用基 {2, 7, 61} 可以保证确定性结果，即对于所有 n < 2^32，测试结果 100% 准确。

## 算法步骤

1. 从 2 开始逐个判断每个整数是否为素数
2. 对每个候选数 n，执行 Miller-Rabin 测试：
   - 将 n-1 分解为 d * 2^s（d 为奇数）
   - 对每个基 a ∈ {2, 7, 61}，计算 a^d mod n
   - 若 a^d ≡ 1 (mod n) 或 a^d ≡ n-1 (mod n)，则该基通过
   - 否则反复平方 d 次，查看是否出现 n-1
   - 若所有基均通过，则 n 为素数
3. 每找到一个素数，计数器加 1；计数器达到 n 时输出结果

## 复杂度

- 时间复杂度：O(k log n) 每次测试（k=3 个基），总体约为 O(n log n)
- 空间复杂度：O(1)，不需要额外数组

## 对比筛法

| 方面 | 埃氏筛 | Miller-Rabin |
|------|--------|-------------|
| 空间 | O(n log n) | O(1) |
| 预处理 | 需要估算上界 | 无需估算 |
| 适用场景 | 批量求素数 | 单个大数素性判断 |
| 确定性 | 完全确定 | 对 32 位确定（基 {2,7,61}） |

C语言
```c
#include <stdio.h>

int pow_mod(int a, int e, int m) {
    int result = 1;
    a %= m;
    while (e) {
        if (e & 1) result = (long long)result * a % m;
        a = (long long)a * a % m;
        e >>= 1;
    }
    return result;
}

int is_prime(int n) {
    if (n < 2) return 0;
    if (n == 2 || n == 3) return 1;
    if (n % 2 == 0) return 0;

    int d = n - 1;
    int s = 0;
    while (d % 2 == 0) {
        d /= 2;
        s++;
    }

    int bases[] = {2, 7, 61};
    for (int i = 0; i < 3; i++) {
        int a = bases[i];
        if (a >= n) continue;
        int x = pow_mod(a, d, n);
        if (x == 1 || x == n - 1) continue;
        int composite = 1;
        for (int r = 0; r < s - 1; r++) {
            x = (long long)x * x % n;
            if (x == n - 1) {
                composite = 0;
                break;
            }
        }
        if (composite) return 0;
    }
    return 1;
}

int main() {
    int n;
    scanf("%d", &n);

    int count = 0;
    for (int i = 2; ; i++) {
        if (is_prime(i)) {
            count++;
            if (count == n) {
                printf("%d\n", i);
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
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for a in (2, 7, 61):
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


n = int(input())
cnt = 0
i = 2
while True:
    if is_prime(i):
        cnt += 1
        if cnt == n:
            print(i)
            break
    i += 1
```
